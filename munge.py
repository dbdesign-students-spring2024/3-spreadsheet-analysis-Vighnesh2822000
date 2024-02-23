import csv
import os

filemta = os.path.join(r'C:\Spring 2024\database\3-spreadsheet-analysis-Vighnesh2822000\data','mta_data.csv')
fvar = open(filemta, 'r')
fileclean = os.path.join(r'C:\Spring 2024\database\3-spreadsheet-analysis-Vighnesh2822000\data','clean_data.csv')
fclean= open(fileclean, 'w', newline ='')
readerobject = csv.DictReader(fvar)
temp =[]    # temporary variable to store all the rows with systemwide data
l =[]      # variable to get the fieldnames
for row in readerobject.fieldnames:
    l.append(row)
l.remove('period')   # removing the period column
writerobject = csv.DictWriter(fclean, fieldnames = l)
writerobject.writeheader()
l = set(l)
for row in readerobject:
    row = {k: row[k] for k in row if k in l}     # taking out the period column from the individual rows
    if row['borough'] =="Systemwide":
        temp.append(row)
    else:
        writerobject.writerow(row) 
      
for row in temp:                 #adding all the systmwide data at the end of the csv
    writerobject.writerow(row)

    

    

