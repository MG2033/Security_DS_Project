from Crypto.Hash import SHA
from utils import generate_safe_prime, generate_hash
from elgamal import ElGamalDS
import random
from ca import CA

# Global Constants
NBYTES = SHA.digest_size + 1
BYTES_TO_BITS = 8
MAX_ID = 30

# CA Creation
ca = CA(NBYTES)

# Alice and Bob Parameters
q = generate_safe_prime(NBYTES * BYTES_TO_BITS)
a = random.randint(2, q - 1)

# Alice Keys
x_a = random.randint(2, q - 1)
y_a = pow(a, x_a, q)
id_a = random.randint(1, MAX_ID)

# Bob Keys
x_b = random.randint(2, q - 1)
y_b = pow(a, x_b, q)
id_b = random.randint(1, MAX_ID)

# Some other keys
for i in range(MAX_ID):
    if i != id_a and i != id_b:
        x = random.randint(2, q - 1)
        y = pow(a, x, q)

##############################################
# Message to be sent by Alice
M = 23
m = generate_hash(M, SHA)

signature = ElGamalDS.sign(x_a, a, q, m)
if ElGamalDS.verify(y_a, a, m, q, signature):
    print("Signature matches!")
else:
    print("Signature doesn't match!")
