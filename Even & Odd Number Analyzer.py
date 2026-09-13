#Even & Odd Number Analyzer

n=int(input("Enter The first Number:"))
m=int(input("Enter the last Number"))

even=[]
odd=[]

for number in range (n,m+1):
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)

print()
print("Result")

print("Even Numbers=",even)
print("Even Number length=",len(even))
print("Odd Numbers=",odd)
print("Odd Number length=",len(odd))

