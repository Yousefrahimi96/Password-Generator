import streamlit as st
import random
import nltk
from nltk.corpus import words
import string

nltk.download('words')  # دانلود لیست کلمات
word_list = words.words()  # دسترسی به لیست کلمات

st.title(":zap: Password Genertaor")
option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))


    
def RandomGenerator(Lengh):
        characters = string.ascii_letters + string.digits  # حروف و اعداد
        password = ''.join(random.choice(characters) for _ in range(Lengh))  # پسورد 10 کاراکتری
        return password
    
def PinGenerator(Lengh):
        number = str(random.randint(10**(Lengh-1), 10**Lengh - 1))  # عدد تصادفی
        return number

    
def MemorableGenerator(Lengh):
        i = 0
        pass_str = ''
        while i < self.size:
            random_word = random.choice(word_list)  # انتخاب یه کلمه تصادفی
            pass_str = pass_str + '-' + random_word
            i = i +1
        return pass_str
    
if option == 'Pin Code':
    Lengh = st.slider("Lengh", min_value=4, max_value=64)
    pincode = Pin.generator(Lengh)
    st.write(pincode)
    
elif option == 'Random Password':
    st.write('random pssword')
    
else:
    st.write('Memorable Password')