import streamlit as st
from cobstickettoy.db import bulk_insert,look_up_js
import pandas as pd

st.set_page_config(page_title="가격 조회하기", page_icon = "🔍")
st.page_link("Main.py", label="Back to Main", icon="🏠")
st.title("리세일 가격 조회하기")
st.subheader("모든 정보를 입력 및 선택하세요")

search_keyword = st.text_input("검색 할 신발의 이름을 입력하세요", placeholder= "ex: jordan 1")
alig_list=["내림차순","오름차순"]
alig = st.selectbox("결과 출력물의 정렬 방식을 선택하세요", alig_list, index=None, placeholder="결과 출력물의 정렬 방식을 선택하세요")

search_column_list =["거래량","출시 가격","평균 거래가격","최고 거래가격","최저 거래가격"]

scolumn = st.selectbox("정렬 기준으로 사용할 내용을 선택하세요",search_column_list, index=None, placeholder="정렬 기준으로 사용할 내용을 선택하세요")


exePress = st.button("조회하기")

if exePress:
    df_result = look_up_js(search_keyword,alig,scolumn)
    if search_keyword and alig and scolumn:
        if isinstance(df_result, pd.DataFrame) and not df_result.empty:
            st.success(f"조회 성공")
            st.dataframe(df_result)
        else:
            st.error(f"데이터가 없습니다")

    else:
        st.warning(f"모든 값을 입력하세요")
