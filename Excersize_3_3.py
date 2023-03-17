score = input("Enter Score between 0.0 and 1.0 \n")
try:
    s = float(score)
except:
    print("Enter numeric value")
    quit()
if s > 1.0 :
    print("Error, please enter a score between 0.0 and 1.0")
    quit()
elif s < 0 :
    print("Error, please enter a score between 0.0 and 1.0")
    quit()    
elif s >= .9 :
    print("A")
elif s >= .8 :
    print("B")
elif s >= .7 :
    print("C")
elif s >= .6 :
    print("D")
elif s < .6 :
    print("F")