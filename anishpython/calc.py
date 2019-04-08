a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the choice"))
def sum():
	d=a+b
	return d
def difference():
	d=a-b
	return d
def product():
	d=a*b
	return d
def quotient():
	if b==0:
		print "Enter a non-zero number"
	else:
        	d=a/b
		return d
if c==1:
	print sum()
elif c==2:
	print difference()
elif c==3:
	print product()
elif c==4:
	print quotient()
else:
	print "Enter a valid choice"


