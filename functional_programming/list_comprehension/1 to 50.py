# 1 to 50 range    1 to 15 - small  16 to 35- medium  above 35 large

lst=[(i,'small') if 0<i<16 else (i,'medium') if 15<i<36 else (i,'large') for i in range(1,51)]
print(lst)