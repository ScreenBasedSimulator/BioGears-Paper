import pandas as pd
from matplotlib.pyplot import cm
import matplotlib.pyplot as plt
import numpy as np
#PatientTime, SCETime, WorldTime, HR, SBP, DBP, RR, SpO2, MAP, CVP, PAS, PAD, PCWP, CO, VT, PAO2, PACO2, PaO2 , PaCO2 , Hb, Hct, pH, TBody, TBlood, ICP, II, PAN2, Alv. ISO., Alv. SEV., Alv. HAL., Alv. ENF., pvO2, pvCO2, C-SPINE X, C-SPINE Y
names = ['PatientTime', 'SCETime', 'WorldTime', 'HR', 'SBP', 'DBP', 'RR', 'SpO2',
         'MAP', 'CVP', 'PAS', 'PAD', 'PCWP', 'CO', 'VT', 'PAO2', 'PACO2', 'PaO2' ,
         'PaCO2' , 'Hb', 'Hct', 'pH', 'TBody', 'TBlood', 'ICP', 'II', 'PAN2', 'Alv. ISO.',
         'Alv. SEV.', 'Alv. HAL.', 'Alv. ENF.', 'pvO2', 'pvCO2', 'C-SPINE X', 'C-SPINE Y']
def convert_column_to_list(df, column):
        res = []
        for item in df[column]:
                res.append(item)
        return res
def recollect_data(csv_file = '2016-02-21_2103_PhysiologicalDataLog.csv', folder_name='succinylcholine-77mg'):
        #read the file from the csv_from_cae folder

        path = '/'.join(['csv_from_cae/output',folder_name, csv_file])
        df = pd.read_csv(path, skiprows=7, header=0, names=names, index_col='PatientTime')

        #time_stamp
        time_stamp = convert_column_to_list(df, 'SCETime')

        #Heart Rate
        HR = convert_column_to_list(df, 'HR')

        #SBP
        SBP = convert_column_to_list(df, 'SBP')

        #DBP
        DBP = convert_column_to_list(df, 'DBP')

        #RR
        RR = convert_column_to_list(df, 'RR')

        #SpO2
        SpO2 = convert_column_to_list(df, 'SpO2')

        return time_stamp, HR, SBP, DBP, RR, SpO2

def convert_to_float(time_stamp):
        import time

# struct_time = time.strptime("30 Nov 00", "%d %b %y")
        res = []
        for item in time_stamp:
                struct_time = time.strptime(item," %H:%M:%S")
                print struct_time
                res.append(struct_time.tm_hour * 3600 + struct_time.tm_min * 60 + struct_time.tm_sec)
        print res
        return res
def max_d(HR, SBP, DBP, RR, SpO2):

        return max(max(max(HR,SBP),max(DBP, RR)),SpO2)
def min_d(HR, SBP, DBP, RR, SpO2):

        return min(min(min(HR,SBP),min(DBP, RR)),SpO2)
def plot_graph(time_stamp, HR, SBP, DBP, RR, SpO2):
        plot = []
        plot.append(HR)
        plot.append(SBP)
        plot.append(DBP)
        plot.append(RR)
        plot.append(SpO2)



        nums = np.linspace(0,1,5) - 0.01
        time_stamp = convert_to_float(time_stamp)

        min_x = time_stamp[0]
        max_x = time_stamp[-1]
        min_y = max_d(HR, SBP, DBP, RR, SpO2)
        max_y = min_d(HR, SBP, DBP, RR, SpO2)

        for i in range(5):
                plt.plot(time_stamp, plot[i], color=cm.rainbow(nums[i]))

        # fig = plt.figure(1)
        # ax = fig.add_subplot(111, autoscale_on=False, xlim=(min_x,max_x), ylim=(min_y,max_y))


        plt.title("Physiological Data Log")
        plt.xlabel("Time")
        plt.ylabel("Value")
        # plt.text(50,80,"purple: HR")
        # plt.text(50,70,"blue: SBP")
        # plt.text(50,60,"green: DBP")
        # plt.text(50,50,"orange: RR")
        # plt.text(50,40,"red: SpO2")

        arrow_width = 6
        arrow_shrink = 0.1
        arrow_frac = 0.4
        plt.annotate("HR", xy=(max_x*4/5,HR[len(time_stamp)*4/5-1]),xytext=(max_x*4/5 - 30,HR[len(time_stamp)*4/5-1] + 10),
                     arrowprops=dict(facecolor='purple', shrink=arrow_shrink, width=arrow_width, frac=arrow_frac))

        plt.annotate("SBP", xy=(max_x*2/5,SBP[len(time_stamp)*2/5-1]),xytext=(max_x*2/5 - 30,SBP[len(time_stamp)*2/5-1] + 10),
                     arrowprops=dict(facecolor='blue', shrink=arrow_shrink, width=arrow_width, frac=arrow_frac))

        plt.annotate("DBP", xy=(max_x*3/5,DBP[len(time_stamp)*3/5-1]),xytext=(max_x*3/5 - 30,DBP[len(time_stamp)*3/5-1] + 10),
                     arrowprops=dict(facecolor='green', shrink=arrow_shrink, width=arrow_width, frac=arrow_frac))

        plt.annotate("RR", xy=(max_x/5,RR[len(time_stamp)/5-1]),xytext=(max_x/5 - 30,RR[len(time_stamp)/5-1] + 10),
                     arrowprops=dict(facecolor='orange', shrink=arrow_shrink, width=arrow_width, frac=arrow_frac))

        plt.annotate("SpO2", xy=(max_x,SpO2[-1]),xytext=(max_x - 30,SpO2[len(time_stamp)-1] + 10),
                     arrowprops=dict(facecolor='red', shrink=arrow_shrink, width=arrow_width, frac=arrow_frac))
        plt.show()
if __name__ == "__main__":
        # time_stamp, HR, SBP, DBP, RR, SpO2 = recollect_data()
        # plot_graph(time_stamp, HR, SBP, DBP, RR, SpO2)

        time_stamp, HR, SBP, DBP, RR, SpO2 = recollect_data(csv_file='2016-02-21_2103_PhysiologicalDataLog.csv',
                                                            folder_name='succinylcholine-77mg')
        plot_graph(time_stamp, HR, SBP, DBP, RR, SpO2)

