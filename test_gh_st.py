# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:10:58 2023

@author: ander
"""

import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("C:/Users/ander/OneDrive - Syddansk Universitet/Ondrive/Dropbox/SKul uni/DS 3. sem/Visualization/Job db/vs/df_test.csv")

# print(df['col1'].mean())

st.title(df['col1'].mean())
