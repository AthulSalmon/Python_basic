try:
    n=int(input("Enter the value : "))
    n2=int(input("Enter the value : "))
    r=n/n2
except ZeroDivisionError:
    print("Zero division")
except ValueError:
    print("String cant insert")
else:
    print(f"{r}")
finally:
    print("Hi")