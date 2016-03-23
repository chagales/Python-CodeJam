def reverse(case, array):
    print 'reverse'
    auxArray = " ".join(array.split()[::-1])
    print ('Case # ' +str(case)+' ' +auxArray + '\n')    
    #print '\n'

    outfile = open('textoReverse.txt', 'a') # Indicamos el valor 'w'.
    outfile.write('Case # '+str(case)+ ' ')
    outfile.write(str(auxArray))
    outfile.write('.\n')
    outfile.close()



#Start
print 'Inicio'
f= open('B-small-practice.in','r')
print f
indexCase=0
indexsimple=1
numper="0123456789"
for line in f:
    print line
    if (indexCase==0):
        cases = line
        indexCase +=1
        print ('Cases ' + str(cases))        
    else:
        reverse(indexCase,line)
        indexCase+=1

