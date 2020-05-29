what = input("Что делаем? (+, -,*,/,^):")
a = float (input ("Введи первое число: "))
b = float (input ("Введи второе число: "))

if what == "+":
	c = a + b
	print ("Результат:" + str(c))
elif what == "-":
	c = a - b
	print ("Результат:" + str(c))
elif what == "/":
	c = a / b
	print ("Результат:" + str(c))
elif what == "*":
	c = a * b
	print ("Результат:" + str(c))
elif what == "^":
	c = a ** b
	print ("Результат:" + str(c))
else:
	print("Извините, такой операции у нас пока что нет!")
