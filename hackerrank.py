def func(n,ls):
    lst=[int(x) for x in str(ls)]
    for i in range(1,n+1): 
        lst.append(i)
    lst.sort()
    l=set(lst)
    e=str(l)
    val=""
    for i in range(len(e)): 
        if e[i]!=',':
            if e[i]!='{' :
                 if e[i]!='}':
                      if e[i]!=' ':
                        val+=e[i]
    print(val)
n=int(input())
func(n,1)
     
