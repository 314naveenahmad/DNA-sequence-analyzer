from dna import (
    validate_sequence,
    sequence_length,
    nucleotide_count,
    gc_content,
    reverse_complement,
    dna_to_rna_transcription
    )

def display_menu() -> int:
    print("=" * 40)
    print("      DNA Sequence Analyzer")
    print("=" * 40)
    print("1. Sequence Length")
    print("2. Nucleotide Count")
    print("3. GC Content")
    print("4. Reverse Complement")
    print("5. DNA to RNA Transcription")
    print("6. Exit")
    return int(input("Enter your choice (1-6): "))

def main() -> None:
    while True:
        try:
            choice = display_menu()
            
            if choice == 6:
                print("\nThank you for using the DNA Sequence Analyzer")
                break

            if choice not in range(1, 6):
                print("Invalid choice. Please select a valid option.")
                continue
                
            sequence = input("Enter a DNA sequence: ")
            validated_sequence = validate_sequence(sequence)
            
        
            match choice:
                case 1:
                    print(f"\nSequence length: {sequence_length(validated_sequence)}")
                case 2:
                    counts = nucleotide_count(validated_sequence)
                    print(f"\nNucleotide count: {counts}")
                case 3:
                    counts = nucleotide_count(validated_sequence)
                    print(f"\nGC content: {gc_content(counts)}%")
                case 4:
                    print(f"\nReverse complement: {reverse_complement(validated_sequence)}")
                case 5:
                    print(f"\nRNA transcription: {dna_to_rna_transcription(validated_sequence)}")

            input("\nPress Enter to continue...")

        except ValueError as e:
            print(f"Error: {e}")
            input("\nPress Enter to continue...")
        
if __name__ == "__main__":
    main()


