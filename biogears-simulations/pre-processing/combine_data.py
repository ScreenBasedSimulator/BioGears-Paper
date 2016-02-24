import numpy as np
import glob, os
fileList=['bradypnea/AnesthesiaMachineStop30Results/AnesthesiaMachineVariedConfigurationResults.txt',
'bradypnea/AnesthesiaMachineStop120Results/AnesthesiaMachineVariedConfigurationResults.txt']

if __name__ == '__main__':
    # path = './drugs/Fentanyl500ugResults/FentanylScenarioResults.txt'
    selected_data = None;
    selected_column = 15;
    for path in fileList:
        data = np.loadtxt(path, delimiter='\t', skiprows=1)
        selected = [0, 15]
        if (selected_data == None):
            selected_data = data[:,[0,15]]
        else:
            print selected_data.shape
            newData =  data[range(0,selected_data.shape[0]),[15]]
            print newData.shape
            selected_data = np.concatenate((selected_data, newData[:,None]), axis=1)
    np.savetxt("./bradypnea/result.csv", selected_data,
            fmt='%.2f', delimiter=',', header="time,30,120",comments='')
