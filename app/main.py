import streamlit as st
import pandas as pd
from scipy import stats
from matplotlib import pyplot


st.header("Barley Visualization & Analysis")
data: pd.DataFrame = pd.read_csv("./data/barley_data.csv")
st.dataframe(data)

variety_names = data["variety"].unique()
years = data["year"].unique()
sites = data["site"].unique()

year1 = data["yield"][data["year"] == 1931]
year2 = data["yield"][data["year"] == 1932]

fig, ax = pyplot.subplots()
ax.hist(year1, label="1931", alpha=0.5, bins=15)
ax.hist(year2, label="1932", alpha=0.5, bins=15)
ax.legend()
st.pyplot(fig)

aov = stats.f_oneway(year1, year2)
t_t = stats.ttest_ind(year1, year2)
wil = stats.wilcoxon(year1, year2)

st.markdown(f'## Satistical Tests\n'
            f'| Test | Statistic | P-value\n'
            f'|-|-|-|\n'
            f'| ANOVA | {aov.statistic} | {aov.pvalue} |\n'
            f'| T Test | {t_t.statistic} | {t_t.pvalue} |\n'
            f'| Wicoxon | {wil.statistic} | {wil.pvalue} | \n')
