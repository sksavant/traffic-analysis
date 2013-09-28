#!/usr/bin/python
# Author : Savant Krishna <savant.2020@gmail.com>

from gpstraces import Point,Trace,Region
import csv

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

class GPSData:
# The CSV files are in data_path
# @TODO Change it to correct path
    def __init__(self):
        self.data_path="/media/savant/DATA/home/Acads/BTP/data/gpstraces/"
# Stores a dictionary of traces with the SIM numbers as key
# Trace is defined in gpstraces module
        self.traces_dict = {}

# gets all the traces for the ith day
    def getDayTrace(self,i):
        data_fn = self.data_path+fileName(i)
        data_file = open(data_fn)
        data_file.readline() #Header files
        reader = csv.reader(data_file,skipinitialspace=True)
        ln = 1
#read x as a csv Simnumber, latitude,longitude,place,data,time,speed
        for x in reader:
            if x=="":
                break
            t = x[5]
            sim = x[0]
            ln = ln + 1
            if len(sim)!=10:
                continue
            try:
                if float(x[6])==0.0:
                    continue
            except ValueError:
                print "Bad data in line",ln
            try:
                self.traces_dict[x[0]].append(Point(float(x[1])/3600.0,float(x[2])/3600.0),t)
            except KeyError:
                #print x[0] #No Key new sim
                trace_temp = Trace()
                trace_temp.append(Point(float(x[1])/3600.0,float(x[2])/3600.0),t)
                self.traces_dict[x[0]] = trace_temp
        #print self.traces_dict.keys()
        #print len(self.traces_dict.keys())
        #temp_key = self.traces_dict.keys()[0]
        #temp_trace = self.traces_dict[temp_key]
        #print len(temp_trace.array)
        #temp_trace.findLowerLeftPoint().printMe()
        #temp_region = temp_trace.findMaxRegion()
        #temp_region.printMe()
        n = 0
        for k in self.traces_dict.keys():
            n = n + len(self.traces_dict[k].array)
        f = open("npoints.txt","a")
        f.write(str(n)+"\n")
        f.close()
        data_file.close()
        return self.traces_dict

    def getSimTrace(self,sim):
        try:
            t =  self.traces_dict[sim]
            return t
        except KeyError:
            return None

if __name__=="__main__":
    d = GPSData()
    for i in range(1,31):
        print "Getting traces from file:",fileName(i)
        d.getDayTrace(i)
    #for i in range(30):
    #    print fileName(i)
