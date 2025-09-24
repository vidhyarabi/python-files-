f=open('C:/Users/vidhy/OneDrive/Documents/movies.csv','r')
dic={}
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    rate=data[3]


# 1.release year above 2000 name,year,rating
#     if year>'2000':
#         print(data[1:4])

# 2. Release year 1975 to 2000 name,year,rating

    # if '1975'<year<'2000':
    #     print(data[1:4])

# 3. Each year release movie count

#     if year not in dic:
#         dic[year]=1
#     else:
#         dic[year]+=1
# for k,v in dic.items():
#     print(k,':',v)


# 4. rating above 4 name , year , rating

    if rate>'4':
        print(data[1:4])

# 5. year above 2005 and rating above 4 name , year, rating

    # if year>'2005' and rate>'4':
    #     print(data[1:4])