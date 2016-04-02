
def givep(f,l):
    temp=f/l
    if(f%l==0):
        P=temp+1
    else:
        P=temp+2
    return P

def returnx(l,p,n,mat1):
    x=[[0 for row in range(0,int(n))] for col in range(0,int(p))]
    z=int(0)
    lenmat1=len(mat1)
    for row in range(0,p-1):
        value=0
        for col in range(0,n):
            if(value<l):
                if(z<lenmat1):
                    x[row][col]=mat1[z]
                    value=value+1
                    z=z+1
                else:
                    x[row][col]=0
    return x
    
    
def findy(p,n,l,x,mat2):
    sfinal=[]
    h=len(mat2)
    run=n-h
    for z in range(1,run+1):
        mat2.append(0)
    y=[[0 for row in range(0,int(n))] for col in range(0,int(p))]
    temp=[]
    for i in range(0,p):
        for j in range(0,n):
            temp.append(x[i][j])
        sfinal=convol(temp,mat2)
        for j in range(0,n):
            y[i][j]=sfinal[j]
        del sfinal[:]
        del temp[:]
    return y
    

def inputmat(z):
    mat=[]
    for v in range(1,z+1):
        q=int(input('Enter %d element : '%(v)))
        mat.append(q)
    return mat

def check_diff(mat1,mat2):
    x=len(mat1)
    h=len(mat2)
    temp=[]
    if(x>h):
        run=x-h
        for z in range(1,run+1):
            mat2.append(0)
        temp=convol(mat1,mat2)
        return mat1,mat2
    else:
         run=h-x
         for z in range(1,run+1):
            mat1.append(0)
         temp=convol(mat2,mat1)
         return mat2,mat1
         

def convol(large,small):
    lenlarge=len(large)
    templist=[0]*lenlarge
    temp=0
    yn=[]
    #print('Last Element is : %d'%(large[lenlarge-1]))
    #convol=[]
    convol=[[0 for row in range(0,lenlarge)] for col in range(0,lenlarge)]
    for r in range(0,lenlarge):
        if(r>0):
            first=large[0]
            last=large[lenlarge-1]
            for q in range(0,lenlarge):
                if(q>0 & q<lenlarge):
                    templist[q]=large[q-1]
                    convol[r][q]=templist[q]
                else:
                    templist[0]=last
                    convol[r][q]=templist[q]
            for p in range(0,lenlarge):
                large[p]=templist[p]
        else:
            for p in range(0,lenlarge):
                convol[r][p]=large[p]
    yn=matmul(convol,small)
    return yn

def matmul(convol1,small):
    final=[]
    lenlarge=len(convol1)
    for i in range(0,lenlarge):
        total=0
        for j in range(0,lenlarge):
            total2=convol1[j][i]*small[j]
            total=total+total2
        final.append(total)
    return final

def giveans(yn,n,p,l):
    ans=[]
    var=0
    temp=[]
    for i in range(0,p):
        for j in range(0,n):
            if(j<l):
                if not temp:
                    var=yn[i][j]
                    ans.append(var)
                else:
                    var=yn[i][j]
                    var=var+temp[0]
                    ans.append(var)
                    del temp[0]
            else:
                temp.append(yn[i][j])
    a=len(ans)
    del ans[a-1]
    return ans

def printvalue(p,n,mat,var):
    printit=[]
    values=1
    for i in range(0,p):
        print('%s%d : '%(var,values))
        for j in range(0,n):
            printit.append(mat[i][j])
        print(printit)
        del printit[:]
        values+=1
            

def main():
    print('\n'*5)
    mat1=[]
    large=[]
    small=[]
    x=[]
    yn=[]
    ans=[]
    f=int(input('Enter the length of the x(n) matrix : '))
    mat1=inputmat(f)
    m=int(input('Enter the length of the h(n) matrix : '))
    mat2=inputmat(m)
    l=int(input('Enter the value of l : '))
    n=l+m-1
    p=int(givep(f,l))
    print('The value of p is : %d '%(p))
    print('The value of n is : %d '%(n))
    print('\nx(n) : ')
    print(mat1)
    print ('h(n) : ')
    print(mat2)
    x=returnx(l,p,n,mat1)
    print('\nThe Different values of X(inputs) : ')
    variable='X'
    printvalue(p,n,x,variable)
    variable='Y'
    yn=findy(p,n,l,x,mat2)
    print('\nThe Different values of Y(Output) : ')
    printvalue(p,n,yn,variable)
    ans=giveans(yn,n,p,l)
    print('\n****** Final answer of overlap add method ******* : ')
    print(ans)
    


if __name__=="__main__":
    main()
    print('\n**** Programmed By : AFZAL JUNEJA *****')


