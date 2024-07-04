import unittest


class TestPackage(unittest.TestCase):
    def test_package(self):
        import package

        self.assertEqual(package.__version__, '0.1.0')


if __name__ == '__main__':
    unittest.main()
