import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import csv

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
    time_stamp[i] = tmp

print time_stamp
plt.plot(time_stamp, HR)
plt.plot(time_stamp, SBP)
plt.plot(time_stamp, DBP)
plt.plot(time_stamp, RR)
plt.plot(time_stamp, SpO2)
plt.title("Physiological Data Log")
plt.xlabel("Time")
plt.ylabel("Value")