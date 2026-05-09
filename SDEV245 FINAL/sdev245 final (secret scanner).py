#Kody Fatch
#SDEV245 Module 8 Final - Secret Scanner
#README file and recording of program in folder that contains this program.

#--------Imports--------------------
import re
import os
import argparse
from pathlib import Path

#---------Functions-----------------
def file_scan(file_path, patterns):
    secrets = []
    compiled_patterns = [re.compile(p) for p in patterns]
    try:
        with open(file_path, "r") as f:
            for line_num, line in enumerate(f, 1):
                for pat in compiled_patterns:
                    if pat.search(line):
                        secrets.append({
                            "line": line_num,
                            "content": line.strip(),
                            "pattern": pat.compiled_patterns
                        })
    except FileNotFoundError:
        print(f"{file_path} not found.")

    return secrets

#-------------Lists-------------------
pattern_list = {"Instagram Username": r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)",
                "Instagram Hashtag": r"(?:#)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)",
                "Google API": r"AIza[0-9A-Za-z-_]{35}",
                "Github PAT": r"^ghp_[a-zA-Z0-9]{36}$",
                "Github Refresh Token": r"^ghr_[a-zA-Z0-9]{36}$"}

#----------Main-Program-------------
print("Starting Secret Scanner...")
file_path = r"C:\Users\knfat\OneDrive\Desktop\SchoolResources\Security_and_Secure_Coding\SDEV245 FINAL\sdev245_final_secrets.txt"
results = file_scan(file_path, pattern_list)
if results == []:
    print("No secrets found.")
else:
    for match in results:
        print(match)
print("Ending Program...")