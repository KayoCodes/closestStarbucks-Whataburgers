import csv
import sys
import math
from haversine import *


class Store:
    def __init__(self,num,address,city,state,postcode,lat,long,distance) :
        self.num = num
        self.address = str(address)
        self.city = str(city)
        self.state = state
        self.postcode = postcode
        self.lat = float(lat)
        self.long = float(long)
        self.distance = float(distance)

    #def pr(self) :
     #   print(f"{self.num}, {self.address}, {self.city}, {self.state}, {self.postcode}, {self.lat}, {self.long}, {self.distance}")
    


class Querie:
    def __init__(self,lati,longi,numStores):
        self.lati = float(lati)
        self.longi = float(longi)
        self.stores= int(numStores)


with open(sys.argv[1], mode ='r')as file:
    csvFile= csv.reader(file)
    next(csvFile)
    stores =[]

    for line in csvFile:
        #if line[0] == "Store ID":
            #continue
        stores.append(Store(line[0],line[1], line[2],line[3],line[4],line[5],line[6],0))
        

with open('Queries.csv', mode ='r')as file:
    csvF= csv.reader(file)
    queries =[]
    next(csvF)
    for line in csvF:
        if line[0] == "Latitude":
            continue
        queries.append(Querie(line[0],line[1],line[2]))
file1 = open('myOutput.txt', 'w+')
#for i in range (0,len(stores)):
   # stores[i].distance = haversine((double)stores[i].lat, stores[i].long, 5,5 )

for i in range(0,len(queries)):
    sAmount = queries[i].stores
    qLat = queries[i].lati
    qLong = queries[i].longi
    sortedStores = []
    for j in range (0,len(stores)):
        stores[j].distance = haversine(stores[j].lat, stores[j].long, qLat, qLong)

    
  
    ith= randSelect(stores,0,len(stores)-1,sAmount)

    for k in range(0,ith):
      sortedStores.append(stores[k])
    sortedStores.sort(key=lambda s: (s.distance))
    
    print(len(sortedStores))
    file1.write("The " + str(sAmount) + " closest stores to (" + str(qLat) + ") (" + str(qLong) +") \n")
    for d in range(0,len(sortedStores)):
        file1.write(str(sortedStores[d].num) +" " +str(sortedStores[d].address)+" " + str(sortedStores[d].city)+" " + str(sortedStores[d].state)+" " + str(sortedStores[d].postcode)+" " + str(sortedStores[d].lat)+" " + str(sortedStores[d].long)+" " + str(round(sortedStores[d].distance,3)) +" miles" +"\n")
 
    file1.write("\n\n")