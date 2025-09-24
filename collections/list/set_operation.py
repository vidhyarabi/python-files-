# set operations

# union
# intersection
# difference
st1={1,2,3,3,4,5,6}
st2={5,6,7,8,9}
st3=st1.union(st2)
print(st3)
# intersection
st3=st1.intersection(st2)
print(st3)
# difference
st3=st1.difference(st2)
print(st3)
st3=st2.difference(st1)
print(st3)
st3=st2.difference(st2)
print(st3)
st3=st1-st2
print(st3)