with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as file,\
    open('duplicate_genes.fa', 'w') as outfile:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if 'duplication' in line:
                outfile.write(line + '\n')
        elif line:
            outfile.write(line)  # 写入序列，直到遇到下一个'>'