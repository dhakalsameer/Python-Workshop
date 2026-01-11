value = int(input("\nEnter a divisor:"))
try:
    quotient = 100/value
except ZeroDivisionError:
    print("You cannot divide number by 0")
except ValueError:
    print("Please enter a proper divisor")
else:
    print(quotient)
finally:
    print("Processes completed")

def exception(value):
    try:
        quotient = 100/value
    except ZeroDivisionError:
        print("You cannot divide number by 0")
    except ValueError:
        print("Please enter a proper divisor")
    else:
         print(quotient)
    finally:
        print("Processes completed")

   

    