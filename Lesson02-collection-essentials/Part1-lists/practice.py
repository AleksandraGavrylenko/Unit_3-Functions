#1
numbers = [1,2,3,4,5,6,7,8,9]
def filter_evens(numbers:list):
    """function that takes out all of the evens in a string

    Args:
        numbers (list): original input
        result (list): result
 
    Returns:
        list: list containing all evens
    """
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result 
print(filter_evens(numbers))

#2
input = [10,20,30,40]
def list_stats(nums):
    """calculate min max avg of a list"""
    if nums:
        return ['min: '+ f'{min(nums)}','max: ' + f'{max(nums)}','avg: ' + f'{(sum(nums))/len(nums)}']
    else:
        return None
print(list_stats(input))