'''
streamlit多页面程序的入口文件
'''
import streamlit as st
st.title("基于AI的租房问答系统")
col, col1, col2 = st.columns(3)
with col:
    st.image("https://img-baofun.zhhainiao.com/pcwallpaper_ugc_mobile/preview/4dda6aa3394c6daf79e89f612c399750_preview_mid.jpg", use_column_width=True)
    flag = st.button("租房助手", use_container_width=True)
    if flag:
        st.switch_page("pages/job-ai.py")
#
with col1:
    st.image("https://th.bing.com/th/id/R.12d984df1b66a65d1570f033b4154a3e?rik=Kn%2bQGpmEwa45Nw&pid=ImgRaw&r=0", use_column_width=True)
    flag = st.button("绘言", use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")
#
with col2:
    st.image("https://th.bing.com/th/id/R.83e7c4e9723767ec14a1f2262572f1da?rik=uHEChftQb1zF%2bw&riu=http%3a%2f%2f222.186.12.239%3a10010%2fsjkta_170810%2f006.jpg&ehk=TKgww3y5C45O7hpzsPwU5cvFrLfIOSbZiAzZSFXkAMk%3d&risl=&pid=ImgRaw&r=0", use_column_width=True)
    flag = st.button("绘图", use_container_width=True)
    if flag:
        st.switch_page("pages/realestate.py")

# c1,c2,c3,c4 = st.columns(4)
# with c1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1 = st.button("进阶版")
#     if flag1:
#         st.switch_page("pages/demo01.py")
# with c3:
#     flag2 = st.button("最终版")
#     if flag2:
#         st.switch_page("pages/huiyan.py")
# with c4:
#     flag3 = st.button("文生图")
#     if flag3:
#         st.switch_page("pages/textToImage.py")