# runs a jupyter notebook and converts it to pdf

import os
import shutil
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def export_code_to_latex(project_nr,latex_filename):
        script_dir = get_script_dir()
        relative_dir = f'latex/project{project_nr}/'
        appendix_dir = script_dir+'/../../../'+relative_dir+'/Appendices/'
        path_to_main_latex_file = f'{script_dir}/../../../{relative_dir}/{latex_filename}'
        root_dir = script_dir[0:script_dir.rfind(f'code/project{project_nr}')]
        
        python_files = get_filenames_in_dir('py',script_dir, ['__init__.py'])
        # notebooks = get_notebook_filenames()
        
        #parent_dir = get_parent_dir()
        
        python_files_already_included_in_appendices = get_code_files_already_included_in_appendices('.py', python_files, appendix_dir, project_nr, root_dir)
        # notebook_files_already_included_in_appendices = get_notebook_files_already_included_in_appendices()
       
        
        missing_python_files_in_appendices = get_code_files_not_yet_included_in_appendices('.py', python_files_already_included_in_appendices, python_files)
        # missing_notebook_files_in_appendices = get_missing_notebook_files_in_appendices(notebook_files_already_included_in_appendices)
        
        
        created_appendix_filenames = create_appendices_with_code('.py', missing_python_files_in_appendices, appendix_dir, project_nr)
        # create_appendices_with_notebook_pdfs()
        
        
        main_tex_code, start_index, end_index, appendix_tex_code = get_appendix_tex_code(path_to_main_latex_file)
        print(appendix_tex_code)
        
        appendix_tex_code_with_python_code_appendices = update_appendix_tex_code(appendix_tex_code,created_appendix_filenames, project_nr)
        exit()
        # appendix_tex_code_with_notebook_code_appendices = include_notebook_files_in_appendix_tex_code(appendix_tex_code_with_python_code_appendices)
        # substitute_existing_appendix(appendix_tex_code_with_notebook_code_appendices)
        
        # move_pdf_into_latex_dir(relative_dir,latex_filename)


def get_filenames_in_dir(extension, folder, excluded_files=None):
    '''Returns a list of the relative paths to all files within the code/projectX/src/ folder that match
    the given file extension.'''
    filepaths=[]    
    for r, d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                
                if (not excluded_files is None) and (not file in excluded_files):
                    filepaths.append(r+'/'+file)
                    
    print(f'filepaths={filepaths}')
    return filepaths
    
# def check_if_is_excluded_file(filename,excluded_files):
    # ''' Retruns true if the file is in the excluded file list, returns false otherwise.'''
    # if filename in 

def get_code_files_already_included_in_appendices(extension, absolute_filepaths, appendix_dir, project_nr, root_dir):
    ''' Returns a list of filepaths that are already properly included in some appendix of this projectX,'''
    # TODO: change search string for python and jupyter notebook
    print(f'appendix_dir={appendix_dir}')
    appendix_files = get_filenames_in_dir('.tex', appendix_dir)
    
    contained_codes = []
    for code_filepath in absolute_filepaths:
        for appendix_filepath in appendix_files:
            appendix_filecontent = read_file(appendix_filepath)
            line_nr = check_if_appendix_contains_file(code_filepath, appendix_filecontent, project_nr, root_dir)
            if line_nr>-1:
                # add filepath to list of files that are already in the appendices
                contained_codes.append(Appendix_with_code(code_filepath,
                appendix_filepath,
                appendix_filecontent,
                line_nr, 
                '.py'))
    return contained_codes
    
    
def check_if_appendix_contains_file(filepath,appendix_content, project_nr, root_dir):
    ''' scans an appendix content to determine whether it contains a substring that 
    includes the python code file.'''
    # TODO: write tests
    
    # convert filepath to the inclusion format in latex format
    latex_relative_filepath = f'latex/project{project_nr}/../../{filepath[len(root_dir):]}'
    #latex_command = f'pythonexternal\{{latex_relative_filepath}\}'
    left = "\pythonexternal{"
    right = "}"
    latex_command = f'{left}{latex_relative_filepath}{right}'
    
    # check if the file is in the latex code
    line_nr = 0
    for text in appendix_content:
        if latex_command in text:
            left_of_command = text[:text.rfind(latex_command)]
            
            # check if it is commented
            if '%' in left_of_command:
                commented=True
            else:
                return line_nr
        line_nr=line_nr+1
    return -1
    
   # return true with filename, line_number and line
   # return false
    
    
    
def read_file(filepath):
    ''' Reads content of a file and returns it as a list of strings'''
    with open(filepath) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    #content = [x.strip() for x in content] 
    return content  


def get_code_files_not_yet_included_in_appendices(extension, contained_codes, code_filepaths):
    ''' Returns a list of filepaths that are not yet properly included in some appendix of this projectX,'''
    contained_filepaths = list(map(lambda contained_file: contained_file.filepath, contained_codes))    
    not_contained = []
    for filepath in code_filepaths:
        if not filepath in contained_filepaths:
           not_contained.append(filepath)
    print(f'not_contained={not_contained}')
    return not_contained


def create_appendices_with_code(extension, relative_filepaths, appendix_dir, project_nr):
    ''' Creates the latex appendix files in with relevant codes included.'''
    appendix_filenames = []
    appendix_reference_index = 0
    for relative_filepath in relative_filepaths:
        content = []
        filename = get_filename_from_dir(relative_filepath)
        content = create_section(content,filename, appendix_reference_index)
        if (extension == '.ipynb') and (verify_notebook_pdf_exists(relative_filepath)):
            # write filecontent
            pass # TODO
        else: 
            left = "\pythonexternal{"
            right = "}"
            content.append(f'{left}latex/project{project_nr}/../../code/project{project_nr}/src/{filename}{right}')
        write_appendix_content_to_file(f'{appendix_dir}Auto_generated_App{appendix_reference_index}.tex',content)
        appendix_filenames.append(f'Auto_generated_App{appendix_reference_index}.tex')
        appendix_reference_index = appendix_reference_index+1
    return appendix_filenames
    
def create_section(content,filename, appendix_reference_index):
    # write section
    left ="\section{Appendix "
    middle = filename.replace("_","\_")
    right = "}\label{app:"
    end = "}" # TODO: update appendix reference index
    content.append(f'{left}{middle}{right}{appendix_reference_index}{end}')
    return content
    
    
def write_appendix_content_to_file(appendix_filepath, appendix_content):
    ''' Writes the content of an appendix to a new appendix'''
    with open(appendix_filepath,'w') as f:
        for line in appendix_content:
            f.write(line+'\n')
            

def verify_notebook_pdf_exists(relative_file_path):
    ''' Returns True if a compiled pdf of the listed Jupyter notebook exists
    that can be included in the latex as appendix. Returns False otherwise.'''
    pass


def get_list_of_appendices_with_code(code_format,relative_paths):
    ''' Returns a list of all the appendices that are available that contain code'''
    pass


def get_appendix_tex_code(main_filename):
    ''' gets the latex appendix code from the main tex file.'''
    main_tex_code = read_file(main_filename)
    start =  '\\begin{appendices}' # TODO: scan for % in front
    end = "\end{appendices}" # TODO: scan for % in front
    start_index = get_index_of_substring_in_list(start,main_tex_code)
    end_index = get_index_of_substring_in_list(end,main_tex_code)
    print(f'start_index={start_index}')
    print(f'end_index={end_index}')
    #print(f'main_tex_code[start_index:end_index]={main_tex_code[start_index:end_index]}')
    #print(f'main_tex_code[start_index:end_index]={main_tex_code[start_index:end_index]}')
    
    return main_tex_code,start_index,end_index,main_tex_code[start_index:end_index]

def get_index_of_substring_in_list(substring, lines):
    for i in range(0, len(lines)):
        if i == 167:
            print(f'line = {lines[i]}') 
            print(f'substring={substring}')
            print(substring in lines[i])
        if substring in lines[i]:
            return i
        

def update_appendix_tex_code(appendix_tex_code,created_appendix_filenames, project_nr):
    ''' Includes the appendices as latex commands in the tex code string'''
    return_lines = appendix_tex_code
    for appendix_filename in created_appendix_filenames:
        left = "\input{latex/project"
        middle = "/Appendices/"
        right = "} \newpage"
        return_lines.append(f'{left}{project_nr}{middle}{appendix_filename}{right}')
    print(f'return_lines={return_lines}')
        
def substitute_appendices(original_appendix_latex_code, updated_appendix_latex_code):
    ''' Replaces the old latex code that include the appendices with the new latex 
    commands that include the appendices in the latex report.'''
    pass
    
    
def compile_latex(relative_dir,latex_filename):
    os.system(f'pdflatex {relative_dir}{latex_filename}')
    
def clean_up_after_compilation(latex_filename):
    latex_filename_without_extention = latex_filename[:-4]
    print(f'latex_filename_without_extention={latex_filename_without_extention}')
    delete_file_if_exists(f'{latex_filename_without_extention}.aux')
    delete_file_if_exists(f'{latex_filename_without_extention}.log')
    delete_file_if_exists(f'texput.log')

def move_pdf_into_latex_dir(relative_dir,latex_filename):
    pdf_filename = f'{latex_filename[:-4]}.pdf'
    destination= f'{get_script_dir()}/../../../{relative_dir}{pdf_filename}'
    
    try:
        shutil.move(pdf_filename, destination)
    except:
        print("Error while moving file ", pdf_filename)



def delete_file_if_exists(filename):
    try:
        os.remove(filename)
    except:
        print(f'Error while deleting file: {filename} but that is not too bad because the intention is for it to not be there.')

def get_filename_from_dir(path):
    print(f'path[path.rfind("/"):]={path[path.rfind("/")+1:]}')
    return path[path.rfind("/")+1:]

def get_script_dir():
    ''' returns the directory of this script regardles of from which level the code is executed '''
    return os.path.dirname(__file__)
	

class Appendix_with_code:
    ''' stores in which appendix file and accompanying line number a code file is 
    already included.'''
    def __init__(self, filepath,appendix_path,appendix_content,file_line_nr, extension):
        self.filepath = filepath
        self.appendix_path = appendix_path
        self.appendix_content = appendix_content
        self.file_line_nr = file_line_nr
        self.extension = extension