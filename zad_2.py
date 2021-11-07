def multiply_numbers_a(numbers_list):
    multiplied_list = list()
    for number in numbers_list:
        multiplied_list.append(number*5)
    return multiplied_list

def multiply_numbers_b(numbers_list):
    return [number*5 for number in numbers_list] 


numbers_list = [2,4,5,7,6]

print(multiply_numbers_a(numbers_list))
print(multiply_numbers_b(numbers_list))
