# python_project
# Flask 웹 프레임워크 사용

- 외부 데이터를 받아 ETL과정을 거쳐 특정일에 10개 국가의 코로나 데이터를 받아 확진자, 사망자, 완치자 컬럼을 생성하여 데이터 저장 (ETL)
- 본 프로젝트는 https://medium.com 의 ETL 관련 글 중 하나를 선택하여 학습하는것이 본래 취지
- 웹 개발(백엔드 관련)을 위해 ETL 후 데이터를 웹 브라우저에 출력하는 것을 목표로 하였음
- CSS 작업은 최소한으로 작업
- Google Chart를 이용

<코로나 데이터 출처>
OWNER = 'CSSEGISandData'
REPO = 'COVID-19'
PATH = 'csse_covid_19_data/csse_covid_19_daily_reports'
URL = f'https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}'
