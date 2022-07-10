from sys import exit

n = input("Enter a number: ")
myDict = {}

try:
    n = int(n)
except Exception:
    print("Please enter a number!")
    exit()

for i in range(n + 1):
    myDict[i] = i*i

print(myDict)