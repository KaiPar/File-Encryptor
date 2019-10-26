import random

def get_primes(l_limit, u_limit): #get prime numbers between 2 numbers
    prime_list = []
    for i in range(l_limit, u_limit+1):
        for j in range(2, (i+1)//2):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    
    return prime_list

def getGCD(n1, n2): #to get gcd using euclid's algorithm
    while(n1 != 0 and n2 != 0):
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n2
    
    return max(n1, n2)


def gen_key(prine_nos, lenNo):
    if lenNo < 4:
        raise("Cannot generate number less then 4 digits")
    else:
        p1 = random.choice(prine_nos)
        prine_nos.remove(p1)
        p2 = random.choice(prine_nos)    

        t = (p1+p2) * (p1-p2)

        p1 = p1 ** t
        p2 = p2 ** t

        public_key = p1 + p2
        private_key = ((p1+p2) * (p1-p2)) * 16

        return public_key, private_key

def main():
    print(gen_key([29,31,47,67], 5))

if __name__ == "__main__":
    main()

