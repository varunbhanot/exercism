def to_rna(dna_strand):
    translation_table = {ord('A'):ord('U'),ord('G'):ord('C'),ord('C'):ord('G'),ord('T'):ord('A')}
    return str(dna_strand).translate(translation_table)