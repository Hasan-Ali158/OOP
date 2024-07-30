import csv
with open("personalities.csv","w") as csvfile:
    fieldnames = ['Name','Nationality','Gender','Age','Note']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnames,delimiter = "\t",quotechar="|")
    writer.writeheader()
    writer.writerow({'Name':'Babar Azam','Nationality': 'Pakistani','Gender' : 'Male', 'Age' : '29', 'Note' : 'G.O.A.T'})
    writer.writerow({'Name':'Adolf Hitler','Nationality': 'German','Gender' : 'Male', 'Age' : '50', 'Note' : 'Massacred Jews'})
