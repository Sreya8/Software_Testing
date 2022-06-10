import unittest
import sha256

class sha256_Test_3(unittest.TestCase):

    def test_Hash(self):
        hash = sha256.Sha256("My Hash")
        print("Hash", hash)
        self.assertNotEqual(hash, TypeError)


    def test_Hash_Not_String(self):
        with self.assertRaises(TypeError) as _:
            sha256.Sha256(20)