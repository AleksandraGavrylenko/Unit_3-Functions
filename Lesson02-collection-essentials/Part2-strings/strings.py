announcement = '  BERGEN TECH robotics meeting TODAY!  '
def format_course_code(code):
    code = code.strip().upper() 
    return code
print(format_course_code(announcement))    

def count_hashtags(post):
    hashtag_count = 0
    # for char in post:
    #     if char == '#':
    #         hashtag_count += 1
    words = post.split()
    for word in words:
        if word.startswith('#'):
            hashtag_count += 1
    return hashtag_count
print(count_hashtags('urbueuyeruy #gyuuy #yuyu #yvtycy'))

