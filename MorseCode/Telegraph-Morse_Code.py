import argparse
import pyfiglet
import os

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def plain_morse(plain):
    morse = []
    morse_str=''
    for i in plain:
        for key,value in MORSE_CODE_DICT.items():
            if key==i:
                morse.append(value)
                break
            elif not i.isalpha():
                morse.append(i)
                break
            else:
                continue
            
    print('\033[93m'+"The Morse Code is -> \n"+'\033[96m'+''.join(morse)+'\033[0m')
    print("\n")


ascii_banner = pyfiglet.figlet_format("Morse Code")
print(ascii_banner)

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encrypt", dest='plaintext', nargs='+', help="Enter the data to encrypt")
parser.add_argument("-f", "--file", dest='file', nargs='+', help="Enter the file path")
parser.add_argument("-d", "--decrypt", dest='morsecode',nargs='+', help="Enter the data to decrypt")

args = parser.parse_args()

plain = []
morse = []
temp = []
if args.plaintext:
    arg_str = ' '.join(args.plaintext)
    for c in arg_str:
        plain.append(c.upper())
    plain_morse(plain)
    
elif args.file:
    with open(args.file[0]) as file:
     
        try:
            for lines in file:
                temp.append(lines)
        except:
            print("The file " + " could not be opened.")
    for i in temp:
        for j in i:
            plain.append(j.upper())
    plain_morse(plain)

else:
    print("Go to help or -h")

