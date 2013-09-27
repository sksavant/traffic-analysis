#!/usr/bin/python
# Author : Savant Krishna <savant.2020@gmail.com>

from os import listdir
from gpstraces import Point,Trace,Region

# Find the map regions for each user the min and max latitude and longitude
# 
data_path = "/media/savant/DATA/home/Acads/BTP/data/geolife/Data/"
#no_of_users = 182
no_of_users = 2 #testing for 2

#Convert number n to a string of 
def toString(n,dig):
    if n==0:
        return "0"*dig
    temp = 1
    while (temp<=dig):
        if n<10**temp:
            return "0"*(dig-temp)+str(n)
        temp=temp+1

def getTraceFromPlt(file_name):
    t = Trace()
    din = open(file_name,"r")
    for i in range(6):
        din.readline() #first 6 lines are useless
    while(True):
        x = din.readline()
        if x=="":
            break
        #read x as a csv <lat>,<lng>,0,<alt>,date1,date2,time\r\n
        x = x.split(',') #split by comma
        p_temp = Point(float(x[0]),float(x[1]),float(x[3]))
        t.append(p_temp,None)
    # TODO write the reading part : done with points, convert time to known thing and pass to append
    return t

#Find the region given a folder path containing plt paths
def findUserRegion(ipath):
    #Now read through all the plt files and get minimum and maximum
    r_ans = None
    # get the filenamelist
    filenamelist = [f for f in listdir(ipath) if ".plt" in f]
    for f in filenamelist:
        t = getTraceFromPlt(ipath+f)
        r = t.findMaxRegion()
        r_ans = r_ans.union(r)
    return r_ans

#Find all the regions for n users in the folder path
def findAllRegions(path, n):
    for i in range(n):
        ipath = path+"/"+toString(i,3)+"/Trajectory/"
        print "Finding regions for user",i
        findUserRegion(ipath)

if __name__=="__main__":
    findAllRegions(data_path, no_of_users)
    print "Test 1"
    ipath = data_path+"/"+toString(0,3)+"/Trajectory/"
    fn = "20081023025304.plt"
    getTraceFromPlt(ipath+fn)
