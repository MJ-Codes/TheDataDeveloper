# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:00:52 2020

@author: crein
"""

# Import plotting modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


SCATTER PLOTS WITH LISTS

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(gdp, phones)
plt.show()


COUNT PLOTS WITH A LIST

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

'''
Count plots take in a categorical list and return bars that 
represent the number of list entries per category.
'''

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()



COUNT PLOTS WITH A DATAFRAME

# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()




HUE AND SCATTERPLOTS

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x='absences', y='G3', data=student_data, hue='location', palette='Greens')

# Show plot
plt.show()




HUE AND COUNTPLOTS

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", data=student_data,
              hue="location",
              palette=palette_colors)

# Display plot
plt.show()



RELATIONAL PLOT INSTEAD OF A SCATTER PLOT
# Replot has more flexibility

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter")

# Show plot
plt.show()




# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",
            col="study_time")

# Show plot
plt.show()



# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()



# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter",
            col='schoolsup'
            col_order=['yes','no'])

# Show plot
plt.show()



# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
# Use the size parameter to vary the point size based on number of cylinders.
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders")

# Show plot
plt.show()




# Import Matplotlib and Seaborn
#Set the hue parameter to the column name "cylinders"
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders", hue="cylinders")

# Show plot
plt.show()




# Import Matplotlib and Seaborn
# Adding style parameter to further differentiate the origin data
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind="scatter", 
            style="origin", hue="origin")

# Show plot
plt.show()





INTERPRETING LINE PLOTS
# Both x and y variables are quantitative variables

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line")

# Show plot
plt.show()



LINE PLOT WITH SUBGROUPS USING STYLE AND HUE

sns.replot(x="hour", y="NO_2_mean",
           data=air_df_loc_mean,
           kine="line",
           style="location",
           hue="location")



CI ARGUMENT WITH LINE PLOTS(DEFAULT CI IS 95%)

# ci is the confidence interval
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",
            ci="sd")


# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None)

# Show plot
plt.show()










# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin")

# Show plot
plt.show()




CATPLOT()

# Create count plot of internet usage
sns.catplot(x="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()


# Seaborn automatically shows 95% confidence intervals for the means
# Create column subplots based on age category with the categorical variable on the y-axis
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")

# Show plot
plt.show()





CATPLOT KIND=BAR PLOT WITH PERCENTAGES

# Create a bar plot of interest in math, separated by gender
# The bar plot in seaborn will show confidence levels surrounding the mean of each categorical value
sns.catplot(x="Gender", y="Interested in Math",
            data=survey_data, kind="bar")

# Show plot
plt.show()




# Add the order argument
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"],
            ci=None)

# Show plot
plt.show()




BOX PLOT
# Show the distribution of quantitative data
# Compare the distribution of a quantitative variable across different groups of a categorical variable

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="box",
            order=study_time_order)

# Show plot
plt.show()




# Create a box plot with subgroups with `hue` and omit the outliers with `sym`
sns.catplot(x="internet", y="G3",
            data=student_data,
            kind="box",
            hue="location",
            sym="")

# Show plot
plt.show()




# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Show plot
plt.show()



# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])

# Show plot
plt.show()




# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100]

# Show plot
plt.show()




POINT PLOTS
# Similar to a Bar Plot with more visually appealing attributes in some data scenarios
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point")
            
# Show plot
plt.show()


# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2)
            
# Show plot
plt.show()



# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join=False)
            
# Show plot
plt.show()




POINT PLOTS WITH SUBGROUPS

# Create a point plot with subgroups(hue), with the confidence interval turned off
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()


"""
Import median function from numpy to eliminate the effect 
of outliers in the data set on the default `mean'
from numpy import median
"""
from numpy import median
# Plot the median number of absences instead of the mean and add caps to the ci's
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            estimator=median,
            capsize=0.2)

# Show plot
plt.show()




CHANGING SYTLE AND PALETTE

# Set the color palette to "Purples"
sns.set_style("whitegrid") # Other possibilities include: white, dark , whitegrid, darkgrid, ticks
sns.set_palette("Purples") # Other possibilites include: pastel, muted, bright, deep, dark, colorblind
                           # Can also use hex color codes like ["#39A7D0", "#36ADA4"]

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()



CHANGING THE SCALE

# Set the context to "paper"
sns.set_context("paper") # Other possibilites include: notebook, talk, poster

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()




USING A CUSTOM PALETTE

# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette(these two hex color codes for the two categorical values in the "Gender" column)
sns.set_palette(["#39A7D0", "#36ADA4"])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()





FACETGRIDS VS AXESSUBPLOTS

# Facet grids allow subplots (relplot, catplot)
# Axes subplots allow single axes plots (scatterlot, countplot)




ADDING A TITLE TO A FACETGRID OBJECT

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
#y manipulates the position of the title above the default position(1.00)
g.fig.suptitle("Car Weight vs. Horsepower", y=1.03)

# Show plot
plt.show()



ADDING A TITLE AND AXIS LABELS TO AXIESSUBPLOT OBJECT

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time", y=1.03)

# Show plot
plt.show()



# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year", 
      ylabel="Average MPG")

# Show plot
plt.show()


ROTATING X-TICK LABELS

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels, this is done outside of your created object with matplotlib  
plt.xticks(rotation=90)

# Show plot
plt.show()




BOXPLOTS WITH SUBGROUPS

# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# To set the titles for each axis subplot
# Use {col_name} to use the column name in the title
g.set_titles("This is {col_name}")

# Show plot
plt.show()





BAR PLOT WITH SUBGROUPS AND SUBPLOTS

# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
      ylabel="% Who Like Techno")

# Show plot
plt.show()







LINE, SCATTER - RELPLOTS relationship between 2 quantitative variables

BAR, COUNT, BOX, POINT - CATPLOTS shows the distribution of a quantitative variable within categories





STATISTICAL GRAPHING WITH SEABORN


   mpg  cyl  displ   hp  weight  accel  yr  origin                              name  color       size marker
0    18.0    6  250.0   88    3139   14.5  71      US                      ford mustang    red  27.370336      o
1     9.0    8  304.0  193    4732   18.5  70      US                          hi 1200d  green  62.199511      o
2    36.1    4   91.0   60    1800   16.4  78    Asia                  honda civic cvcc   blue   9.000000      x
3    18.5    6  250.0   98    3525   19.0  77      US                      ford granada    red  34.515625      o
4    34.3    4   97.0   78    2188   15.8  80  Europe                         audi 4000   blue  13.298178      s
5    32.9    4  119.0  100    2615   14.8  81    Asia                      datsun 200sx   blue  18.995069      x
6    32.2    4  108.0   75    2265   15.2  80    Asia                    toyota corolla   blue  14.250625      x
7    22.0    4  121.0   76    2511   18.0  72  Europe               volkswagen 411 (sw)   blue  17.514225      s
8    15.0    8  302.0  130    4295   14.9  77      US           mercury cougar brougham  green  51.241736      o
9    17.0    8  302.0  140    3449   10.5  70      US                       ford torino  green  33.043336      o
10   44.0    4   97.0   52    2130   24.6  82  Europe                         vw pickup   blue  12.602500      s
11   24.5    4  151.0   88    2740   16.0  77      US             pontiac sunbird coupe   blue  20.854444      o
12   32.0    4  135.0   84    2295   11.6  82      US                     dodge rampage   blue  14.630625      o
13   14.0    8  351.0  148    4657   13.5  75      US                          ford ltd  green  60.243469      o
14   15.0    8  400.0  150    3761    9.5  70      US             chevrolet monte carlo  green  39.292003      o
15   13.0    8  307.0  130    4098   14.0  72      US  chevrolet chevelle concours (sw)  green  46.648900      o
16   36.0    4   79.0   58    1825   18.6  77  Europe                     renault 5 gtl   blue   9.251736      s
17   31.0    4  119.0   82    2720   19.4  82      US                        chevy s-10   blue  20.551111      o
18   32.0    4   71.0   65    1836   21.0  74    Asia               toyota corolla 1200   blue   9.363600      x
19   21.5    3   80.0  110    2720   13.5  77    Asia                        mazda rx-4  black  20.551111      x
20   19.0    6  225.0   95    3264   16.0  75      US           plymouth valiant custom    red  29.593600      o
21   17.0    6  231.0  110    3907   21.0  75      US                     buick century    red  42.401803      o
22   16.0    8  302.0  140    4141   14.0  74      US                  ford gran torino  green  47.633003      o
23   15.0    8  383.0  170    3563   10.0  70      US               dodge challenger se  green  35.263803      o
24   23.0    4  140.0   78    2592   18.5  75      US                     pontiac astro   blue  18.662400      o
25   26.0    4   98.0   90    2265   15.5  73  Europe              fiat 124 sport coupe   blue  14.250625      s
26   32.0    4  144.0   96    2665   13.9  82    Asia                  toyota celica gt   blue  19.728403      x
27   24.0    4  113.0   95    2372   15.0  70    Asia             toyota corona mark ii   blue  15.628844      x
28   21.0    6  231.0  110    3039   15.0  75      US                     buick skyhawk    red  25.654225      o
29   31.3    4  120.0   75    2542   17.5  80    Asia                         mazda 626   blue  17.949344      x
..    ...  ...    ...  ...     ...    ...  ..     ...                               ...    ...        ...    ...
362  26.0    4   97.0   46    1950   21.0  73  Europe           volkswagen super beetle   blue  10.562500      s
363  30.0    4  135.0   84    2385   12.9  81      US                  plymouth reliant   blue  15.800625      o
364  29.0    4   90.0   70    1937   14.2  76  Europe                         vw rabbit   blue  10.422136      s
365  14.0    8  351.0  153    4154   13.5  71      US                  ford galaxie 500  green  47.932544      o
366  25.4    6  168.0  116    2900   12.6  81    Asia                   toyota cressida    red  23.361111      x
367  19.0    6  232.0  100    2901   16.0  74      US                        amc hornet    red  23.377225      o
368  12.0    8  400.0  167    4906   12.5  73      US                      ford country  green  66.857878      o
369  20.0    4   97.0   88    2279   19.0  73    Asia                     toyota carina   blue  14.427336      x
370  27.0    4   97.0   88    2130   14.5  71    Asia                      datsun pl510   blue  12.602500      x
371  22.3    4  140.0   88    2890   17.3  79      US                   ford fairmont 4   blue  23.200278      o
372  10.0    8  307.0  200    4376   15.0  70      US                         chevy c20  green  53.192711      o
373  19.2    8  267.0  125    3605   15.0  79      US     chevrolet malibu classic (sw)  green  36.100069      o
374  26.0    4  156.0   92    2585   14.5  82      US        chrysler lebaron medallion   blue  18.561736      o
375  16.0    6  258.0  110    3632   18.0  74      US                       amc matador    red  36.642844      o
376  37.3    4   91.0   69    2130   14.7  79  Europe                fiat strada custom   blue  12.602500      s
377  26.0    4   79.0   67    1963   15.5  74  Europe                 volkswagen dasher   blue  10.703803      s
378  20.2    6  232.0   90    3265   18.2  79      US                  amc concord dl 6    red  29.611736      o
379  13.0    8  318.0  150    3755   14.0  76      US                        dodge d100  green  39.166736      o
380  21.0    6  199.0   90    2648   15.0  70      US                       amc gremlin    red  19.477511      o
381  25.0    4   90.0   71    2223   16.5  75  Europe                 volkswagen dasher   blue  13.727025      s
382  20.5    6  231.0  105    3425   16.9  77      US                     buick skylark    red  32.585069      o
383  37.7    4   89.0   62    2050   17.3  81    Asia                     toyota tercel   blue  11.673611      x
384  36.0    4  120.0   88    2160   14.5  82    Asia                  nissan stanza xe   blue  12.960000      x
385  20.0    6  156.0  122    2807   13.5  73    Asia                    toyota mark ii    red  21.886803      x
386  37.0    4   85.0   65    1975   19.4  81    Asia                    datsun 210 mpg   blue  10.835069      x
387  18.0    6  250.0   88    3021   16.5  73      US                     ford maverick    red  25.351225      o
388  27.0    4  151.0   90    2950   17.3  82      US                  chevrolet camaro   blue  24.173611      o
389  29.5    4   98.0   68    2135   16.6  78    Asia                   honda accord lx   blue  12.661736      x
390  17.5    6  250.0  110    3520   16.4  77      US                chevrolet concours    red  34.417778      o
391  25.1    4  140.0   88    2720   15.4  78      US               ford fairmont (man)   blue  20.551111      o




PLOTTING A LINEAR REGRESSION FOR TWO CONTINUOUS VARIABLES

sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()



PLOTTING A LINEAR REGRESSION FOR TWO CONTINUOUS VARIABLES
APPLIED SEPARATELY FOR SUBSETS OF DATA

''' Plot a linear regression between 'weight' and 'hp', with a row of 'origin' and palette of 'Set1'
on different rows'''
# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row='origin' , palette='Set1')

# Display the plot
plt.show()



PLOTTING THE RESIDUALS OF THE REGRESSION

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show() 


HIGHER ORDER REGRESSIONS USING REGPLOT
''' Use regplot instead of lmplot for more permissive arguments like the order
of polynomial regression'''


# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, order=1,scatter=None, color='blue', label='order 1')

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, order=2,scatter=None, color='green', label='order 2')

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()




GROUPING LINEAR REGRESSIONS BY HUE, ROW, OR COLUMN

# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
# hue plots all separate groups on the same axis
sns.lmplot(x='weight', y='hp', data=auto, hue='origin' , palette='Set1')

# Display the plot
plt.show()


# using row to plot each group in a separate row
# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row='origin' , palette='Set1')

# Display the plot
plt.show()






VISUALIZING ONE CONTINUOUS VARIABLE AFFECTED BY A SECOND CATEGORICAL VARIABLE(UNIVARIATE)


STRIP PLOTS
# plots the relationship between a single continous variable grouped by a second categorical variable

# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='hp', data=auto)

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.stripplot(x='cyl', y='hp', jitter=True, size= 3,data=auto)

# Display the plot
plt.show()



SWARM PLOT
# like a stripplot but data points are graphically more spread out
# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'  
plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='hp', data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
# orient 'h' transposes the graph
plt.subplot(2,1,2)
sns.swarmplot(x='hp', y='cyl', data=auto, hue='origin', orient='h')

# Display the plot
plt.show()



VIOLIN PLOT


# Generate a violin plot to reduce overplotting of large datasets using 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', inner=None, color='lightgray',data=auto)
# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl', y='hp', jitter=True, size= 1.5,data=auto)
# Display the plot
plt.show()



VISUALIZING MULTIVARIATE DISTRIBUTIONS

USING JOINTPLOT
'visualizing a bivariate distribution'

# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row='origin' , palette='Set1')

# Display the plot
plt.show()

# Generate a joint plot of 'hp' and 'mpg' using a hexbin plot
sns.jointplot(x='hp',y='mpg', data=auto, kind='hex')

# Display the plot
plt.show()



USING PAIRPLOT

# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions from the DataFrame 
sns.pairplot(auto)

# Display the plot
plt.show()


# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto, kind='reg', hue='origin')

# Display the plot
plt.show()



COVARIANCES BETWEEN VARIABLES SHOWN AS A HEATMAP

'covariance measures the degree to which variable pairs vary jointly(bwtween -1 and +1)'
 # Print the covariance matrix
print(cov_matrix)

# Visualize the covariance matrix using a heatmap
sns.heatmap(cov_matrix)

# Display the heatmap
plt.show()














