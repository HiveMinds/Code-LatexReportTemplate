import unittest
import os
from ..src.Main import Main
import testbook

class Test_main(unittest.TestCase):
    
    # Initialize test object
    def __init__(self, *args, **kwargs):
        super(Test_main, self).__init__(*args, **kwargs)
        self.script_dir = self.get_script_dir()
        
        self.main = Main()
        print(f'self.main.addTwo(3)={self.main.addTwo(3)}')
        
    # returns the directory of this script regardles of from which level the code is executed
    def get_script_dir(self):
        return os.path.dirname(__file__)

    # tests unit test on addTwo function of main class 
    def test_addTwo(self):
        expected_result = 7
        result = self.main.addTwo(5)
        self.assertEqual(expected_result,result)

# test jupiter notebook function        
#@testbook.testbook('../src/AE4868_example_notebook_update20201025.ipynb', execute=True)
@testbook.testbook('code/project2/src/AE4868_example_notebook_update20201025.ipynb', execute=True)
def test_addThree(tb):
    func = tb.ref("addThree")

    assert func(2) == 5
    
if __name__ == '__main__':
    unittest.main()