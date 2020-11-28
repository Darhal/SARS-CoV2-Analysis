from Bio import Seq
from src.stats import *

TEST_CASES = [
    "UUUUUCUUAUUGUCUUCCUCAUCGUAUUACUAAUAGUGUUGCUGAUGGCUUCUCCUACUGCCUCCCCCACCGCAUCACCAACAGCGUCGCCGACGGAUUAUCAUAAUGACUACCACAACGAAUAACAAAAAGAGUAGCAGAAGGGUUGUCGUAGUGGCUGCCGCAGCGGAUGACGAAGAGGGUGGCGGAGGG",
]

TEST_FASTA = [
    "./genome/sequences.fasta"
]

def test_codon():
    for s in TEST_CASES:
        mul3 = (len(s) - len(s)%3)
        assert codons(s[:mul3]) == str(Seq.Seq(s[:mul3]).translate())
    
    for f in TEST_FASTA:
        arn = fasta_to_genome(f)
        arn = arn[:(len(arn) - len(arn)%3)]
        assert codons(arn) == str(Seq.Seq(arn).translate()) 


def test_transcription():
    for s in TEST_CASES:
        assert transcription_complementaire(s) == str(Seq.Seq(s).transcribe())
    
    for f in TEST_FASTA:
        arn = fasta_to_genome(f)
        assert transcription_complementaire(arn) == str(Seq.Seq(arn).transcribe()) 

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
