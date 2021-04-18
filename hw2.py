import numpy as np
import sys
# 第一个人的收益
policy1 = []
# 第二个人收益的转置
policy2 = []

# set1 行
st = []
st1 = []

# single - policy ans
ans = []

def LoadFromFile(filename) :
    f = open(filename)
    line = f.readline()
    l = len(line[:-1].split(","))    
    l //= 2
    for i in range(0,l) :
        policy2.append([])
    
    while line:
        # print(line)
        if len(line) < 3:
            break
        strs = line[:-1].split(',')
        tmp1,tmp2  = [],[]
        for i in range(len(strs)):
            if i%2 == 0 :
                tmp1.append(int(strs[i].strip()))
            else :
                policy2[i//2].append(int(strs[i].strip()))
        policy1.append(tmp1)
       # print(strs)
        line = f.readline()
    f.close()

def GetIndex() :
    tmp = {}
    l = len(policy1)
    for i in range(0,l) :
        tmp = set()
        mx = policy1[i][0]
        for j in range (0,l) :
            if policy1[i][j] > mx :
                tmp = set()
                tmp.add(j)
                mx = policy1[i][j]
            elif mx == policy1[i][j] :
                tmp.add(j)
        st.append(tmp)
    print(st)

    for i in range(0,l) :
        tmp = set()
        mx = policy2[i][0]
        for j in range (0,l) :
            if policy2[i][j] > mx :
                tmp = set()
                tmp.add(j)
                mx = policy2[i][j]
            elif mx == policy2[i][j] :
                tmp.add(j)
        st1.append(tmp)
    print(st1)
# 删除的列
delst1,delst2 =set(),set()

def check(arr,st):
    n = len(arr)
    m = len(arr[0])
    ans = set()
    #print(arr)
    for idx in range(0,n) :# 对 第idx 列
        for i in range(idx+1,n) : # 遍历所有矩阵的策略
            if i == idx :  #同一列不比较
                continue   
            if i in ans : # 已经被删除，如果相对与被删除的不占优，必然存在其他策略更不占优，故可跳过
                continue
            flag = 1      # 默认被删除
            for j in range(0,m):
                if j in st  :
                    continue
                if  arr[idx][j] > arr[i][j]: # 策略i 不占优于策略 idx
                    flag = 0
                    break
            if flag == 1:
                ans.add(idx)
                break
        
    return ans

def deletebadpolicy(arr1,arr2):
    while(1) :
        st1 = check(policy1,delst1)
        st2 = check(policy2,delst2)
        #print(st1,st2)
        if len(st1) == 0 and len(st2) == 0:
            break
        i = 0
        for idx in  st1 :
            delst2.add(idx)
            del arr1[idx-i]
            i += 1
        i = 0
        for idx in st2 :
            delst1.add(idx)
            del arr2[idx-i]
            i += 1
    return     

def GetSingleAns():
    l = len(st)
    for i in range(0,l) :
        for idx in st[i]:
            if i in st1[idx] :
                #print(i,idx)
                ans.append((i,idx))
                
# B policy A 收益相同               
def mixedBPolicy(arr,flag):
    n = len(arr)
    m = len(arr[0])
    b = []
    A = np.array(arr)
    for i in range(0,n-1):
        for j in range(0,m):
            A[i][j] -= A[i+1][j]
    for i in range(0,n):
        A[n-1][i]=1
        b.append([0])
    b[n-1] = [1]
    B = np.array(b)
    #print(A,B)
    ranka =  np.linalg.matrix_rank(A) 
    rankb = np.linalg.matrix_rank( np.hstack((A,B)))
    #print(ranka,rankb)
    if ranka != rankb :
        if flag == 0:
            print("no ans")
            return 0
    if ranka == m :
        if flag ==  1 :
            q = np.linalg.solve(A,B)
            print("one answer: ",q)
        if flag == 0:
            print("only one answer")
            return 1
    else :
        if flag == 0 :
            print("mutil ans")
            return 0
# A policy B 收益相同
def mixedAPolicy(arr,flag):
    n = len(arr)
    m = len(arr[0])
    b = []
    A = np.array(arr)
    for i in range(0,n-1):
        for j in range(0,m):
            A[i][j] -= A[i+1][j]
    for i in range(0,n):
        A[n-1][i]=1
        b.append([0])
    b[n-1] = [1]
    B = np.array(b)
    #print(A,B)
    ranka =  np.linalg.matrix_rank(A) 
    rankb = np.linalg.matrix_rank( np.hstack((A,B)))
    #print(ranka,rankb)
    if ranka != rankb :
        if flag == 0:
            print("no ans")
            return 0
    if ranka == m :
        if flag ==  1 :
            q = np.linalg.solve(A,B)
            print("one answer: ",q)
        if flag == 0 :
            print("one answer")
            return 1
    else :
        if flag == 0 :
            print("mutil ans")
            return 0

def getnewpolicy(arr,st):
    if len(st) == 0:
        return arr
    ans = []
    n = len(arr)
    m = len(arr[0])
    #print(st)
    for i in range(0,n) :
        tmp = []
        for j in range(0,m):
            if j in st :
                continue
            tmp.append(arr[i][j])
        ans.append(tmp)
    return ans

if __name__ == "__main__":
    #print("exe")
    LoadFromFile(sys.argv[1])
    #print(policy1)
    #print(policy2)
    GetIndex()
    GetSingleAns()
    if len(ans) != 0 :
        print("find single policy balance:",ans)
    else :
        deletebadpolicy(policy1,policy2)
        #print(delst1,delst2) 
        arr1 = getnewpolicy(policy1,delst1)
        #print(arr1)
        arr2 = getnewpolicy(policy2,delst2)
        #print(arr2)
        if mixedBPolicy(policy1,0) == 1:
            print("Bpolidcy")
            mixedBPolicy(policy1,1)
        if mixedAPolicy(policy2,0) == 1:
            print("Apolidcy")
            mixedAPolicy(policy2,1)




