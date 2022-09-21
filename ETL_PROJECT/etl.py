import requests
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from tqdm.auto import tqdm

OWNER = 'CSSEGISandData'
REPO = 'COVID-19'
PATH = 'csse_covid_19_data/csse_covid_19_daily_reports'
URL = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}'
print(f'Downloading paths from {URL}')

# 1 extract_df
def extract_df():
    download_urls = []
    response = requests.get(URL)
    for data in tqdm(response.json()):
        if data['name'].endswith('.csv'):
            download_urls.append(data['download_url'])
            
    raw_data = pd.read_csv(download_urls[0]) #01-01-2021 데이터 #https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv
    return raw_data

# 2 Transform
def transform_df(data):

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
    for label in data:
        if label in relabel:
            data = data.rename(columns = {label: relabel[label]})
    
    # datetime 로 변환
    if 'last_update' in data:
        data['last_update'] = pd.to_datetime(data['last_update'])


    # 특정 컬럼 반환
    data = data[['province_state', 'country_region', 'last_update', 'confirmed', 'deaths', 'recovered']]
    
    # replace columns not in dataframe with nan
    # for label in labels:
    #     if label in dat:
    #         dat[label] = np.nan
    
    # 확진자 기준 상위 10개국 정렬
    data = data.groupby('country_region')[['confirmed', 'deaths', 'recovered']].sum()
    data = data.sort_values('confirmed', ascending=False).head(10)
    data = data.reset_index()
    
    return data
    


# 3 Load - db 연동
def db_conn(data):

    pymysql.install_as_MySQLdb()

    engine = create_engine("mysql+pymysql://bigdata:bigdata@127.0.0.1:3306/playdata")
    data.to_sql(name = 'covidTest',
          con = engine,
          if_exists = 'append',
          index = False
          )
          
    engine.dispose()


if __name__ == '__main__':
    
    data = extract_df()
    newdata = transform_df(data)
    db_conn(newdata)