import xml.etree.ElementTree as ET
tree = ET.parse('/home/nigel/Desktop/data.xml')
root = tree.getroot()

for country in root.findall('country'):
    outtext = str(country.tag) + " " + str(country.get('name')) + " "
    list = []
    flag = False
    if len(country.findall('rank')) > 1:
        print()
    else:
        outtext = outtext + str(country.find('rank').tag) + " " + str(country.find('rank').text) + " "
    if len(country.findall('year')) > 1:
        print()
    else:
        outtext = outtext + str(country.find('year').tag) + " " + str(country.find('year').text) + " "
    if len(country.findall('gdppc')) > 1:
        print()
    else:
        outtext = outtext + str(country.find('gdppc').tag) + " " + str(country.find('gdppc').text) + " "
    if len(country.findall('neighbor')) > 1:
        flag = True
        for neighbor in country.findall('neighbor'):
            list.append(outtext + str(neighbor.get('name') + " " + str(neighbor.get('direction'))))
    else:
        outtext = outtext + str(country.find('neighbor').get('name') + " " +
                                str(country.find('neighbor').get('direction')))
    if flag is True:
        for item in list:
            print(item)
    else:
        print(outtext)
