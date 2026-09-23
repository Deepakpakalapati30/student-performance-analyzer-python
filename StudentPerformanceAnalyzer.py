try:
  Student_name=input("Enter student name:")
  marks=list(map(int,input("enter five marks:").split()))
  total=sum(marks)
  average=total/5
  highestmarks=max(marks)
  print("Student Name:", Student_name)
  print("Total:",total)
  print("Average:",average)
  print("Highest mark:", highestmarks)
  count=0
  for i in marks:
      if i>=40:
          count+=1
  print("Count of greater tha 40marks:",count)
  if average>=90:
      print("Grade A")
  elif average>=75:
      print("Grade B")
  elif average>=60:
      print("Grade C")
  elif average>=40:
      print("Grade D")
  else:
      print("Fail")

except ValueError:
  print("Invalid input")
finally:
  print("finished successfully")