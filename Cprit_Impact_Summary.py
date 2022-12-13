import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from streamlit_extras.metric_cards import style_metric_cards
st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)







cprit_grants_funded_df = pd.read_excel('datasets\CpritGrantsFunded.xlsx')
cgf_copy = cprit_grants_funded_df.copy()

pd.options.display.float_format = '{:,}'.format
programs = cprit_grants_funded_df['Program'].unique()
#Functions used later

def cancer_num(year,program):
    v = cgf_copy.loc[cgf_copy['Program']==program]
    empty = []
    df = pd.DataFrame(v.loc[v['YEAR'] == int(year)])
    df2 = df.copy()
    df2['cancer_list'] = df2['Cancer Types'].str.split(',')
    df2 = df2.fillna('r')
    for i in df2['cancer_list']:
        for x in i:
            if x not in empty:
                empty.append(x)
    if 'r' in empty:
        empty.remove('r')
    if 'All Sites' in empty:
        new_str = str(len(empty))+"+"
        return new_str
    else:
        return len(empty)

def total_funded_grants(year,program):
    v = cgf_copy.loc[cgf_copy['Program']==program]
    df = pd.DataFrame(v.loc[v['YEAR'] == int(year)])
    df2 = df.copy()
    return df2['Grant ID'].nunique()

def entitities_funded(year,program):
    df = cgf_copy.loc[cgf_copy['Program']==program]    
    df = pd.DataFrame(df.loc[df['YEAR'] == int(year)])
    df2 = df.copy()
    return df2['Organization'].nunique()

def total_money(year,program):
    x = year_df['Values'].sum()/1_000_000
    return str(x.round(1))+'M'

link1 = '[Apply for Funding](https://www.cprit.state.tx.us/funding-opportunities)'
link2 = '[About Us](https://www.cprit.state.tx.us/about-us)'


def html_button_maker(link):
    button="""
       <button type="button" class="btn btn-link">{linker}</button>
""".format(linker=link)
    st.markdown(button, unsafe_allow_html=True)


# Using "with" notation
with st.sidebar:
    st.title('Cprit Impact Summary')
    button1 = html_button_maker(link1)
    button2 = html_button_maker(link2)

   











title_container = st.container()
big_container = st.container()
container1 = st.container()
container2 = st.container()
with title_container:
    st.title("Cprit Impact Summary") 
with container1:# main container that has everything
    selected_program=st.selectbox('Select Program', programs)
    df1 = cprit_grants_funded_df.loc[cprit_grants_funded_df['Program']==selected_program]
    df1 =df1.loc[:,['Organization','Program','Award Amount','YEAR']]
    df1 = df1.groupby(['YEAR','Organization'])['Award Amount'].sum()
    df1 = pd.DataFrame(df1)
    df1 = df1.pivot_table(index='YEAR',columns='Organization',values='Award Amount').fillna(0)
    df1['Total'] = df1.sum(axis=1)
    df1_years = pd.DataFrame(df1.index) #Index for bar graph
        
      
    nested_cont = st.container()
    
        
   
    with st.container(): # graph 1
        col1,col2 = st.columns([1,1.40],gap='small') # coloumns for the graphs

        with col1:
            bar_options = {
                "title": {
                    "text": "Total Funding by Year",
                },
                "yAxis": {"type": "category",'axisTick':{'alignWithLabel':True},"data": df1_years.values.tolist(),},
                "xAxis": {"type": "value"},"tooltip": {"trigger": "item"},"emphasis": {"itemStyle": {"color": "#a90000"}},
                "series": [{"data": df1['Total'].tolist(), "type": "bar"}],}
            clicked_label= st_echarts(
                options=bar_options,
                events={"click": "function(params) {return params.name}"},
                height="35rem",
                width="35rem",
                key="bar",
            )
            

            if clicked_label ==None:
                clicked = 2010
            else:
                clicked = int(clicked_label)
        with col2:
            
            year_df = df1.loc[clicked]
            year_df = pd.DataFrame(year_df)
            year_df = year_df.drop('Total')
            year_df.rename(columns={clicked:'Values'},inplace=True)
            year_df.drop(year_df[year_df['Values'] == 0].index, inplace=True)
            year_df_index = pd.DataFrame(year_df.index)

            

            with nested_cont:
                card_col1,card_col2,card_col3,card_col4 = st.columns(4)
                card_col1.metric(label="Total Funding",value=total_money(clicked,selected_program))
                card_col2.metric(label="Total Grants Funded",value=total_funded_grants(clicked,selected_program))
                card_col3.metric(label="Total Entities Funded",value=entitities_funded(clicked,selected_program))
                card_col4.metric(label="Total Cancer Types Funded",value=cancer_num(clicked,selected_program))
                # with card_col1:
                #     st.metric(label="Total Funding",value=total_money(clicked,selected_program))
                # with card_col2:
                #     st.metric(label="Total Grants Funded",value=total_funded_grants(clicked,selected_program))
                # with card_col3:
                #     st.metric(label="Total Entities Funded",value=entitities_funded(clicked,selected_program))
                # with card_col4:
                #     st.metric(label="Total Cancer Types Funded",value=cancer_num(clicked,selected_program))
                style_metric_cards(background_color='bg',box_shadow=True,border_color='white',border_left_color='#184D5E')










            bar_max = year_df['Values'].max()
            bar_interval_max = str(bar_max/1.25)
            bar_interval_min = str(bar_max/2)
            bar2_options = {
                "title": {"text": "Total Funding by Organization for "+str(clicked),},
                "grid": {"right": "35rem", "bottom": "3%", "containLabel": True}, 
                "yAxis":{"type":"category","data":year_df_index.values.tolist(),"axisLabel":{'fontSize':10}},
                "xAxis":{'align':'center',"type":"value"},'minInterval':bar_interval_min,'maxInterval':bar_interval_max,"tooltip": {"trigger": "item"},"emphasis": {"itemStyle": {"color": "#a90000"}},
                "series":[{"data":year_df['Values'].tolist(),"type":"bar"}],}
            st_echarts(
                options=bar2_options,
                height="35rem",
                width="100vw",
                key="bar2",
            )
            
with container2: # container 2
    df2 = cprit_grants_funded_df.loc[cprit_grants_funded_df['Program']==selected_program]
    df2 = df2.loc[:,['Grant ID','Organization','Title','Program','Award Amount','Cancer Types','YEAR']]
    df2 = pd.DataFrame(df2.loc[df2['YEAR'] == int(clicked)])



    st.dataframe(df2,use_container_width=True)
    
