import random
import time

def go():
  print("Launching Coterminal/Reference Angle Calculator")
  print()
  # time.sleep(2)
  print("One Moment...")
  print()
  # time.sleep(2)
  print("Ready!")
  print()
  cot_or_ref = input("Would you like to find an angle's coterminal (cot) angle or reference (ref) angle? ")
  if cot_or_ref == "cot":
      print()
      print("You Chose: COTERMINAL")
      time.sleep(1.5)
      print()
      ask1 = input("What is your initial angle? (0-360 degrees) ")
      ask2 = int(ask1)
      print()
      pos_neg1 = input("Would you like a positive (p) or negative (n) coterminal angle? ")
      if pos_neg1 == "p":
          randomnum = random.randint(1, 10)
          coterminalangle = ask2 + (randomnum * 360) ##RANDOM NUMBER
          coterminalanglestr = str(coterminalangle)
          print()
          print("Your positive coterminal angle is " + coterminalanglestr + " degrees") 
          print("------------------------------")
          # main() #ANSWER; COTERMINAL-POSITIVE
          return True
      elif pos_neg1 == "n":
          randomnum2 = random.randint(1, 10)
          coterminalangle = int(ask2) - (randomnum2 * 360) #RANDOM NUMBER
          coterminalanglestr = str(coterminalangle)
          print()
          print("Your negative coterminal angle is: " + coterminalanglestr + " degrees") 
          print("------------------------------")
          # main() #ANSWER; COTERMINAL-NEGATIVE
          return True
      else:
          print('unknown response')
          return False

  elif (cot_or_ref == "ref"):
      print()
      print("You chose: REFERENCE")
      time.sleep(1.5)
      print()
      ask1 = input("What is your initial angle? (0-360 degrees) ")
      ask2 = int(ask1) 
      print() 
      if (ask1[0] != "-" ): 
          if (ask2 < 90 and ask2 >= 0): #REF ANGLE; Terminal < 90 degrees
              calc = ask1
              print()
              print("Your reference angle is: " + str(calc) + " degrees")
              print("------------------------------")
              # main()
              return True
          elif (ask2 < 180 and ask2 > 80): #REF ANGLE; Terminal < 180 degrees and >
              calc = 180 - ask2
              print()
              print("Your reference angle is: " + str(calc) + " degrees")
              print("------------------------------")
              # main()
              return True
          elif (ask2 > 180 and ask2 < 270): # REF ANGLE; Terminal > 180 and < 270
              calc = ask2 - 180
              print()
              print("Your reference angle is " + str(calc) + " degrees")
              print("------------------------------")
              # main()
          elif (ask2 > 270 and ask2 < 360): # REF ANGLE; Terminal > 270 and < 360
              calc = 360 - ask2
              print()
              print("Your reference angle is " + str(calc) + " degrees")
              print("------------------------------")
              # main()
              return True

          elif (ask2 == 0 or ask2 == 180 or ask2 == 360):
            print("Your reference angle is 0 degrees")
            print("------------------------------")
            # main()
            return True

          elif (ask2 == 90 or ask2 == 270):
            print("Your reference angle is 90 degrees")
            print("------------------------------")
            # main()
            return True


      elif (ask1[0] == "-"): #NEGATIVE ANGLE
          if (ask2 > -90 and ask2 <= 0):
            calc = (ask2 - ask2) - ask2 
            print()
            print("Your reference angle is: " + calc + " degrees")
            print("------------------------------")
            # main()
            return True
          elif (ask2 > -180 and ask2 < -90):
            calc = -180 - ask2
            print()
            print("Your reference angle is: " + str(abs(calc)) + " degrees")
            print("------------------------------")
            # main()
            return True
          elif (ask2 > -270 and ask2 < -180):
            calc = ask2 + 180
            print()
            print("Your reference angle is: " + str(abs(calc)) + " degrees")
            print("------------------------------")
            # main()
            return True
          elif (ask2 > -360 and ask2 < -270):
            calc = ask2 + 270
            print()
            print("Your reference angle is: " + str(abs(calc)) + " degrees")
            print("------------------------------")
            # main()
            return True

          elif (ask2 == 0 or ask2 == -180 or ask2 == -360):
            print("Your reference angle is 0 degrees")
            print("------------------------------")
            # main()
            return True

          elif (ask2 == -90 or ask2 == -270):
            print("Your reference angle is 90 degrees")
            print("------------------------------")
            # main()
            return True


def main():
  
  again = go()
  while again:
    again = go()


if __name__ == '__main__':
  main()
