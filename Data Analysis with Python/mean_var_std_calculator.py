import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots()

    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    years_predict = [x for x in range(1880,2050)]
    years_predict = pd.Series(years_predict)
    sea_level_predict = years_predict * slope + intercept

    ax.plot(years_predict, sea_level_predict, 'red')


    df_2000 = df.loc[df['Year'] >= 2000]

    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])

    years_predict2 = [x for x in range(2000,2050)]
    years_predict2 = pd.Series(years_predict2)
    sea_level_predict2 = years_predict2 * slope2 + intercept2

    ax.plot(years_predict2, sea_level_predict2, 'green')
    
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
