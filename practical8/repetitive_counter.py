seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
element1 = 'GTGTGT'
element2 = 'GTCTGT'
import re 
number1 = len(re.findall(element1, seq))
number2 = len(re.findall(element2, seq))
print(number1+number2)