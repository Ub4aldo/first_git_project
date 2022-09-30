#reading
#f=open('textfile.txt', 'r')
#print([line for line in f.readlines()])

#for line in f.readlines():
#    print(line.strip())

#writing
fw = open('newTextFile.txt', 'w')
print(fw)

fw.write('Line 1\n')
fw.write('Line 2\n')
fw.write('Line 3')
fw.close()

fa = open('newTextFile.txt', 'a')

fa.write('Line 1\n')
fa.write('Line 2\n')
fa.write('Line 3')

fa.close()


with  open('newTextFile.txt', 'a') as fwith:
    fwith.write('FWLine 1\n')
    fwith.write('FWLine 2\n')
    fwith.write('FWLine 3')
    #this file will be closed after the executioin of this block of code.