x = []
count, suma = 0, 0

while True:
	a=input("Enter a number or Enter to finish: ")
	if a.isdigit():
		x.append(int(a))
		count +=1
		suma += int(a)
	elif a.isalpha():
		print("Enter a number, not a word. Enter to finish.")
		continue
	else:
		if len(x) > 0:
			print("      --------------------------------"+'\n'+"      You entered:",x)
			print("      Total = ",count,",", "sum = ",suma,",","maximum = ",max(x),",","minimum = ",min(x))	
			break
		else:
			print("You not enter any number. Program aborted.")
			break