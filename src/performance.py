
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from src.levenshtein import *

def func_performance(func, args_arr, sizes, figure=True, sort_by=0):
    performance = []

    for args in args_arr:
        start = timer() 
        func(*args)
        end = timer()
        if len(sizes) > 1:
            argument_size = tuple([len(args[i]) for i in sizes])
        else:
            argument_size = len(args[0])
        ms = (end-start) / 1000
        performance.append((argument_size, ms))
    
    performance.sort(key=lambda p: p[sort_by])
    
    if figure:
        plt.style.use('seaborn-whitegrid')
        fig, ax = plt.subplots()
        ax.plot([ str(t[0]) for t in performance ], [ t[1] for t in performance ])
        ax.set_xlabel('Argument (s) Size')                  # Add an x-label to the axes.
        ax.set_ylabel('Time (ms)')                          # Add a y-label to the axes.
        ax.set_title(f"'{func.__name__}' Performance")      # Add a title to the axes.
        if len(args_arr) > 70:
            plt.xticks(fontsize=(9/len(args_arr))*100, rotation=90)
        plt.show()
    return performance

def funcs_performance(funcs, args_arr, sizes, figure=True, title="Function Performance Comparison"):
    performance = [ [] for _ in range(len(funcs))]
    for i in range(len(funcs)):
        for args in args_arr:
            start = timer() 
            funcs[i](*args)
            end = timer()
            if len(sizes) > 1:
                argument_size = tuple([len(args[i]) for i in sizes])
            else:
                argument_size = len(args[0])
            ms = (end-start) / 1000
            performance[i].append((argument_size, ms))
    
        performance[i].sort(key=lambda p: p[0])
    
    if figure:
        plt.style.use('seaborn-whitegrid')
        fig, ax = plt.subplots()

        for i in range(len(funcs)):
            ax.plot([ str(t[0]) for t in performance[i] ], [ t[1] for t in performance[i] ], label=f'{funcs[i].__name__} performance')

        ax.set_xlabel('Argument (s) Size')                  # Add an x-label to the axes.
        ax.set_ylabel('Time (ms)')                          # Add a y-label to the axes.
        ax.set_title(title)                                 # Add a title to the axes.
        ax.legend()
        if len(args_arr) > 70:
            plt.xticks(fontsize=(9/len(args_arr))*100, rotation=90)
        plt.show()
    return performance