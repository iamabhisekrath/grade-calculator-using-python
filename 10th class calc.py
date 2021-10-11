english=int(input("enter your mark of english"))
maths=int(input("enter your mark of math"))
science=int(input("enter your mark of science"))
sst=int(input("enter your mark of sst"))
odia=int(input("enter your mark of odia"))
                              

t=english+maths+science+sst+odia
a=(t/5)
print("total mark",t)
print("percentage",a)
if 35<=a<50:
    print("3rd division")
elif 50<=a<60:
    print("2nd division")
elif 60<=a<100:
    print("1st division")
else:
    print("fail")
