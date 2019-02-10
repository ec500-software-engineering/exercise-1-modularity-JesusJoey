import sys
from Input_module import input_module
from Analyzer import Analyzer
import Output_Module


def main():
    # user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time):
    data = {}
    LINES=open("input").read().splitlines()
    for idx,line in enumerate(LINES):
        items = line.split()
        #print(items)
        Data=input_module(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[8])
        #Data=input_module.implement_filter(Data)
        data[idx]=Data.dic
        print data[idx]

    #def __init__(self, Systolic_BP, Diastolic_BP, Heart_Rate, Heart_Oxy_Level, Body_temp):
    for idx,content in enumerate(data):
        process=Analyzer(data[idx]["Systolic_BP"],data[idx]["Diastolic_BP"],data[idx]["heartrate"],data[idx]["blood_oxygen"],data[idx]["temperature"])
        signal_loss=process.Signal_Loss(data[idx]["heartrate"],data[idx]["temperature"])
        shock_alert=process.Shock_Alert(data[idx]["heartrate"],data[idx]["temperature"])
        oxygen_supply=process.Oxygen_Supply(data[idx]["blood_oxygen"])
        fever=process.Fever(data[idx]["temperature"])
        hypotension=process.Hypotension(data[idx]["Systolic_BP"],data[idx]["Diastolic_BP"])
        hypertension=process.Hypertension(data[idx]["Systolic_BP"],data[idx]["Diastolic_BP"])

        result=Output_Module.display_basic_iuput_data(signal_loss, shock_alert, oxygen_supply, fever, hypotension, hypertension)
        print 'Patient',idx,'Alert'
        print result





if __name__ == '__main__':
    main()
