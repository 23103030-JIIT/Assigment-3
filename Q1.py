def invertMap(mp):
    s=len(mp);
    for key in mp:
        mp[mp.pop(key)]=key;
    print(mp)

mp={"one": "Ove", 2: "Circle", 'a': 3};
print(mp)
invertMap(mp)
        
        
