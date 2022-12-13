import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import json
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px
from streamlit_echarts import st_echarts

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


df = pd.read_excel(r'datasets\race&ethnicity.xlsx')
df2 = pd.read_excel(r'datasets\Houston_VC_FUnd.xlsx')
df3  = pd.read_excel(r'datasets\texas_biotech_joobs.xlsx')

houston_df = df[df['Location'] == 'Houston']
texas_df = df[df['Location'] == 'Texas']




def card_maker2(card_text,icon):
    card = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">     
            <div class="metric-card";border-style:solid;order-color: #22aaf8;>                                                                                               
            <p style=font-size:1rem;><b>{card}</b></p>
            <hr style="border: none; border-bottom: 1px solid black; opacity:0.25;">
            <i class="{icon} fa-3x"style=color:black;></i>                                                                                                                                                                          
            </div>""".format(card=card_text,icon=icon)
    st.markdown(card, unsafe_allow_html=True)





container1 = st.container()
container2 = st.container()
container3 = st.container()
container4 = st.container()
container5 = st.container()

with container1:
    st.title('Life Science and Economic Summary')


with container2:
    col1, col2 = st.columns(2)
    with col1:
        st.header('Census Houston Population by Ethnicity in 2021')
        fig1 = px.treemap(houston_df, path=['Race/Ethnicity'], values=houston_df['Population'])
        fig1.update_layout(margin = dict(t=0, l=0, r=0, b=0))
        fig1.data[0].textinfo = 'label+text+value'
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.header('Census Texas Population by Ethicity in 2021')
        fig2 = px.treemap(texas_df,path=['Race/Ethnicity'], values='Population')
        fig2.update_layout(margin = dict(t=0, l=0, r=0, b=0))
        fig2.data[0].textinfo = 'label+text+value'
        st.plotly_chart(fig2, use_container_width=True)

with container3:
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df2, x='Industry', y='Millions Invested (2016-2021)', barmode='group')
        fig1.update_layout(margin = dict(t=0, l=0, r=0, b=0))
        st.plotly_chart(fig1, use_container_width=True)

        
    with col2:
        fig2 = px.bar(df3,y='INDUSTRY SECTOR',x=['INDIRECT EMPLOYMENT','DIRECT EMPLOYMENT','TOTAL EMPLOYMENT'],orientation='h')
        fig2.update_layout(margin = dict(t=0, l=0, r=0, b=0))
        st.plotly_chart(fig2, use_container_width=True)
    
with container4:
    col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
    with col1:
        card_maker2("#1 Diversity in U.S Cities","fas fa-handshake")
    with col2:
        card_maker2("#4 Largest City in the U.S","fas fa-city")
    with col3:
        card_maker2("#1 in Clinical Healthcare & Medical Reasearch","fas fa-heartbeat")
    with col4:
        card_maker2("1,145 Active Clinical Trials","fas fa-dna")
    with col5:
        card_maker2("#1 Jobs Creator i the Nation","fas fa-briefcase")
    with col6:
        card_maker2("Largest medical Center in the World","fas fa-hospital")
    with col7:
        card_maker2("#1 Medical & Clinical Lab Technologists","fas fa-vial")
    with col8:
        card_maker2("9th largest Economy in the World","fas fa-dollar-sign")
with container5:
    col9,col10,col11,col12,col13,col14,col15,col16 = st.columns(8)
    with col9:
        card_maker2("#2 Emerging Life Clusters","fas fa-dna")
    with col10:
        card_maker2("$1.9B Spent in Life Science Research Annually","fas fa-money-bill")
    with col11:
        card_maker2("1700+ Life Science Companies","fas fa-building")
    with col12:
        card_maker2("177,650 Health & Life Sciences Professionals","fas fa-ribbon")
    with col13:
        card_maker2("4000+ Annual Surgeries","fas fa-clipboard-list")
    with col14:
        card_maker2("$2.5B Annual Research & Development Expenditures Spending","fas fa-money-bill")
    with col15:
        card_maker2("11,159 Total Clinical Trials","fas fa-microscope")
    with col16:
        card_maker2("22,160 Clinical Trials Underway","fas fa-truck-pickup")
    





