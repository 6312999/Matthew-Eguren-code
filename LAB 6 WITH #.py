dna = 'atgcgatgcgatgcg'         #defining what the variable is equal to
exons = [(2,5), (10,12)]        #telling me that between 2-5 there are exons, also in 10-12
dna = 'gctagctagctagcta'        #redefining what the variable is equal to
exons = [(0,3),(5,8)]       #telling me that between 0-3 there are exons, also in 5-8
annot = list(dna.lower())
for s,e in exons:    
  for i in range(s,e):        
    annot[i] = annot[i].upper() #annot is short for annotate and its just said to list values in i (range from s,e)
print(''.join(annot))       


dna = 'gctagctagctagcta'            #defining what the variable is equal to
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'}        #telling me to know the values of A T C and G
print(counts)   #printing the A T G C with the nucleotide count
dna = 'gctagctagctagcta' #redefining what the variable is equal to
print(dna[::-1])    #print the code but without the last character
