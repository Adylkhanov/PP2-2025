import  datetime

x = datetime.datetime.now()

x2 = x.replace(microsecond=0)

print(x2)