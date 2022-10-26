numbers = [10,15,3,7]
results = []

def add_up(k):
    for n in numbers:
        for i in numbers:
            add = n+i
            results.append(add)
    if k in results:
        print(True)
    else:
        print(False)

add_up(18)

