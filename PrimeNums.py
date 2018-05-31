# A prime number is a number only divisible by 1 and itself.
# You can check if a number is prime easily by taking all of the numbers smaller than the number and dividing the number
# by them to see if there is a remainder.
# Check all numbers less than the number.
# Calculate the first 50 prime numbers and add them to a list.
# This uses two optimizations - it doesn't check even numbers, and doesn't check for factors > 1/2 the size of the number being factored
# This makes the code about 4x faster

# function takes optional boolean to determine whether it will print the output or simply return a list of primes
def primeNums(print_output = False):
    # we know 2 is the first prime number
    primeList = [2]
    # this is where we start our loop - we start our loop at 2 . i is the number we check to see if prime
    i = 1
    # makes sure we only return 50 prime numbers
    while len(primeList) < 50:
        # until the list is 50 primes in length, keep trying to add primes, but skipping even numbers (which can't be prime)
        i +=2
        # initializing (creating / defining) the variable isPrime and making default value to true
        isPrime = True
        # for every number less than i (which starts at 2 but then increments) and greater than 2 but less than half the number, do:
        for x in range(2,(i+1)/2):
            # initialize var called remainder - check if all numbers less than i are evenly divisible (no remainder)
            remainder = i % x
            if remainder == 0:
                # if i is divisible by any number less than it (x), it's not prime and we set isPrime to False
                isPrime = False
                #print str(i) + " divided by" + str(x) + "has remainder " + str(remainder)
                # because its not prime, stop checking other numbers
                break
            #if i % x != 0:
            #break
        # but if the number is prime, append the number (called i) to the list of primes (primeList)
        if isPrime == True:
            primeList.append(i)
    # bookending the function - also making it so you can call the function.
    if print_output == True:
        print primeList
    return primeList