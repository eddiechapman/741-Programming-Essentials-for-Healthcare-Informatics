import re

# A function that makes a dictionary from ICD-O codes;
# codes as keys and disease name as values
def ICDO_dictionary():
 
    d = {}

    infile = open("icdo3.txt","r")
    for line in infile:
        # regular expression to read the codes and diesaes names
        r = re.search("(\d+/\d+)\s+(.+)",line)
     
        if (r) :
            code = r.group(1)
            code = code.replace("/","")
            disease = r.group(2)
            disease=disease.rstrip()
            disease = disease.lower()
            d[code] = disease

    infile.close()
    return d        

def query_ICDO_dictionary():

    di = ICDO_dictionary()
    
    while (True):
        code = input("Give the code without slash (empty to quit): ")
        if (code=="") :
            break
        if code in di:
            print("The disease is: ",di[code],"\n")
        else:
             print("The code does not exist in ICD-O.\n")
