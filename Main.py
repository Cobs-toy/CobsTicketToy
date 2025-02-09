import streamlit as st
from cobstickettoy.db import bulk_insert


st.set_page_config(page_title="Find out the resale price of Jordans", page_icon="💵")

st.title("Find out the resale price of Jordans")
st.subheader("사용방법")
st.image("./src/images/toy.png",caption=None, use_container_width=True)

st.markdown('''
        - :red[모든 칸]을 입력해야 검색 가능합니다 
        
        - :red[전체 이름]을 입력하거나 :blue[연속 된 이름] 혹은 :rainbow[닉네임]으로 검색 가능합니다
        
        - ex: jordan 1 retro black toe => :green-background["jordan 1 retro"] or :green-background["1 retro"] or :green-background["black toe"]

        ''')

