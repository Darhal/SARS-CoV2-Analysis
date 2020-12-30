
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

nw_args = arg_generator(N=500, stride=5, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0, 1], static_args=[[1, -1, -1]])
average_args = arg_generator(N=1000, stride=5, type=NUMBERS, lower=3000, upper=10000, variant_arg_pos=[0])
lev_args = arg_generator(N=500, stride=5, type=STRINGS, samples=NUCLEOTIDES, variant_arg_pos=[0, 1])

func_performance(needleman, args_arr=nw_args, sizes=[0])
func_performance(moyenne, args_arr=average_args, sizes=[0], sort_by=0)
funcs_performance([ lev_rec, lev_dp, lev ], args_arr=lev_args, sizes=[0])

# func_performance(lev, args_arr=lev_args, sizes=[0], sort_by=1)
# funcs_performance([needleman_all], args_arr=nw_args, sizes=[0])