# big-data-hackathon-2017
This repository contains the materials created during the UIowa Big Data Hackathon from September 16th to September 18th.

First and foremost, the crux of the project depended on big data representation using Bokeh/Pandas and later embedded onto 
a webpage using Django and Bootstrap. The specific dataset in question is "Inpatient Prospective Payment System (IPPS) Provider Summary for the Top 100 Diagnosis-Related Groups (DRG)" which is available to the public from data.cms.gov.

Pandas allowed for easy manipulation/viewing of initial changes and formatting of different subsets of the above set.
Moving to Bokeh was a new experience but allowed the cleanest representation given the time.

The first data table was strictly comparing the number of a specific procedure versus the population of a state for all states.
This later evolved into an idea of comparing number of procedures per average cost of the procedure in a given area.
The result of the above would yield an "efficiency" map for states in the united States given an operation of interest.

One of the other data visualizations was of the cost per person of a specific procedure for any given state.
This data can be further augmented to see which procedures are most cost-efficient in a state vs most-expensive.
Furthermore, cross-comparing states for most cost-efficient procedures in the United States is also viable.

Challenges faced along the way were that two members had not experienced Python before this day (one of created the Bokeh graphs),
nobody had formal education on data analysis, and one of the members that did know Python was incapacitated for eight hours over a 
Numpy and Pandas packaging error that was finally resolved by reinstalling the current Anaconda distribution.
