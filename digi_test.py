Digi1 = int(input("Give me any number: "))
Digi2 = int(input("Give me another number: "))
Digi3 = int(input("Give me the last number: "))
if Digi1 > Digi2 and Digi1 > Digi3:
  print ("First is greater than the Second and third")
elif Digi1 < Digi2 and Digi1 < Digi3:
  print ("Second is greater than the First and third is greater then the first")
elif Digi1 < Digi2 and Digi2 > Digi3:
  print ("Second is Highest in the room")
elif Digi1 > Digi2 and Digi1 < Digi3:
  print ("the third is highest in the room")
else:
  print ("What cannot be done does not exist")
