class fraaction():
    def __init__(self,s,m,ss,mm):
        self.s=s
        self.m=m
        self.ss=ss
        self.mm=mm
    def sum(self):
        res={}
        res['m']=self.m*self.mm
        res['s']=self.s*self.mm+self.ss*self.m
        return res
    def mul(self):
        res={}
        res['s']=self.s*self.ss
        res['m']=self.m*self.mm
        return res
    def div(self):
        res={}
        res['m']=self.m*self.mm
        res['s']=self.s*self.mm-self.ss*self.m
        return res
    def sub(self):
        res={}
        res['s']=self.s*self.mm
        res['m']=self.m*self.ss
        return res
def menu():
    while True:
        print('1:sum')
        print('2:mul')
        print('3:div')
        print('4:sub')
        p=input('select a number:')
        if p=='1' or p=='2' or p=='3' or p=='4':
            p=int(p)
            break
        else:
            print('wrong value')
    return p
try:
    f=float(input('inter s:'))
    d=float(input('enter m:'))
    c=float(input('enter ss:'))
    g=float(input('enter mm:'))
except:
    print('wrong values')
# a=fraaction(4,5,8,3)
b=fraaction(f,d,c,g)
# r=a.sum()
# rr=b.sum()
# print(str(r['s'])+'/'+str(r['m']))
# print(str(rr['s'])+'/'+str(rr['m']))

x=menu()
if x==1:
    rr=b.sum()
elif x==2:
    rr=b.mul()
elif x==3:
    rr=b.div()
elif x==4:
    rr=b.sub()
print(str(rr['s'])+'/'+str(rr['m']))


        