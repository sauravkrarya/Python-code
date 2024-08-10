try:
    age =int(input("how old are you: "))
    value=10/age
    print(age)
except ValueError:
    print("your entered value are wrong please input valid value ")
except Exception as e:
    print("somehthing went wrong")
except ZeroDivisionError:
    print("please enter no greater than zero")
finally:
    print("thank you your excecution completed")