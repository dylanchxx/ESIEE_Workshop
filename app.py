#x = 150
#y = "Marceille"

z = x + y


#Python is using indents
name = "Anna"
surname = "Logique"

student_name = name + " " + surname

a = 10
b = 5
c = a - b
d = a * b
e = a % b

#a == b 
#a || b
#a === b
#a != b
#a ^^ b 
#a && b

print(student_name)


#TASK

#1. Write IF ELSE Statement to validate if x is larger than y. Return TRUE if YES.

x = 5
y = 4

if x > y:
  print("TRUE")
elif x == y:
  print("equal")
else:
  print("FALSE")


def compare(x , y):
  if y > x:
    return TRUE
  return FALSE

print(compare(200,300))


#2. Write IF ELSE Statement to validate if x is larger than y and less than b. Return TRUE if YES.

def compare2(x , y, b):
  if x > y and x < b :
    return TRUE
  return FALSE


print(compare2(200,300,50))
