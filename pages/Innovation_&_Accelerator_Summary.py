import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import json
from streamlit_extras.metric_cards import style_metric_cards
st.set_page_config(layout="wide")
from streamlit_card import card
from streamlit.components.v1 import html
from streamlit_extras.metric_cards import style_metric_cards

with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
     



link1 = '[About Us](https://www.tmc.edu/about-tmc/)'
link2 = '[TMC Innovation](https://www.tmc.edu/innovation/)'
link3 =  '[Apply For Tmc Accelerator](https://7470277.hs-sites.com/act2022)'
link4 = '[Cancer Therapeutics](https://www.tmc.edu/innovation/accelerator-cancer/)'
link5 = '[Health Tech](https://www.tmc.edu/innovation/accelerator-healthcare/)'
link6 = '[Bio-Design](https://www.tmc.edu/innovation/biodesign/)'
link7 =  '[Co Working](https://www.tmc.edu/innovation/co-working/)'

card1_text = """ <p style=color:White; font-size:16px;><b>Accelerator for Cancer Therapeutics</b></p>
                <p style=color:White; >• Investigators and early stage biotechnology company executives can access guidance on 
                clinical and business development through the Accelerator.</p>

                <p style=color:White>• The Accelerator provides a forum for investigators and biotechnology company executives 
                to share information and ideas.</p>"""

card2_text = """ <p style=color:White; font-size:16px;><b>Curriculum</b></p>
                 <p style=color:White; >•Program participants will develop and incorporate an integrated strategic plan that guides their company’s business and drug development efforts.</p>"""

card3_text = """ <div id="testing"><p style=color:White; font-size:16px; border-style:solid;><b>Key Program Benefits</b></p>
                <p style=color:White; >•Curated mentor network and dedicated entrepreneurs-in-residence to enable progress toward a comprehensive product and business development road map</p>
                <p style=color:White; >•Identification of and plan to address critical gaps and key experiments to enable funding</p>
                <p style=color:White; >•Proximity to world-class researchers and experts in the Texas Medical Center</p>
                <p style=color:White; >•Access to competitive intelligence</p>
                <p style=color:White; >•GCC Drug Development Core Network and GCC training and resources</p>
                <p style=color:White; >•JLABS @ TMC Lab space</p>
                <p style=color:White; >•Venture capital relationship development and pitch opportunities</p>
                <p style=color:White; >•Program participant portal</p>
                <p style=color:White; >•TMC Accelerator Bootcamp portal</p></div>"""


metric1 = """<div class="metric-card";border-style:solid;order-color: #22aaf8>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    
            <p style=font-size:24px;paddings: 5px 20px 5px 20px;><b>Program Duration</b></p>
            <hr style="border: none; border-bottom: 1px solid black; opacity:0.25;">
            <p style=font-size:24px>6 months</p>
            <i class="fa-solid fa-dragon fa-2x"></i>                                                                                                                                                                          
            </div>"""



def card_maker2(card_text,icon):
    card = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">     
            <div class="metric-card";border-style:solid;order-color: #22aaf8;>                                                                                               
            <p style=font-size:1rem;><b>{card}</b></p>
            <hr style="border: none; border-bottom: 1px solid black; opacity:0.25;">
            <i class="{icon} fa-3x"style=color:black;></i>                                                                                                                                                                          
            </div>""".format(card=card_text,icon=icon)
    st.markdown(card, unsafe_allow_html=True)



def html_button_maker(link):
    button="""
       <button type="button" class="btn btn-link">{linker}</button>
""".format(linker=link)
    st.markdown(button, unsafe_allow_html=True)


with st.sidebar:
    st.title('Innovation & Accelerator Summary')
    button1 = html_button_maker(link1)
    button2 = html_button_maker(link2)
    button3 = html_button_maker(link3)
    st.title('TMC Innovation')
    button4 = html_button_maker(link4)
    button5 = html_button_maker(link5)
    button6 = html_button_maker(link6)
    button7 = html_button_maker(link7)







container0 = st.container()
container1  = st.container()
container2 = st.container()
container3 = st.container()
container4 = st.container()

with container0:
    st.title('TMC Innovation & Accelerator Summary')    

with container1:
    col1,col2,col3 = st.columns(3)
    # with col1:
    #     html(card1_text,height=150, scrolling=True)
    # with col2:
    #     html(card2_text,height=150, scrolling=True)
    # with col3:
    #     html(card3_text,height=150, scrolling=True)
    with col1:
        with st.expander('Accelerator for Cancer Therapeutics', expanded=False):
            html(card1_text,height=150, scrolling=True)
    with col2:
        with st.expander('Curriculum', expanded=False):
            html(card2_text,height=150, scrolling=True)
    with col3:
        with st.expander('Key Program Benefits', expanded=False):
            html(card3_text,height=250, scrolling=True)




with container2:
    card_col1,card_col2,card_col3,card_col4 = st.columns(4)
    with card_col1:
        card_maker2('221 TMC Healthtech Accelerator Companies','fa fa-heartbeat')
    with card_col2:
        card_maker2('$5.82 Billion raised by TMC Innovation','fa fa-arrow-trend-up')

    with card_col3:
        card_maker2('7 Life Science Startups made in the Community','fa fa-atom')
    with card_col4:
        card_maker2('7 Biodesign Companies with $33M Raised','fa fa-dna')
    

with container3:
    card2_col1,card2_col2,card2_col3,card2_col4 = st.columns(4)
    with card2_col1:
        card_maker2("World's Largest Medical Complex",'fa-solid fa-hospital')
    with card2_col2:
        card_maker2('8th Largest business District in the U.S.','fa-solid fa-building')
    with card2_col3:
        card_maker2('50 Million Developed Square Feet','fa-solid fa-city')
    with card2_col4:
        card_maker2("$3 Billion of Costructioon Projects Underway",'fa-solid fa-helmet-safety')

with container4:
    card3_col1,card3_col2,card3_col3,card3_col4 = st.columns(4)
    with card3_col1:
        card_maker2("Home to the World's Largest Children's Hospital",'fa-solid fa-child')
    with card3_col2:
        card_maker2("MD Anderson is the World's Largest Cancer Hospital",'fa-solid fa-disease')
    with card3_col3:
        card_maker2("180,000+ Annual Surgeries done",'fa-solid fa-syringe')
    with card3_col4:
        card_maker2("20% of All Global Clinical Trials",'fa-solid fa-flask')




  

      
        
