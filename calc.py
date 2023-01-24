print("Birinci Degeri Giriniz:")
valueOne = int(input())
print("İkinci Degeri Giriniz:")
valueTwo = int(input())

print("Operatoru Giriniz")
operator = input()
if operator == "+":
	print("İki Degerin Toplami: " + str(valueOne + valueTwo))
elif operator == "-":
	print("İki Degerin Farki: " + str(valueOne - valueTwo))
elif operator == "*":
	print("İki Degerin Carpimi: " + str(valueOne * valueTwo))
elif operator == "/":
	print("İki Degerin Bölümü: " + str(valueOne / valueTwo))
else :
	print("Operatorunuz Gecersiz")	
