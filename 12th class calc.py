english=int(input("enter your mark of english"))
maths=int(input("enter your mark of math"))
physic=int(input("enter your mark of physic"))
chemistry=int(input("enter your mark of chemistry"))
computerorbiology=int(input("enter your mark of computerorbiology"))
physicaleduorart=int(input("enter your mark of physicaleduorart"))
                              

t=english+maths+physic+chemistry+computerorbiology+physicaleduorart
a=(t/6)
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
