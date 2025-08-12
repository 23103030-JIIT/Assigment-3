def findCombination(mp, n):
    str=mp[n];
    s=len(str);
    if(s<=2):
        print("Not possible");
    else:
        print(str[0]+str[1]);
        print(str[1]+str[2]);
        print(str[2]+str[0]);

mp={1: "abc", 2: "def", 3:"ghi", 4:"jkl", 5:"mno", 6:"pqr", 7:"stu", 8: "vwx", 9:"yz"};
findCombination(mp, 5);
findCombination(mp, 8);
