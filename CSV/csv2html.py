import csv

total = []

# file = 'CSV\optredens_aankomend.csv'
file = 'CSV\optredens_geweest.csv'


with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        total.append(row)



for gig in total:
    print("<tr>")
    for data in gig:
        print("<td>",data,"</td>")
    print("</tr>")