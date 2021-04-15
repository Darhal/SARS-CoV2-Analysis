
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from src.levenshtein import *
import matplotlib.ticker as ticker
import random
import string
from multiprocessing import Pool # we will be doing some multiprocessing as some performance tests are painfully slow
import os

STRINGS = 1
NUMBERS = 1 << 1

'''
Number of cores used to execute in parralel the performance tests
'''
CORES = os.cpu_count() if os.cpu_count() <= 3 else os.cpu_count() - 2


def arg_generator(N=10, stride=1, type=STRINGS, variant_arg_pos=[0], static_args=None, samples=string.ascii_lowercase, 
                    lower=0, upper=100, start=0, same_size=True):
    '''
        Generate pseudo-random arguments, can be used for testing or performance measurment.

        Args:
            N: upper bound of the arguments to be generated (inclusif)
            start: start position for the number of arguments generated
            stride: step of the increment
            type: Strings or numbers, strings will generate one random character of length 'i' if same_size is set to True
                other wise the length will be chosen randomly between upper and lower.
                If numbers are chosen, an array of numbers between lower and upper in the incremented order 
            variant_arg_pos: the position of the varying arguments in the function
                E.g: needleman's variant arguments should be [0, 1] position 0 and 1
            static_arg: the invariant (static) arguments in the function
                E.g: needleman's static arguments will be the similarity matrix and the key for example
            samples: The characters that the random string should be generated from
            lower: depends on the type and same_size
            upper: depends on the type and same_size
            same_size: if same_size is set string length will increase otherwise its randomly chosen between lower and upper

        Returns:
            Array of functions arguments 
    '''
    args = []
    total_nb_args = len(variant_arg_pos)

    if static_args != None:
        total_nb_args += len(static_args)

    for i in range(start, N+stride, stride):
        arg = [None for _ in range(0, total_nb_args)]

        for k in variant_arg_pos:
            gen_arg = None
            if type & STRINGS and samples != None:
                size = i
                if not same_size:
                    size = random.randint(lower, upper)
                gen_arg = ''.join(random.choices(samples, k=size))
            elif type & NUMBERS:
                gen_arg = [ random.randint(lower, upper) for _ in range(0, i) ]
            arg[k] = gen_arg

        if static_args != None:
            static_arg_itr = 0
            for j in range(0, total_nb_args):
                if arg[j] == None:
                    arg[j] = static_args[static_arg_itr]
                    static_arg_itr += 1

        args.append(arg)

    return args


def measure_single_call(func, args, sizes):
    '''
        Measures the execution time of 'func' executed on args, and returns (arg_size, seconds)

        Args:
            func: the function to measure its execution
            args: the arguments to be run on 'func'
            sizes: the len of the i'th argument where i is in sizes
        
        Return:
            a tuple containg argment sies and the execution time in seconds
    '''
    start = timer() 
    func(*args)
    end = timer()
    if len(sizes) > 1:
        argument_size = tuple([len(args[i]) for i in sizes])
    else:
        argument_size = len(args[0])
    s = (end-start)
    return (argument_size, s)


def plot_multi_graph(graphs, legends, tick_spacing=1, title="Function Performance Comparison", save=True):
    '''
        Used to polt many or single graph with legends
        
        Args:
            graphcs: array of (x, y) coordinates or multiple arrays of them
            legends: array of legends for the respectives curves in graphs
            title: the graph title
            save: if set to True the file will be saved on disk else will be drawn on a window
        
        Returns:
            None / Void
    '''
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots()
    fig.set_size_inches(16, 9)
    
    if isinstance(graphs, list) and isinstance(graphs[0], list):
        for i in range(len(graphs)):
            ax.plot([ str(t[0]) for t in graphs[i] ], [ t[1] for t in graphs[i] ], label=legends[i])
    else:
        ax.plot([ str(t[0]) for t in graphs ], [ t[1] for t in graphs ], label=legends[0])
    
    ax.set_xlabel('Argument(s) Size')                  # Add an x-label to the axes.
    ax.set_ylabel('Time (in seconds)')                          # Add a y-label to the axes.
    ax.set_title(title)                                 # Add a title to the axes.
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.legend()
    plt.xticks(fontsize=9, rotation=90)
    if not save:
        plt.show()
    else:
        plt.savefig(f"benchmark_{''.join(legends)}-{title}-{random.randint(0, 99)}.png", bbox_inches='tight', dpi=200)


def func_performance(func, args_arr, sizes, figure=True, sort_by=0, tick_spacing=1, save=True):
    '''
        Measure the individual execution time of funcs on arg in args_array and return a plottable tuple array
        
        Args:
            funcs: the functioncs to be measured
            args_arr: the argments array that func will be executed on
            sizes: specify which arguments the function depends on 
            figure: if figure is set True a the result will be plotted
            save: if save is set to True the graph result will be saved on disk
            tick_spacing: the spacing between the x axis labels
            sort_by: 0 sort by argument size, 1 sort by execution time
        
        Returns: 
            Array of tuples of the measured performance
    '''
    performance = []

    for args in args_arr:
        performance.append(measure_single_call(func, args, sizes))
    
    performance.sort(key=lambda p: p[sort_by])
    
    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance'], tick_spacing=tick_spacing, title=f'{func.__name__} performance', save=save)
    return performance


def funcs_performance(funcs, args_arr, sizes, figure=True, tick_spacing=1, title="Function Performance Comparison", save=True):
    '''
        Measure the individual execution time of func on arg in args_array and return an array of plottable tuple array.

        Args:
            funcs: the functions to be measured
            args_arr: the argments array that funcs will be executed on
            sizes: specify which arguments the function depends on 
            figure: if figure is set True a the result will be plotted
            save: if save is set to True the graph result will be saved on disk
            tick_spacing: the spacing between the x axis labels
        
        Returns: 
            Array of tuples of the measured performance
    '''
    performance = [ [] for _ in range(len(funcs))]

    for i in range(len(funcs)):
        for args in args_arr:
            performance[i].append(measure_single_call(funcs[i], args, sizes))
        
        performance[i].sort(key=lambda p: p[0])
    
    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance' for func in funcs], tick_spacing=tick_spacing, title=title, save=save)
    return performance


# Multi-threading solutions

def func_performance_mt(func, args_arr, sizes, figure=True, sort_by=0, tick_spacing=1, save=True):
    '''
        Measure the individual execution time of func on arg in args_array and return a plottable tuple array
        The execution will be done in parallel

        Args:
            func: the functions to be measured
            args_arr: the argments array that func will be executed on
            sizes: specify which arguments the function depends on 
            figure: if figure is set True a the result will be plotted
            save: if save is set to True the graph result will be saved on disk
            tick_spacing: the spacing between the x axis labels
            sort_by: 0 sort by argument size, 1 sort by execution time
        
        Returns: 
            Array of tuples of the measured performance
    '''
    performance = []
    mt_pool = Pool(CORES)
    performance = mt_pool.starmap(measure_single_call, [(func, args, sizes) for args in args_arr])
    performance.sort(key=lambda p: p[sort_by])

    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance'], tick_spacing=tick_spacing, title=f'{func.__name__} performance', save=save)
    
    return performance

def funcs_performance_mt(funcs, args_arr, sizes, figure=True, tick_spacing=1, title="Function Performance Comparison", save=True):
    '''
        Measure the individual execution time of func on arg in args_array and return an array of plottable tuple array.
        The execution of each measurment of the funcs will runn in parrallel

        Args:
            funcs: the functions to be measured
            args_arr: the argments array that funcs will be executed on
            sizes: specify which arguments the function depends on 
            figure: if figure is set True a the result will be plotted
            save: if save is set to True the graph result will be saved on disk
            tick_spacing: the spacing between the x axis labels
            title: the title of the figure

        Returns: 
            Array of tuples of the measured performance
    '''
    performance = []
    mt_pool = Pool(CORES)
    performance = mt_pool.starmap(func_performance, [(func, args_arr, sizes, False) for func in funcs])

    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance' for func in funcs], tick_spacing=tick_spacing, title=title, save=save)
    
    return performance


def funcs_performance_mt_v2(funcs, args_arr, sizes, figure=True, tick_spacing=1, title="Function Performance Comparison", save=True):
    '''
        Measure the individual execution time of func on arg in args_array and return an array of plottable tuple array.
        The execution of functions in single measurement will run on parralel on the args_arr.

        Args:
            funcs: the functions to be measured
            args_arr: the argments array that funcs will be executed on
            sizes: specify which arguments the function depends on 
            figure: if figure is set True a the result will be plotted
            save: if save is set to True the graph result will be saved on disk
            tick_spacing: the spacing between the x axis labels
            title: the title of the figure

        Returns: 
            Array of tuples of the measured performance
    '''
    performance = []

    for func in funcs:
        performance.append(func_performance_mt(func, args_arr, sizes, figure=False))
        # print(f"{func.__name__} finished.")

    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance' for func in funcs], tick_spacing=tick_spacing, title=title, save=save)
    
    return performance