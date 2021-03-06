import random
import math
import gmpy


class ElGamalDS:
    @staticmethod
    def sign(x, a, q, m):
        """Used to generate a digital signature for a message m using ElGamal Digital Signature Algorithm"""
        # Step 1: Make sure that hash of M satisfies the following condition
        assert 0 <= m <= (q - 1)

        # Step 2: Choose random integer K
        K = random.randint(1, q - 1)
        while math.gcd(K, q - 1) != 1:
            K = random.randint(1, q - 1)

        # Step 3: Calculate S1
        S1 = pow(a, K, q)

        # Step 4: Calculate inverse of K mod q-1
        Kinv = gmpy.invert(K, q - 1)

        # Step 5: Calculate S2
        S2 = (Kinv * (m - x * S1)) % (q - 1)

        return [int(S1), int(S2)]

    @staticmethod
    def verify(y, a, m, q, signature):
        """Used to verify a digital signature for a message m using ElGamal Digital Signature Algorithm"""
        S1, S2 = signature[0], signature[1]
        V1 = pow(a, m, q)
        V2 = (pow(y, S1, q) * pow(S1, S2, q)) % q
        return V1 == V2
