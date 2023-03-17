def computepay(a, b) :
    if a <= 40.0 :
        return a * b
    else :
        extrapay = 40.0 * b
        return extrapay + ((a - 40) * (b * 1.5))
try:
    hours = float(input("Enter Number of Worked Hours\n"))
    rate = float(input("Enter The Hourly Rate \n"))
except:
    print("Please Enter a numaric value")
    quit()
print("Pay", computepay(hours, rate))