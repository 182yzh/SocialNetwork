import random 
import sys


class Test:
    
    def __init__(self,n,p,r):
        self.p=p
        self.n=n
        self.r=r
        self.graph = []
        #self.degree = []
        self.ruleEdge = set()
        self.normalEdge = set()
     
        for i in range(0,n):
            tem = []
            for j in range(0,n):
                tem.append(0)
                # all Edge to Zeros
                #self.normalEdge.add((i,j))
            for k in range(0,r//2):
                t1 = (i+k+1)%n
                t2 = ((i-k-1)+n)%n
                tem[t1]=1
                tem[t2]=1
                # edge remove and add
                #self.ruleEdge.add((i,t1))
                #self.ruleEdge.add((i,t2))
                #self.normalEdge.remove((i,t1))
                #self.normalEdge.remove((i,t2))
            self.graph.append(tem)
        
        if self.r % 2==1 :
            if self.n%2==1:
                raise Exception("n or r is err")
            q  = self.r+1
            if self.n % q == 0:
                for i in range(0,self.n):
                    if 2*(i%q) < q:
                        t = (i+q//2)%self.n
                        self.graph[i][t] = 1
                        self.graph[t][i] = 1
                        # remove edge 
                        #self.ruleEdge.add((i,t))
                        #self.ruleEdge.add((t,i))
                        #self.normalEdge.remove((i,t))
                        #self.normalEdge.remove((t,i))
            else :
                se = (self.n//q-1)*q
                for i in range(0,se):
                    if 2*(i%q) < q:
                        t = (i+q//2)%self.n
                        self.graph[i][t] = 1
                        self.graph[t][i] = 1
                        #remove edge
                        #self.ruleEdge.add((i,t))
                        #self.ruleEdge.add((t,i))
                        #self.normalEdge.remove((i,t))
                        #self.normalEdge.remove((t,i))
                nq = self.n - se
                if nq % 2 == 1 :
                    raise Exception("Error")
                for i in range (0,nq//2):
                    self.graph[se+i][se+i+nq//2]=1
                    self.graph[se+i+nq//2][se+i]=1
                    # remove edge
                    #self.ruleEdge.add((se+i,se+i+nq//2))
                    #self.ruleEdge.add((se+i+nq//2,se+i))
                    #self.normalEdge.remove((se+i,se+i+nq//2))
                    #self.normalEdge.remove((se+i+nq//2,se+i))
        for i in range(0,n):
            for j in range(i+1,n):
                if self.graph[i][j] ==1 :
                    self.ruleEdge.add((i,j))
                else :
                    self.normalEdge.add((i,j))
        
    def change(self):
        n = self.n
        r = self.r
        p = self.p
        nums = int(n*r/2 * p)
        #print(nums,len(self.ruleEdge))
        #for i in range(0,30):
        arcset1 = random.sample(self.ruleEdge,nums)
        arcset2 = random.sample(self.normalEdge,nums)
        for item in arcset1 :
            self.ruleEdge.remove(item)
            self.normalEdge.add(item)
        
        for item in arcset2 :
            self.ruleEdge.add(item)
            self.normalEdge.remove(item)

    def Judge( self):
        n = self.n
        sumd = []
        numv = []
        degree = []
        for i in range (0,n):
            sumd.append(0)
            degree.append(0)
            numv.append(0)
        
        for x,y in self.ruleEdge:
            #(x,y) = item
            degree[x] += 1
            degree[y] += 1

        for x,y in self.ruleEdge : 
            #(x,y) = item
            sumd[x] += degree[y]
            sumd[y] += degree[x]  
            numv[x] += 1
            numv[y] += 1
        cnt = 0
        for i in range(0,n):
            if numv[i] == 0:
                continue
            if numv[i] ==0 and sumd[i] != 0:
                raise Exception("Error")
            if degree[i] < sumd[i]/numv[i]:
                cnt += 1
            
        return cnt
#        return 0
 
    def Print(self):
        print("n==",self.n,"  p==",self.p,"  r==",self.r)
        for i in range(0,self.n):
            print(self.graph[i])
        print(len(self.ruleEdge),self.ruleEdge,"\n",len(self.normalEdge),self.normalEdge)

def main():
    cnt1 = 0
    cnt2 = 0
    #n  =int(sys.argv[1])
    #r= int(sys.argv[3])
    #p = float(sys.argv[2])
    n  = 100
    r = 5
    p = 0.25
    for i in range(50,1001,50):
        ans = []
        for j in range(0,100):
            t = Test(i,p,r)
            t.change()
            ans.append(t.Judge())
        sum = 0
        for ii in  ans:
            sum += ii
        print(sum/len(ans)/i*100)
    
main()


"""
470 12
391 22
486 36
457 60
452 62
440 62
457 85
418 93
419 109
361 151
350 143
349 170
411 155
378 212
402 194
396 209
384 208
386 213
366 225
350 265
"""
"""
57.66
57.81
58.199999999999996
58.13
58.724
57.85
58.05428571428571
57.955
58.18
58.099999999999994
58.125454545454545
58.20166666666666
58.010769230769235
58.13857142857143
58.08533333333333
58.01124999999999
58.05529411764706
57.96333333333333
58.16526315789474
57.962
"""

"""
56.24
57.379999999999995
58.82000000000001
58.22999999999999
58.18
58.269999999999996
57.98
57.18
"""

"""
58.87
59.540000000000006
59.34
58.98
59.099999999999994
58.70000000000001
58.84
58.989999999999995
59.61
"""

"""
56.26
57.95
57.29
57.9
57.41
57.26
57.49999999999999
57.13

"""

"""

58.4
57.98
58.08
58.065
58.147999999999996
58.13333333333334
58.16571428571429
58.2375
58.02222222222223
58.248
58.18727272727272
58.24
57.900000000000006
57.89714285714286
58.233333333333334
58.045
58.114117647058826
58.075555555555546
58.18
58.090999999999994

"""