import unittest
import sha256

class sha256_Test_2(unittest.TestCase):

    # Generating hash for a String: Coverage 94%
    def test_generate_hash_String(self):
        hash = sha256.generate_hash("My Hash").hex()
        self.assertEquals(hash, "6b513e9bd247d21c854f25c9f48f42b04eabbaa23e6a586b4d64f024b6e3b0c8")

    # Generating hash for Bytes Input: Coverage 96%
    def test_generate_hash_Bytes(self):
        message = "My Hash"
        hash = sha256.generate_hash(bytes(message, 'utf-8')).hex()
        self.assertEquals(hash, "6b513e9bd247d21c854f25c9f48f42b04eabbaa23e6a586b4d64f024b6e3b0c8")

    # Generating hash for other data types: Coverage 98%
    def test_generate_hash_Other(self):
        with self.assertRaises(TypeError) as _:
            sha256.generate_hash(20).hex()
