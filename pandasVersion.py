import xml.etree.ElementTree as ET
import pandas as pd
tree = ET.parse('/home/nigel/Desktop/data.xml')
root = tree.getroot()

df_cols = ["country", "rank", "year", "gdppc", "neighbor", "direction"]
rows = []

for node in root:
    country = node.attrib.get("name")
    rank = node.find("rank").text if node is not None else None
    year = node.find("year").text if node is not None else None
    gdppc = node.find("gdppc").text if node is not None else None
    if len(node.findall("neighbor")) > 1:
        for temp in node.findall("neighbor"):
            neighbor = temp.attrib.get("name")
            direction = temp.attrib.get("direction")
            rows.append({"country": country, "rank": rank,
                         "year": year, "gdppc": gdppc, "neighbor": neighbor, "direction": direction})
    else:
        neighbor = node.find("neighbor").attrib.get("name")
        direction = node.find("neighbor").attrib.get("direction")
        rows.append({"country": country, "rank": rank,
                     "year": year, "gdppc": gdppc, "neighbor": neighbor, "direction": direction})

out_df = pd.DataFrame(rows, columns=df_cols)
print(out_df)
out_df.to_csv('/home/nigel/Desktop/dataframe.csv', header=True)
