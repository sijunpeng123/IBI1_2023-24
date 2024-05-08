def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines)  
        return sequence

def score_and_identity_rate(seq1, seq2):
    score = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            score += 1
    identity_rate = score/len(seq1)
    return identity_rate, score
    
    
rat_sequence = read_fasta(r'C:\Users\14125\Desktop\work\IBI\SLC6A4_RAT.fa')
human_sequence = read_fasta(r'C:\Users\14125\Desktop\work\IBI\SLC6A4_HUMAN.fa')
cat_sequence = read_fasta(r'C:\Users\14125\Desktop\work\IBI\SLC6A4_CAT.fa')

identity_rate_1, score_1 = score_and_identity_rate(human_sequence, cat_sequence)
identity_rate_2, score_2 = score_and_identity_rate(human_sequence, rat_sequence)
identity_rate_3, score_3 = score_and_identity_rate(rat_sequence, cat_sequence)

print('Human and cat:',  identity_rate_1,  score_1)
print('Human and rat:', identity_rate_2, score_2)
print('Rat and cat:', identity_rate_3, score_3)

# Rat's and cat's sequendce are more related
# Mouse is better model organism for human