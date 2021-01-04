
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

CORES = os.cpu_count() if os.cpu_count() <= 2 else os.cpu_count() - 4

def arg_generator(N=10, stride=1, type=STRINGS, variant_arg_pos=[0], static_args=None, samples=string.ascii_lowercase, 
                    lower=0, upper=100, start=0, same_size=True):
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
    start = timer() 
    func(*args)
    end = timer()
    if len(sizes) > 1:
        argument_size = tuple([len(args[i]) for i in sizes])
    else:
        argument_size = len(args[0])
    ms = (end-start) / 1000
    return (argument_size, ms)


def plot_multi_graph(graphs, legends, tick_spacing=1, title="Function Performance Comparison", save=True):
    plt.style.use('seaborn-whitegrid')
    fig, ax = plt.subplots()
    fig.set_size_inches(16, 9)
    
    if isinstance(graphs, list) and isinstance(graphs[0], list):
        for i in range(len(graphs)):
            ax.plot([ str(t[0]) for t in graphs[i] ], [ t[1] for t in graphs[i] ], label=legends[i])
    else:
        ax.plot([ str(t[0]) for t in graphs ], [ t[1] for t in graphs ], label=legends[0])
    
    ax.set_xlabel('Argument (s) Size')                  # Add an x-label to the axes.
    ax.set_ylabel('Time (ms)')                          # Add a y-label to the axes.
    ax.set_title(title)                                 # Add a title to the axes.
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax.legend()
    plt.xticks(fontsize=9, rotation=90)
    if not save:
        plt.show()
    else:
        plt.savefig(f"benchmark_{''.join(legends)}-{title}-{random.randint(0, 99)}.png", bbox_inches='tight', dpi=200)


def func_performance(func, args_arr, sizes, figure=True, sort_by=0, tick_spacing=1, save=True):
    performance = []

    for args in args_arr:
        performance.append(measure_single_call(func, args, sizes))
    
    performance.sort(key=lambda p: p[sort_by])
    
    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance'], tick_spacing=tick_spacing, title=f'{func.__name__} performance', save=save)
    return performance


def funcs_performance(funcs, args_arr, sizes, figure=True, tick_spacing=1, title="Function Performance Comparison", save=True):
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
    performance = []
    mt_pool = Pool(CORES)
    performance = mt_pool.starmap(measure_single_call, [(func, args, sizes) for args in args_arr])
    performance.sort(key=lambda p: p[sort_by])

    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance'], tick_spacing=tick_spacing, title=f'{func.__name__} performance', save=save)
    
    return performance

def funcs_performance_mt(funcs, args_arr, sizes, figure=True, tick_spacing=1, title="Function Performance Comparison", save=True):
    performance = []
    mt_pool = Pool(CORES)
    performance = mt_pool.starmap(func_performance, [(func, args_arr, sizes, False) for func in funcs])

    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance' for func in funcs], tick_spacing=tick_spacing, title=title, save=save)
    
    return performance


def funcs_performance_mt_v2(funcs, args_arr, sizes, figure=True, tick_spacing=1, title="Function Performance Comparison", save=True):
    performance = []

    for func in funcs:
        performance.append(func_performance_mt(func, args_arr, sizes, figure=False))
        print(f"{func.__name__} finished.")

    if figure:
        plot_multi_graph(performance, legends=[f'{func.__name__} performance' for func in funcs], tick_spacing=tick_spacing, title=title, save=save)
    
    return performance