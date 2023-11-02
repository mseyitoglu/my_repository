student_scores=input().split()
for n in range (0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
highest_score = 0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f"the heighest score is {highest_score}")


           
    
# print(f"the heighest score in the class is{highest_score}")
