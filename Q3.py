def findNGreatest(L, n):
    s=len(L);
    if(s<n):
        print("Not possible");
    L.sort();
    l=L[::-1];
    for i in range(n):
        print(l[i])

L=[45, 67, 988.3, -123, -.092];
findNGreatest(L, 3);
        
    
    
    
    
