x = []
count = 0
suma = 0

while True:
	a=input("Enter a number or Enter to finish: ")
	if a.isdigit():
		x.append(int(a))
		count +=1
		suma += int(a)

	else:
		print("------------------------------------"'\n'+"You entered:",x)
		print("total = ",count,",", "suma = ",suma,",","maximum = ",max(x),",","minimum = ",min(x))	
		break