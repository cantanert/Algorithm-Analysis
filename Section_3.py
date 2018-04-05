import sys

my_L_1 = []
size_1 = sys.getsizeof(my_L_1)
print("Başlangıç Boyutu: " , size_1, end="")
print()

for i in range(2000):
    my_L_1.append(str(i+1) + ".test")
    if(size_1 != sys.getsizeof(my_L_1)):
        print("dizi yer değiştirdi" , end=" ~~ ")
        size_1 = sys.getsizeof(my_L_1)
        print("size: " , size_1)


#başlangıç boyutu : 64
# dizi yer değiştirdi , size:  96
dizi yer değiştirdi , size:  128
dizi yer değiştirdi , size:  192
dizi yer değiştirdi , size:  264
dizi yer değiştirdi , size:  344
dizi yer değiştirdi , size:  432
dizi yer değiştirdi , size:  528
dizi yer değiştirdi , size:  640
dizi yer değiştirdi , size:  768
dizi yer değiştirdi , size:  912
dizi yer değiştirdi , size:  1072
dizi yer değiştirdi , size:  1248
dizi yer değiştirdi , size:  1448
dizi yer değiştirdi , size:  1672
dizi yer değiştirdi , size:  1928
dizi yer değiştirdi , size:  2216
dizi yer değiştirdi , size:  2536
dizi yer değiştirdi , size:  2896
dizi yer değiştirdi , size:  3304
dizi yer değiştirdi , size:  3760
dizi yer değiştirdi , size:  4272
dizi yer değiştirdi , size:  4848
dizi yer değiştirdi , size:  5496
dizi yer değiştirdi , size:  6232
dizi yer değiştirdi , size:  7056
dizi yer değiştirdi , size:  7984
dizi yer değiştirdi , size:  9024
dizi yer değiştirdi , size:  10200
dizi yer değiştirdi , size:  11520
dizi yer değiştirdi , size:  13008
dizi yer değiştirdi , size:  14680
