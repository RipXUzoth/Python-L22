student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, maths, science']},'id2':{'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 'id3': {'name': ['john'], 'class': ['V'], 'subject_integration': ['english, IT, maths']},'id4':{'name': ['ron'], 'class': ['V'], 'subject_integration': ['english, math, science']}}  
result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)