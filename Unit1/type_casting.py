# Type Casting in Python
x = 5
y = float(x) #5.0

print("This is an int", x)
print("This is a float", y)

# Number to str
n = 42
print("This variable is now ", n)
print("This variable is now ", type(n))
s = str(n)
print("This variable is now", s)
print("This variable is now", type(s))

# Str to number
s = "3.14"
f = float(s)
s = "42"
i = int(s)

print("This variable is now", f)
print("This variable is now", i)

# With numbers you are now able to do calculations
i = i * 3
f = f + 1.0
print("This variable is now", i)
print("This variable is now", f)