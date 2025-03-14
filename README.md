# Password Generator

Welcome to the **Password Generator** project! This is a Python-based tool designed to create three distinct types of passwords:
- **Random Password**: A secure combination of uppercase letters, lowercase letters, and digits.
- **Memorable Password**: A random sequence of digits for easy recall.
- **Pin-like Password**: A sequence of random words separated by hyphens, generated using the NLTK library.

This project leverages Python’s standard libraries and the NLTK package to provide versatile password generation options.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
- [Configuration](#configuration)
- [Examples](#examples)

---

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/password-generator.git

Replace yourusername with your actual GitHub username.

    Navigate to the Project Directory:
    bash

cd password-generator
Install Dependencies: Ensure you have Python 3.6+ installed, then install the required packages:
bash
pip install -r requirements.txt

    Note: The requirements.txt file lists nltk, which is used for word generation in the pin-like password.

Download NLTK Word Data: The pin-like password generator requires a list of English words from NLTK. Run the following in a Python shell:
python

    import nltk
    nltk.download('words')

## Usage

To generate passwords, simply run the main script:
bash
python main.py

This will output three types of passwords with default settings:

    A random password (10 characters, e.g., Kj9pLm2xQv)
    A memorable password (10 digits, e.g., 5839201746)
    A pin-like password (5 words, e.g., apple-river-cloud-tree-stone)

You can also customize the password generation by interacting with the classes directly (see Configuration and Examples).
Classes

The project is structured around the following classes:

    Parent: An abstract base class defining the common interface for all password generators.
    RandomPassword: Generates a random password with a mix of uppercase letters, lowercase letters, and digits.
    Memorable: Produces a numeric password of specified length, ideal for memorization.
    Pin: Creates a hyphen-separated sequence of random words using NLTK’s word list.

## Configuration

You can customize the password length or number of words by passing a size parameter when instantiating the classes. The default size is 10 for RandomPassword and Memorable, and 5 for Pin.

Example customization:
python
from password_generator import RandomPassword
rp = RandomPassword(12)  # Set length to 12 characters
print("Random Password:", rp.generator())
## Examples

Here are some practical examples to demonstrate how to use the password generator:

    Generate a Random Password (12 characters):
    python

from password_generator import RandomPassword
rp = RandomPassword(12)
print("Random Password:", rp.generator())  # Output: e.g., X7kP9mN2vR4q
Generate a Memorable Password (8 digits):
python
from password_generator import Memorable
mp = Memorable(8)
print("Memorable Password:", mp.generator())  # Output: e.g., 92748301
Generate a Pin-like Password (3 words):
python
from password_generator import Pin
pp = Pin(3)
print("Pin Password:", pp.generator())  # Output: e.g., sun-rain-forest