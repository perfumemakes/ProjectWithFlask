from dbutil import getConnect

class covidDAO:
    
    def get(self):
        sql = 'select * from covidtest'

        with getConnect() as connection:
            with connection.cursor() as cursor:
            #       select문 실행
                    cursor.execute(sql)
            #       select 결과 조회 (cursor.fetchXXX() 메소드 이용)
                    result = cursor.fetchall()
        return result
    
    def select(self, country_region):

        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute( "select * from covidtest where country_region = %s" , (country_region) )

            result = cur.fetchone()
            return result
            
        except Exception as e:
            conn.rollback()
            print(e)
            cur.close()
            conn.close()
            
            
if __name__=="__main__":
    
    covidDAO().get()
    covidDAO().select("United States")