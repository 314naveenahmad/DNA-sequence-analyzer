from dna import validate_sequence, dna_to_rna_transcription
sequence = input("Enter a DNA sequence: ")
try:
    validated_sequence = validate_sequence(sequence)
    transcribed_sequnece = dna_to_rna_transcription(validated_sequence)
    print(f"validated sequence: {validated_sequence}")
    print(f"transcribed sequence: {transcribed_sequnece}")
except ValueError as e:
    print(e)
    