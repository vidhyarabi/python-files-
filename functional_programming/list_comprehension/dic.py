# find the vehicles with weight above 3000 and print their name in uppercase

dic={'car':2500,'bus':7000,'bike':500,'cycle':100,'jeep':3000,'truck':4000}
lst=[i.upper() for i in dic if dic[i]>3000]
print(lst)