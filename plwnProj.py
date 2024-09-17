def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def lcm_using_prime_factors(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    lcm = 1
    for factor in set(factors_a + factors_b):
        lcm *= factor ** max(factors_a.count(factor), factors_b.count(factor))
    return lcm

# Example usage:
num1 = 12
num2 = 15
print("LCM of", num1, "and", num2, "is:", lcm_using_prime_factors(num1, num2))
