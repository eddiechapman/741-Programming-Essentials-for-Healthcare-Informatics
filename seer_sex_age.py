# Using SEER dataset, this program computes distribution of various cancer types
# among age and sex.

import glob

import icdo # creates the icdo dictionary

def main():
    # make a list of all relevant file nmes in SEER dataset folder
    filelist = glob.glob("SEER_1973_2014_TEXTDATA/incidence/yr*/*.TXT")

    # initialize dictionaries seperated by sex and age
    m24_di = {}
    m49_di = {}
    m74_di = {}
    m75_di = {}
    f24_di = {}
    f49_di = {}
    f74_di = {}
    f75_di = {}

    for file in filelist:  # process each file
        infile = open(file, "r")
        for line in infile:
            # extract data via slice
            sex = line[23:24]
            age = line[24:27]
            disease = line[52:57]
            if sex == "1" and age <= "24":
                m24_di[disease] = m24_di.get(disease,0) + 1
            elif sex == "1" and (age >= "25" and age <= "49"):
                m49_di[disease] = m49_di.get(disease,0) + 1
            elif sex == "1" and (age >= "50" and age <= "74"):
                m74_di[disease] = m74_di.get(disease,0) + 1
            elif sex == "1" and age >= "75":  # any age greater than 74
                m75_di[disease] = m75_di.get(disease,0) + 1
            elif sex == "2" and age <= "24":
                f24_di[disease] = f24_di.get(disease,0) + 1
            elif sex == "2" and (age >= "25" and age <= "49"):
                f49_di[disease] = f49_di.get(disease,0) + 1
            elif sex == "2" and (age >= "50" and age <= "74"):
                f74_di[disease] = f74_di.get(disease,0) + 1
            elif sex == "2" and age >= "75":  # any age greater than 74
                f75_di[disease] = f75_di.get(disease,0) + 1
        infile.close()

    icdo_di = icdo.ICDO_dictionary() # use the ICD-O dictionary for disease names

    outfile = open("SEER_sex+age_out.csv", "w")
    # compute demographic totals for each disease
    for code in icdo_di:
        m24 = m24_di.get(code,0)
        m49 = m49_di.get(code,0)
        m74 = m74_di.get(code,0)
        m75 = m75_di.get(code,0)
        f24 = f24_di.get(code,0)
        f49 = f49_di.get(code,0)
        f74 = f74_di.get(code,0)
        f75 = f75_di.get(code,0)
        print(icdo_di[code].replace(",",""), ",", m24, ",", m49, ",", m74,
              ",", m75, ",", f24, ",", f49, ",", f74, ",", f75, file=outfile)
    outfile.close()

main()
