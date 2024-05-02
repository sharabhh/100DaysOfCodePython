# Sets are unique, one value is present only once
# There is no order in sets, items can be anywhere

s = {1,5,6,0,1, "pretty"}
print(s)

# set methods
s1 = {1,2,3,4}
s2 = {4,5,6}
print(s1.union(s2))    #shows all elements without repeatation like AUB in maths
print(s1,s2)

print(s1.intersection(s2))  #shows common elements
print(s1.symmetric_difference(s2))     #shows the non common values
print(s1.isdisjoint(s2))     #shows whether they are disjoint or not
print(s1.issuperset(s2))     #shows whether it is superset or not
s1.update(s2)
print(s1,s2)