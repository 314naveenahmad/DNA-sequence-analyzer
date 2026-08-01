from dna import validate_sequence, reverse_complement
sequence = input("Enter a DNA sequence: ")
try:
    validated_sequence = validate_sequence(sequence)
    reverse_complement_sequence = reverse_complement(validated_sequence)
    print(f"validated sequence: {validated_sequence}")
    print(f"Reverse complement: {reverse_complement_sequence}")
except ValueError as e:
    print(e)