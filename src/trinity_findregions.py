#!/usr/bin/python
from gpstraces import Point,Trace,Region

data_path="/media/savant/DATA/home/Acads/BTP/data/gpstraces/"

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
    traces_dict = {}
    while(True):
        x = data_file.readline()
        if x=="":
            break
        #read x as a csv Simnumber, latitude,longitude,place,data,time,speed
        x = x.split(',')
        t = x[5]
        try:
            traces_dict[x[0]].append(Trace(Point(x[1]/3600.0,x[2]/3600.0),t))
        except KeyError:
            #No key
            traces_dict[x[0]]=[Trace(Point(float(x[1])/3600.0,float(x[2])/3600.0),t)]
    data_file.close()

if __name__=="__main__":
    getAllTraces(1)
    #for i in range(30):
    #    print fileName(i)
