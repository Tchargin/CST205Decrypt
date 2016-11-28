from PIL import Image
import smtplib
import os, sys, subprocess

def decode_image(img):
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    r, g, b, a = img.getpixel((col, row))
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    msg += chr(r)
                index += 1
        return msg

# Opening the picture for windows or iOS depending on your system.
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(encoded_image_file)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, encoded_image_file])


encoded_image_file = "enc_Image.png"
img2 = Image.open(encoded_image_file)
hidden_text = decode_image(img2)
print("Secret message: {}".format(hidden_text))
img_data= open('enc_Image.png','rb').read()


decryption=input("Enter the sentence you would like decrypt: ")
new = list(decryption)
i=0
for letter in decryption:


    if new[i]=='d':
        new[i]= 'a'
    elif new[i]=='e':
        new[i]="b"
    elif new[i]==' ':
        new[i]=' '
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
print("Message Decrypted")
print (msg)
