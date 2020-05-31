from os import listdir, path
import xml.etree.ElementTree as ET
import pandas as pd
import csv
from os import listdir, path


def filldata(newroot):
    header = pd.MultiIndex.from_product([[newroot.find("date").attrib.get("name")],
                                         ["country", "rank", "year", "gdppc", "neighbor", "direction"]],
                                        names=['date', 'data'])
    rows = []
    for node in newroot:
        for inner in node.findall("country"):
            country = inner.attrib.get("name")
            rank = inner.find("rank").text if inner is not None else None
            year = inner.find("year").text if inner is not None else None
            gdppc = inner.find("gdppc").text if inner is not None else None
            if len(inner.findall("neighbor")) > 1:
                for temp in inner.findall("neighbor"):
                    neighbor = temp.attrib.get("name")
                    direction = temp.attrib.get("direction")
                    rows.append({header[0]: country, header[1]: rank,
                                 header[2]: year, header[3]: gdppc, header[4]: neighbor,
                                 header[5]: direction})
            else:
                neighbor = inner.find("neighbor").attrib.get("name")
                direction = inner.find("neighbor").attrib.get("direction")
                rows.append({header[0]: country, header[1]: rank,
                             header[2]: year, header[3]: gdppc, header[4]: neighbor,
                             header[5]: direction})
    out_df = pd.DataFrame(rows, columns=header)
    dataframes.append(out_df)


mypath = '/home/nigel/Desktop/'
files = [path.join(mypath, f) for f in listdir(mypath) if f.endswith('.xml')]
dataframes = []
for file in files:
    tree = ET.parse(file)
    root = tree.getroot()
    filldata(root)
concat_dfs = pd.concat(dataframes, axis=1, sort=False)
concat_dfs.to_csv('/home/nigel/Desktop/dataframe.csv', index=False, header=True)
holdRows = []
with open('/home/nigel/Desktop/dataframe.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in readCSV:
        if count == 1:
            count += 1
            continue
        if row[0] == row[1]:
            original = row[0]
            for i in range(len(row)):
                if i == 0:
                    continue
                else:
                    if row[i] == original:
                        row[i] = ''
                    else:
                        original = row[i]
        holdRows.append(row)
        count += 1
with open('/home/nigel/Desktop/dataframe.csv',  'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in holdRows:
        writer.writerow(row)
