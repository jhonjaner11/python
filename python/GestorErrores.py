temp=[]
f=open('algo.txt','r')
lista=[y.split(' ') for y in [x.strip('\n') for x in (f.readlines())]]


print lista
