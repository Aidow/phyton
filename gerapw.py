palavra = input("Palavra: ")
k = 0
troca = ""
while k < len(palavra):
	if palavra[k] in "a":
	   troca = troca + "@"
	elif palavra[k] in "e":
	   troca = troca + "3"
	elif palavra[k] in "i":
	   troca = troca + "1"
	elif palavra[k] in "o":
	   troca = troca + "0"
	else:
	   troca = troca + palavra[k]
	k += 1
print ("Nova palavra %s" %troca)
