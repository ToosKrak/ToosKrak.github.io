import csv
import numpy as np
import datetime as dt

header_file_path = "CSV/optredens_head.html"
footer_file_path = "CSV/optredens_foot.html"


with open(header_file_path, 'r') as file:
    header_file_content = file.read()

with open(footer_file_path, 'r') as file:
    footer_file_content = file.read()


total = []
totalBev = []
totalGeweest = []
totalAankomend = []



csv_data = 'CSV/optredens.csv'

with open(csv_data, newline='') as csvfile:
    # spamreader = csv.reader(csvfile, delimiter=',', quotechar='|', encoding='utf-8-sig')
    spamreader = csv.reader(open(csv_data, encoding='utf-8-sig'), delimiter=',', quotechar='|')
    # spamreader = open(csv_data, 'r', delimiter=',', encoding='utf-8-sig')
    for row in spamreader:
        total.append(row)

print(total)

for gig in total:
    if gig[-1] == '1':
        totalBev.append(gig)

for gig in totalBev:
    gig[0] = str(gig[0])
    gig[1] = str(gig[1])
    date = gig[2]
    gig[2] = np.datetime64(date[6:10] + "-" + date[3:5] + "-" + date[0:2])
    gig[3] = str(gig[3])

totalBev = np.array(totalBev)
totalBev = totalBev[:,0:4]

totalBev = totalBev[totalBev[:, 2].argsort()]


for gig in totalBev:
    if gig[2] >= np.datetime64('today'):
        totalAankomend.append(gig)
    else:
        totalGeweest.append(gig)

totalGeweest = np.array(totalGeweest)
totalGeweest = np.flip(totalGeweest,axis=0)


with open("CSV/Optredens.html", "w", encoding="utf-8") as f:
    f.write(header_file_content)
    for gig in totalAankomend:
        f.write("\n")
        f.write("		    <tr>\n")
        f.write("		        <td> " + gig[0] + " </td>\n")
        f.write("				<td> " + gig[1] + " </td>\n")
        date = str(gig[2])
        f.write("				<td> " + date[8:10] + "-" + date[5:7] + "-" + date[0:4] + " </td>\n")
        f.write("				<td> " + gig[3] + " </td>\n")
        f.write("		    </tr>\n")

    f.write("		</table>\n\n		<hr>\n		<h2>Afgelopen optredens</h2>\n		<p>Hier kan je ons niet meer live zien, omdat het al geweest is.</p>\n\n		<table>")
    f.write("\n")
    f.write("			<tr>\n")
    f.write("    			<th>Zaal</th>\n")
    f.write("    			<th>Plaats</th>\n")
    f.write("    			<th>Datum</th>\n")
    f.write("				<th>Met, waar of waarom</th>\n")
    f.write("  			</tr>\n")



    for gig in totalGeweest:
        f.write("\n")
        f.write("		    <tr>\n")
        f.write("				<td> " + gig[0] + " </td>\n")
        f.write("				<td> " + gig[1] + " </td>\n")
        date = str(gig[2])
        f.write("				<td> " + date[8:10] + "-" + date[5:7] + "-" + date[0:4] + " </td>\n")
        f.write("				<td> " + gig[3] + " </td>\n")
        f.write("		    </tr>\n")
    f.write(footer_file_content)



# print(data)

# print(totalBev)
