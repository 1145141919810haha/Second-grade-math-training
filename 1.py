import sys
import random
from time import sleep
judge = True
score = 0
while judge:
  a = random.randint(1,100)
  b = random.randint(1,100)
  print(a,"+",b,"=?")
  c = int(input())
  if score >= 50:
    print("Your position: silver")
    sleep(5)
    judge = False
  elif c == a + b: 
    score = score + 5
    print("""You are so good!
score:""",score)
    judge = True
  else:
    print("Are you sure?")
    sleep(3)
    sys.exit()

judge2 = True 
while judge2:
  a = random.randint(1,20)
  b = random.randint(1,20)
  print(a,"x",b,"=?")
  c = int(input())
  if score >= 150:
    print("Your position: gold")
    sleep(5)
    judge2 = False
  elif c == a * b: 
      score = score + 10
      print("""You are so good!
score:""",score)
      judge2 = True
  else:
      print("Are you sure?")
      sleep(3)
      sys.exit()
