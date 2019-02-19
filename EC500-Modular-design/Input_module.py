import time
class input_module:

    def __init__(self, user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time):

        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.heartrate = heartrate
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.blood_oxygen = blood_oxygen
        self.temperature = temperature
        self.time = time
        self.dic = {"gender": gender, "heartrate": heartrate,
                    "Diastolic_BP": Diastolic_BP, "Systolic_BP":Systolic_BP, "blood_oxygen": blood_oxygen,
                    "temperature": temperature, "time": time}


    def implement_filter(self):
        for key in self.dic.keys():
            if (key != "user_id" and key != "age" and key != "gender" and key != "time"):
                tmp = filter(self.dic[key])
                self.dic[key] = tmp



    def return_request(self, wire):
        alert = 1
        data_db = 2
        if (wire == alert):
            user_data_dic = {"heartrate": self.heartrate,
                    "Diastolic_BP": self.Diastolic_BP, "Systolic_BP": self.Systolic_BP, "blood_oxygen": self.blood_oxygen, 
                    "temperature": self.temperature, "time": self.time}
            return user_data_dic
        if (wire == data_db):
            return self.user_id, self.dic
        
        
#my_data = input_api('a', 1, 'male', 1, 1, 10000, 1, 1, 1)
#print(my_data.dic)
#my_data.implement_filter()
#print(my_data.dic)
#print(my_data.return_request())

def input():
    # user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time):
    data={}
    LINES=open("input").read().splitlines()
    time.sleep(0.5)
    for idx,line in enumerate(LINES):
        items = line.split()
        #print(items)
        Data=input_module(items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[8])
        #Data=input_module.implement_filter(Data)
        data[idx]=Data.dic
        #print data[idx]
    return data

data = input()
for item in data:
    print(data[item])
