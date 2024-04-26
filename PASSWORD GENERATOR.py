import random
print("PASSWORD GENERATOR IN PYTHON")
length = int(input("Enter length of the password: "))
Lower = "abcdefghijklmnopqrstuvwxyz"
Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "0123456789"
Symbols = "@#^&$%*()!/."
string = Lower+Upper+Numbers+Symbols
password = "".join(random.sample (string, length))
print("New password is:", password)
