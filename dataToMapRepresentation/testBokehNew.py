import pandas as pd

from bokeh.sampledata import us_states, unemployment
from bokeh.sampledata.us_counties import data as us_counties_data
from bokeh.plotting import figure
from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.models import LogColorMapper, LogTicker, ColorBar
from bokeh.models import ColumnDataSource, HoverTool
import bokeh.palettes as bp
from bokeh.palettes import Viridis6 as myPalette # @UnresolvedImport

EXCLUDED = ("ak", "hi", "pr", "gu", "vi", "mp", "as")

uscountiesdf = pd.DataFrame(us_counties_data)
print(uscountiesdf)

us_states = us_states.data.copy()
counties = {
    code: county for code, county in us_counties_data.items() if county["state"] not in EXCLUDED
}
unemployment = unemployment.data

del us_states["HI"]
del us_states["AK"]

state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

county_xs=[us_counties_data[code]["lons"] for code in us_counties_data if us_counties_data[code]["state"] not in EXCLUDED]
county_ys=[us_counties_data[code]["lats"] for code in us_counties_data if us_counties_data[code]["state"] not in EXCLUDED]
county_names = [county['name'] for county in counties.values()]

us_counties_df2 = pd.DataFrame(county_names)
print(us_counties_df2)

# colors = ["#FF3030", "#FF9E9E", "#FFF2F2", "#B1B5F9", "#5159EF", "#000CFC"]
colors = myPalette
county_colors = []
color_mapper = LogColorMapper(palette=myPalette)
for county_id in us_counties_data:
    if us_counties_data[county_id]["state"] in EXCLUDED:
        continue
    try:
        rate = unemployment[county_id]
        idx = min(int(rate/2), 5)
        county_colors.append(colors[idx])
    except KeyError:
        county_colors.append("black")

output_file("choropleth.html", title="choropleth.py example")

tools = "pan,wheel_zoom,box_zoom,reset,hover"
source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names[:3109],
))

source2 = ColumnDataSource(data=dict(
    x2=state_xs,
    y2=state_ys,
))

p = figure(title="US Unemployment 2009", tools=tools,toolbar_location="left",
    plot_width=1100, plot_height=700)
p.patches('x', 'y', source=source)
p.patches(county_xs, county_ys, fill_color=county_colors, fill_alpha=0.7,
    line_color="white", line_width=0.5)
p.patches(state_xs, state_ys, fill_alpha=0.0,
    line_color="#884444", line_width=2)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("(x,y)", "($x , $y)"),
    ("County Name", "@name")
]

# print(county_names)
# show(p)
p2 = figure(title="US Map",tools=tools,toolbar_location="left",
            plot_width=1100, plot_height=700)
p2.patches('x2','y2',source=source2)
p2.patches(state_xs,state_ys,fill_alpha=0.2,line_color='#288bd0',line_width=2)
hover2 = p2.select_one(HoverTool)
hover2.point_policy = "follow_mouse"
hover2.tooltips = [
    ("(x,y)","($x2, $y2)"),
]

output_file('color_bar.html')
color_mapper = LogColorMapper(palette=myPalette, low=1, high=1e7)
color_bar = ColorBar(color_mapper=color_mapper, ticker=LogTicker(),
                     label_standoff=12, border_line_color=None, location=(0,-10))
p.add_layout(color_bar, 'right')

output_file("slider.html")

p1 = p
tab1 = Panel(child=p1, title="Map1")
tab2 = Panel(child=p2, title="Map2")
tabs = Tabs(tabs=[ tab1, tab2 ])
show(tabs)