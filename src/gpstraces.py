
class Point:
    def __init__(self):
        self.lat = 0.0
        self.lng = 0.0
        self.alt = 0.0
    def __init__(self,p):
        self.lat = p.lat
        self.lng = p.lng
        self.alt = p.alt
    def __init__(self,lat,lng,alt=0.0):
        self.lat = lat
        self.lng = lng
        self.alt = alt
    def getLat(self):
        return self.lat
    def getLng(self):
        return self.lng
    def getLatLng(self):
        return (self.getLat(),self.getLang())

class Trace:
    def __init__(self):
        self.array = []
    def append(self,p,t):
        self.array.append((p,t))
    def delete(self):
        self.array.pop()
    def findLowerLeftPoint(self):
        x = map(min, zip(*self.array))
        return Point(0,0,0) #Point(x[0],x[1])
    def findUpperRightPoint(self):
        x = map(max, zip(*self.array))
        return Point(x[0],x[1])
    def findMaxRegion(self):
        return Region(self.findLowerLeftPoint(), self.findUpperRightPoint())


class Region:
    def __init__(self,pll,pur):
        self.pl = []
        self.pl.append(Point(pll))
        self.pl.append(Point(pur.getLat(),pll.getLng()))
        self.pl.append(Point(pur))
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

