#1
def combine_values(*nums):
    if not nums:
        return None 
    product = 1
    for num in nums:
        product *= num 
    return product
print(combine_values(2,3,4))

#2
def merge_details(label, **details):
    if not label:
        print('error')
        return None 
    return {'label':label} | details 
print(merge_details(label='ItemA', size='large',cost=12.50))

#3
''' 1) 8; 2)10;  3)0'''

#4
'''1){'name':'Alpha','x':1,'y':2,'count':2}
   2){'name':'Beta','count':0}'''