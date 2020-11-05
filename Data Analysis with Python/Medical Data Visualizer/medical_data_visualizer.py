import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

bmi = df['weight'] / ((df['height'] / 100) **2)

df['overweight'] = bmi.apply(lambda x: 1 if x>25 else 0)

df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x>1 else 0)

df['gluc'] = df['gluc'].apply(lambda x: 1 if x>1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars =["cardio"], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    df_cat["total"] = 1
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index =False).count()


    fig = sns.catplot(x = "variable", y = "total", data = df_cat, hue ="value", kind = "bar", col = "cardio").fig


    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

    corr = df_heat.corr()

    mask = np.triu(corr)

    fig, ax = plt.subplots(figsize=(12, 12)) 

    sns.heatmap(corr, linewidths=1, annot = True, square = True, mask = mask, fmt =".1f")

    fig.savefig('heatmap.png')
    return fig
