import os
import wget

YEARS = [2017, 2016]
WEEKS = [i for i in range(1, 52)]
INDICES = ['VCI', 'TCI', 'VHI', 'SMN', 'SMT']

TEMPLATE = 'ftp://ftp.star.nesdis.noaa.gov/pub/corp/scsb/wguo/data/'\
    'VHP_4km/geo_TIFF/VHP.G04.C07.{}.P{}{}.{}.{}.tif'

OUTPUT_DIRECTORY = 'data'

def file_type(index):
    return 'SM' if index in ['SMN', 'SMT'] else 'VH'

def that_strange_code(year, week):
# There is no explicit logic behind these codes

    if year == 2005:
        if week < 23:
            return 'NL'
        else:
            return 'NN'

    year_codes = [
        {'from': 1981, 'to': 1984, 'code': 'NC'},
        {'from': 1985, 'to': 1988, 'code': 'NF'},
        {'from': 1989, 'to': 1994, 'code': 'NH'},
        {'from': 1995, 'to': 2000, 'code': 'NJ'},
        {'from': 2001, 'to': 2005, 'code': 'NL'},
        {'from': 2005, 'to': 2010, 'code': 'NN'},
        {'from': 2011, 'to': 2017, 'code': 'NP'}]

    for each in year_codes:
        if year >= each['from'] and year <= each['to']:
            return each['code']

def int_to_week_code(num):
    strNum = str(num)
    zeros = ''.join(['0' for _ in range(3 - len(strNum))])
    return zeros + strNum

def get_url(year, week, index):
    return TEMPLATE.format(
        that_strange_code(year, week),
        str(year),
        int_to_week_code(week),
        file_type(index),
        index)

def download_from_to(url, path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as exc:
        # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    print('\nCollecting', url)

    try:
        wget.download(url, out=path)
    except:
        print('File does not exist')

for year in YEARS:
    for week in WEEKS:
        for index in INDICES:
            download_from_to(
                get_url(year, week, index),
                '{}/{}/{}/'.format(OUTPUT_DIRECTORY, year, index))