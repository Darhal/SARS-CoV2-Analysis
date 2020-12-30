
import random
import string

from src.utility import *
from src.codon import *
from src.stats import *
from src.levenshtein import *
from src.needleman import *
from src.performance import *

moyenne_args = [ 
    [ [ random.randint(0, 100) for _ in range(0, N) ] ] for N in range(1, 201) 
]

lev_args = [ 
    [ ''.join(random.choices(string.ascii_lowercase + string.digits, k=N)), ''.join(random.choices(string.ascii_lowercase + string.digits, k=N)) ]
    for N in range(0, 101)
]

nw_args = [ 
    [ 
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=N)), 
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=N)),
        [1, -1, -1] 
    ]
    for N in range(0, 50)
]


#################################################################
#--------------------- TEST DE PERFORMANCE ---------------------#
#################################################################

# nw_args = arg_generator(N=500, stride=5, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0, 1], static_args=[[1, -1, -1]])
# average_args = arg_generator(N=1000, stride=5, type=NUMBERS, lower=3000, upper=10000, variant_arg_pos=[0])
# lev_args = arg_generator(N=100, stride=5, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0, 1])

# func_performance(needleman, args_arr=nw_args, sizes=[0], tick_spacing=10)
# func_performance(moyenne, args_arr=average_args, sizes=[0], sort_by=0, tick_spacing=10)
# funcs_performance([ lev_rec, lev_dp, lev ], args_arr=lev_args, sizes=[0])

###################### MOYENNE ######################
average_args = arg_generator(N=100000, stride=150, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0])[1:]
func_performance(moyenne, args_arr=average_args, sizes=[0], tick_spacing=100)


###################### MEDIANE ######################
median_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0])[1:]
func_performance(mediane, args_arr=median_args, sizes=[0], tick_spacing=25)


###################### QUARTILE ######################
perf_graph = []
quart_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=3000, upper=10000, variant_arg_pos=[0], static_args=[1])
perf_graph.append(func_performance(quartile, args_arr=quart_args, sizes=[0], sort_by=0, figure=False))
for arg in quart_args:
    arg[1] = 3 # n de quartile
perf_graph.append(func_performance(quartile, args_arr=quart_args, sizes=[0], sort_by=0, figure=False))
plot_multi_graph(perf_graph, ["quart1", "quart3"], tick_spacing=20)


###################### PROPORTION ######################
prop_args = arg_generator(N=100000, stride=100, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0], static_args=[NUCLEOTIDES])[1:]
func_performance(proportions, args_arr=prop_args, sizes=[0], tick_spacing=25)


###################### VARIANCE ######################
variance_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0])[1:]
func_performance(variance, args_arr=variance_args, sizes=[0], tick_spacing=25)


###################### ECART-TYPE ######################
ecatt_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0])[1:]
func_performance(ecart_type, args_arr=ecatt_args, sizes=[0], tick_spacing=25)


###################### INTERQUARTILE ######################
interquart_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0])[1:]
func_performance(intervalle_interquartile, args_arr=interquart_args, sizes=[0], tick_spacing=25)


###################### CODONS ######################


###################### LEVENSHTEIN ######################


###################### NEEDLEMAN ######################