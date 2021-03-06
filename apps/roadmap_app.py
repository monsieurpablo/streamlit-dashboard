from pathlib import Path

import streamlit as st
import numpy as np
import pandas as pd

# #add an import to Hydralit
# from hydralit import HydraHeadApp

def read_markdown(markdown_file):
    return Path(markdown_file).read_text()

#create a wrapper class
def RoadmapApp(): 
    #-------------------existing untouched code------------------------------------------
    # company logo on top
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Hoare_Lea_logo.svg/1200px-Hoare_Lea_logo.svg.png", width=200)

    # set 2 columns
    space1, col,space2  = st.columns([1,3,1])
    
    with col:
        roadmap_md = read_markdown('apps/data/roadmap.md')
        st.markdown(roadmap_md, unsafe_allow_html=True)
            