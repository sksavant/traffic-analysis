#!/usr/bin/python
from gpstraces import Point,Trace,Region

data_path="/media/savant/DATA/home/Acads/BTP/data/gpstraces/"
traces_dict = {}

#Convert number n to a string of 
def toString(n,dig):
    if n==0:
        return "0"*dig
    temp = 1
    while (temp<=dig):
        if n<10**temp:
            return "0"*(dig-temp)+str(n)
        temp=temp+1

def fileName(i):
    return "h"+toString(i,2)+"062011.csv"

def getAllTraces(i):
    data_fn = data_path+fileName(i)
    data_file = open(data_fn)
    data_file.readline() #Header files
    while(True):
        x = data_file.readline()
        if x=="":
            break
        #read x as a csv Simnumber, latitude,longitude,place,data,time,speed
        x = x.split(',')
        t = x[5]
        try:
            t = traces_dict[x[0]].append(Point(float(x[1])/3600.0,float(x[2])/3600.0),t)
        except KeyError:
            #print x[0] #No Key new sim
            trace_temp = Trace()
            trace_temp.append(Point(float(x[1])/3600.0,float(x[2])/3600.0),t)
            traces_dict[x[0]] = trace_temp
    data_file.close()

if __name__=="__main__":
    getAllTraces(1)
    #for i in range(30):
    #    print fileName(i)
