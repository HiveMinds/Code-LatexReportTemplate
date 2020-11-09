# Example code that creates plots directly in report
# Code is an implementation of a genetic algorithm
import random
from matplotlib import pyplot as plt
from matplotlib import lines
import matplotlib.pyplot as plt
import numpy as np

from .Compile_latex import Compile_latex
from .Plot_to_tex import Plot_to_tex as plt_tex
from .Run_jupyter_notebooks import Run_jupyter_notebook

# define global variables for genetic algorithm example
string_length = 100
mutation_chance= 1.0/string_length
max_iterations = 1500

class Main:
    
    def __init__(self):
        self.run_jupyter_notebook = Run_jupyter_notebook()
        pass
        
    
    def run_jupyter_notebooks(self,project_nr,notebook_names):
        '''runs a jupyter notebook'''
        notebook_path = f'code/project{project_nr}/src/'
        
        for notebook_name in notebook_names:
            self.run_jupyter_notebook.run_notebook(f'{notebook_path}{notebook_name}')
    
    def convert_notebooks_to_pdf(self,project_nr,notebook_names):
        '''converts a jupyter notebook to pdf'''
        notebook_path = f'code/project{project_nr}/src/'
        
        for notebook_name in notebook_names:
            self.run_jupyter_notebook.convert_notebook_to_pdf(f'{notebook_path}{notebook_name}')
    
    def compile_latex_report(self,project_nr):
        '''compiles latex code to pdf'''
        compile_latex =Compile_latex(project_nr ,'main.tex')
    
    ################################################################
    ############example code to illustrate python-latex  image sync#########
    ##############runs arbitrary genetic algorithm, can be deleted###########
    ################################################################
    def count(self,bits):
        count = 0
        for bit in bits:
            if bit:
                count = count + 1
        return count

    def gen_bit_sequence(self):
        bits = []
        for _ in range(string_length):
            bits.append(True if random.randint(0, 1) == 1 else False)
        return bits

    def mutate_bit_sequence(self,sequence):
        retval = []
        for bit in sequence :
            do_mutation = random.random() <= mutation_chance
            if(do_mutation):
                retval.append(not bit)
            else:
                retval.append(bit)
        return retval

    #execute a run a
    def do_run_a(self):

        seq = self.gen_bit_sequence()
        fitness = self.count(seq)
        results = [fitness]
        for run in range(max_iterations-1):
            new_seq = self.mutate_bit_sequence(seq)
            new_fitness = self.count(new_seq)
            if new_fitness > fitness:
                seq = new_seq
                fitness = new_fitness
            results.append(max(results[-1],fitness))
        return results


    #execute a run c
    def do_run_c(self):
        seq = self.gen_bit_sequence()
        fitness = self.count(seq)
        results = [fitness]
        for run in range(max_iterations):
            new_seq = self.mutate_bit_sequence(seq)
            new_fitness = self.count(new_seq)
            seq = new_seq
            fitness = new_fitness
            results.append(max(results[-1], fitness))
        return results

    def do4b(self,project_nr):
        optimum_found = 0

        # generate plot data
        plotResult = np.zeros((10,max_iterations), dtype=int);
        lineLabels = []

        # perform computation
        for run in range(10):
            res = self.do_run_a()
            if res[-1] == string_length:
                optimum_found +=1

            # store computation data for plotting
            lineLabels.append(f'Run {run}')
            plotResult[run,:]=res;

        # plot multiple lines into report (res is an array of dataseries (representing the lines))
        # plt_tex.plotMultipleLines(plt_tex,x,y,"x-axis label","y-axis label",lineLabels,"filename",legend_position,project_nr)
        plt_tex.plotMultipleLines(plt_tex,range(0, len(res)),plotResult,"[runs]]","fitness [%]",lineLabels,"4b",4,project_nr)
        print("total optimum found: {} out of {} runs".format(optimum_found,10))

    def do4c(self,project_nr):
        optimum_found = 0

        # generate plot data
        plotResult = np.zeros((10,max_iterations+1), dtype=int);
        lineLabels = []

        # perform computation
        for run in range(10):
            res = self.do_run_c()
            if res[-1] == string_length:
                optimum_found +=1

            # Store computation results for plot
            lineLabels.append(f'Run {run}')
            plotResult[run,:]=res;

        # plot multiple lines into report (res is an array of dataseries (representing the lines))
        # plt_tex.plotMultipleLines(plt_tex,x,y,"x-axis label","y-axis label",lineLabels,"filename",legend_position,project_nr)
        plt_tex.plotMultipleLines(plt_tex,range(0, len(res)),plotResult,"[runs]]","fitness [%]",lineLabels,"4c",4,project_nr)
        
        print("total optimum found: {} out of {} runs".format(optimum_found, 10))
        
    def addTwo(self,x):
        ''' adds two to the incoming integer and returns the result of the computation.'''
        return x+2

if __name__ == '__main__':
    # initialize main class
    main = Main()