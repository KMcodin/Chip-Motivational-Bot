import csv

file = open('Contact Information (Responses).csv')
nameFile = open('names and nums.txt','a')
csvreader = csv.DictReader(file)


for row in csvreader:
    print(row['First Name'], row['Phone Number'])
    str = row['First Name'] + ":" + row['Phone Number'] + '\n'
    nameFile.write(str) 	


file.close()
nameFile.close()