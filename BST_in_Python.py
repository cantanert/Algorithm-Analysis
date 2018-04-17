
# coding: utf-8

# In[89]:


def scale(data,factor):
    n=len(data)
    for i in range(n):
        data[i]*=factor
my_list_1=["1","2",3,4,5]
scale(my_list_1,5)
my_list_1


# In[57]:


from random import randint
def create_n_random_numbers_to_be_inserted_tree(size):
    my_vector=[]
    for i in range(size):
        my_vector.append(randint(-500,500))
    print(my_vector)
    return my_vector
def BinaryTree(r=0):
    return [0, [], []]
def insertData(tree_root,data):
    if(tree_root[0]==None):
        tree_root=[0,[],[]]
        return 
    if(tree_root is not None and tree_root!=[]):
        
        if(tree_root[0]>data and tree_root[1]==[]):
            tree_root[1]=[data,[],[]]
        elif(tree_root[0]>data and tree_root[1]!=[]):
            insertData(tree_root[1],data)
        
        elif(tree_root[0]<data and tree_root[2]==[]):
            tree_root[2]=[data,[],[]]
        elif(tree_root[0]<data and tree_root[2]!=[]):
            insertData(tree_root[2],data)  
    else:
        print(" duplicate  .... ")
def prety_print(tree, depth=0):
    ret = ""

    # Print right branch
    if tree[2] != []:
        ret += prety_print(tree[2],depth + 1)

    # Print own value
    ret += "\n" + ("    "*depth) + str(tree[0])

    # Print left branch
    if tree[1] != []:
        ret += prety_print(tree[1],depth + 1)
    
    return ret
def get_minimum_of_the_tree(tree_pass_parameter):
    tree_root=tree_pass_parameter
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[1]==[]):
            return tree_root[0]
        else:
            return get_minimum_of_the_tree(tree_root[1])
def get_maximum_of_the_tree(tree_pass_parameter):
    tree_root=tree_pass_parameter
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[2]==[]):
            #print("şu an max da  : ",tree_root[2])
            return tree_root[0]
        else:
            #print("şu an ilerliyor : ",tree_root[2])
            return get_maximum_of_the_tree(tree_root[2])    
def traverse_the_tree(tree,depth=0):
    global sum_of_the_depth_for_all_nodes
    # sum_of_the_depth_for_all_nodes=0
    tree_root=tree
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[1]==[]):
            pass
            #print(tree_root[0],",",end="")
        else:
            depth=depth+1
            traverse_the_tree(tree_root[1],depth)  
    if (tree_root is not None and tree_root!=[]):
        print(tree_root[0],",",end="")
        sum_of_the_depth_for_all_nodes=sum_of_the_depth_for_all_nodes+depth
        
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[2]==[]):
            pass
            #print(tree_root[0],",",end="")
        else:
            traverse_the_tree(tree_root[2],depth)
    #return sum_of_the_depth_for_all_nodes       
def find_data_on_tree(tree,data,position="0"): 
    tree_root=tree
    #print("tree : ",tree)
    #print("data :",data)
    #print()
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[0]==data):
            print("found on",position)
            print(tree_root[0],",",end="")
            return position
        elif (tree_root[1]!=[] and data<tree_root[0]):
            find_data_on_tree(tree_root[1],data,position+"1")
        elif (tree_root[2]!=[] and data>tree_root[0]):
            find_data_on_tree(tree_root[2],data,position+"2")
            
    else:
        print("not found ")
        return 0


# In[71]:


r=BinaryTree()
agacta_kac_sayi_var=10
my_numbers=create_n_random_numbers_to_be_inserted_tree(agacta_kac_sayi_var)
for i in my_numbers:
    insertData(r,i)
## print(prety_print(r))
max=get_maximum_of_the_tree(r)
min=get_minimum_of_the_tree(r)
max,min
print(prety_print(r))
sum_of_the_depth_for_all_nodes=0  
traverse_the_tree(r)
sum_of_the_depth_for_all_nodes


# In[65]:


r


# In[66]:


find_data_on_tree(r,-38)


# In[67]:


r=None
my_list=[]
r=BinaryTree(0)
my_numbers=create_n_random_numbers_to_be_inserted_tree(15)
for i in my_numbers:
    insertData(r,i)
## print(prety_print(r))
max=get_maximum_of_the_tree(r)
min=get_minimum_of_the_tree(r)

min,max
traverse_the_tree(r)

