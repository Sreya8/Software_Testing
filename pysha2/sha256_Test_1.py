import unittest
import sha256

class sha256_Test_1(unittest.TestCase):
    obj = sha256.new("My Obj")

    def setUp(self):
        self.f = sha256

    def test_update_String(self):
        # Correct Input: Lines Covered 44%
        result = self.obj.update("New String")
        self.assertEquals(result, None)

    def test_update_Empty(self):
        # When empty string is passed: Lines Covered 45%
        result = self.obj.update("")
        self.assertEquals(result, None)

    def test_update_Int(self):
        # When input parameter is not String Lines Covered 47%
        with self.assertRaises(TypeError) as _:
            self.obj.update(5)

    # Copying the objects using deepcopy: Lines Covered 97%
    def test_copy(self):
        copy = self.obj.copy()
        self.assertEquals(copy.hexdigest(), self.obj.hexdigest())







