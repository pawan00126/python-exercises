# Level 2: Logic & Collections
# Functions are most powerful when they process data like lists or strings.

# The Even Filter: Write a function get_evens that takes a list of numbers and returns a new list containing only the even ones.
def get_evens(nums:list):
    return [x for x in nums if x%2 == 0]


def get_evens_2(nums:list):
    return [x if x%2 == 0 else 'Hii' for x in nums]

list1 = [1,2,3,4,5,6,7,8,8]

print(get_evens(list1))
print(get_evens_2(list1))



# Palindrome Checker: Create a function is_palindrome that takes a string and returns True if it reads the same backward (like "radar") and False otherwise.
# 
# r  a  d  a  r
#   i       j
# 
# 
# 
# 


def is_palindrome(string:str):
    i,j = 0,len(string)-1
    # is_true = True
    if j>=0 and j<2:
        return True
    while i<=j:
        if string[i] == string[j]:
            i+=1
            j-=1
        else:
            return False
        
    return True

print(is_palindrome('rajdar'))

# Find the Max: Write a function find_max that takes a list of numbers and returns the largest one without using the built-in max() function. (Great for practicing loops inside functions!)

def find_max(nums:list):
    if nums :
        nums.sort(reverse=True)
        max = nums[0]

    return f'Max : {max}'

    # x = float('-inf')
    # for i in nums:
    #     if i>x:
    #         x = i
        
    # print('final min : ',x)

print(find_max([1,2,3,4,67,34,2,3,4,54,3,2]))