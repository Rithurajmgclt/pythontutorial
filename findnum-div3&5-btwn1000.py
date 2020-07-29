If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
def findSum(input=1000):
	res=1
	for nums in input(1,input+1):
		if nums%5==0 or nums%3==0:
			res=nums*res
			print(res)

findSum()
