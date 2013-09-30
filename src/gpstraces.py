#!/usr/bin/python
# Author : Savant Krishna <savant.2020@gmail.com>

import math as math

class Point:
    def __init__(self,lat=0.0,lng=0.0,alt=0.0):
        self.lat = lat
        self.lng = lng
        self.alt = alt

    def getLat(self):
        return self.lat

    def getLng(self):
        return self.lng

    def getLatLng(self):
        return (self.getLat(),self.getLang())

    def getCopy(self):
        p = Point()
        p.lat = self.lat
        p.lng = self.lng
        p.alt = self.alt
        return p

    def printMe(self):
        print "Lat: ",self.lat,", Lng:",self.lng,", Alt:",self.alt

    # Haversine formula example in Python
    # Author: Wayne Dyck
    def getDistance(self,p):
        lat1, lon1 = [self.lat,self.lng]
        lat2, lon2 = [p.lat,p.lng]
        radius = 6371.0 # km

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c

        return d

class Trace:
    def __init__(self):
        self.array = []
    def append(self,p,t):
        self.array.append((p,t))
    def delete(self):
        self.array.pop()
    def findLowerLeftPoint(self):
        #x = map(min, zip(*self.array)) #Incorrect
        lt = 200
        ln = 200
        for x in self.array:
            if x[0].lat < lt:
                lt = x[0].lat
            if x[0].lng < ln:
                ln = x[0].lng
        return Point(lt,ln)
    def findUpperRightPoint(self):
        #x = map(max, zip(*self.array))
        lt = 0
        ln = 0
        for x in self.array:
            if x[0].lat > lt:
                lt = x[0].lat
            if x[0].lng > ln:
                ln = x[0].lng
        return Point(lt,ln)
    def findMaxRegion(self):
        return Region(self.findLowerLeftPoint(), self.findUpperRightPoint())


class Region:
    def __init__(self,pll,pur):
        self.pl = []
        self.pl.append(pll.getCopy())
        self.pl.append(Point(pur.getLat(),pll.getLng()))
        self.pl.append(pur.getCopy())
        self.pl.append(Point(pll.getLat(),pur.getLng()))
    def union(self,r):
        #TODO write the union of regions function
        #Assuming rectangular regions
        pll_temp = Point(min(self.getLLPoint().getLat(),r.getLLPoint().getLat()),min(self.getLLPoint().getLng(),r.getLLPoint().getLng()))
        pur_temp = Point(max(self.getURPoint().getLat(),r.getURPoint().getLat()),max(self.getURPoint().getLng(),r.getURPoint().getLng()))
        rnew = Region(pll_temp,pur_temp)
        return rnew
    def getLLPoint(self):
        return self.pl[0]
    def getURPoint(self):
        return self.pl[2]
    def printMe(self):
        print "LowerLeftPoint:\n",
        (self.getLLPoint()).printMe()
        print "UpperRightPoint:\n",
        self.getURPoint().printMe()

