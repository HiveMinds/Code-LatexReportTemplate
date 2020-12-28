import unittest
import os
from ..src.Main import Main
from ..src.Export_code_to_latex import *
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
	    
        
    def check_if_appendix_contains_file(self):
        filepaths = ['/home/username/Documents/git/Code-LatexReportTemplate/code/project1/src/Main.py']
        root_dir = '/home/username/Documents/git/Code-LatexReportTemplate/'
        appendix_content = ["\section{Appendix Main.py}\label{app:2}","\pythonexternal{latex/project1/../../code/project1/src/Main.py}"]
        project_nr = 1
        result = check_if_appendix_contains_file(filepath, appendix_content, project_nr, root_dir)
        expected_result = 1 #expect the command to be in line number 1.
        self.assertEqual(result,expected_result)
 
 
if __name__ == '__main__':
    unittest.main()