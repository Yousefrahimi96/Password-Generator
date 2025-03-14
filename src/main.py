from abc import ABC, abstractmethod
import random
import nltk
from nltk.corpus import words
import string

word_list = words.words()  # دسترسی به لیست کلمات


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
    
class Memorable(Parent):
    def __init__(self, size):
        super().__init__(size)
        
    def generator(self):
        number = str(random.randint(10**(self.size-1), 10**self.size - 1))  # عدد تصادفی
        return number

    
class Pin(Parent):
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
    
if __name__ == "__main__":
    nltk.download('words')  # دانلود لیست کلمات
    word_list = words.words()
    
    rp = RandomPassword(15)
    print("Random Password:", rp.generator())
    
    mp = Memorable(100)
    print("Memorable Password:", mp.generator())
    
    pp = Pin(38)
    print("Pin Password:", pp.generator())

    