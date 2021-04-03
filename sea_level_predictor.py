import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter') # seems overly simple

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # add years to the dataframe up to 2050
    append_years = []
    for x in range(df['Year'].min(), 2051):
        if x <= df['Year'].max():
            pass
        else:
            append_years.append({'Year': x})
    df = df.append(append_years, ignore_index=True)

    # re-plot the chart (this will likely need to be done in a specific way that I'm not doing)
    # df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter') # seems overly simple
    plt.plot(df['Year'], res.intercept + res.slope * df['Year'])    # this might be working?

    # Create second line of best fit
    df2 = df[(df.Year >= 2000) & (df.Year <= 2013)]
    new_res = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], new_res.intercept + new_res.slope * df['Year'])


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# ignore, only include function in repl.it
draw_plot()