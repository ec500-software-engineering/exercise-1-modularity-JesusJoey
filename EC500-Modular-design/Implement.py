import time
import threading
import  Input_module
from Analyzer import Analyzer
import Output_Module

def process():
    # user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time):
    #def __init__(self, Systolic_BP, Diastolic_BP, Heart_Rate, Heart_Oxy_Level, Body_temp):
    data=Input_module.input()
    time.sleep(0.5)
    for idx,content in enumerate(data):
        process=Analyzer(data[idx]["Systolic_BP"],data[idx]["Diastolic_BP"],data[idx]["heartrate"],data[idx]["blood_oxygen"],data[idx]["temperature"])
        signal_loss=process.Signal_Loss(data[idx]["heartrate"],data[idx]["temperature"])
        shock_alert=process.Shock_Alert(data[idx]["heartrate"],data[idx]["temperature"])
        oxygen_supply=process.Oxygen_Supply(data[idx]["blood_oxygen"])
        fever=process.Fever(data[idx]["temperature"])
        hypotension=process.Hypotension(data[idx]["Systolic_BP"],data[idx]["Diastolic_BP"])
        hypertension=process.Hypertension(data[idx]["Systolic_BP"],data[idx]["Diastolic_BP"])

        result=Output_Module.display_basic_iuput_data(signal_loss, shock_alert, oxygen_supply, fever, hypotension, hypertension)
        print('--------------------------------------')
        print ('Patient  No', idx, 'Alert')
        for index in result:
            print(index,':',result[index])


def main():
    #t1 = threading.Thread(target=Input_module.input())
    t2 = threading.Thread(target=process)

    #t1.start()
    t2.start()

    #t1.join()
    t2.join()



if __name__ == '__main__':
    main()
