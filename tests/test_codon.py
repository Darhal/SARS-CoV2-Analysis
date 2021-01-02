from Bio import Seq
from src.stats import *
from src.codon import *

# used to generate bunch of random arguments for testing
from src.performance import * 

# Settings for randomly generated arguments tests
# If you want tests to run quickly then you should modify these 
# you can also set EPOCHS to 0 to completely turn them off:
# TOTAL_TESTS_PER_FUNCTION = FUNC_RUNS * EPOCHS
EPOCHS           = 4      # How many times we test iterations we should run per function
CODONS_RUNS      = 1000    # How many arguments we will generate per epoch for codons
CODONSV2_RUNS    = 1000    # How many arguments we will generate per epoch for codons_v2
CODONSV3_RUNS    = 1000    # How many arguments we will generate per epoch for codons_v3

TEST_CASES = [
    "UUUUUCUUAUUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGACGGAUUAUCAUAAUGACUACCACAACGAAUAACAAAAAGAGUAGCAGAAGGGUUGUCGUAGUGGCUGCCGCAGCGGAUGACGAAGAGGGUGGCGGAGGG",
]

TEST_FASTA = [
    "./genome/sequences.fasta"
]


def test_nb_nucl():
    for s in TEST_CASES:
        dict = nombre_elements(s, NUCLEOTIDES)
        seq = Seq.Seq(s)
        assert dict["A"] == seq.count("A")
        assert dict["U"] == seq.count("U")
        assert dict["G"] == seq.count("G")
        assert dict["C"] == seq.count("C")
    
    for f in TEST_FASTA:
        arn = fasta_to_genome(f)
        dict = nombre_elements(arn, NUCLEOTIDES)
        seq = Seq.Seq(arn)
        assert dict["A"] == seq.count("A")
        assert dict["U"] == seq.count("U")
        assert dict["G"] == seq.count("G")
        assert dict["C"] == seq.count("C")


def test_codon_v2():
    for s in TEST_CASES:
        # mul3 = len(s)
        mul3 = (len(s) - len(s)%3)          # This is used to avoid an annoying warning in BioSeq library
        assert codons_v2(s[:mul3]) == str(Seq.Seq(s[:mul3]).translate())
    
    for f in TEST_FASTA:
        arn = fasta_to_genome(f)
        # arn = arn[:(len(arn) - len(arn)%3)]
        arn = arn[:(len(arn) - len(arn)%3)] # This is used to avoid an annoying warning in BioSeq library
        assert codons_v2(arn) == str(Seq.Seq(arn).translate())


def test_codons_v3():
    assert codons_v3('UUUUUCUUAUUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUG') == ''
    assert codons_v3('UUUUUCUUAUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUG') == 'MSSSSYY'
    assert codons_v3('UUUUUCUUAUGUCUUCCUCAUCGUAUUACUAAUAUGUGUUGCUGAUAG') == 'MSSSSYY' + 'MCC'


def test_codons_v3_bio_seq():
    for s in TEST_CASES:
        cds = start_to_stop(s)
        amino_acids = ''.join([ str(Seq.Seq(c).translate(to_stop=True)) for c in cds ])
        assert codons_v3(s) == amino_acids

    for f in TEST_FASTA:
        arn = fasta_to_genome(f)
        cds = start_to_stop(arn)
        amino_acids = ''.join([ str(Seq.Seq(c).translate(to_stop=True)) for c in cds ])
        assert codons_v3(arn) == amino_acids


def test_codons():
    assert codons('UUUUUCUUAUUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUG') == []
    assert codons('UUUUUCUUAUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUG') == ['MSSSSYY']
    assert codons('UUUUUCUUAUGUCUUCCUCAUCGUAUUACUAAUAUGUGUUGCUGAUAG') == ['MSSSSYY','MCC']
    assert codons('UUUUUCUUAUUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGACGGAUUAUCAUAAUGACUACCACAACGAAUAACAAAAAGAGUAGCAGAAGGGUUGUCGUAGUGGCUGCCGCAGCGGAUGACGAAGAGGGUGGCGGAGGG') == [codons_v2('AUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGACGGAUUAUCAUAAUGACUACCACAACGAA')]


def test_codons_bio_seq():
    for s in TEST_CASES:
        cds = start_to_stop(s)
        amino_acids = [ str(Seq.Seq(c).translate(to_stop=True)) for c in cds ]
        assert codons(s) == amino_acids

    for f in TEST_FASTA:
        arn = fasta_to_genome(f)
        cds = start_to_stop(arn)
        amino_acids = [ str(Seq.Seq(c).translate(to_stop=True)) for c in cds ]
        assert codons(arn) == amino_acids


def test_transcription():
    for s in TEST_CASES:
        assert transcription_complementaire(s) == str(Seq.Seq(s).transcribe())
    
    for f in TEST_FASTA:
        arn = fasta_to_genome(f)
        assert transcription_complementaire(arn) == str(Seq.Seq(arn).transcribe())


def test_start_to_stop():
    assert start_to_stop('SDFAUGUAG') == ['AUG']
    assert start_to_stop('SDFAUGUAA') == ['AUG']
    assert start_to_stop('SDFAUGUAR') == ['AUG']
    assert start_to_stop('SDFAUGFRGUAG') == ['AUGFRG']
    assert start_to_stop('SDFAUGGHYUAA') == ['AUGGHY']
    assert start_to_stop('SDFAUGLOLUAR') == ['AUGLOL']
    assert start_to_stop('AUGUAG') == ['AUG']
    assert start_to_stop('AUGUAA') == ['AUG']
    assert start_to_stop('AUGUAR') == ['AUG']
    assert start_to_stop('SDFAUGUAGAUG') == ['AUG']
    assert start_to_stop('SDFAUGUAAAUG') == ['AUG']
    assert start_to_stop('SDFAUGUARAUG') == ['AUG']
    assert start_to_stop('SDFAUGUAGGHFYTAUGJHGFHGFHFUAA') == ['AUG', 'AUGJHGFHGFHF']
    assert start_to_stop('SDFAUGUAAHGHJFHGFKAUGJHKUAR') == ['AUG', 'AUGJHK']
    assert start_to_stop('SDFAUGUARHGFRRDDAUGKUUHJBUAR') == ['AUG', 'AUGKUUHJB']
    assert start_to_stop('UAG') == []
    assert start_to_stop('UAGGFDAUG') == []
    assert start_to_stop('AUGGDHDTHAUGDJHUAR') == ['AUGGDHDTHAUGDJH']
    assert start_to_stop('UUUUUCUUAUGUCUUCCUCAUCGUAUUACUAAUAUGUGUUGCUGAUAG') == ['AUGUCUUCCUCAUCGUAUUAC', 'AUGUGUUGC']
    assert start_to_stop('UUUUUCUUAUUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGACGGAUUAUCAUAAUGACUACCACAACGAAUAACAAAAAGAGUAGCAGAAGGGUUGUCGUAGUGGCUGCCGCAGCGGAUGACGAAGAGGGUGGCGGAGGG') == ['AUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGACGGAUUAUCAUAAUGACUACCACAACGAA']

############################################################
###################  THE ULTIMATE TEST!  ###################
# we will test wide variety of codons functions and compare
# them to BioPython
############################################################

def test_codons_gen():
    for _ in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        args = arg_generator(N=CODONS_RUNS, stride=1, type=STRINGS, samples=NUCLEOTIDES, start=1,
                    same_size=False, lower=CODONS_RUNS/2, upper=CODONS_RUNS)
        for arg in args:
            cds = start_to_stop(arg[0])
            amino_acids = [ str(Seq.Seq(c).translate(to_stop=True)) for c in cds ]
            assert codons(arg[0]) == amino_acids

def test_codonsv2_gen():
    for _ in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        args = arg_generator(N=CODONSV3_RUNS, stride=1, type=STRINGS, samples=NUCLEOTIDES, start=1,
                    same_size=False, lower=CODONSV3_RUNS/2, upper=CODONSV3_RUNS)
        for arg in args:
            #------------------ Test ------------------
            s = arg[0]
            mul3 = (len(s) - len(s)%3) # This is used to avoid an annoying warning in BioSeq library
            assert codons_v2(s[:mul3]) == str(Seq.Seq(s[:mul3]).translate())

def test_codonsv3_gen():
    for _ in range(0, EPOCHS) :
        #----------- Generating random arguments -----------
        args = arg_generator(N=CODONSV2_RUNS, stride=1, type=STRINGS, samples=NUCLEOTIDES, start=1,
                    same_size=False, lower=CODONSV2_RUNS/2, upper=CODONSV2_RUNS)
        for arg in args:
            cds = start_to_stop(arg[0])
            amino_acids = ''.join([ str(Seq.Seq(c).translate(to_stop=True)) for c in cds ])
            assert codons_v3(arg[0]) == amino_acids