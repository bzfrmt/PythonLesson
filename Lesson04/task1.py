from sys import argv

def zp(h=0,r=1,b=0):
    return h*r+b

try:
    h=argv[1]
    r=argv[2]
    b=argv[3]
except:
    print("Error. Input 3 paramets")


else:
    print("Cash: ",zp(int(h),int(r),int(b)))



