# ASCII Text
import time
import pyfiglet

print(pyfiglet.figlet_format("Email Extractor", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

# Import Inbuilt Regex Module

import re

text = input("Enter the text >>> ")

pattern = re.compile("[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")

email = pattern.findall(text)

print(f"Emails Found > {email}" )
time.sleep(7)
