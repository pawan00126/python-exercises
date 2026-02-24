# The Word Frequency Counter:
# Write a function count_words(text) that:

# Takes a string.

# Removes punctuation (optional but better).

# Returns a dictionary where the keys are the words and the values are how many times that word appeared.

# Example Input: "apple banana apple cherry banana apple"
# Example Output: {'apple': 3, 'banana': 2, 'cherry': 1}

def count_words(text:str):
    list1 = text.split()
    # print(list1)
    result = {}

    for item in list1:
        if item in result.keys():
            result[item] = result[item]+1
        else:
            result[item] = 1

    print(result)


count_words("apple banana apple cherry banana apple")



print(list(range(0,10,2)))