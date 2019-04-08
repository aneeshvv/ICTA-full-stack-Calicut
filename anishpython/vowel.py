a=raw_input("Enter the string").upper()
n=0
p=0
k=0
j=0
for i in a:
	if i in "aeiouAEIOU":
		n=n+1
	elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
		p=p+1
	elif i in " ":
		k=k+1
	elif i in "?":
		j=j+1
print("The number of vowels is",n)
print("The number of consonants is",p)
print("The number of words are",k+1)
print("The number of ? is",j)
	

