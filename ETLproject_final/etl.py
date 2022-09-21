# ETL _ covid-19 data set

import requests
import pandas as pd

from sqlalchemy import create_engine
import pymysql

from tqdm.auto import tqdm

OWNER = 'CSSEGISandData'
REPO = 'COVID-19'
PATH = 'csse_covid_19_data/csse_covid_19_daily_reports'
URL = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}'

# 1 Extract
def extract_df():
    download_urls = []
    response = requests.get(URL)

    for data in tqdm(response.json()):
        if data['name'].endswith('.csv'):
            download_urls.append(data['download_url'])

    dat = pd.read_csv(download_urls[0]) #01-03-2021 데이터 #https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv
    
    return dat

# 2 Transform
def transform_df(dat):
    relabel = {
        'Last_Update': 'last_update',
        'Country_Region': 'country_region',
        'Lat': 'latitude',
        'Long': 'longitude',
        'Province_State': 'province_state',
        'Confirmed':'confirmed',
        'Deaths':'deaths',
        'Recovered':'recovered'
    }

    # 컬럼명 수정
    for label in dat:
        if label in relabel:
            dat = dat.rename(columns = {label: relabel[label]})
    
    # datetime 타입으로 변환
    if 'last_update' in dat:
        dat['last_update'] = pd.to_datetime(dat['last_update'])

    # 특정 컬럼 반환
    labels = ['province_state', 'country_region', 'last_update', 'confirmed', 'deaths', 'recovered']

    return dat[labels]

# 개별 도시 한 나라로 groupby 적용
def transform_df2(dat):
    data1=dat.groupby('country_region')[['confirmed', 'deaths', 'recovered']].sum()
    data1 = data1.sort_values('confirmed', ascending=False).head(10)
    data1 = data1.reset_index()

    return data1

# 3 Load - db 연동
def db_conn(dat):

    pymysql.install_as_MySQLdb()

    engine = create_engine("mysql+pymysql://bigdata:bigdata@127.0.0.1:3306/playdata")
    dat.to_sql(name = 'covidData',
          con = engine,
          if_exists = 'append',
          index = False
          )
          
    engine.dispose()


if __name__ == '__main__':
    
    dat = extract_df()
    newDat = transform_df(dat)
    newDat = transform_df2(newDat)
    db_conn(newDat)




