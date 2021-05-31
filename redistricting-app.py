#!/usr/bin/env python
# coding: utf-8

# In[78]:


import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import textwrap


# Load and preprocess data.

# In[2]:


#Load the Excel file saved locally and read the tab I normalized into a dataframe
#Original Excel file source under subheading "Table C2. Apportionment Population and Number of Seats in U.S. House of Representatives by State: 1910 to 2020"
#can be found at: https://www.census.gov/data/tables/2020/dec/2020-apportionment-data.html
df = pd.read_excel("../data/apportionment-2020-tableC2.xlsx", sheet_name="Table_C2_df")
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
split_text_graph_title = textwrap.fill("States in the map are colored by the number of House seats each gained or lost after that year.<br>Select the play button to watch changes over this period, or select a specific year on the timeline.",
                                  width=30)
#plot it as a choropleth map
fig = px.choropleth(df_map,
          locations = 'State_code',
          color="Seat change",
          hover_name="State", #column to add to hover information
          hover_data={#determines what shows in hover text (default was everything in mapped variables)
              'Year':True, 'Seat change':True,'Apportionment population':True,
   'Number of representatives':True, 
   'Average persons per representative':True, 'State_code':False
          },
          labels={#replaces default labels by column name
          'Seat_change': 'Seat change', 'Year': 'Census Year'
          },
          animation_frame="Year",
          color_continuous_scale="Inferno",
          locationmode='USA-states',
          scope="usa",
          range_color=(-5, 10),
          title=split_text_graph_title,
          height=600
         )


app = JupyterDash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.layout = dbc.Card(
    [
        dbc.CardHeader(html.H1("Changing U.S. Population Impacts Redistricting", style={'text-align': 'left'})),
        dbc.CardBody(
            [
                html.H3("Since 1970, as required by Article I, Section 2, of the U.S. Constitution, every ten years state populations have determined the number of seats appropriated for each state in the U.S. House of Representatives. Decennial census data for 1910 to 2020 show changes in state populations that resulted in the redrawing of district areas when the number of House seats for a state increased or decreased.", className="card-title"),
                html.Br(), #adds a line break
                dcc.Graph(figure=fig, className="card-text"),
            ]
        ),
        dbc.CardFooter(
            [
                dbc.CardLink("Data source: U.S. Census Bureau, Table C2. Apportionment Population and Number of Seats in U.S. House of Representatives by State: 1910 to 2020", href="www.census.gov/data/tables/2020/dec/2020-apportionment-data.html"),
                dbc.Button("Be the first to know when 2020 Census results become available! Sign up at www.census.gov.", href="https://public.govdelivery.com/accounts/USCENSUS/signup/22746", color="info"),
            ]
        ),
    ],
    style={"width": "100rem"}

# app.layout = html.Div([
#     html.H1("Changing U.S. Population Impacts Redistricting", style={'text-align': 'left'}),
#     html.H3("Since 1970, as required by Article I, Section 2, of the U.S. Constitution, every ten years state populations have determined the number of seats appropriated for each state in the U.S. House of Representatives. Decennial census data for 1910 to 2020 show changes in state populations that resulted in the redrawing of district areas when the number of House seats for a state increased or decreased."),
#     html.Br(), #adds a line break
#     html.Br(), #adds a line break
#     dcc.Graph(figure=fig)
)


#Create server variable with Flask server object for use with gunicorn ("Green Unicorn" Python Web Server Gateway Interface HTTP server)
server = app.server

#Run i.e. serve the app using run_server, and display result inline in the notebook.
#Unlike the standard Dash.run_server method, the JupyterDash.run_server method doesn't block execution of the notebook. It serves the app in a background thread, making it possible to run other notebook calculations while the app is running.
#This makes it possible to iterativly update the app without rerunning the potentially expensive data processing steps.
#By default, run_server displays a URL that you can click on to open the app in a browser tab. The mode argument to run_server can be used to change this behavior. 
#Setting mode="inline" will display the app directly in the notebook output cell.
app.run_server(debug=True, use_reloader=False)#or add mode='inline' to display in Jupyter Notebook.

