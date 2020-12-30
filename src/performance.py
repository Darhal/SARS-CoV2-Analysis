
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from src.levenshtein import *
import matplotlib.ticker as ticker
import random
import string

STRINGS = 1
NUMBERS = 1 << 1

def arg_generator(N=10, stride=1, type=STRINGS, variant_arg_pos=[0], static_args=None, samples=string.ascii_lowercase, lower=0, upper=100):
    args = []
    total_nb_args = len(variant_arg_pos)

    if static_args != None:
        total_nb_args += len(static_args)

    for i in range(0, N+1, stride):
        arg = [None for _ in range(0, total_nb_args)]

        for k in variant_arg_pos:
            gen_arg = None
            if type == (STRINGS | NUMBERS):
                gen_arg = ''.join(random.choices(string.ascii_lowercase + string.digits, k=i))
            elif type & STRINGS and samples != None:
                gen_arg = ''.join(random.choices(samples, k=i))
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


def func_performance(func, args_arr, sizes, figure=True, sort_by=0, tick_spacing=1):
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
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        if len(args_arr) > 70:
            plt.xticks(fontsize=9, rotation=90)
        plt.show()
    return performance

def funcs_performance(funcs, args_arr, sizes, figure=True, tick_spacing=1, title="Function Performance Comparison"):
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
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ax.legend()

        if len(args_arr) > 70:
            plt.xticks(fontsize=9, rotation=90)
        plt.show()
    return performance

def plot_multi_graph(graphs, legends, tick_spacing=1, title="Function Performance Comparison"):
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots()
    
    for i in range(len(graphs)):
        ax.plot([ str(t[0]) for t in graphs[i] ], [ t[1] for t in graphs[i] ], label=legends[i])
    
    ax.set_xlabel('Argument (s) Size')                  # Add an x-label to the axes.
    ax.set_ylabel('Time (ms)')                          # Add a y-label to the axes.
    ax.set_title(title)                                 # Add a title to the axes.
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.legend()
    plt.xticks(fontsize=9, rotation=90)
    plt.show()