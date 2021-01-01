
import random
import string

from numpy.core.defchararray import title

from src.utility import *
from src.codon import *
from src.stats import *
from src.levenshtein import *
from src.needleman import *
from src.performance import *


#################################################################
#--------------------- TEST DE PERFORMANCE ---------------------#
#################################################################

###################### MOYENNE ######################
average_args = arg_generator(N=100000, stride=150, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0], start=1)
func_performance(moyenne, args_arr=average_args, sizes=[0], tick_spacing=100)


###################### MEDIANE ######################
median_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0], start=1)
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
prop_args = arg_generator(N=100000, stride=100, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0], static_args=[NUCLEOTIDES], start=1)
func_performance(proportions, args_arr=prop_args, sizes=[0], tick_spacing=25)


###################### VARIANCE ######################
variance_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0], start=1)
func_performance(variance, args_arr=variance_args, sizes=[0], tick_spacing=25)


###################### ECART-TYPE ######################
ecatt_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0], start=1)
func_performance(ecart_type, args_arr=ecatt_args, sizes=[0], tick_spacing=25)


###################### INTERQUARTILE ######################
interquart_args = arg_generator(N=100000, stride=100, type=NUMBERS, lower=1000, upper=100000, variant_arg_pos=[0], start=1)
func_performance(intervalle_interquartile, args_arr=interquart_args, sizes=[0], tick_spacing=25)


###################### CODONS ######################
codons_args = arg_generator(N=9000, stride=25, type=STRINGS, samples=NUCLEOTIDES)
funcs_performance([ codons, codons_v2, codons_v3 ], args_arr=codons_args, sizes=[0], tick_spacing=10)

###################### LEVENSHTEIN ######################
lev_args = arg_generator(N=200, stride=10, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0, 1])
funcs_performance([ lev_rec, lev_dp, lev ], args_arr=lev_args, sizes=[0], tick_spacing=5)

###################### NEEDLEMAN ######################
nw_args = arg_generator(N=40, stride=5, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0, 1], static_args=[[1, -1, -1]])
funcs_performance([ needleman, needleman_all, nw_bio_generic ], args_arr=nw_args, sizes=[0], tick_spacing=10, 
                title="Performance comparison (Standard needleman)")

nw_args = arg_generator(N=40, stride=5, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0, 1], 
                static_args=[None, [1, -1, -2, -3, -1, 1, -2, -3, -1, -2, 1, -3, -1, -2, -3, 1, -4], NUCLEOTIDES])
funcs_performance([ needleman, needleman_all, nw_bio_generic ], args_arr=nw_args, sizes=[0], tick_spacing=10, 
                title="Performance comparison (Similarity matrix)")