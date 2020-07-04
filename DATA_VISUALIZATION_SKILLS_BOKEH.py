# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:48:14 2020

@author: crein
"""

import numpy as np


# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show



fertility = np.array([ 1.769,  2.682,  2.077,  2.132,  1.827,  3.872,  2.288,  5.173,
        1.393,  1.262,  2.156,  3.026,  2.033,  1.324,  2.816,  5.211,
        2.1  ,  1.781,  1.822,  5.908,  1.881,  1.852,  1.39 ,  2.281,
        2.505,  1.224,  1.361,  1.468,  2.404,  5.52 ,  4.058,  2.223,
        4.859,  1.267,  2.342,  1.579,  6.254,  2.334,  3.961,  6.505,
        2.53 ,  2.823,  2.498,  2.248,  2.508,  3.04 ,  1.854,  4.22 ,
        5.1  ,  4.967,  1.325,  4.514,  3.173,  2.308,  4.62 ,  4.541,
        5.637,  1.926,  1.747,  2.294,  5.841,  5.455,  7.069,  2.859,
        4.018,  2.513,  5.405,  5.737,  3.363,  4.89 ,  1.385,  1.505,
        6.081,  1.784,  1.378,  1.45 ,  1.841,  1.37 ,  2.612,  5.329,
        5.33 ,  3.371,  1.281,  1.871,  2.153,  5.378,  4.45 ,  1.46 ,
        1.436,  1.612,  3.19 ,  2.752,  3.35 ,  4.01 ,  4.166,  2.642,
        2.977,  3.415,  2.295,  3.019,  2.683,  5.165,  1.849,  1.836,
        2.518,  2.43 ,  4.528,  1.263,  1.885,  1.943,  1.899,  1.442,
        1.953,  4.697,  1.582,  2.025,  1.841,  5.011,  1.212,  1.502,
        2.516,  1.367,  2.089,  4.388,  1.854,  1.748,  2.978,  2.152,
        2.362,  1.988,  1.426,  3.29 ,  3.264,  1.436,  1.393,  2.822,
        4.969,  5.659,  3.24 ,  1.693,  1.647,  2.36 ,  1.792,  3.45 ,
        1.516,  2.233,  2.563,  5.283,  3.885,  0.966,  2.373,  2.663,
        1.251,  2.052,  3.371,  2.093,  2.   ,  3.883,  3.852,  3.718,
        1.732,  3.928])

female_literacy = np.array([  90.5,   50.8,   99. ,   88.8,   90.2,   40. ,   49.8,   48.8,
         99.4,   99. ,   91.5,   93.9,   90.2,   99. ,   57.8,   22.8,
         81.3,   77.2,   91.5,   56.1,   99. ,   99. ,   98.5,   89.2,
         88.1,   96.6,   99.6,   96.9,   93.4,   66.3,   59.6,   97.7,
         82.8,   99.3,   63.9,   99. ,   66.8,   44.1,   69.2,   12.6,
         84.6,   45.4,   94.9,   98.9,   89.8,   80.2,  100. ,   59.3,
         42.8,   40.1,   96.9,   44.3,   77.2,   89.1,   65.3,   67.8,
         57. ,   98.7,   99. ,   99.5,   21.6,   65.8,   15.1,   70.9,
         68.7,   81.7,   18.2,   61. ,   88.8,   33. ,   95.9,   99.8,
         21.9,   99. ,   92.9,   99. ,   71. ,   98.9,   88.3,   26.4,
         66.1,   86. ,   99.7,   99. ,   99.2,   28.1,   59.9,   99. ,
         97.9,   96.2,   83.5,   95.9,   99.5,   55.6,   53.7,   81.3,
         93.5,   63.2,   81.4,   88.9,   77.9,   28.9,   99. ,  100. ,
         99.1,   99.3,   54.5,   91.6,  100. ,   96.2,   91.5,   98. ,
         99. ,   41.1,   99.7,   99. ,   86. ,   53. ,   95.9,   97.8,
         92.8,   99.7,   98.5,   49.5,   98.7,   99.4,   80.9,   93.1,
         90.8,   97.8,   99.8,   87.7,   95.1,   95.4,   99.7,   83.5,
         34.3,   36.5,   83.2,   99.8,   98.2,   90.4,   84.8,   85.6,
         96.7,   89.4,   38.7,   89.1,   67.8,   90.7,   88.4,   79.3,
         93.5,   93.3,   96.5,   99. ,   98.4,   79.5,   98.5,   83.3,
         98. ,   99.1])



fertility_latinamerica = np.array([ 1.827,  2.156,  2.404,  2.223,  2.53 ,  2.498,  1.926,  4.018,
        2.513,  1.505,  2.612,  3.371,  3.19 ,  2.977,  2.295,  2.683,
        1.943,  2.516,  2.089,  2.362,  1.647,  2.373,  3.371,  1.732])



female_literacy_latinamerica = np.array([ 90.2,  91.5,  93.4,  97.7,  84.6,  94.9,  98.7,  68.7,  81.7,
        99.8,  88.3,  86. ,  83.5,  93.5,  81.4,  77.9,  96.2,  92.8,
        98.5,  90.8,  98.2,  88.4,  96.5,  98. ])



fertility_africa = np.array([ 5.173,  2.816,  5.211,  5.908,  2.505,  5.52 ,  4.058,  4.859,
        2.342,  6.254,  2.334,  4.22 ,  4.967,  4.514,  4.62 ,  4.541,
        5.637,  5.841,  5.455,  7.069,  5.405,  5.737,  3.363,  4.89 ,
        6.081,  1.841,  5.329,  5.33 ,  5.378,  4.45 ,  4.166,  2.642,
        5.165,  4.528,  4.697,  5.011,  4.388,  3.29 ,  3.264,  2.822,
        4.969,  5.659,  3.24 ,  1.792,  3.45 ,  5.283,  3.885,  2.663,
        3.718])


female_literacy_africa = np.array([ 48.8,  57.8,  22.8,  56.1,  88.1,  66.3,  59.6,  82.8,  63.9,
        66.8,  44.1,  59.3,  40.1,  44.3,  65.3,  67.8,  57. ,  21.6,
        65.8,  15.1,  18.2,  61. ,  88.8,  33. ,  21.9,  71. ,  26.4,
        66.1,  28.1,  59.9,  53.7,  81.3,  28.9,  54.5,  41.1,  53. ,
        49.5,  87.7,  95.1,  83.5,  34.3,  36.5,  83.2,  84.8,  85.6,
        89.1,  67.8,  79.3,  83.3])


CREATING A FIGURE WITH A CIRCLE AND X GLYPH

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.wedge(fertility, female_literacy, 10,45)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot

show(p)





CREATING A FIGURE WITH A CIRCLE AND X GLYPH

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color='blue',size=10,alpha=0.8)

# Add a red circle glyph to the figure p
p.x(fertility_africa, female_literacy_africa, color='red',size=10,alpha=0.8)

# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)




CUSTOMIZING YOUR PLOT

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, color='blue',size=10,alpha=0.8)

# Add a red circle glyph to the figure p
p.circle(fertility_africa, female_literacy_africa, color='red',size=10,alpha=0.8)

# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)






BOKEH LINE GLYPH
# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create a figure with x_axis_type="datetime": p
p = figure(x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x axis and price along the y axis
p.line(date,price)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)



# Import figure from bokeh.plotting
from bokeh.plotting import figure

#Since we are plotting dates on the x-axis, you must add x_axis_type='datetime' when creating the figure object.
# Create a figure with x_axis_type='datetime': p
p = figure(x_axis_type='datetime', x_axis_label='Date', y_axis_label='US Dollars')

# Plot date along the x-axis and price along the y-axis

p.line(date,price)
# With date on the x-axis and price on the y-axis, add a white circle glyph of size 4
p.circle(date,price,fill_color='white', size=4)

# Specify the name of the output file and show the result
output_file('line.html')
show(p)


 
USING BOKEH PATCHES
 
# Extended geometrical shapes can be plotted by using the patches() glyph function

# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats, ut_lats]

# Add patches to figure p with line_color=white for x and y
p.patches(x,y,line_color='white')

# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)





PLOTTING DATA FROM NUMPY ARRAYS

# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt
# Create array using np.linspace: x
x = np.linspace(0, 5, 100)

# Create array using np.cos: y
y = np.cos(x)

# Add circles at x and y
p.circle(x, y)

# Specify the name of the output file and show the result
output_file('numpy.html')
show(p)



PLOTTING DATA FROM PANDAS DATAFRAMES
# Import pandas as pd
from bokeh.io import output_file, show
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('auto.csv')

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Create the figure: p
p = figure(x_axis_label='HP', y_axis_label='MPG')

# Plot mpg vs hp by color using appropriate columns from dataframe df
p.circle(df['hp'],df['mpg'], color= df['color'], size=10)

# Specify the name of the output file and show the result
output_file('auto-df.html')
show(p)


'''
ColumnDataSource is the object where the data of a Bokeh graph is stored. 
You can choose not to use a ColumnDataSource and feed your graph directly 
with Python dictionaries, pandas dataframes, etc, but for certain features 
such as having a popup window showing data information when the user hovers
 the mouse on glyphs, you are forced to use a ColumnDataSource otherwise the
 popup window will not be able to get the data. Other uses would be when streaming data.
You can create a ColumnDataSource from dictionaries and pandas dataframes 
and then use the ColumnDataSource to create the glyphs.'''

# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource

# Create a ColumnDataSource: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p.circle(x='Year', y='Time', color='color', size=8, source=source)

# Specify the name of the output file and show the result
output_file('sprint.html')
show(p)



# Create a figure with the "box_select" tool: p
p = figure(x_axis_label='Year', y_axis_label='Time', tools=
'box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle(x='Year', y='Time', selection_color='red', nonselection_alpha=0.1, source=source)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)





ADDING BOX SELECTION AND NON SELECTION GLYPHS

# Create a figure with the "box_select" tool: p
p = figure(x_axis_label='Year', y_axis_label='Time', tools=
'box_select')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle(x='Year', y='Time', selection_color='red', nonselection_alpha=0.1, source=source)

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)






ADDING A HOVERTOOL

# import the HoverTool
from bokeh.models import HoverTool

# Add a circle glyphs to figure p
p.circle(x, y, size=10,
         fill_color='grey', alpha=0.1, line_color=None,
         hover_fill_color='firebrick', hover_alpha=0.5,
         hover_line_color='white')

# Create a HoverTool: hover
hover = HoverTool(tooltips=None, mode='vline')

# Add the hover tool to the figure p 
p.add_tools(hover)

# Specify the name of the output file and show the result
output_file('hover_glyph.html')
show(p)




COLORMAPPING

"""
The CategoricalColorMapper is used to color each
glyph by a categorical property

"""

#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper, HoverTool
from bokeh.plotting import ColumnDataSource, figure

# Convert df to a ColumnDataSource: source
source = ColumnDataSource(df)

# Make a CategoricalColorMapper object: color_mapper
color_mapper = CategoricalColorMapper(factors=['Europe', 'Asia', 'US'],
                                      palette=['red', 'green', 'blue'])

# Add a circle glyph to the figure p
p.circle(x='weight',y='mpg', source=source,
            legend='origin',
            color={'field':'origin',
                   'transform':color_mapper})

p.legend.location = 'top_left'
p.title = 'Weight vs MPG'
# Specify the name of the output file and show the result
output_file('colormap.html')
show(p)






LAYOUTS(collections of bokeh figure objects)

from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import column, row


source = ColumnDataSource(df)

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p1
p1.circle('fertility', 'female_literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='population', y_axis_label='female_literacy (% population)')

# Add a circle glyph to p2
p2.circle('population', 'female_literacy', source=source)

# Put p1 and p2 into a horizontal row: layout
layout = row(p1,p2) #can also use vertical column

# Specify the name of the output_file and show the result
output_file('fert_row.html')
show(layout)






NESTED LAYOUT

# mpg_hp, mpg_weight, avg_mpg, row2 are all bokeh figures
# Import column and row from bokeh.layouts
from bokeh.layouts import column, row

# Make a column layout that will be used as the second row: row2
row2 = row([mpg_hp, mpg_weight], sizing_mode='scale_width')


# nested layout using row2 from above
# Make a row layout that includes the above column layout: layout
layout = column([avg_mpg, row2], sizing_mode='scale_width')

# Specify the name of the output_file and show the result
output_file('layout_custom.html')
show(layout)





GRIDPLOT


# Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot

'''each plot is a list of two lists of the same length each data point
in one list matches up with the corresponding data point in the other
list to create the plot'''
# Create a list containing plots p1 and p2: row1
row1 = [p1,p2]

# Create a list containing plots p3 and p4: row2
row2 = [p3,p4]

# Create a gridplot using row1 and row2: layout
layout = gridplot([row1,row2])

# Specify the name of the output_file and show the result
output_file('grid.html')
show(layout)




CREATING TABS FOR YOUR PLOTS

# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Tabs, Panel

# Create tab1 from plot p1: tab1
tab1 = Panel(child=p1, title='Latin America')

# Create tab2 from plot p2: tab2
tab2 = Panel(child=p2, title='Africa')

# Create tab3 from plot p3: tab3
tab3 = Panel(child=p3, title='Asia')

# Create tab4 from plot p4: tab4
tab4 = Panel(child=p4, title='Europe')
 

# Create a Tabs layout: layout
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

# Specify the name of the output_file and show the result
output_file('tabs.html')
show(layout)



LINKING PLOTS

# when one plot is zoomed or dragged, one or more of the other plots will respond
# Link the x_range of p2 to p1: p2.x_range
p2.x_range = p2.x_range = p1.x_range

# Link the y_range of p2 to p1: p2.y_range
p2.y_range = p2.y_range = p1.y_range

# Link the x_range of p3 to p1: p3.x_range
p3.x_range = p3.x_range = p1.x_range

# Link the y_range of p4 to p1: p4.y_range
p4.y_range = p4.y_range = p1.y_range

# Specify the name of the output_file and show the result
output_file('linked_range.html')
show(layout)






LINKED BRUSHING

# can also link plots  with bokeh glyphs that share the same ColumnDataSource


from bokeh.io import output_file, show
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import column, row

# Create ColumnDataSource: source
source = ColumnDataSource(data)

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select')

# Add a circle glyph to p1
p1.circle('fertility','female literacy', source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',
            tools='box_select,lasso_select')

# Add a circle glyph to p2

p2.circle('fertility','population', source=source)

# Create row layout of figures p1 and p2: layout
layout = row(p1,p2)

# Specify the name of the output_file and show the result
output_file('linked_brush.html')
show(layout)






CREATING LEGENDS

# Add the first circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=latin_america, size=10, color='red', legend='Latin America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'female_literacy', source=africa, size=10, color='blue', legend='Africa')


POSITIONING AND STYLING LEGENDS

# Assign the legend to the bottom left: p.legend.location
p.legend.location = 'bottom_left'

# Fill the legend background with the color 'lightgray': p.legend.background_fill_color
p.legend.background_fill_color = 'lightgray'



# Specify the name of the output_file and show the result
output_file('fert_lit_groups.html')
show(p)







ADDING A HOVER TOOLTIP

# Import HoverTool class from bokeh.models library
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips=[ ('Country', '@Country')]) # @ extracts the data rom the Country column of the dataframe

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)



ANOTHER HOVERTOOL EXAMPLE

from bokeh.models import HoverTool

 hover = HoverTool(tooltips=[
         ('species name', '@species'),
         ('petal length', '@petal_length),
         ('sepal length', '@sepal_length')
         ])

plot = figure(tools=[hover, 'pan', 'wheel_zoom'])




INTERACTIVE BOKEH APP WITH THE BOKEH SERVER (CONNECTING PLOTS TO LIVE PYTHON CODE)

# Perform necessary imports
from bokeh.plotting import figure
from bokeh.io import curdoc 
'''
curdoc used for building an interactive Bokeh app
it will  hold all the plots, controls, and layouts that you create
'''

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line([1,2,3,4,5], [2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)





ADDING MULTIPLE SLIDERS TO YOUR BOKEH APP

 # Perform necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create first slider: slider1
slider1 = Slider(title='slider1', start=0, end=10, step=0.1, value=2)

# Create second slider: slider2
slider2 = Slider(title='slider2', start=10, end=100, step=1, value=20)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1,slider2)

# Add the layout to the current document
curdoc().add_root(layout)




BOKEH MODELS INTO LAYOUTS
'''
Create ColumnDataSource: source manually to update 
the data interactively
'''
source = ColumnDataSource(data={'x': x, 'y': y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)




WIDGET CALLBACKS
'''
Define a callback function: callback
with the attribute that changed with old and new values:
'''
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
 '''
the name of the property you want to watch and the 
callback as the first and second arguments respectively
'''

# callback to execute whenever the value of the slider changes
slider.on_change('value', callback)
'''
Create layout and add to current document, here the 
widgetbox(slider) will be above the plot column-wise
'''
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)



USING DROPDOWN CALLBACKS TO UPDATE DATA SOURCES

# Perform necessary imports
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.layouts import column, row


# Create ColumnDataSource: source, these are taken from dataframe columns
source = ColumnDataSource(data={
    'x' : fertility,
    'y' : female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy': 
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : fertility,
            'y' : population
            }

# Create a dropdown Select widget: select    
select = Select(title="distribution", options=['female_literacy', 'population'], value = 'female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)



SYNCHRONIZE TWO DROPDOWNS

# Create two dropdown Select widgets: select1, select2
select1 = Select(title='First', options=['A', 'B'], value='A')
select2 = Select(title='Second', options=['1', '2', '3'], value='1')

# Define a callback function: callback
def callback(attr, old, new):
    # If select1 is 'A' 
    if select1.value == 'A':
        # Set select2 options to ['1', '2', '3']
        select2.options = ['1', '2', '3']
        
        # Set select2 value to '1'
        select2.value = '1'
    else:
        # Set select2 options to ['100', '200', '300']
        select2.options = ['100', '200', '300']
        
        # Set select2 value to '100'
        select2.value = '100'

# Attach the callback to the 'value' property of select1
select1.on_change('value', callback)

# Create layout and add to current document
layout = widgetbox(select1, select2)
curdoc().add_root(layout)




BUTTON WIDGETS AND STYLES


from bokeh.models import CheckboxGroup, RadioGroup, Toggle
from bokeh.models import Button
from bokeh.layouts import widgetbox

# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():
    
    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x': x, 'y': y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)



# Add a Toggle: toggle
toggle = Toggle(label='Toggle button', button_type='success')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox(toggle, checkbox, radio))



BOKEH PLOT EXAMPLES

# Perform necessary imports
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
          'x' : data.loc[1970,'fertility'],
          'y' : data.loc[1970,'life'],
    'country' : data.loc[1970,'Country']
})

# Create the figure: p
p = figure(title='1970', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@country')])








# Add a circle glyph to the figure p
p.circle(x='x', y='y', source=source)

# Output the file and show the figure
output_file('gapminder.html')
show(p)
    

# create plots and widgets
# add callbacks
# arrange plots and widgets in layouts


# Import the necessary modules
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country' : data.loc[1970].Country,
    'pop'     : data.loc[1970].population,
    'region'  : data.loc[1970].region,
})

# Save the minimum and maximum values of the fertility column: xmin, xmax
xmin, xmax = data.fertility.min(), data.fertility.max()

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
ymin, ymax = data.life.min(), data.life.max()

# Create the figure: plot
plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700, 
              x_range=(xmin, xmax), y_range=(ymin, ymax), x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)')

# Add circle glyphs to the plot
plot.circle(x='x', y='y', fill_alpha=0.8, fill_color='red', source=source)

# Set the x-axis label
#plot.xaxis.axis_label ='Fertility (children per woman)'

# Set the y-axis label
#plot.yaxis.axis_label = 'Life Expectancy (years)'

# Add the plot to the current document and add a title
curdoc().add_root(plot)
curdoc().title = 'Gapminder'



ENHANCE PLOT DELINEATING REGIONS WITH CATEGORICAL COLOR MAPPER

# Make a list of the unique values from the region column: regions_list
regions_list = list(data.region.unique())#.tolist(), this will be added to your glyph

# Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6#Magma 

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

# Add the color mapper to the circle glyph
plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'top_right'
plot.title.text = 'Gapminder'

# Add the plot to the current document and add the title
curdoc().add_root(plot)
#curdoc().title = 'Gapminder'



ADDING A SLIDER AND A CALLBACK FOR DYNAMIC DATA

# Import the necessary modules
from bokeh.layouts import row, widgetbox
from bokeh.models import Slider

# Define the callback function: update_plot
def update_plot(attr, old, new):
    # Set the yr name to slider.value and new_data to source.data
    yr = slider.value
    new_data = {
        'x'       : data.loc[yr].fertility,
        'y'       : data.loc[yr].life,
        'country' : data.loc[yr].Country,
        'pop'    :  data.loc[yr].population,
        'region'  : data.loc[yr].region,
    }
    source.data = new_data


# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)
curdoc().add_root(layout)



CUSTOMIZING CALLBACK FUNCTION FOR USER INPUT IN THE SLIDER

# Define the callback function: update_plot
def update_plot(attr, old, new):
    # Assign the value of the slider: yr
    yr = slider.value
    # Set new_data
    new_data = {
        'x'       : data.loc[yr].fertility,
        'y'       : data.loc[yr].life,
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to: source.data
    source.data = new_data

    # Add title to figure: plot.title.text
    '''
    formatting strings by specifying placeholders with the % keyword for printing values 
    that are not static such as the value of the slider year
    
    %d is the placeholder for a number that is dynamically updating within you callback function.
    The year display will now be in accordance with the value of the slider year
    '''
    plot.title.text = 'Gapminder data for %d' % yr
    
# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)
curdoc().add_root(layout)


    
ADDING A HOVER TOOL

# Display underlying info in the Data Columns of your Callback function
    
from bokeh.layouts import widgetbox, row
from bokeh.models import Slider, HoverTool
from bokeh.io import curdoc

 # Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool: hover
# 'Country' is a title, '@country' is the column with @ extracting the data for the hovertool
hover = HoverTool(tooltips=[('Country','@country')])

#plot = figure(tools=[hover])

# Amend the plot and add the HoverTool 
plot.add_tools(hover)

# Create layout: layout
layout = row(widgetbox(slider), plot)

# Add layout to current document
curdoc().add_root(layout)


ADDING DROPDOWN MENUS FOR INTERACIVE DATA SELECTION

from bokeh.models import  Slider, Select, HoverTool
from bokeh.layouts import WidgetBox, row
from bokeh.io import curdoc

# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    '''
    Label axes of plot dynamically as x, y values 
      change in the callback function
    '''
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    
    # Set new_data
    new_data = {
        'x'       : data.loc[yr][x],
        'y'       : data.loc[yr][y],
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes using updated x,y values
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr

# Create a dropdown slider widget: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data'
)

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data'
)

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)



# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)



    
    
    



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 