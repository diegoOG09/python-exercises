numbers = [1,2,3,4,5]
result_array = []
total = []
li_1 = []
li_4 = []

def multiplyList(li):
    result = 1
    for x in li:
        result = result * x
    return result

def product(numbers):
    for number in numbers:
        # 1
        for element in numbers:
            if numbers.index(number) == 0:
                if numbers.index(element) > 0:
                    li_1.append(element)

        # 2
            elif numbers.index(number) > 0 and numbers.index(number) < len(numbers)-1:
                nums_izq = []
                nums_der = []
                li_2 = []
                li_3 = []
                nums = []
                if (numbers.index(element)-1) < numbers.index(number):
                    for i in range(0, numbers.index(number)):
                        nums_izq.append(numbers[i]) 
                if (numbers.index(element)+1) > numbers.index(number):
                    for d in range(numbers.index(number)+1, len(numbers)):
                        nums_der.append(numbers[d])
                    nums = nums_izq + nums_der
                    total = multiplyList(nums)
                    result_array.append(total)
        # 3
            elif numbers.index(number) == len(numbers):
                if numbers.index(element) < len(numbers):
                   li_4.append(element) 
                   result_array.append(multiplyList(li_4))

    result_array.append(multiplyList(li_1))

    print(result_array)

product(numbers)
