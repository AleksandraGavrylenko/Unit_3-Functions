#1
def remove_duplicates(list):
    """func that removes duplicates in a list

    Args:
        list (list): list inputed into function
        dupl_list (list): list w/out the duplicates
    """
    dupl_list = []
    for i in list:
        if i in dupl_list:
            continue 
        else:
            dupl_list.append(i)
    return dupl_list
print(remove_duplicates([1,2,2,3,1,4]))
#2
def find_common(list1,list2):
    """finds common items in both lists

    Args:
        list1 (list): inputed list #1
        list2 (list): inputed list #2
    """
    common_list = []
    for i in list1:
        if i in list2:
            common_list.append(i)
    common_list = remove_duplicates(common_list)
    return common_list
print(find_common([1,2,3],[2,3,4]))

#3
def reverse_sublists(data,size):
    """takes a list and revreses each chunk of a particular size

    Args:
        data (list): list to be reversed
        size (int): chunk size
    """
    chunk = []
    reversed_list = []
    for i in data:
        chunk.append(i)
        if len(chunk) == size:
            while chunk:
                last_value = chunk.pop()
                reversed_list.append(last_value)
    if chunk:
        while chunk:
            last_value = chunk.pop()
            reversed_list.append(last_value)
    return reversed_list
print(reverse_sublists([1,2,3,4,5,6],2))
#4
def rotate_list(items, positions):
    """rotate list items by position given

    Args:
        items (list): list to be rotated
        positions (int): how many positions to rotate it by
    """
    rotated_list  = []
    for i in items:
        rotated_list.append(0)
    for i in range(len(items)):
        index = (i+positions) % len(items)
        rotated_list[index] = items[i]
        
    return rotated_list
print(rotate_list([1,2,3,4,5],2))
                