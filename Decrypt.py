encryption=input("Enter the sentance you would like Decrypt")
new = list(encryption)
i=0
for letter in encryption:


    if new[i]=='d':
        new[i]= 'a'
    elif new[i]=='e':
        new[i]="b"
    elif new[i]==' ':
        new[i]=" "
    elif new[i]=='f':
        new[i]='c'
    elif new[i]=='g':
        new[i]='d'
    elif new[i]=='h':
        new[i]='e'
    elif new[i]=='i':
        new[i]='f'
    elif new[i]=='j':
        new[i]='g'
    elif new[i]=='k':
        new[i]='h'
    elif new[i]=='l':
        new[i]='i'
    elif new[i]=='m':
        new[i]='j'
    elif new[i]=='n':
        new[i]='k'
    elif new[i]=='o':
        new[i]='l'
    elif new[i]=='p':
        new[i]='m'
    elif new[i]=='q':
        new[i]='n'
    elif new[i]=='r':
        new[i]='o'
    elif new[i]=='s':
        new[i]='p'
    elif new[i]=='t':
        new[i]='q'
    elif new[i]=='u':
        new[i]='r'
    elif new[i]=='v':
        new[i]='s'
    elif new[i]=='w':
        new[i]='t'
    elif new[i]=='x':
        new[i]='u'
    elif new[i]=='y':
        new[i]='v'
    elif new[i]=='z':
        new[i]='w'
    elif new[i]=='a':
        new[i]='x'
    elif new[i]=='b':
        new[i]='y'
    elif new[i]=='z':
        new[i]='z'

    i=i+1
msg=str(new)
print("Message decrypted")
print (msg)
