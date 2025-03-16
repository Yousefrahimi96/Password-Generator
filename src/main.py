import streamlit as st
from abc import ABC, abstractmethod
import random
import nltk
from nltk.corpus import words
import string

nltk.download('words')  # دانلود لیست کلمات
word_list = words.words()  # دسترسی به لیست کلمات

st.title(":zap: Password Genertaor")
option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

class Parent(ABC):
    def __init__(self, size = 10):
        self.size = size
        
    @abstractmethod
    def generator(self):
        pass
    
class RandomPassword(Parent):
    def __init__(self, size):
        super().__init__(size)
        
    def generator(self):
        characters = string.ascii_letters + string.digits  # حروف و اعداد
        password = ''.join(random.choice(characters) for _ in range(self.size))  # پسورد 10 کاراکتری
        return password
    
class Pin(Parent):
    def __init__(self):
        pass
        
    def generator(size):
        number = str(random.randint(10**(size-1), 10**size - 1))  # عدد تصادفی
        return number

    
class Memorable(Parent):
    def __init__(self, size):
        super().__init__(size)
        
    def generator(self):
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