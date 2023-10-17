"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError()
    list = []
    prime_index, counter, prime_break = 0, 2, False
    while(prime_index < number_of_primes):
        prime_break = True
        for j in range(2, math.floor(math.sqrt(counter)) + 1):
            if (counter%j == 0):
                prime_break = False
                break
        if(prime_break):
            list.append(counter)
            prime_index+=1
        counter+=1

    return list
