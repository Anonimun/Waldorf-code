ts = int(input("hány tantárgyad van?"))
sum = 0
for i in range(ts):
    jegy = int(input("tantárgy jegye"))
    #sum = sum + jegy
    sum += jegy
atlag = sum/ts
print("jegy átlag: ",atlag)