#fib equation
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

#defining the range
nterms = 36
#sum value to add applicable results to
sum = 0
#value to track index
counter = 0

#function that runs the the fib sequence and filters out for the proper terms
for i in range(nterms):
    if recur_fibo(i) % 2 == 0 and recur_fibo(i) < 4000000:
#adds the matching fib sequence values to sum variable
        sum += recur_fibo(i)
#prints sum value when it has all the even values under 4 million
        if sum > 2000000:
            print(f"The sum of all even values below 4 million is {sum}.")

#creates while loop to enumerate index value above 4 million
while recur_fibo(i) > 4000000:
    counter += i
    print(f"The index of the first value above 4 million is {counter}.")
    break
