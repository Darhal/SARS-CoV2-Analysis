from Bio import SeqIO


def bank_sequences(n):
    S = fasta_to_genome("./genome/20000_sequences.fasta")
    echantillon = []
    k = 0
    if not S:
        print(k)
        return echantillon

    for i in S:
        test = False
        if k == n:
            break

        for j in 'RYSWKMBDHVN':
            if j in i:
                test = True
                break
        if test:
            continue
        else:
            echantillon.append(i)
            k += 1

    return echantillon


def bank_sequences_rec(n):
    def recursion(S, echantillon, k):
        if k == n:
            return echantillon

        elif not S:
            print(k)
            return echantillon

        else:
            for i in 'RYSWKMBDHVN':
                if i in S[0]:
                    return recursion(S[1:], echantillon, k)
            return recursion(S[1:], echantillon+[S[0]], k+1)

    return recursion(fasta_to_genome("./genome/20000_sequences.fasta"), [], 0)


def transcription_complementaire(ADNc):
    '''Function qui remplace la séquence de ADNc (ADN complémentaire) en ARNm
    
    Args:
        ADN : La séquence d'ADN complémentaire du génome à retranscrire en ARNm

    Returns:
        ARNm : La séquence d'ARNm issue de la séquence d'ADNc entrée.
    '''
    d_transcription = []
    
    for base in ADNc:
        if base == "T" :
            d_transcription.append("U")
        else:
            d_transcription.append(base)

    ARNm = ''.join(d_transcription)
        
    return ARNm


def fasta_to_genome(filename):
    '''Function that parse a fasta file
    
    Args:
        filename: the fasta file that contain the genomic data

    Returns:
        The first sequence if the file contains only one, a table of sequences otherwise
    '''
    genome = []

    for seq_record in SeqIO.parse(filename, "fasta"):
        genome.append(transcription_complementaire(seq_record.seq))

    if len(genome) == 1:
        return genome[0]
    return genome


def total_elements(sequence):
    '''Nombre total d'éléments dans une sequence (ARN, ADN ou Acides aminés)

    Args:
        sequence: the RNA/DNA/amino-acid sequence

    Returns:
        Length of the RNA sequence
    '''
    return len(sequence)


def taille_ensemble(L): # liste de la taille de chaque séquence d'une liste de séquence
    ''' On aura un échantillon de séquence, la fonction permet de donner la taille de chaque séquence dans une liste

    Args :
        L : liste de séquences

    Returns :
        liste de la taille de chaque séquence de l'échantillon
    '''
    l = []

    for k in L:
        l.append(len(k))
    return l


def nombre_elements(sequence, sampler):
    '''Retourne un dictionnaire indiquant le nombre de chaque element de la sequence

    Args:
        sequence: the RNA/DNA/amino-acid sequence
    
    Returns:
        Dictionary that contains the number of elements as value and the element as key
    '''
    d = {s: 0 for s in sampler}

    for i in sequence:
        if i in sampler:
            d[i] += 1

    return d


def nombre_element_echantillon(tab, sampler):
    '''Retourne un dictionnaire indiquant le nombre de chaque element dans l'echantillon

       Args:
           sequence: the RNA/DNA/amino-acid sequence

       Returns:
           Dictionary that contains the number of elements (a list) as value and the element as key
    '''
    d = {}

    for seq in tab:
        nbr = nombre_elements(seq, sampler)
        l = list(nbr.keys())

        for element in l:
            if element not in d:
                d[element] = [nbr[element]]
            else:
                d[element].append(nbr[element])

    return (d)