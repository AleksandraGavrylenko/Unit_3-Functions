#1 
#avg grade, highest grade, lowest grade, pass/fail status
def analyze_grades(grades):
    if not grades:
        return 0,0,0,False 
    for g in grades:
        if not isinstance(g, int):
            return False
    avg = sum(grades)/len(grades)
    max_grade = max(grades)
    min_grade= min(grades)
    pass_fail = True if avg >= 60 else False 
    return avg, max_grade, min_grade, pass_fail
print(analyze_grades([95,92,78,90]))
print(analyze_grades([]))
print(analyze_grades(['90']))