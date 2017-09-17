from bokeh.io import show
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_states import data as us_states
from bokeh.sampledata.us_counties import data as us_counties
from bokeh.sampledata.unemployment import data as unemployment

palette.reverse()

state_xs = [us_states[code]["lons"] for code in us_states]
state_ys = [us_states[code]["lats"] for code in us_states]

county_xs = [us_counties[code]["lons"] for code in us_counties
             if us_counties[code]["state"] not in ["ak","hi","pr","gu","vi","mp","as"]]
county_ys = [us_counties[code]["lats"] for code in us_counties
             if us_counties[code]["state"] not in ["ak","hi","pr","gu","vi","mp","as"]]

for county_id in us_counties:
    if us_counties[county_id]["state"] in ["ak","hi","pr","gu","vi","mp","as"]:
        continue
    try:
      rate = unemployment[county_id]
      # idx = min(int(rate/2),5)
      color_mapper = LogColorMapper(palette=palette)
    except KeyError :
        continue

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    tools = TOOLS
)
p.grid.grid_line_color = None

p.patches(county_xs,county_ys,fill_color={'transform': color_mapper},fill_alpha=0.7,line_color="white",line_width=0.5)
p.patches(state_xs,state_ys,fill_color={'transform': color_mapper},fill_alpha=0.7,line_color="black",line_width=0.7)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
        ("Name", "@name"),
        ("Unemployment rate)", "@rate%"),
        ("(Long, Lat)", "($x, $y)"),
]

show(p)
