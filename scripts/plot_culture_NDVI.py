import pandas as pd

FILE = '../data/yield/Сводная вегетация.xlsx'
YEARS = ['2012', '2013', '2014', '2015', '2016']

cultures = set()

for year in YEARS:
    df = pd.read_excel(FILE, sheetname=year, header=1)
    cultures = cultures.union(df['Культура {}'.format(year)].unique())

def get_all_ndvi_of(culture):
    all_ndvi = pd.DataFrame()

    for year in YEARS:
        df = pd.read_excel(FILE, sheetname=year, header=1)
        ndvi_columns = [col for col in df.columns if 'неделя' in col]
        culture_column = 'Культура {}'.format(year)

        df_culture = df[df[culture_column] == culture]

        for col in ndvi_columns:
            df_culture[col].name = '{}, {}'.format(col, year)
            all_ndvi = all_ndvi.append(df_culture[col])

    return all_ndvi.T

def plot_all_ndvi(all_ndvi):
    ax = all_ndvi.T.plot(legend=False, figsize=(12,8))
    fig = ax.get_figure()
    fig.suptitle(culture, fontsize=20)
    fig.savefig('../img/{}_NDVI.png'.format(culture))

for culture in cultures:
    all_ndvi = get_all_ndvi_of(culture)

    if not all_ndvi.empty:
        print('Plotting {}...'.format(culture))
        plot_all_ndvi(all_ndvi)
