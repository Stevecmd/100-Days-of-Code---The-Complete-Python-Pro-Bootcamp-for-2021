a = [("Tim", 30), ("Tom", 45), ("Tam", 88)]

def mySorter(a):
    return a[1]

a.sort(key=mySorter, reverse=True)

print(a)