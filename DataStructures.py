#Name: Gil-li Ness Grota

# t = (10, 20, 30)
# print(t[0])
# print(len(t))
# t[0] = 99

#10, 3
#TypeError: 'tuple' object does not support item assignment
#you can't change exist valuse in tuple


#t.count(x): count the time x appears
#t.index(x): return the first index of the value
#a, b, c = t: creating tuple

#tuple are good for time that you want to creat a list that no one can change except you


s = {3, 1, 2, 3, 1}
print(s)
s.add(5)
s.discard(1)
print(s)
print(2 in s)