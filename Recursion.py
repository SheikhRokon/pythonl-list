
# এখানে ফ্যাক্টরিয়াল বের করার প্রোগ্রাম দেখা হয়েছে
# 5= 5*4*3*2*1
# n*(n-1)

def fact(n):
    if n==1:
        return 1

    else:
        return n * fact(n-1)

print(fact(4))

