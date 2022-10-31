# lambda funcion দিয়ে করা  


num=[1,2,3,4,5,6]   

x = list(filter(lambda x: x%2==0,num))
print(x)

# user difind function দিয়ে করা ।।

def rokon(x):
    if x%2==0:
        return x   

num=[1,2,3,4,5,6]

x = list(filter(rokon,num))
print(x)