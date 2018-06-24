# ICDdict.py
# A function that makes a dictionary from ICD codes;
# codes as keys and disease names as values

import re

def ICD_dictionary():

    d = {}

    infile = open("ICD.txt", "r")
    for line in infile:
        # Regular expression to read codes and disease names
        r = re.search("\s+([A-Z]\S+)\s+(.+)\s+", line)

        if (r):
            code = r.group(1)
            disease = r.group(2)
            disease = disease.rstrip()
            disease = disease.replace("\"","")
            disease = disease.lower()
            d[code] = disease

    infile.close()

    return d

# An interactive function to query the ICD dictionary.
def query_ICD_dictionary():

    di = ICD_dictionary()

    while (True):
        code = input("Give the code (empty to quit): ")
        if (code == ""):
            break
        if code in di:
            print("The disease is: ",di[code],"\n")
        else:
            print("Code does not exist.\n")

ICD_dictionary()
query_ICD_dictionary()
