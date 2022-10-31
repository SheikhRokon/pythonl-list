
#   *args এর সুবিদা হল এখানে bar bar pera mitar pass না করে শুধ call করে 
#      args pass kora jai.

def jugful(*adadd):

    sum=0
    for x in adadd:
        sum = sum + x
    print(sum)

jugful(20,1,10)
jugful(20,1,10,22,33,22,33,1,23)       


