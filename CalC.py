print("Hello, I'm Your Personal CalC...\nPlease Enter two numbers -->")

x=float(input('X = '))
y=float(input('Y = '))

print("Choose One Operator from Bellow: ")
print("(+) - Addition\n(-) - Subtraction\n(*) - Multiplication\n(/) - Division\n(**) - Exponential\n(%) - Modulus\n(//) - Floor Division")
z=str(input("OPERATOR = "))

print("X = ",x)
print("Y = ",y)

if z=='+':
    print("X + Y = ", x+y)
elif z=='-':
    print("X - Y = ", x-y)
elif z=='*':
    print("X * Y = ", x*y)
elif z=='/':
    print("X / Y = ", x/y)
elif z=='**':
    print("X ** Y = ", x**y)
elif z=='%':
    print("X % Y = ", x%y)
elif z=='//':
    print("X // Y = ", x//y)
else:
    print('Something Went Wrong...\nError\nError\nError')
print('Thanks for using me\nFor more calculations ReRun me (CalC.py)...\nBye :)')


