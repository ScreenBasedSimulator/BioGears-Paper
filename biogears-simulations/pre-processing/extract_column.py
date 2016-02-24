import numpy as np

if __name__ == '__main__':
    # path = './drugs/Fentanyl500ugResults/FentanylScenarioResults.txt'
    path = './drugs/Succinylcholine5mgResults/SuccinylcholineScenarioResults.txt'
    data = np.loadtxt(path, delimiter='\t', skiprows=1)
    selected = [0, 2, 8, 9, 14, 15]
    selected_data = data[:,selected]
    np.savetxt("./drugs/SuccinylcholineScenarioResults.csv", selected_data,
            fmt='%.2f', delimiter=',', header="time,hr,sp,dp,rr,spo2",comments='')
