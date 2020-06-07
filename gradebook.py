# Gradebook
print('*****************')
print('*** GRADEBOOK ***')
print('*****************')
score = input('Enter your score as a percent: ')
try:
    grade = float(score)
except:
    print('Your score must be a float data type.')
    quit()
def computegrade(score):
    if grade >= 94.0 and grade <= 100.0:
        score = 'A'
    elif grade >= 90.0 and grade < 94.0:
        score = 'A-'
    elif grade >= 87.0 and grade < 90.0:
        score = 'B+'
    elif grade >= 84.0 and grade < 87.0:
        score = 'B'
    elif grade >= 80.0 and grade < 84.0:
        score = 'B-'
    elif grade >= 77.0 and grade < 80.0:
        score = 'C+'
    elif grade >= 74.0 and grade < 77.0:
        score = 'C'
    elif grade >= 70.0 and grade < 74.0:
        score = 'C-'
    elif grade >= 67.0 and grade < 70.0:
        score = 'D+'
    elif grade >= 64.0 and grade < 67.0:
        score = 'D'
    elif grade >= 61.0 and grade < 64.0:
        score = 'D-'
    elif grade >= 0.0 and grade < 61.0:
        score = 'F'
    else:
        score = 'out of range'
    return score
print('Your score is',score,'% and your grade is', computegrade(score),'.')
