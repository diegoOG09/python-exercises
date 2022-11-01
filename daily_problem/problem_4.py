def generate_new_list(arr):
    return [*range(min(arr),max(arr)+1)]

def first_positive_missing(arr):
    new_list = generate_new_list(arr)
    list_of_posibilities = []

    if arr != new_list:
        for i in new_list:
            if i not in arr and i > 0:
                list_of_posibilities.append(i)
    print(list_of_posibilities)

        
arr = [3,4,-1,1]
# print([*range(min(arr),max(arr)+1)])
print(first_positive_missing(arr))
