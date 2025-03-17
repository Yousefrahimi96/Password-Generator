# Password Generator

A simple, interactive password generator built with **Streamlit** in Python. Generate random passwords, memorable word-based passwords, or PIN codes with customizable lengths.

---

## Installation

1. **Install dependencies**: Ensure Python 3.x is installed, then run:
   ```bash
   pip install -r requirements.txt

2. **Run the app**: Launch the script with Streamlit:
bash
streamlit run your_script_name.py
Replace 'your_script_name.py' with your file name.

## How to Use

1. Choose a password type:

   * Random Password: Letters and digits (e.g., Kj9p2m).
   * Memorable Password: Words separated by - (e.g., cat-river-tree).
   * Pin Code: Numeric code (e.g., 5829).

2. Set length: Use the slider (4–64 characters/digits/words).
3. View password: Generated instantly based on your input.

## Features

* **Three password types**: Random, memorable, or PIN.
* **Customizable length**: 4 to 64 characters/digits words.
* **Interactive UI**: Powered by Streamlit.
* **Word-based passwords**: Uses NLTK’s word list.

## Prerequisites

All required libraries and tools are listed in 'requirements.txt' To install them, run:

```bash

pip install -r requirements.txt
```

## Code Snippet

```python

import streamlit as st
import random
import nltk
from nltk.corpus import words
import string

nltk.download('words')
word_list = words.words()

st.title(":zap: Password Generator")
option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == 'Pin Code':
    length = st.slider("Number of digits", 4, 64)
    pincode = str(random.randint(10**(length-1), 10**length - 1))
    st.write(pincode)
elif option == 'Random Password':
    length = st.slider("Password length", 4, 64)
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    st.write(password)
else:
    length = st.slider("Number of words", 4, 64)
    words = [random.choice(word_list) for _ in range(length)]
    password = '-'.join(words)
    st.write(password)
    ```