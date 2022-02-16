word = input('entrada: ').lower()
lista = []
#anagramas = []
count = 0
control = 0 

for i in list(word):
    control += 1
    if i not in lista:
        lista.append(i)
    else:
        lst1 = []
        lst2 = []
        count += 1
        #anagramas.append(i)
        pos1 = word.find(i)
        if(control - 1) != (pos1+1):
            while(pos1+1 )< control:
                lst1 += word[pos1]
                pos1 += 1
                lst2 += word[pos1]
            #anagramas.append(str(lst1) + str(lst2))
            if set(lst1) == set(lst2):
                count += 1
print(count)
#print(anagramas)
        
            
