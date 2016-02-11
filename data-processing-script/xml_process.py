import xml.etree.ElementTree as ET
tree = ET.parse('case1.xml')
root = tree.getroot()
output = root.find('data')
time_list_integer = []
val_list_integer = []
for var in output:
    for i in range(len(var)):
        if var[i].tag == 'vaname' and var[i].text == 'HR':
            time_text = var[i+1].text

            val_text = var[i+2].text
            time_list = time_text.split(",")
            val_list = val_text.split(",")

            for item in time_list:
                # print item
                if item != "":
                    time_list_integer.append(float(item))
            for item in val_list:
                if item != "":
                    val_list_integer.append(float(item))
        # if v[i].tag == 'vaname' and v.text == 'HR':
        #     print v.attrib

print time_list_integer
print "---------------------------------------------------------------------------------------------"
print val_list_integer

import numpy as np
np.savetxt("time_list_integer.csv", time_list_integer, delimiter=",", fmt='%s')
np.savetxt("val_list_integer.csv", val_list_integer, delimiter=",", fmt='%s')