from random import randrange

def createRandomList(n):
    myarray = []
    for i in range(n):
        temp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        random_index = randrange(0,len(foo))
        myarray.append(temp[random_index])
    return myarray

def bubbleSort(alist):
    step = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                step += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return step

def insertionSort(alist):
    step = 0
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            step += 1
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
    return step

newArray = createRandomList(20)
print("Bubble Sort\n-----------")
print("Eski Liste: " , newArray)
step = bubbleSort(newArray)
print("Yeni Liste: " , newArray)
print("Adım Sayısı: " , step, "\n")

newArray = createRandomList(20)
print("Insertion Sort\n--------------")
print("Eski Liste: " , newArray)
step = insertionSort(newArray)
print("Yeni Liste: " , newArray)
print("Adım Sayısı: " , step)
