#PROGRAM TO PRINT GRADABLE MARK SHEET OF STUDENT USING elif
sub1=int(input("ENTER THE MARKS IN SUBJECT 1:"))
sub2=int(input("ENTER THE MARKS IN SUBJECT 2:"))
sub3=int(input("ENTER THE MARKS IN SUBJECT 3:"))
sub4=int(input("ENTER THE MARKS IN SUBJECT 4:"))
sub5=int(input("ENTER THE MARKS IN SUBJECT 5:"))
mark = (sub1 + sub2 + sub3 +sub4 + sub5)/5
if mark > 90:
     grade="AA"
elif mark > 80 and mark <=90:
     grade="AB"
elif mark > 70 and mark<=80:
     grade="BB"
elif mark >60 and mark <=70:
     grade="BC"
elif mark >50 and mark <=60:
     grade="CC"
elif mark>40 and mark<=50:
     grade="D"
else:
     grade="NEEDS IMPROVEMENT"
print("AGGREGATE MARKS (OUT OF 100) ",mark," & GRADE OF THE STUDENT IS ",grade)
