# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:21:13 2018

@author: Mohammad Ronosentono
"""
import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

def convertName(full_name):
    splitName = full_name.split()
    return splitName

def convertDOB(dob):
    splitDOB = dob.split('-')
    newDOB = splitDOB[1] + "/" + splitDOB[2] + "/" + splitDOB[0]   
    return newDOB

def convertSSN(ssn):
    splitSSN = ssn.split('-')
    newSSN = "***-**-" + splitSSN[2]
    return newSSN


employee_data = []
employee_data_list = []

# Path to collect data from the Resources folder
employeeCSV = os.path.join(".", "employee_data.csv")

# Read in the CSV file
with open(employeeCSV, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        #print(row)
        employee_data.append(row[0])
        
        # Split Name
        name = convertName(row[1])
        employee_data.append(name[0])
        employee_data.append(name[1])
        
        # Convert DOB
        employee_data.append(convertDOB(row[2]))
        
        # Convert SSN
        employee_data.append(convertSSN(row[3]))
        
        #Convert State
        employee_data.append(us_state_abbrev[row[4]])
        
#        print(employee_data)
        employee_data_list.append(employee_data)
        employee_data = []

# -------- Write Result to file-------- 
header = "Emp ID,First Name,Last Name,DOB,SSN,State"

with open("PyBoss.csv","w") as csvfile:
    csvfile.write(header + "\n") 

    for employee_data_csv in employee_data_list:
#        print(employee_data_csv)
        csvfile.write(employee_data_csv[0] + "," + employee_data_csv[1] + "," + \
                      employee_data_csv[2] + "," + employee_data_csv[3] + "," + \
                      employee_data_csv[4] + "," + employee_data_csv[5] + "\n") 

    csvfile.close()
