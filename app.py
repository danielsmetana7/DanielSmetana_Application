#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: danielsmetana7@ MABA CLASS
"""

import streamlit as st
import pandas as pd

import plotly.express as px


st.title("Daniel Smetana Application")
st.markdown("My name is Daniel Smetana, and this is my Streamlit Application..")
st.markdown("This is v1")

st.title("Project Idea")
st.markdown("My project idea is to create a restauarant recommender application.\
The application will prompt the user with various questions (e.g. food type, \
price range, distance from current location, restaurant style, etc) and then leverage\
a model (likely a decision tree) to produce a recommendation to the user. \
My initial thought is for the output to give the user three top options, giving them \
some level of choice. The output would contain not only the restaurant name, but \
also the location of the restaurant and potentially any dishes they are known for.")

st.markdown("This project idea was spurred by the constant question of where to eat...\
seemingly every weekend I struggle choosing between the numerous restaurants available,\
and often would like someone (or something) to just decide for me. This application \
looks to fill this need.")


st.title("Reflection")
st.markdown("I was able to produce a basic streamlit application shell that links to GitHub \
(leveraging GitHub Desktop) and use Atom to edit my code. Obviously this is just the\
start of the application, with the more technical aspects presenting potential \
issue down the road - however, I feel comfortable with the overall idea and process.")

st.markdown("The tools that work for me currently are GitHub, Atom, Spyder, and Google Cloud.\
I am unsure if Docker or Google SDK are working, but they were downloaded following the steps outlined.\
Additionally, I redownloaded Visual Basic using the new link, but still have struggled to use it... \
I am just not very familiar with the inteface, but from what I understand it is not necessary\
to use the tool because of the alternatives avaiable? Please let me know if there would \
be any concern with not using it.")
