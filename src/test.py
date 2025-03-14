import streamlit as st
from abc import ABC, abstractmethod
import random
import nltk
from nltk.corpus import words
import string

word_list = words.words()  # دسترسی به لیست کلمات


option = st.selectbox(
    "Type",
    ("Random Password", "Memorable Password", "Pin Code"),
)

if option == "Pin Code":
    st.write("yeah")