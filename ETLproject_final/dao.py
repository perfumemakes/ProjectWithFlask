# dao.py

from dbutil import getConnect

class CovidDAO():

    # 모든 데이터 select
    def covidSelect(self):      
        try:
            conn = getConnect()
            cursor = conn.cursor()
            cursor.execute('select * from covidData')
            result = cursor.fetchall()

            return result

        except Exception as e:
            print("ALL error")
        
        finally:
            cursor.close()
            conn.close()

    # 특정 나라의 데이터 select
    def covidSelectOne(self, country):      
        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute('select * from covidData where country_region = %s', country)
            result = cur.fetchone()

            return result

        except Exception as e:
            print("ONE error")
        
        finally:
            cur.close()
            conn.close()   
