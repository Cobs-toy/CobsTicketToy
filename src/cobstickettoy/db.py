import streamlit as st
import pandas as pd
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = { 
    "dbname": os.getenv("DB_NAME"),
    "user":os.getenv("DB_USERNAME"),
    "password":os.getenv("DB_PASSWORD"),
    "host":os.getenv("DB_HOST"),
    "port":os.getenv("DB_PORT")                                         
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)


def look_up_js(search_keyword,alig,scolumn):
    alig_convert = {"내림차순":False,"오름차순":True}
    alig_val = alig_convert.get(alig)
    skey_convert = {
            "거래량":"sale",
            "출시 가격":"retail_price",
            "평균 거래가격":"averge_sale_price",
            "최고 거래가격":"highest_price",
            "최저 거래가격":"lowest_price"
            }
    skey_val = skey_convert.get(scolumn)

    query = """
        select *
        from ajs
        """

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                df = pd.DataFrame(rows,columns=['name','sales','retail_price','averge_sale_price','highest_price','lowest_price','release_date'])
                df['name']=df['name'].astype(str).str.strip()
                fdf = df[df['name'].str.contains(search_keyword,case=False,na=False)]
                if not fdf.empty:
                    sdf = fdf.sort_values(by=skey_val, ascending = alig_val).reset_index(drop=True)
                    return sdf
                else:
                    return "정보가 없습니다 다시 확인하고 입력해주세요"

    except Exception as e:
        return f"오류가 발생 했습니다 {e}"

# Bulk insert
def bulk_insert():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                df = pd.read_csv('data/AJs.csv')
                blm=[]

                success_cnt = 0
                fail_cnt = 0

                for i in df.index:
                    Name = df.loc[i,"Name"]
                    Sales = df.loc[i,"Sales"]
                    Retail_Price = df.loc[i,"Retail_Price"]
                    Averge_Sale_Price = df.loc[i,"Averge_Sale_Price"]
                    Highest_Price = df.loc[i,"Highest_Price"]
                    Lowest_Price = df.loc[i,"Lowest_Price"]
                    Release_Date = df.loc[i,"Release_Date"]
                    blm.append((Name,Sales,Retail_Price,Averge_Sale_Price,Highest_Price,Lowest_Price,Release_Date))

                cursor.executemany("""INSERT INTO ajs (Name,Sales,Retail_Price,Averge_Sale_Price,Highest_Price,Lowest_Price,Release_Date) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (name)  DO NOTHING""",blm)
                
                success_cnt = cursor.rowcount
                fail_cnt = len(blm) - success_cnt

                if success_cnt == len(blm):
                    return st.success(f" 벌크 인서트 완료 총 {success_cnt} 건")

                else:
                    return st.error(f"총 {len(blm)} 건 중 {fail_cnt} 건 실패")
    except Exception as e:
        print(f"Exception: {e}")
        return st.warning(f"오류 발생 ; {e}")
