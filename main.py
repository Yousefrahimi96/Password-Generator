import streamlit as st
import random
import nltk
from nltk.corpus import words
import string

nltk.download('words')  #download the list of word
word_list = words.words()

st.image('./data/images.png')
st.title(":zap: Password Generator")
option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))


    
def random_generator(length):
        characters = string.ascii_letters + string.digits  #characters and numbers
        password = ''.join(random.choice(characters) for _ in range(length))  # password with lentgh character
        return password
    
    
def pin_generator(length):
        number = str(random.randint(10**(length-1), 10**length - 1))  # random number
        return number

    
def memorable_generator(length):
    words = [random.choice(word_list) for _ in range(length)]
    password = '-'.join(words)
    return password
    
    
if option == 'Pin Code':
    length = st.slider("Number of digits", min_value=4, max_value=64)
    pincode = pin_generator(length)
    st.write(pincode)
    
elif option == 'Random Password':
    length = st.slider("Password length", min_value=4, max_value=64)
    password = random_generator(length)
    st.write(password)
    
else:
    length = st.slider("Number of words", min_value=4, max_value=64)
    password = memorable_generator(length)
    st.write(password)