# runs a jupyter notebook and converts it to pdf

import os
import shutil
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def export_code_to_latex(project_nr,latex_filename)
        script_dir = get_script_dir()
        relative_dir = f'latex/project{project_nr}/'
        parent_dir = get_parent_dir()
        
        python_files = get_filenames_in_src('py')
        # notebooks = get_notebook_filenames()
        
        # python_files_already_included_in_appendices = get_python_files_already_included_in_appendices()
        # notebook_files_already_included_in_appendices = get_notebook_files_already_included_in_appendices()
       
        
        # missing_python_files_in_appendices = get_missing_python_files_in_appendices(python_files_already_included_in_appendices)
        # missing_notebook_files_in_appendices = get_missing_notebook_files_in_appendices(notebook_files_already_included_in_appendices)
         
        # create_appendices_with_python_codes()
        # create_appendices_with_notebook_pdfs()
        
        # appendix_tex_code = get_appendix_tex_code()
        # appendix_tex_code_with_python_code_appendices = include_python_files_in_appendix_tex_code(appendix_tex_code)
        # appendix_tex_code_with_notebook_code_appendices = include_notebook_files_in_appendix_tex_code(appendix_tex_code_with_python_code_appendices)
        # substitute_existing_appendix(appendix_tex_code_with_notebook_code_appendices)
        
        # move_pdf_into_latex_dir(relative_dir,latex_filename)


def get_filenames_in_src(extension='.py', folder=get_script_dir()):
    '''Returns a list of the relative paths to all files within the code/projectX/src/ folder that match
    the given file extension.'''
    "Create a txt file with all the file of a type"
    filepaths=[]
    with open(extension[1:] + "file.txt", "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk(folder):
            for file in f:
                if file.endswith(extension):
                    #filewrite.write(f"{r + file}\n")
                    filepaths.append(file)
    return filepaths
    

    
def get_code_files_already_included_in_appendices(code_format, relative_filepaths):
    ''' Returns a list of filepaths that are already properly included in some appendix of this projectX,'''
    pass


def get_code_files_not_yet_included_in_appendices(code_format, relative_filepaths):
    ''' Returns a list of filepaths that are not yet properly included in some appendix of this projectX,'''
    pass


def create_appendices_with_code(code_format,relative_filepaths):
    ''' Creates the latex appendix files in with relevant codes included.'''
    for relative_file_path in relative_filepaths:
        if verify_notebook_pdf_exists(relative_file_path):
            pass
    pass


def verify_notebook_pdf_exists(relative_file_path):
    ''' Returns True if a compiled pdf of the listed Jupyter notebook exists
    that can be included in the latex as appendix. Returns False otherwise.'''
    pass


def get_list_of_appendices_with_code(code_format,relative_paths):
    ''' Returns a list of all the appendices that are available that contain code'''
    pass


def get_appendix_tex_code(main_filename):
    ''' gets the latex appendix code from the main tex file.'''
    pass


def update_appendix_tex_code(appendices_with_python_code,appendices_with_notebooks):
    ''' Includes the appendices as latex commands in the tex code string'''
    pass
    
    
def substitute_appendices(original_appendix_latex_code, updated_appendix_latex_code):
    ''' Replaces the old latex code that include the appendices with the new latex 
    commands that include the appendices in the latex report.'''
    pass
    
    
def compile_latex(self,relative_dir,latex_filename):
    os.system(f'pdflatex {relative_dir}{latex_filename}')
    
def clean_up_after_compilation(self,latex_filename):
    latex_filename_without_extention = latex_filename[:-4]
    print(f'latex_filename_without_extention={latex_filename_without_extention}')
    delete_file_if_exists(f'{latex_filename_without_extention}.aux')
    delete_file_if_exists(f'{latex_filename_without_extention}.log')
    delete_file_if_exists(f'texput.log')

def move_pdf_into_latex_dir(self,relative_dir,latex_filename):
    pdf_filename = f'{latex_filename[:-4]}.pdf'
    destination= f'{get_script_dir()}/../../../{relative_dir}{pdf_filename}'
    
    try:
        shutil.move(pdf_filename, destination)
    except:
        print("Error while moving file ", pdf_filename)



def delete_file_if_exists(self,filename):
    try:
        os.remove(filename)
    except:
        print(f'Error while deleting file: {filename} but that is not too bad because the intention is for it to not be there.')

def get_script_dir(self):
    ''' returns the directory of this script regardles of from which level the code is executed '''
    return os.path.dirname(__file__)
	
