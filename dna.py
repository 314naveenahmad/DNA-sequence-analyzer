def validate_sequence(sequence):

    sequence = "".join(sequence.split()).upper()
    #first i remove all the whitespaces and convert to upper case

    valid_bases = {"A", "T", "C", "G"}
    if not sequence:
        raise ValueError("Invalid DNA sequence: sequence is empty")
    #to detect an empty set
    
    if not set(sequence).issubset(valid_bases):
        raise ValueError("Invalid DNA sequence: contains invalid bases")

    return sequence

def sequence_length(sequence):
    return len(sequence)

def nucleotide_count(sequence):
    counts = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0
    }
    for base in sequence:
        counts[base] += 1
    return counts

def gc_content(counts):

    gc_count = counts["G"] + counts["C"]
    total_count = sum(counts.values())
    if total_count == 0:
        return 0.0
    return round((gc_count / total_count) * 100, 2)

def reverse_complement(sequence):
    reversed_sequence = sequence[::-1]
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    return "".join(complement[base] for base in reversed_sequence)
