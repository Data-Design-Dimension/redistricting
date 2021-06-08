## Changing U.S. Population Impacts Redistricting
---

__Watch how changing populations have impacted the need for redistricting in some states more than others over 100 years of United States history, at [https://dadeda.pythonanywhere.com/](https://dadeda.pythonanywhere.com/).__

Pictured here, CA gained 8 seats in 1960, a gain exceeded only by Califoria itself 30 years earlier. Alaska and Hawaii were admitted, respectively, as the 49th and 50th states of the Union in 1959, and their first comparison for change in House seats was recorded in the next decennial census of 1970.

<img src="https://github.com/Data-Design-Dimension/redistricting/blob/main/img/redistricting-plot.png" alt="Interactive choropleth map animating U.S. population change 1910 to 2020 and colored by a scale of number of House of Representative seats gained or lost each ten years.">

Before Californian voters gained more input to their state's redistricting process through a series of passed propositions, California saw significant increases in its number of House of Representatives seats over the first half of the 20th century. Shifts included massive migration following the Great Depression during the decade when it gained a record high nine House seats in 1930, and again its growth returned after World War II ended in 1945. __Learn more and explore the changes in specific years at the link above.__

This visualization project was built by Kathryn Hurchla for *Data Design Dimension* in Python libraries Plotly.Express, Dash, Bootstrap Components for responsive web modules, and deployed using a virtual environment with PythonAnywhere. Exploratory data analysis was first completed in Jupyter Notebook. As a reference to *dadeda* process, a design brief and research citations written in early stages are included below. These serve to align with objectives and audience, and final products often transcend aims outlined in such planning. Project fulfilled a masters in data analytics and visualization course assignment of Kathryn's.

---

*(Redistricting Brief)*

- __Goal(s):__ Visualize how related dataset(s) show the ‘face’ of some electoral districts; unearth stories of district attributes, like economic and/or judicial power.

- __Primary Audience:__ Described as folks who spend time researching or are well informed on the topic of redistricting. They are at minimum readers or podcast listeners of Five Thirty Eight or equivalent media outlets This visualization is not necessarily tuned for the general public, and is not designed to provide a visual solution to the gerrymandering problem the general public would likely want from a visualization on this topic. Their characteristics might affect my editorial and design decisions by enabling me to highlight singular districts as story examples without providing a broader context of districts as a full picture, because this audience can envision how a few examples can illustrate how the data overlaid might look or play out in other districts with their broad understanding of districting. Labels may be shorter, or definitions can be skipped or not listed as centrally to the visual, e.g. as a footnote.

- __Approach:__ Show economic power balances. See how I can overlay political donations over districts, aligned by years. Another option is to show what political parties state judges align with to the extent possible, in order to illustrate how that might impact a state level judge run non-politician commission to set districts, a solution some folks have inquired to Five Thirty Eight about through questions addressed in their podcasts, and which some other countries use.

- __Proposed format and delivery channel(s):__ Possibly a zoomed in area map, e.g. to a single district showing overlay data areas such as zip codes or other relevant format the donation is organized as (full donor address I believe is public). Judicial representation could be with quickly recognizable gavel symbol. Show enough background, or greyed out portion of state district is part of to be immediately recognizable. Alternately pan out and do a weighted map where the state polygons are sized based on the ‘power’ the data shows. Will it be easy enough to tie donation candidate recipients to a political party?


### Cited

It’s Probably Not Possible to End Gerrymandering, Series: The Gerrymandering Project, By Galen Druke, 1/11/2018, [https://fivethirtyeight.com/features/its-probably-not-possible-to-end-gerrymandering/](https://fivethirtyeight.com/features/its-probably-not-possible-to-end-gerrymandering/)

The Atlas of Redistricting, By Aaron Bycoffe, Ella Koeze, David Wasserman and Julia Wolfe, 1/25/2018, [https://projects.fivethirtyeight.com/redistricting-maps/](https://projects.fivethirtyeight.com/redistricting-maps/)

govunits (MapServer), USGS, Last accessed 5/23/2021, [https://carto.nationalmap.gov/arcgis/rest/services/govunits/MapServer](https://carto.nationalmap.gov/arcgis/rest/services/govunits/MapServer)

District Builder, Azavea, Last accessed 5/23/2021 (PA House of Reps stated Last updated 3 months ago), [https://app.districtbuilder.org/projects/705c42ad-34e4-4321-bd62-579b2c26c0b0](https://app.districtbuilder.org/projects/705c42ad-34e4-4321-bd62-579b2c26c0b0)


[https://www.fec.gov/](https://www.fec.gov/)
[https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/](https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/)

Decennial Census, United States Census Bureau, Accessed 5/30/2021, https://www.census.gov/history/www/programs/demographic/decennial_census.html

### Referenced
State-by-state redistricting procedures, Ballotpedia.org, Last accessed 5/23/2021, [https://ballotpedia.org/State-by-state_redistricting_procedures](https://ballotpedia.org/State-by-state_redistricting_procedures)

8 THINGS PROPORTIONAL REPRESENTATION DOES FOR EVERY VOTER, Sightline Institute, By Anna Fahey and Kristin Eberhard, 11/15/2018, [https://www.sightline.org/2018/11/15/8-things-proportional-representation-does-for-every-voter/](https://www.sightline.org/2018/11/15/8-things-proportional-representation-does-for-every-voter/)

Redistricting Data Program Management, United States Census Bureau, 3/16/2021, [https://www.census.gov/programs-surveys/decennial-census/about/rdo/program-management.html](https://www.census.gov/programs-surveys/decennial-census/about/rdo/program-management.html)

Gerry, a font based on gerrymandered congressional districts, FlowingData, 8/2/2019, [https://flowingdata.com/2019/08/02/gerrymandering-font/](https://flowingdata.com/2019/08/02/gerrymandering-font/)

MIT Election Lab: Data, Last accessed 5/23/2021, [https://electionlab.mit.edu/data](https://electionlab.mit.edu/data)

[https://github.com/MEDSL/elections](https://github.com/MEDSL/elections)

Election Geodata, Last accessed 5/23/2021, [https://github.com/nvkelso/election-geodata](https://github.com/nvkelso/election-geodata)
