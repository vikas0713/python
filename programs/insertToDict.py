#program to insert in a dictionary


a={}
a.setdefault('key','value')
a.setdefault('key1','value1')
a.setdefault('key2',[]).append('value2_1') #appending as a list
a.setdefault('key2',[]).append('value2_2')
a.setdefault('key2',[]).append('value2_3')
a.setdefault('key3','value3')

print a