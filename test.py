kor = [1, 2, 3, 4, 5]
math = [1, 2, 3, 4, 5]
eng = [1, 2, 3, 4, 5]
mid = [kor, math, eng]

student = [0] * 5

for subject in mid:
    i = 0
    for score in subject:
        student[i] += score/3
        i += 1

print(student)
