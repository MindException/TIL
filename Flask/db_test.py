import pymysql
import pandas as pd

#데이터베이스 연결 전 데이터 기본 세팅
host_name = 'localhost'
port = 3306
user_name = 'root'
user_password = '1234'
database_name = 'product_detection'

test_db = pymysql.connect( 
    host = host_name,
    port = port,
    user = user_name,
    passwd = user_password,
    db = database_name,
    charset = 'utf8'
)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 데이터 INSERT ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
cursor = test_db.cursor()


# SQL 커맨드(INSERT INTO "TABLE NAME" (COLUMNS) VALUES (DATA))   <- 여기서 DB 보낼때 %s로 하여도 db에서는 알아서 int형으로 저장되어진다.
# 대소세 테이블에 데이터를 무조건 먼저 입력하여야 됩니다!! FK(외래키) 때문에 특정 튜플이 없으면 label 테이블에 튜플을 삽입을 못 해요

# 각 테이블에 필요한 쿼리문
sql_div_large = "INSERT INTO div_large (div_l_no, div_l_name) VALUES (%s, %s)"
sql_div_small = "INSERT INTO div_small (div_s_no, div_s_name) VALUES (%s, %s)"
sql_div_detail = "INSERT INTO div_detail (div_n_no, div_n_name) VALUES (%s, %s)"
sql_label = "INSERT INTO label(item_no,barcd,prod_nm,div_l_no,div_s_no,div_n_no,vessel,volume,nutrition_info) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

cursor.execute(sql_div_large, (400, "파이썬 테스트 대분류"))
cursor.execute(sql_div_small, (500, "파이썬 테스트 소분류"))
cursor.execute(sql_div_detail, (600, "파이썬 테스트 세분류"))
cursor.execute(sql_label, (7, "99999", "상품 테스트", 400, 500, 600, "용기 테스트", 100, "영양정보 테스트"))

test_db.commit()
test_db.close()
