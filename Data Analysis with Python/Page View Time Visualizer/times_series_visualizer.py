import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates = ["date"], index_col = "date")

df = df[
  (df["value"] >= df["value"].quantile(0.025)) &
  (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    fig, ax = plt.subplots()
    fig, ax = plt.subplots()
    
    ax.plot(df.index, df["value"], color = "red")
    
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df["month"] = df.index.month
    df["year"] = df.index.year
    df_bar = df.groupby(["year", "month"])["value"].mean()
    
    df_bar = df_bar.unstack()
    
    fig = df_bar.plot(kind ="bar", legend = True).figure
    
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
 
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")
    
    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2)

    ax1 = sns.boxplot(x=df_box["year"], y=df_box["value"], ax = ax1)
    
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')    


    ax2 = sns.boxplot(x=df_box["month"], y=df_box["value"], ax = ax2)
    
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
