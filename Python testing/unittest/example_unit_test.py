import unittest
from sample import check_even
import sys

'''
-->unittest: A unit test is a test that checks a single component of code, usually 
   modularized as a function, and ensures that it performs as expected
-->Each method name should be start with name 'test'.
-->Each test case is executed in the alphabetical order
-->Syntax to execute tests:
    'python script_path'
    - To see order of execution of test cases
      'python script_path -v'
      
    -->Syntax to execute individual tests:
        'python -m unittest file_name.class_name.method_name'
        example: 'python -m unittest example_unit_test.Testing.test_example'
--> To skip a particular test case we want the use decorator '@unittest.skip('')'
    -Want to skip based on specific condition then:
        '@unitest.skipIf(condition,'msg')'
'''


class Testing(unittest.TestCase):

    # def test_example(self):
    #     a = 12
    #     b = 12
    #     self.assertEqual(a, b)
    #     self.assertNotEqual(a, 13)

    def test_upper(self):
        a = 'TEST'
        b = 'test'
        result = {}
        # self.assertTrue(a.isupper())
        # self.assertFalse(b.isupper())
        self.assertIsInstance(result, dict)

    # Want to skip a specific test case then use decorator
    # @unittest.skip('skipping')
    # @unittest.skip('skipping')
    # def test_isupper(self):
    #     a = 'TEST'
    #     b = 'test'
    #     self.assertTrue(a.isupper())
    #     self.assertFalse(b.isupper())
    #
    # # To raise error from function and the use of assertRaises
    # # Riases error if we sent a integer value to function
    # # self.assertRaises(ValueError, check_even, 8)
    # def test_errors(self):
    #     self.assertRaises(ValueError, check_even,
    #                       '8')  # pass the function paarameter to assertRiases method
    #
    # @unittest.skipIf(sys.version_info[0] < 3,
    #                  'Skipping because of older version of python')
    # def test_sample(self):
    #     a = 'TEST'
    #     b = 'test'
    #     self.assertTrue(a.isupper())
    #     self.assertFalse(b.isupper())
    #
    # @unittest.skipUnless(sys.platform.startswith('Lin'), 'Need Linux platform '
    #                                                      'to execute the test')
    # def test_skip_unless(self):
    #     a = 'TEST'
    #     b = 'test'
    #     self.assertTrue(a.isupper())
    #     self.assertFalse(b.isupper())


if __name__ == '__main__':
    unittest.main()
