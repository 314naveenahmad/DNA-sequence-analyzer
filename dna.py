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
