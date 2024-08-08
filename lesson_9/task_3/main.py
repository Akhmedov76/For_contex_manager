def outer(num1):
    def inner(num2, num3):
        if (num2 + num3) < num1:
            return (num2 + num3) * num1
        elif (num2 + num3) > num1:
            return (num2 + num3) / num1
        else:
            return num2 + num3


    return inner


a = outer(6)
print(a(3, 4))
