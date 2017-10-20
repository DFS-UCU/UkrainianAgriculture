import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

FILE = '../Сводная вегетация.xlsx'
SHEET = '2014'

df = pd.read_excel(FILE, sheetname=SHEET, header=1)

NDVI_COLUMNS = [col for col in df.columns if 'неделя' in col]
CULTURE_COLUMN = 'Культура ' + SHEET
YIELD_COLUMN = 'Урожайность, т./га.'

df_cultures = df.groupby(df[CULTURE_COLUMN]).mean()


dfc = df_cultures.copy()
dfc = dfc[NDVI_COLUMNS]
#dfc = dfc.loc['Кукуруза']


dfc = dfc.apply(lambda x: x.interpolate(method='linear'), axis=1)
ax = dfc.T.plot(figsize=(12,8))
fig = ax.get_figure()
fig.savefig('../img/{}_NDVI.png'.format(SHEET))
