from random import randint
print(randint(0,9))

from random import randint


def create_A_vector(size): #size
    my_vector=[]
    for i in range(size):
        my_vector.append(randint(0,9))
        
    return my_vector
my_vector_1=create_A_vector(5)

def create_a_matrix(m,n):
    my_matrix=[]
    for i in range(m):
        my_matrix.append(create_A_vector(n))
    return my_matrix
a=create_a_matrix(2,3)

def matrix_multiplication(a,b):
    m=len(a)
    n=len(a[0])
    # n is also rows of the b
    p=len(b[0])
    
    my_matrix=create_a_matrix(m,p)
    
    for i in range(m):
        for j in range(p):
            
            vector_1=a[i]
            vector_2=[i[j] for i in b]
            
            my_matrix[i][j]=vector_inner_product(vector_1,vector_2)
    
    return (my_matrix,m*n*p)

a=create_a_matrix(2,3)
b=create_a_matrix(3,5)
c=matrix_multiplication(a,b)

def vector_inner_product(v1,v2):
    if (len(v1)!=len(v2)):
        print("vektörler aynı boyutta olmalı")
        return
    result=0
    for i in range(len(v1)):
        result=result+v1[i]*v2[i]
    return result
    

my_vector_1=create_A_vector(5)
my_vector_2=create_A_vector(5)
print (my_vector_1,my_vector_2)
vector_product=vector_inner_product(my_vector_1,my_vector_2)
vector_product

#[3, 9, 0, 9, 3] [3, 1, 2, 3, 8]


a_1= create_a_matrix(1,10)
a_2= create_a_matrix(10,1000)
a_3= create_a_matrix(1000,1)
a_4= create_a_matrix(1,5)
a_5= create_a_matrix(5,3)

islem_sayisi=0
r_1=matrix_multiplication(a_2,a_3)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(a_1,r_1[0])
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_4)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_5)
islem_sayisi=islem_sayisi+r_1[1]

print (r_1,"toplam islem sayisi: ",islem_sayisi)

#([[119606926, 90151489, 66944175]], 15) toplam islem sayisi:  10030

a_1= create_a_matrix(1,1000)
a_2= create_a_matrix(1000,1)
a_3= create_a_matrix(1,1)
a_4= create_a_matrix(1,5)
a_5= create_a_matrix(5,3)

islem_sayisi=0
r_1=matrix_multiplication(a_1,a_2)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_3)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_4)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_5)
islem_sayisi=islem_sayisi+r_1[1]

print (r_1,"toplam islem sayisi: ",islem_sayisi)
#([[3782520, 3384360, 4678380]], 15) toplam islem sayisi:  1021

a_1= create_a_matrix(1,10)
a_2= create_a_matrix(10,1000)
a_3= create_a_matrix(1000,1)
a_4= create_a_matrix(1,5)
a_5= create_a_matrix(5,3)

islem_sayisi=0
r_1=matrix_multiplication(a_2,a_3)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_4)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_5)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(a_1,r_1[0])
islem_sayisi=islem_sayisi+r_1[1]

print (r_1,"toplam islem sayisi: ",islem_sayisi)
#([[48692045, 27119620, 65949985]], 30) toplam islem sayisi:  10230
