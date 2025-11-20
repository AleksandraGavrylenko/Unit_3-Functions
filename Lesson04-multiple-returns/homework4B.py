#1
print('======================')
database = ['aaa','bbb','ccc','ddd','aaa','john','john','john'] #database
def search_user_database(query):
    result, message, success = 0,'search succesful', True
    if query == '' or query.isspace():
        result, message, success = None,'empty query', False
        return result, message, success     
    for q in query:
        if not q.isalpha():

            result, message, success = None,'invalid query', False     
            return result, message, success     
    if not query in database:
        result = 0
        return result, message, success     
    return database.count(query), f'found {database.count(query)} cases', success
print(search_user_database('3'))
# TEST 1: Empty string → None (no value provided)
result, message, success = search_user_database("")
print(result) # None
print(message) # "No search query"
print(success) # False
print('-')
# TEST 2: Whitespace only → None (no value provided)
result, message, success = search_user_database(" ")
print(result) # None
print(message) # "No search query"
print(success) # False
print('-')
# TEST 3: Has numbers → False (operation failed)
result, message, success = search_user_database("user123")
print(result) # False
print(message) # "Invalid characters"
print(success) # False

print('-')
# TEST 4: Has special chars → False (operation failed)
result, message, success = search_user_database("user@email")
print(result) # False
print(message) # "Invalid characters"
print(success) # False
print('-')
# TEST 5: Valid but no results → 0 (valid count of zero)
result, message, success = search_user_database("admin")
print(result) # 0
print(message) # "No users found"
print(success) # True ← Search worked! Just found nothing
print('-')

# TEST 6: Valid with results → positive int
result, message, success = search_user_database("john")
print(result) # 3 (or any positive number)
print(message) # "Found 3 users"
print(success) # True
print('-')
#2
print('=====================================')
def analyze_book_pages(books):
    if not books:
        return 0,0,0.0,False
    lg_tn_500 = False
    for b in books:
        if not isinstance(b,int):
            books.pop(books.index(b))
    if books == []:
        return 0,0,0.0,False 
    for b in books:
        if b > 500:
            lg_tn_500 = True
    
    return len(books),sum(books), sum(books)/len(books), lg_tn_500
print(analyze_book_pages([]))
print(analyze_book_pages([123,234,345,456,567,678,789,890]))
print(analyze_book_pages([123,234,'bbb']))

print('-')
# TEST 1: Mixed collection with one long book
count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count) # 4
print(total) # 1360
print(avg) # 340.0
print(has_long) # True (because 620 > 500)
print('-')

# TEST 2: No long books
count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(count) # 3
print(total) # 650
print(avg) # 216.67 (approximately)
print(has_long) # False (all books ≤ 500)
print('-')
# TEST 3: Empty list - EDGE CASE!
count, total, avg, has_long = analyze_book_pages([])
print(count) # 0
print(total) # 0
print(avg) # 0.0
print(has_long) # False
print('-')

# TEST 4: Exactly 500 pages - TRICKY!
count, total, avg, has_long = analyze_book_pages([500, 400, 300])
print(has_long) # False (500 is NOT > 500)
print('-')

# TEST 5: Exactly 501 pages
count, total, avg, has_long = analyze_book_pages([501, 400, 300])
print(has_long) # True (501 IS > 500)
print('-')