import pandas as pd
#PatientTime, SCETime, WorldTime, HR, SBP, DBP, RR, SpO2, MAP, CVP, PAS, PAD, PCWP, CO, VT, PAO2, PACO2, PaO2 , PaCO2 , Hb, Hct, pH, TBody, TBlood, ICP, II, PAN2, Alv. ISO., Alv. SEV., Alv. HAL., Alv. ENF., pvO2, pvCO2, C-SPINE X, C-SPINE Y
# names = ['SCETime', 'WorldTime', 'HR','SBP','DBP','RR','SpO2','MAP','CVP',
#         'PAS','PAD','PCWP','CO','VT','PAO2','PACO2','PaO2','PaCO2','Hb',
#         'Hct','pH','TBody','TBlood', 'ICP','II','PAN2','Alv. ISO.','Alv. SEV.'
#         'Alv. HAL.','Alv. ENF.','pvO2','pvCO2','C-SPINE X', 'C-SPINE Y']
def recollect_data(csv_file = '2016-02-21_2103_PhysiologicalDataLog.csv'):
        #read the file from the csv_from_cae folder
        df = pd.read_csv('csv_from_cae/'+csv_file, header = None)
        i = 0

        #time_stamp
        time_stamp = []
        for row in df[2]:
                time_stamp.append(row)

        #HR
        HR = []
        for row in df[3]:
                print row
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

        return time_stamp,HR,SBP,DBP,RR,SpO2

if __name__ == "__main__":
        #test
        time_stamp,_,_,_,_,_ = recollect_data()