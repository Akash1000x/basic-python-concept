citytemp = open("citytemp.csv")

rec1 = citytemp.readline()
cityname,temprature,unit = rec1.split(',')
prev_city = cityname 
# print(temprature)

citytemp.seek(0)

avgtemp = 0.0
count = 0
tempsum = 0

for i in citytemp:
    i = i.rstrip("\n")
    cityname,temprature,unit = i.split(',')
    # print(i)

    if unit=="C":
        temprature = (float(temprature)*9/5)+32
    if cityname != prev_city:
        avgtemp = tempsum/count
        print(prev_city+ "="+str(round(avgtemp,2)))
        prev_city= cityname
        avgtemp = 0.0
        tempsum  = 0
        count = 0 
    
    tempsum = tempsum + float(temprature) 
    count = count+1

else:
    avgtemp = tempsum/count
    print(prev_city+ "="+str(round(avgtemp,2)))





