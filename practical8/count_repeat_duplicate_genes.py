def write_fasta_entry(outfile, gene_name, sequence, repeat_count):
    outfile.write(f'>{gene_name} ({repeat_count})\n')
    outfile.write(sequence + '\n')

with open('duplicate_genes.fa', 'r') as infile, \
     open('GTGTGT_duplicate_genes.fa', 'w') as outfile:  
    repeat_pattern = input("Enter one of the repetitive sequences ('GTGTGT' or 'GTCTGT'): ")
    gene_name = ''
    sequence = ''
    repeat_count = 0

    for line in infile:
        if line.startswith('>'):
            if gene_name:  
                write_fasta_entry(outfile, gene_name, sequence, repeat_count)
            gene_name = line[1:]  
            sequence = ''
            repeat_count = 0
        else:
            sequence += line.strip()
            # count for the repetitive tims
            repeat_count += sequence.count(repeat_pattern)

    # write
    write_fasta_entry(outfile, gene_name, sequence, repeat_count)