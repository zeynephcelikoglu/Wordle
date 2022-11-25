import sys

woD = sys.argv[1]
woD = woD.upper()

if (len(woD) < 5) or (len(woD) > 5):
     print("The length of WoD must be five!")
     sys.exit()

else:
 for m in range(6):
     idea = str(input("Enter your guess: "))
     for x in range(1,6):
      idea = idea.upper()
     print(f"Try{m+1} ({idea}): ", end="")
     if (len(idea) < 5) or (len(idea) > 5):
         print("The length of idea must be five!")

     else:
         if woD == idea:
             list = ["st", "nd", "rd", "th", "th", "th"]
             for j in range(1,7):
              print(f"Congratulations! You guess right in {m+1}{list[j+1]} shot!")
              sys.exit()

         else:
             print(" ")
         for i in range(5):
              if idea[i] in woD:
                  if woD[i] == idea[i]:
                     print(f"{i+1}. letter exists and located in right position.")
                  else:
                    print(f"{i+1}. letter exists but located in wrong position.")
              else:
               print(f"{i+1}. letter does not exist")

print("You are failed!")
