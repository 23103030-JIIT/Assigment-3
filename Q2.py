def valueSort(mp):
    temp={};
    L=[];
    for key, value in mp.items():
        temp[value]=key;
        L.append(value);
    mp.clear();
    L.sort();
    for data in L:
        mp[temp[data]]=data;
    print(mp)

mp={1: 23, 2: 45.6, 3: -91, 4:-121, 5: 0.091};
print(mp);
valueSort(mp);
