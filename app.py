#!/usr/bin/env python
# coding: utf-8

# In[78]:


import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
# from dash.dependencies import Input, Output
import pandas as pd
# import textwrap


# Load and preprocess data.

# In[2]:


#Load the Excel file saved locally and read the tab I normalized into a dataframe
#Original Excel file source under subheading "Table C2. Apportionment Population and Number of Seats in U.S. House of Representatives by State: 1910 to 2020"
#can be found at: https://www.census.gov/data/tables/2020/dec/2020-apportionment-data.html
df = pd.read_excel("/home/dadeda/redistricting/data/apportionment-2020-tableC2.xlsx", sheet_name="Table_C2_df")
#Sort the dataframe by year ascending, then State will be alpha as is; ascending=True is defaulted.
df = df.sort_values(by=['Year','State'])
#To use Plotly Express built in US States geography, the two letter abbreviated state code is required.

#introducing us_state_abbrev as dictionary
#Using dictionary to translate State names to codes from https://gist.github.com/rogerallen/1583593
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

#reversing it for reference only
# thank you to @kinghelix and @trevormarburger for this idea
#abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))
#abbrev_us_state

#Mapping the dictionary keys to the data frame
df['State_code'] = df['State'].map(us_state_abbrev)
#Remove 'All State' totals by year rows from dataframe in order to have range only apply to actual state values.
#Make a boolean variable for State rows with 'All States' to isolate what we don't want to map.
is_All_States = df['State']=='All States'

#Filter rows for State 'All States' using the boolean variable.
#We may want to use the Totals by year values later so let's name this a new mapping df also.
#There are 12 years so expecting to remove 12 rows from df.
df_map = df[-is_All_States]


# Construct the graph, app and run the app.

# In[153]:


#Assign a variable for text wrapped descriptive graph title that will be called in choropleth title attribute.
# split_text_graph_title = textwrap.fill("Select the play button to watch changes over this period, or select a specific year on the timeline.<br>States in the map are colored by the number of House seats each gained or lost after that year.",
#                                   width=30) # commented out from Plotly.Express title to move to Dash text component to wrap responsively instead.
#plot it as a choropleth map
fig = px.choropleth(df_map,
          locations = 'State_code',
          color="Seat change",
          hover_name="State", #column to add to hover information
          hover_data={#determines what shows in hover text (default was everything in mapped variables)
              'Year':True, # add column with default formatting
              'Seat change':True, # add column with default formatting
              'Number of representatives':True, # add column with default formatting
              'Apportionment population':':,', # add column with comma as thousands separator formatting
              'Average persons per representative':':,', # add column with comma as thousands separator formatting
              'State_code':False # Remove two letter abbreviated State_code from hover data as unnecessary, provides no additional knowledge or context needed in this app.
          },
          labels={#replaces default labels by column name
          'Seat_change': 'Seat change', 'Year': 'Census Year'
          },
          animation_frame="Year",
          color_continuous_scale="BrBG",
          locationmode='USA-states',
          scope="usa",
          range_color=(-5, 10)#,
          # below did not wrap responsively either; commented out from Plotly.Express title to move to Dash text component to wrap responsively instead.
        #   title="Select the play button to watch changes over this period, or select a specific year on the timeline. Map colors represent the number of House seats each state gained or lost from the previous decennial census." #split_text_graph_title,
        #   height=600
         )

fig.update_layout(
    hoverlabel_align = 'right', # Right aligns the hover box components.
    font_family='"News Cycle", "Arial Narrow Bold", sans-serif',
    # Customize the map's color legend orientation to be centered horizontal, instead of default vertical position, in order to make more room for the map in all screen viewport modes.
    coloraxis_colorbar=dict(
        title="Seat change"
        )
    )

# app, from Dash Bootstrap Components library using Journal theme; and from dbc also scaling the viewport by device width to be responsive e.g. on mobile, and avoid horizontal scrollbars if possible and ensure legend is visible always.
app = JupyterDash(
    __name__,
    external_stylesheets=[dbc.themes.JOURNAL],
    meta_tags=[
        {"name": "viewport",
        "content": "width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=1.0"},
    ],
    )

app.layout = dbc.Card(
    [
        dbc.CardHeader(html.H1("Changing U.S. Population Impacts Redistricting", style={'text-align': 'left'})),
        dbc.CardBody(
            [
                html.H4("Since 1970, as required by Article I, Section 2, of the U.S. Constitution, every ten years state populations have determined the number of seats appropriated for each state from among the 435 seats in the U.S. House of Representatives. Decennial census data for 1910 to 2020 show changes in state populations that resulted in the redrawing of district areas when the number of House seats for a state increased or decreased.", className="card-title"),
                html.Br(), #adds a line break
                html.H5("Select the play button to watch changes over this period, or select a specific year on the timeline. Map colors represent the number of House seats each state gained or lost from the previous decennial census."),
                dcc.Graph(id='map-animated', figure=fig,
                         config={
                             'staticPlot': False,       # True, False
                             'scrollZoom': True,        # True, False
                             'doubleClick': 'reset',    # 'reset', 'autosize' or 'reset+autosize', False
                             'showTips': True,          # True, False
                             'displayModeBar': 'hover', # True, False, 'hover'
                             'watermark': True,         # Shows Plotly logo in mode bar
                             # 'modeBarButtonsToRemove': ['pan2d', 'select2d'],
                             },
                         className="card-text"
                         ),
                html.Br(), #adds a line break
                html.H5("States that have seen a large degree of variability in population, whether growth or detraction due to historical events, have seen frequent district changes as a direct result. California saw significant increases in House seats over the first half of the 20th century, with massive early 1900s population growth including foreign immigrants, then more workers from other states following the Great Depression which lasted until the late 1930s, and again after World War II ended in 1945."),
                html.Br(), #adds a line break
                html.H5("Californian voters have gained more public input with redistricting over the years through the passing of state propositions which led to its current Citizens Redistricting Commission, but the lines of other states are drawn solely by political party leaders, or by judicial oversight with varying degree of party leanings."),
                html.Br(), #adds a line break
                html.H5("Although the 2020 decennial census population figures have been delivered by the U.S. Census Bureau on time in spring 2021, release of the full data results necessary for redistricting has been delayed due to the COVID-19 pandemic. The federal government's limited requirements on the redrawing of district boundaries is upheld by the one person, one vote clause of the Voting Rights Act, and the rest is governed by guidelines that vary from state to state. Many sources believe that compressed timelines for redistricting caused by this delay will put the public transparency at risk within states' procedures, in particular forcing political watchdog organisations to be at the ready for likely accelerated review periods. Many states are now forced to extensive legal measures to amend timelines, and to follow and wait for the release of data, now slated for August to September."),
                html.Br() #adds a line break
            ]
        ),
        dbc.CardFooter(
            [
                html.H6("Visualization by Kathryn Hurchla"),
                html.H6("Assignment 2 - Redistricting, Design Lab: Case Studies, MICA Data Analytics and Visualization"),
                dbc.Button("Be the first to know when 2020 Census results become available! Sign up at www.census.gov.", href="https://public.govdelivery.com/accounts/USCENSUS/signup/22746", color="info"),
                html.Br(), #adds a line break
                dbc.CardLink("Data source: U.S. Census Bureau, Table C2. Apportionment Population and Number of Seats in U.S. House of Representatives by State: 1910 to 2020    ", href="https://www.census.gov/data/tables/2020/dec/2020-apportionment-data.html")
            ]
        ),
    ],
    # style={"width": "100rem"}

)


#Create server variable with Flask server object for use with gunicorn ("Green Unicorn" Python Web Server Gateway Interface HTTP server)
server = app.server

#Run i.e. serve the app using run_server, and display result inline in the notebook.
#Unlike the standard Dash.run_server method, the JupyterDash.run_server method doesn't block execution of the notebook. It serves the app in a background thread, making it possible to run other notebook calculations while the app is running.
#This makes it possible to iterativly update the app without rerunning the potentially expensive data processing steps.
#By default, run_server displays a URL that you can click on to open the app in a browser tab. The mode argument to run_server can be used to change this behavior.
#Setting mode="inline" will display the app directly in the notebook output cell.
#app.run_server(debug=True, use_reloader=False)#or add mode='inline' to display in Jupyter Notebook. #commented out for running on PythonAnywhere so it does not prevent WSGI from working

