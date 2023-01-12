# 교재 dictionary 예제


# quotes = {
#     "Moe": "A wise guy, huh?",
#     "Larry": "Ow!",
#     "Curly": "Nyuk nyuk!", # key : value
#     }
# stooge = "Curly"
# print(stooge, "says:", quotes[stooge])

subjects = {
    'Eng': 'A+',
    'His': 'A0',
    'Sci': 'B+'
           }
student = 'Jane'
subject = 'Sci'
print(student, "'s", subject, "grade is", subjects[subject], '.')

#old style
print("%s s %s grade is %s ." % (student, subject, subjects[subject]))

#format func
print("{0} s {1} grade is {2}.".format(student, subject, subjects[subject])) # key positioning possibility

#fString
print(f'{student}s {subject} grade is {subjects[subject]}.')
