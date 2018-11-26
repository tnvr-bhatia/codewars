# def remove_smallest(numbers):
#     if not numbers:
#         return []
#     else:
#         ## Generates a Shallow Copy of the List
#         k = numbers.copy()
#         ## remove the first minimum element from the list
#         k.remove(min(k))
#         return k

## Effective Solution

def remove_smallest(numbers):
    if len(numbers) < 1: 
        return numbers
    idx = numbers.index(min(numbers))
    ## Slicing removes the need for Shallow Copy of the List
    return numbers[0:idx] + numbers[idx+1:]