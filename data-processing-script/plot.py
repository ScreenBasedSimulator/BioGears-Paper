import matplotlib.pyplot as plt
import numpy as np
# import datetime as dt
# import csv
import pandas as pd
plot = []

#read the file from the csv_from_cae folder
csv_file = '2016-02-21_2103_PhysiologicalDataLog.csv'
df = pd.read_csv('csv_from_cae/'+csv_file, header = None)
i = 0

#time_stamp
time_stamp = []
for row in df[2]:
        time_stamp.append(row)

#HR
HR = []
for row in df[3]:
        HR.append(int(row))

#SBP
SBP = []
for row in df[4]:
        SBP.append(int(row))

#DBP
DBP = []
for row in df[5]:
        DBP.append(int(row))

#RR
RR = []
for row in df[6]:
        RR.append(int(row))

#SpO2
SpO2 = []
for row in df[7]:
        SpO2.append(int(row))

#plot.append(time_stamp)
plot.append(HR)
plot.append(SBP)
plot.append(DBP)
plot.append(RR)
plot.append(SpO2)

#time_stamp
#HR
#SBP
#DBP
#RR
#SpO2
#Barry: I changed the time from string to float because if the time is in string,
#plt.plot(time_stamp, HR) does not work: it says an array of float numbers is needed.
for i in range(0, len(time_stamp)):
    tmp = ""
    for letter in time_stamp[i]:
        
        if (letter.isdigit()):
            tmp += letter
    time_stamp[i] = int(tmp[-4:])

print time_stamp

from matplotlib.pyplot import cm

nums = np.linspace(0,1,5) - 0.01
color1=cm.rainbow(nums[0]) #purple  HR
color2=cm.rainbow(nums[1]) #blue    SBP
color3=cm.rainbow(nums[2]) #green   DBP
color4=cm.rainbow(nums[3]) #orange  RR
color5=cm.rainbow(nums[4]) #red     SpO2
# print color

for i in range(5):
    plt.plot(time_stamp, plot[i], color=cm.rainbow(nums[i]))

plt.title("Physiological Data Log")
plt.xlabel("Time")
plt.ylabel("Value")
plt.text(850,80,"purple: HR")
plt.text(850,70,"blue: SBP")
plt.text(850,60,"green: DBP")
plt.text(850,50,"orange: RR")
plt.text(850,40,"red: SpO2")
plt.show()