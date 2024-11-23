import random

# Low prime numbers for basic checks
LOW_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
             449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

# Modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# 2. GCD
def gcd(a, b): 
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclid Algorithm using Bezout equation
def egcd(a, b):
    x, last_x = 0, 1
    y, last_y = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x, last_x = last_x - q * x, x
        y, last_y = last_y - q * y, y
    return a, last_x, last_y

# 3. Modular inverse
def mod_inverse(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse exists")
    return x % m

# Primality test using Miller-Rabin
def is_prime(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as d*2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test primality using Miller-Rabin Algothrim for k times
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# 1. Generate a large prime 
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(num):
            return num

# 4. Generate RSA keys
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # e = 65537  # Common public exponent
    # while gcd(e, phi) != 1:
    #     e = random.randint(2, phi - 1)

    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:  
            break


    d = mod_inverse(e, phi)
    return e, d, n

# RSA class
class RSA:
    def __init__(self, keysize=512):
        self.keysize = keysize
        self.p = generate_prime(keysize)
        self.q = generate_prime(keysize)
        self.e, self.d, self.n = generate_keys(self.p, self.q)

    # 5. Encrypt
    def encrypt(self, plaintext): 
        ciphertext = []
        for char in plaintext:
            m = ord(char)
            ciphertext.append(str(mod_exp(m, self.e, self.n)))
        return " ".join(ciphertext)

    # 6. Decrypt
    def decrypt(self, ciphertext):
        plaintext = []
        for part in ciphertext.split():
            c = int(part)
            plaintext.append(chr(mod_exp(c, self.d, self.n)))
        return "".join(plaintext)

# Main program
if __name__ == "__main__":
    print("RSA Encryption/Decryption")
    rsa = RSA(keysize=512)

    msg = input("Enter a message: ")
    encrypted = rsa.encrypt(msg)
    decrypted = rsa.decrypt(encrypted)

    print(f"Public Key (e, n): ({rsa.e}, {rsa.n})")
    print(f"Private Key (d, n): ({rsa.d}, {rsa.n})")
    print(f"Encrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")
