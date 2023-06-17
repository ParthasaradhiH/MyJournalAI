import transformers
import torch

from transformers import pipeline
import streamlit as st


st.title("DiaryAI")
prompt=st.text_area("How was today")

classifier = pipeline("sentiment-analysis")
input_variables = ['response'], 

if prompt:
    response=classifier(prompt)
    st.write(response)
