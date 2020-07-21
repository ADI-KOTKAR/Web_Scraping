lst = [1,2,3,4,5]
n=3
def divide_chunks(l, n):   
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n]

x = list(divide_chunks(lst,n))
print(x)

