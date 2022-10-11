import sys

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if len(num1) > len(num2):
	print ("False")
	sys.exit(0)

isSubset = ', '.join(map(str, num1)) in ', '.join(map(str, num2))
if isSubset:
	print("True")
else:
	print("False")
