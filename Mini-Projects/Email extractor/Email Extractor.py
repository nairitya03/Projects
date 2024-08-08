import pyfiglet

print(pyfiglet.figlet_format("Email Extractor", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

import re
import email_validator

pattern = re.compile(r"[a-zA-Z0-9._%+-]+(?:\.[a-zA-Z0-9._%+-]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

def valid_emails(text):
  email = pattern.findall(text)
  print(f"Valid Emails Found > {email}")

valid_emails(input("Enter the text >>> "))
# while True:
#     response = input("Do you want to extract emails from another text? (yes/no) >>> ")
#     if response.lower() == "yes":
#       valid_emails()
#     elif response.lower() == "no":
#         break
#     else:
#         print("Invalid response. Please enter 'yes' or 'no'.")
