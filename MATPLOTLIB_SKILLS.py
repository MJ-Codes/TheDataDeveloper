# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 18:39:48 2020

@author: crein
"""
CREATE A FIGURE AND AN AXIS

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()


ADDING DATA TO AN AXES OBJECT WITH ALTERNAIVE PLT.SUBPLOT METHOD

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()
#_ = plt.subplot(2,1,1)

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
#_ = plt.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

#_ = plt.subplot(2,1,2)
# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["MONTH"], austin_weather['MLY-PRCP-NORMAL'])
#_ = plt.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# Call the show function
plt.show()




CUSTOMIZING DATA APPEARANCE


colors = {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}

markers = 
"."	m00	point
","	m01	pixel
"o"	m02	circle
"v"	m03	triangle_down
"^"	m04	triangle_up
"<"	m05	triangle_left
">"	m06	triangle_right
"1"	m07	tri_down
"2"	m08	tri_up
"3"	m09	tri_left
"4"	m10	tri_right
"8"	m11	octagon
"s"	m12	square
"p"	m13	pentagon
"P"	m23	plus (filled)
"*"	m14	star
"h"	m15	hexagon1
"H"	m16	hexagon2
"+"	m17	plus
"x"	m18	x
"X"	m24	x (filled)
"D"	m19	diamond
"d"	m20	thin_diamond
"|"	m21	vline
"_"	m22	hline


line-styles
'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style



# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"],
        color='b', marker='o', linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"],
        color='r', marker='v', linestyle='--')

# Call show to display the resulting plot
plt.show()





CUSTOMIZING AXIS LABELS AND ADDING TITLES

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")
# plt.xlabel()

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")
# plt.ylabel()

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")
#plt.title()

# Display the figure
plt.show()





CREATING MULTIPLE SUBPLOTS

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()




CREATING SUBPLOTS WITH A SHARED Y AXIS SCALE(Sharey=True)

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation in the top axes
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color='b', linestyle='--')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color='b', linestyle='--')

# Plot Austin precipitation in the bottom axes
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color='r', linestyle='--')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color='r', linestyle='--')

plt.show()



CREATING A DATATIME INDEX ON IMPORT

# Import pandas
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")




PLOTTING TIME SERIES DATA

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label 
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()


import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()





PLOTTING TWO VARIABLES ON THE SAME X-AXIS

import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color='red')

plt.show()




TIME SERIES PLOTTING FUNCTION

# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color,)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)
  
  
  
fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create a twin Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)", "Relative temperature (Celsius)")

plt.show()



USING ANNOTATION ON TIME SERIES PLOT

fig, ax = plt.subplots()

# Plot the relative temperature data
ax.plot(climate_change.index, climate_change['relative_temp'])

# Annotate the date at which temperatures exceeded 1 degree
ax.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1))

plt.show()



fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)", "Relative temp (Celsius)")

# Annotate the point with relative temperature >1 degree
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={'arrowstyle':'->', 'color':'gray'})

plt.show()



PLOTTING BAR CHARTS

# Bar charts show us the values of one variable across different conditions
# Organized into categories
fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation=90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





STACKED BAR CHARTS

# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals["Gold"], label="Gold")

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals["Silver"], bottom=medals["Gold"], label="Silver")

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals["Bronze"], bottom=medals["Silver"] + medals["Gold"], label="Bronze")

# Display the legend
ax.legend()

plt.show()

import numpy as np
import matplotlib.pyplot as plt

countries = ['Norway', 'Germany', 'Canada', 'United States', 'Netherlands']
bronzes = np.array([10,7,10,6,6])
silvers = np.array([14,10,8,8,6])
golds = np.array([14,14,11,9,8])
ind = [country for country in countries]
 
plt.bar(ind, golds, width=0.6, label='golds', color='gold'), bottom=silvers+bronzes)
plt.bar(ind, silvers, width=0.6, label='silvers', color='silver', bottom=bronzes)
plt.bar(ind, bronzes, width=0.6, label='bronzes', color='#CD7F32')
 
plt.xticks(ind)
plt.ylabel("Medals")
plt.xlabel("Countries")
plt.legend(loc="upper right")
plt.title("2018 Winter Olympics Top Scorers")
plt.show()
  

CREATING HISTOGRAMS

# Histograms compare total distributions of data
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()



fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"], histtype='step', label="Rowing", bins=5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"], histtype='step', label="Gymnastics", bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()



ADDING ERROR-BARS TO A BAR CHART

# Error Bars tell us something about the distribution of the data through a summary
fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std, yerr creates an error-bar of its standard deviation
ax.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std, yerr creates an error-bar of its standard deviation
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr=mens_gymnastics["Height"].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()


ADDING ERROR-BARS TO A LINE PLOT

fig, ax = plt.subplots()

# Adding error-bars to a plot is done by using the errorbars method of the Axes object WITH YERR
# Add the Seattle temperature data in each month with standard deviation error bars
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add the Austin temperature data in each month with standard deviation error bars
ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()




CREATING BOX PLOTS

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing", "Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()




CREATING SCATTER PLOTS
# The standard visualization for visually distinct bivariate comparisons
# Compares the values of different variables across observations(bivariate comparisons)


fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change["co2"], climate_change["relative_temp"])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()



ENCODING TIME BY COLOR

fig, ax = plt.subplots()

"""
c key-word argument is used to pass in the index of the DataFrame as input to
color each point according to its date

"""
# Add data: "co2", "relative_temp" as x-y
ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()


SWITCHING BETWEEN STYLES

# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()


SAVING YOUR VISUALIZATONS

# Save as a PNG file
fig.savefig('my_figure.png')

# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png', dpi=300)

# Set figure dimensions and save as a PNG
fig.set_size_inches([3, 5])
fig.savefig('figure_3_5.png')



EXTRACTING UNIQUE VALUES IN A COLUMN

# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)



AUTOMATE YOUR VISUALIZATIONS DEPENDING ON DATA INPUT

fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
  # Extract the rows only for this sport
  sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig("sports_weights.png")






import numpy as np
import matplotlib.pyplot as plt




#PLotting Distributions
year = np.array([1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
       1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991,
       1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
       2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011])


physical_sciences = np.array([13.8, 14.9, 14.8, 16.5, 18.2, 19.1, 20. , 21.3, 22.5, 23.7, 24.6,
       25.7, 27.3, 27.6, 28. , 27.5, 28.4, 30.4, 29.7, 31.3, 31.6, 32.6,
       32.6, 33.6, 34.8, 35.9, 37.3, 38.3, 39.7, 40.2, 41. , 42.2, 41.1,
       41.7, 42.1, 41.6, 40.8, 40.7, 40.7, 40.7, 40.2, 40.1])

computer_science = np.array([13.6, 13.6, 14.9, 16.4, 18.9, 19.8, 23.9, 25.7, 28.1, 30.2, 32.5,
       34.8, 36.3, 37.1, 36.8, 35.7, 34.7, 32.4, 30.8, 29.9, 29.4, 28.7,
       28.2, 28.5, 28.5, 27.5, 27.1, 26.8, 27. , 28.1, 27.7, 27.6, 27. ,
       25.1, 22.2, 20.6, 18.6, 17.6, 17.8, 18.1, 17.6, 18.2])


education = np.array([74.53532758, 74.14920369, 73.55451996, 73.50181443, 73.33681143,
       72.80185448, 72.16652471, 72.45639481, 73.19282134, 73.82114234,
       74.98103152, 75.84512345, 75.84364914, 75.95060123, 75.86911601,
       75.92343971, 76.14301516, 76.96309168, 77.62766177, 78.11191872,
       78.86685859, 78.99124597, 78.43518191, 77.26731199, 75.81493264,
       75.12525621, 75.03519921, 75.1637013 , 75.48616027, 75.83816206,
       76.69214284, 77.37522931, 78.64424394, 78.54494815, 78.65074774,
       79.06712173, 78.68630551, 78.72141311, 79.19632674, 79.5329087 ,
       79.61862451, 79.43281184])

health = np.array([77.1, 75.5, 76.9, 77.4, 77.9, 78.9, 79.2, 80.5, 81.9, 82.3, 83.5,
       84.1, 84.4, 84.6, 85.1, 85.3, 85.7, 85.5, 85.2, 84.6, 83.9, 83.5,
       83. , 82.4, 81.8, 81.5, 81.3, 81.9, 82.1, 83.5, 83.5, 85.1, 85.8,
       86.5, 86.5, 86. , 85.9, 85.4, 85.2, 85.1, 85. , 84.8])



MULTIPLE PLOTS ON ONE AXIS

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')


# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')




DEFINING AXES MANUALLY

# Create plot axes for the first line plot
plt.axes([0.05,0.05,0.425,0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
plt.axes([0.525, 0.05,0.425, 0.9])

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science,color='red')




CREATING SUBPLOTS

# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(2,1,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(2,1,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()



# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2,2,1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the top right subplot active in the current 2x2 subplot grid 
plt.subplot(2,2,2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2,2,3)

# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2,2,4)

# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='black')
plt.title('Education')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()


CUSTOMIZING AXES

# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red') 
plt.plot(year, physical_sciences, color='blue')

# Add the axis labels
plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Set the x-axis range
plt.xlim(1990,2010)

# Set the y-axis range
plt.ylim(0,50)

#or you can use this
# Set the x-axis and y-axis limits
plt.axis((1990,2010,0,50))

# Add a title and display the plot
plt.title('Degrees awarded to women (1990-2010)\nComputer Science (red)\nPhysical Sciences (blue)')
plt.show()

# Save the image as 'xlim_and_ylim.png'
plt.savefig('xlim_and_ylim.png')




# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science') 

# Specify the label 'Physical Sciences' 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

# Add a legend at the lower center
plt.legend(loc='lower center')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()


USING PLT.ANNOTATE

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')

# Add a black arrow annotation
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='orange'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()




CHANGING STYLES

# Set the style to 'ggplot'
plt.style.use('ggplot')

# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1) 

# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Add annotation
cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))

# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()



PLOTTING MULTIPLE TIME SERIES SLICES

# Plot the series in the top subplot in blue
plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001 to 2011')
plt.plot(aapl, color='blue')

# Slice aapl from '2007' to '2008' inclusive: view
view = aapl['2007':'2008']

# Plot the sliced data in the bottom subplot in black
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()
plt.show()


PLOTTING AS INSET VIEW

# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']

# Plot the entire series 
plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')

# Specify the axes for the inset view
plt.axes([0.25, 0.5, 0.35, 0.35])

# Plot the sliced series in red using the current axes
plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()




PLOTTING MOVING AVERAGES

# Each moving_avg subplot in overlayed with its main plot(aapl) in dash/dot line style
# Plot the 30-day moving average in the top left subplot in green
plt.subplot(2, 2, 1)
plt.plot(mean_30, 'green')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('30d averages')
plt.show()

# Plot the 75-day moving average in the top right subplot in red
plt.subplot(2, 2, 2)
plt.plot(mean_75, 'red')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('75d averages')

# Plot the 125-day moving average in the bottom left subplot in magenta
plt.subplot(2, 2, 3)
plt.plot(mean_125, 'magenta')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('125d averages')

# Plot the 250-day moving average in the bottom right subplot in cyan
plt.subplot(2, 2, 4)
plt.plot(mean_250, 'cyan')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')

# Display the plot
plt.show()



















PLOTTING SMOOTH FUNCTIONS

#Plotting Smooth Functions
# Generate two 1-D arrays: u, v
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y and build an image with meshgrid
X,Y = np.meshgrid(u,v)

#Compute Z based on X and Y.  Z compiles into 1 2d array from 2 2d arrays(X,Y)
Z = np.sin(3*np.sqrt(X**2 + Y**2)) #f(x,y) = sinΘ(3*√(x² +  y²))

'''Display the resulting image with pseudocolor:pcolor()
When displaying a 2-D array with plt.imshow() or plt.pcolor(),
the values of the array are mapped to a corresponding 
color.The set of colors used is determined by a colormap(plt.set_cmap) 
which smoothly maps values to colors, making it easy to
understand the structure of the data at a glance.'''

plt.set_cmap('inferno')
plt.pcolor(Z)
plt.show()

# Save the figure to 'sine_mesh.png'
plt.savefig('sine_mesh.png')



VISUALIZING BIVARIATE FUNCTIONS
# using data from above
# Generate a default contour map of the array Z
plt.subplot(2,2,1)
plt.contour(X,Y,Z)

# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(X,Y,Z,20)

# Generate a default filled contour map of the array Z
plt.subplot(2,2,3)
plt.contourf(X,Y,Z)

# Generate a default filled contour map with 20 contours
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20)

# Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()


# Create a filled contour plot with a color map of 'viridis'
plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()

plt.title('Viridis')

# Create a filled contour plot with a color map of 'gray'
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

# Create a filled contour plot with a color map of 'autumn'
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20, cmap='autumn')
plt.title('Autumn')
plt.colorbar()

# Create a filled contour plot with a color map of 'winter'
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20, cmap='winter')
plt.title('Winter')
plt.colorbar()

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()



hp = np.array([ 88, 193,  60,  98,  78, 100,  75,  76, 130, 140,  52,  88,  84,
       148, 150, 130,  58,  82,  65, 110,  95, 110, 140, 170,  78,  90,
        96,  95, 110,  75, 132, 150,  83,  85,  86,  75, 140, 139,  70,
        52,  60,  84, 138, 180,  65,  67,  97, 150,  70, 100, 180, 129,
        95,  90,  83,  75, 100,  85, 112,  67,  65,  88, 100,  75, 100,
        70, 145, 110, 210,  80, 145,  69, 150, 198, 120,  92,  90, 115,
        95,  75,  76,  67,  71, 115,  84,  91, 150, 215,  67, 175,  60,
       175, 110,  95,  68, 150,  67,  95, 110, 105, 102, 110,  89,  66,
        88,  75,  78, 105,  70, 103,  60, 150,  72, 170,  90, 110,  58,
       152, 145, 139,  83,  69, 150,  67,  80,  71,  46, 105,  90, 110,
       175,  80,  74, 150, 150,  65, 100,  48, 105,  90,  48, 105, 105,
        88, 100,  75, 113, 190,  92,  80, 165, 180,  71,  97,  72, 105,
        90,  75,  88, 155,  68,  90,  84,  87, 112,  87, 125, 108, 142,
        97, 105,  75, 137, 150,  88, 145,  63,  95, 140,  88,  85,  70,
        85, 115,  86,  79, 120, 120,  65, 110, 220, 115, 170, 100,  90,
       225,  85,  65,  97,  90,  90,  49, 110,  70,  92,  53, 100, 190,
        63,  90,  67,  65,  75, 100, 110,  60,  93,  88, 150, 100, 150,
        88, 225,  68,  70, 208, 105,  74,  90, 110,  72,  97,  88,  88,
       129,  85,  86, 150,  70,  48,  77,  65, 175,  90, 150, 110, 130,
        53,  65, 158,  95,  61, 215, 100, 145,  68, 150,  88,  67, 105,
       175, 160,  74, 135, 100,  67, 198, 180, 215, 100, 225, 155, 170,
        81,  85,  95,  80,  92,  70, 149,  84,  97,  52,  72,  85,  52,
        95,  71, 140, 100,  96, 150,  75, 107, 110,  75,  97, 133,  70,
        67, 112, 145, 115,  98,  70,  78, 230,  63,  76, 105,  95,  62,
       165, 165, 160, 190,  95, 180,  78, 120,  80,  75,  68,  67,  95,
       140, 110,  72, 150,  95,  54, 153, 130, 170,  86,  97,  90, 145,
        86,  79, 165,  83,  64,  92,  72, 140, 150,  96, 150,  80, 130,
       100, 125,  90,  94,  76,  90, 150,  97,  85,  81,  78,  46,  84,
        70, 153, 116, 100, 167,  88,  88,  88, 200, 125,  92, 110,  69,
        67,  90, 150,  90,  71, 105,  62,  88, 122,  65,  88,  90,  68,
       110,  88])


mpg = np.array([18. ,  9. , 36.1, 18.5, 34.3, 32.9, 32.2, 22. , 15. , 17. , 44. ,
       24.5, 32. , 14. , 15. , 13. , 36. , 31. , 32. , 21.5, 19. , 17. ,
       16. , 15. , 23. , 26. , 32. , 24. , 21. , 31.3, 32.7, 15. , 23. ,
       17.6, 28. , 24. , 14. , 18.1, 36. , 29. , 35.1, 36. , 16.5, 16. ,
       29.9, 31. , 27.2, 14. , 32.1, 15. , 12. , 17.6, 25. , 28.4, 29. ,
       30.9, 20. , 20.8, 22. , 38. , 31. , 19. , 16. , 25. , 22. , 26. ,
       13. , 19.9, 11. , 28. , 15.5, 26. , 14. , 12. , 24.2, 25. , 22.5,
       26.8, 23. , 26. , 30.7, 31. , 27.2, 21.5, 29. , 20. , 13. , 14. ,
       38. , 13. , 24.5, 13. , 25. , 24. , 34.1, 13. , 44.6, 20.5, 18. ,
       23.2, 20. , 24. , 25.5, 36.1, 23. , 24. , 18. , 26.6, 32. , 20.3,
       27. , 17. , 21. , 13. , 24. , 17. , 39.1, 14.5, 13. , 20.2, 27. ,
       35. , 15. , 36.4, 30. , 31.9, 26. , 16. , 20. , 18.6, 14. , 25. ,
       33. , 14. , 18.5, 37.2, 18. , 44.3, 18. , 28. , 43.4, 20.6, 19.2,
       26.4, 18. , 28. , 26. , 13. , 25.8, 28.1, 13. , 16.5, 31.5, 24. ,
       15. , 18. , 33.5, 32.4, 27. , 13. , 31. , 28. , 27.2, 21. , 19. ,
       25. , 23. , 19. , 15.5, 23.9, 22. , 29. , 14. , 15. , 27. , 15. ,
       30.5, 25. , 17.5, 34. , 38. , 30. , 19.8, 25. , 21. , 26. , 16.5,
       18.1, 46.6, 21.5, 14. , 21.6, 15.5, 20.5, 23.9, 12. , 20.2, 34.4,
       23. , 24.3, 19. , 29. , 23.5, 34. , 37. , 33. , 18. , 15. , 34.7,
       19.4, 32. , 34.1, 33.7, 20. , 15. , 38.1, 26. , 27. , 16. , 17. ,
       13. , 28. , 14. , 31.5, 34.5, 11. , 16. , 31.6, 19.1, 18.5, 15. ,
       18. , 35. , 20.2, 13. , 31. , 22. , 11. , 33.5, 43.1, 25.4, 40.8,
       14. , 29.8, 16. , 20.6, 18. , 33. , 31.8, 13. , 20. , 32. , 13. ,
       23.7, 19.2, 37. , 18. , 19. , 32.3, 18. , 13. , 12. , 36. , 18.2,
       19. , 30. , 15. , 11. , 10. , 16. , 14. , 16.9, 13. , 25. , 21. ,
       21.1, 26. , 28. , 29. , 16. , 26.6, 19. , 32.8, 22. , 19. , 31. ,
       23. , 29.5, 17.5, 19. , 24. , 14. , 28. , 21. , 22.4, 36. , 18. ,
       16.2, 39.4, 30. , 18. , 17.5, 28.8, 22. , 34.2, 30.5, 16. , 38. ,
       41.5, 27.9, 22. , 29.8, 17.7, 15. , 14. , 15.5, 17.5, 12. , 29. ,
       15.5, 35.7, 26. , 30. , 33.8, 18. , 13. , 20. , 32.4, 16. , 27.5,
       23. , 14. , 17. , 16. , 23. , 24. , 27. , 15. , 27. , 28. , 14. ,
       33.5, 39. , 24. , 26.5, 19.4, 15. , 25.5, 14. , 27.4, 13. , 19. ,
       17. , 28. , 22. , 30. , 18. , 14. , 22. , 23.8, 24. , 26. , 26. ,
       30. , 29. , 14. , 25.4, 19. , 12. , 20. , 27. , 22.3, 10. , 19.2,
       26. , 16. , 37.3, 26. , 20.2, 13. , 21. , 25. , 20.5, 37.7, 36. ,
       20. , 37. , 18. , 27. , 29.5, 17.5, 25.1])



VISUALIZING BIVARIATE DISTRIBUTIONS

# Generate a 2-D histogram with region covered using range(a set of 2 tuples)
plt.hist2d(hp,mpg, bins=(20,20), range=((60,235),(8,48)))

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()


# Generate a 2d histogram with hexagonal bins and region covered using extent(a set of 1 tuple)
plt.hexbin(hp, mpg, gridsize=(15,12), extent=((40,235,8,48)))

           
# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()




PLOTTING IMAGES

# Load the image from a file into an array using plt.imread()
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)

# Display the image with imshow()
plt.imshow(img)

# Hide the axes
plt.axis('off')
plt.show()



# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Print the shape of the image
print(img.shape)
print(img)

# Compute the sum of the red, green and blue channels: intensity
intensity = img.sum(axis=2)
print(intensity)

# Print the shape of the intensity
print(intensity.shape)

# Display the intensity with a colormap of 'gray'
plt.imshow(intensity, cmap='gray')

# Add a colorbar
plt.colorbar()

# Hide the axes and show the figure
plt.axis('off')
plt.show()




# Load the image into an array: img
img = plt.imread('480px-Astronaut-EVA.jpg')

# Specify the extent and aspect ratio of the top left subplot
plt.subplot(2,2,1)
plt.title('extent=(-1,1,-1,1),\naspect=0.5') 
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=0.5)

# Specify the extent and aspect ratio of the top right subplot
plt.subplot(2,2,2)
plt.title('extent=(-1,1,-1,1),\naspect=1')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=1)

# Specify the extent and aspect ratio of the bottom left subplot
plt.subplot(2,2,3)
plt.title('extent=(-1,1,-1,1),\naspect=2')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-1,1,-1,1), aspect=2)

# Specify the extent and aspect ratio of the bottom right subplot
plt.subplot(2,2,4)
plt.title('extent=(-2,2,-1,1),\naspect=2')
plt.xticks([-2,-1,0,1,2])
plt.yticks([-1,0,1])
plt.imshow(img, extent=(-2,2,-1,1), aspect=2)

# Improve spacing and display the figure
plt.tight_layout()
plt.show()



RESCALING IMAGES FOR IMPROVED CONTRAST

# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Extract minimum and maximum values from the image: pmin, pmax
pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))

# Rescale the pixels: rescaled_image
rescaled_image = 256*(image - pmin) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." % 
      (rescaled_image.min(), rescaled_image.max()))

# Display the rescaled image
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)

plt.show()




MULTIPLE TIME SERIES ON COMMON AXES


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot the aapl time series in blue
plt.plot(aapl, color='blue', label='AAPL')

# Plot the ibm time series in green
plt.plot(ibm, color='green', label='IBM')

# Plot the csco time series in red
plt.plot(csco, color='red', label='CSCO')

# Plot the msft time series in magenta
plt.plot(msft,color='magenta', label='MSFT')

# Add a legend in the top left corner of the plot
plt.legend(loc='upper left')

# Specify the orientation of the xticks
plt.xticks(rotation=60)

# Display the plot
plt.show()


VISUALIZATIONS ON DIFFERENT AXIS USING SUBPLOTS

# Plot the series in the top subplot in blue
plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001 to 2011')
plt.plot(aapl, color='blue')

# Slice aapl from '2007' to '2008' inclusive: view
view = aapl['2007':'2008']

# Plot the sliced data in the bottom subplot in black
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()
plt.show()



USING PLT.AXES TO CREATE AN INSET PLOT

# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']

# Plot the entire series 
plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')

# Specify the axes
plt.axes([0.25, 0.5, 0.35, 0.35])

# Plot the sliced series in red using the current axes
plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()



PLOTTING MOVING AVERAGES

# Plot the 30-day moving average in the top left subplot in green
plt.subplot(2, 2, 1)
plt.plot(mean_30, 'green')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('30d averages')
plt.show()

# Plot the 75-day moving average in the top right subplot in red
plt.subplot(2, 2, 2)
plt.plot(mean_75, 'red')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('75d averages')

# Plot the 125-day moving average in the bottom left subplot in magenta
plt.subplot(2, 2, 3)
plt.plot(mean_125, 'magenta')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('125d averages')

# Plot the 250-day moving average in the bottom right subplot in cyan
plt.subplot(2, 2, 4)
plt.plot(mean_250, 'cyan')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')

# Display the plot
plt.show()



PLOTTING MOVING STANDARD DEVIATIONS

# Plot std_30 in red
plt.plot(std_30, 'red', label='30d')

# Plot std_75 in cyan
plt.plot(std_75, 'cyan', label='75d')

# Plot std_125 in green
plt.plot(std_125, 'green', label='125d')

# Plot std_250 in magenta
plt.plot(std_250, 'magenta', label='250d')

# Add a legend to the upper left
plt.legend(loc = 'upper left')

# Add a title
plt.title('Moving standard deviations')

# Display the plot
plt.show()






HISTOGRAM FROM A GRAYSCALE IMAGE

# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')


# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap = 'gray')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0,256), normed=True,#to control numerical binning and the vertical scale 
color='red', alpha=0.4)

# Display the plot
plt.show()






ADDING A CUMULATIVE DISTRIBUTION TO THE ABOVE HISTOGRAM PLOT

# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False, color='red', alpha=0.4)
               
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()

# Display a cumulative histogram of the pixels
cdf = plt.hist(pixels, bins=64, range=(0,256),
               color='blue', cumulative=True,
               normed=True, alpha=0.4)
               
# Specify x-axis range, hide axes, add title and display plot
plt.xlim((0,256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()


EQUALIZING AN IMAGE HISTOGRAM

# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()
#print(pixels.shape)
#new_pixels = np.interp(pixels, bins[:-1], cdf*255)
# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)
#print(new_pixels.shape)
#print(type(new_pixels))
#plt.show()


# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)



# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image,cmap='gray')

# Generate a histogram of the new pixels
plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')


# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')

# Add title
plt.title('PDF & CDF (equalized image)')

# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.show()







EQUALIZING AN IMAGE HISTOGRAM

# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)

'''
use np.interp to spread out the  pixel intensities having the practical effect of making a sharper, contrast-enhanced image
'''

new_pixels = np.interp(pixels, bins[:-1], cdf*255)

#plt.show()


# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)



# Display the new image with 'gray' color map
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image,cmap='gray')

# Generate a histogram of the new pixels
plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')


# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')

# Add title
plt.title('PDF & CDF (equalized image)')

# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.show()








EXTRACTING HISTOGRAMS FROM A  COLOR IMAGE

# Load the image into an array: image
image = plt.imread('hs-2004-32-b-small_web.jpg')

# Display image in top subplot
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.grid('off')
plt.imshow(image)


# Extract 2-D arrays of the RGB channels: red, blue, green
red, blue, green = image[:,:,0], image[:,:,1], image[:,:,2]

# Flatten the 2-D arrays of the RGB channels into 1-D
red_pixels = red.flatten()
blue_pixels = blue.flatten()
green_pixels = green.flatten()

# Overlay histograms of the pixels of each color in the bottom subplot
plt.subplot(2,1,2)
plt.title('Histograms from color image')
plt.xlim((0,256))
plt.hist(red_pixels, bins=64, normed=True, color='red', alpha=0.2)
plt.hist(blue_pixels, bins=64, normed=True, color='blue', alpha=0.2)
plt.hist(green_pixels, bins=64, normed=True, color='green', alpha=0.2)

# Display the plot
plt.show()





JOINT DISTRIBUTIONS/BIVARIATE HISTOGRAMS FROM A COLOR IMAGE


# Load the image into an array: image
image = plt.imread('hs-2004-32-b-small_web.jpg')

# Extract RGB channels and flatten into 1-D array
red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
red_pixels = red.flatten()
green_pixels = green.flatten()
blue_pixels = blue.flatten()

# Generate a 2-D histogram of the red and green pixels
plt.subplot(2,2,1)
plt.grid('off') 
plt.xticks(rotation=60)
plt.xlabel('red')
plt.ylabel('green')
plt.hist2d(red_pixels, green_pixels, bins=(32,32))


# Generate a 2-D histogram of the green and blue pixels
plt.subplot(2,2,2)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('green')
plt.ylabel('blue')
plt.hist2d(green_pixels, blue_pixels, bins=(32, 32))

# Generate a 2-D histogram of the blue and red pixels
plt.subplot(2,2,3)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('blue')
plt.ylabel('red')
plt.hist2d(blue_pixels, red_pixels, bins=(32, 32))

# Display the plot
plt.show()






























