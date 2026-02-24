# Level 3: Advanced Concepts
# This is where you handle "edge cases" and more complex Python features.

# 1. The Keyword Dictionary: Write a function describe_pet that takes two arguments: animal_type and pet_name. Give animal_type a default value of "dog".
def describe_pet(animal_type, pet_name = 'dog'):
    return f'Animal Type : {animal_type}, Pet Name : {pet_name}'

print(describe_pet('MKC'))



# 2. The Calculator (Multiple Returns): Write a function basic_stats that takes a list of numbers and returns both the sum and the average of those numbers.
def basic_stats(nums:list):
    return sum(nums), round((sum(nums)/len(nums)), 3)

print(basic_stats([1,2,3,5,6]))

# 3. The "Args" Summer: Write a function sum_all that can take any number of arguments (using *args) and returns their total sum.
def sum_all(*nums):
    return sum(nums)


print(sum_all(1,2,3,4,5,6,7,8,9,10))