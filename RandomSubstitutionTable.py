# Importing Random Package of Python
import random

# Empty List
numlst = []

# List of Alphabets
alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z' ] 

# Random generation of the Alphabets 
while len(numlst) < 26:
      rnd = alphabet[random.randint(0,25)]
      if rnd in numlst:
          continue
      else:
          numlst += [rnd]

dictOfWords=dict()
for i in range(0,26):
    dictOfWords.update({alphabet[i]:numlst[i]})

print("|-------------------------------------|")
print("| R.A.N.D.O.M S.U.B.S.T.I.T.U.T.I.O.N |")
print("|-------------------------------------|")
# Getting Input from the user
inputData = input("\n\nEnter the data to be encrypted:")
data=(list)(inputData.upper())

data1=[]

# Encrypting the data (plain-text)
for i in range(0,len(data)):
    for keys,values in dictOfWords.items():
        if data[i].isalpha() == False:
            data1.append(data[i])
            break
        if data[i]==keys:
            data1.append(values)
            break

encrypted = ""
            
for i in data1:
    encrypted+=i

print("\nEncrypted Data is: "+encrypted)

print("\n\nRandom substitution table used:")
print(dictOfWords)