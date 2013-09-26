#!/usr/bin/python
from gpstraces import Point,Trace,Region

# The CSV files are in data_path
# @TODO Change it to correct path
data_path="/media/savant/DATA/home/Acads/BTP/data/gpstraces/"
# Stores a dictionary of traces with the SIM numbers as key
# Trace is defined in gpstraces module
traces_dict = {}

#Convert number n to a string of dig digits
def toString(n,dig):
    if n==0:
        return "0"*dig
    temp = 1
    while (temp<=dig):
        if n<10**temp:
            return "0"*(dig-temp)+str(n)
        temp=temp+1

# Returns the filename given the day
def fileName(i):
    return "h"+toString(i,2)+"062011.csv"

# gets all the traces for the ith day
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
        sim = x[0]
        if len(sim)!=10:
            continue
        try:
            t = traces_dict[x[0]].append(Point(float(x[1])/3600.0,float(x[2])/3600.0),t)
        except KeyError:
            #print x[0] #No Key new sim
            trace_temp = Trace()
            trace_temp.append(Point(float(x[1])/3600.0,float(x[2])/3600.0),t)
            traces_dict[x[0]] = trace_temp
    print traces_dict.keys()
    print len(traces_dict.keys())
    #temp_key = traces_dict.keys()[0]
    #temp_trace = traces_dict[temp_key]
    #print len(temp_trace.array)
    #temp_trace.findLowerLeftPoint().printMe()
    #temp_region = temp_trace.findMaxRegion()
    #temp_region.printMe()
    data_file.close()

if __name__=="__main__":
    for i in range(1,31):
        print "Getting traces from file:",fileName(i)
        getAllTraces(i)

    #for i in range(30):
    #    print fileName(i)
