#Kody Fatch
#SDEV245 Module 8 Final - Secret Scanner
#README file and recording of program in folder that contains this program.

#--------Imports--------------------
import re
import os
import argparse

#---------Functions-----------------

def file_scan(file_path):
    patterns = [(r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)"),
                (r"(?:#)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)"),
                (r"AIza[0-9A-Za-z-_]{35}"),
                (r"^ghp_[a-zA-Z0-9]{36}$"),
                (r"^ghr_[a-zA-Z0-9]{36}$")
                ]
    secrets = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            # for  in patterns.items():
            #     if re.search(pattern, line):
            #         secrets.append[])
    return secrets

#----------Main-Program-------------
print("Starting Secret Scanner...")
# file_path = input("Enter the file path to be scanned:\n") Commented out for testing
file_path = "C:/Users/knfat/OneDrive/Desktop/SchoolResources/sdev245_final_secrets.txt"
if os.path.exists(file_path):
    results = file_scan(file_path)
    if results:
        print(results)
    else:
        print("No secrets found in given file path.")
print("Ending Program...")

#-----------Test--------------
# patterns = {"Instagram Username": r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)",
#                 "Instagram Hashtag": r"(?:#)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)",
#                 "Google API": r"AIza[0-9A-Za-z-_]{35}",
#                 "Github PAT": r"^ghp_[a-zA-Z0-9]{36}$",
#                 "Github Refresh Token": r"^ghr_[a-zA-Z0-9]{36}$"}