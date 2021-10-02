#Calc
#
#Russia laung

from fractions import Fraction
from os import system
from random import choice
from time import sleep


print('1)Дробь\n2)Обычное число\n3)Степень\n4)Уравнение\n5)Процент от числа\n6)Выйти')
vib = int(input('Выбор: '))

#####################
#Переменные и масивы#
pod = ['**-Степень',
	'кста можно мне написать в дс по поводу уравнение(Чел богач#3175)',
	'Этот калькулятор был сделал как быстрый калькулятор для владельца',
	'/ - Деление кто не знал',
	'Калькулятор корней не буду делать ок да',
	'Код открыт скачивай и показывай на информатике мне все равно',
	'Если у вас очистилась консоль и не показал ответ то произошла ошибка',
	'Всегда читайте подсказки']
bye = ['Пока!', 'Еще увидимся:)', 'Прощай:(', 'До встречи(!_!)']
error = 'Произошла ошибка'
hello = 'Привет от меня'
#Переменные и масивы#
#####################


##################################################
#########Некому не нужные функции#################
def podskaska():
	print(choice(pod))
def bay():
	print(choice(bye))
def c():
	system('cls')

#########Некому не нужные функие######################
######################################################


########################################################
#########Математика непосильная мне#####################

def proc():
	podskaska()
	a = int(float(input('Число: ')))
	b = int(float(input('От числа: ')))
	print(f'Число {a} от числа {b} = {a / 100 * b} процент')

def x():
	podskaska()
	print('X = неизвестное')
	a = int(float(input('Известное число: ')))
	znak = str(input('Знак(* / + -): '))
	b = int(float(input('Ответ: ')))
	system('cls')

	if (znak == '+'):
		print(f'''
x + {a} = {b}  
x = {b} - {a}  
Ответ : {b - a}
---------------
{a} + x = {b}
x = {b} - {a}
Ответ: {b - a}''')

	if(znak == '-'):
		print(f'''
x - {a} = {b}  
x = {b} + {a}  
Ответ: {b + a} 
-----------------
{a} - x = {b}
x = {b} - {a}
Ответ: {b + a}''')

	if (znak == '*'):
		print(f'''
x * {a} = {b}  
x = {b} / {a}  
Ответ: {b / a}
-----------------
{a} * x = {b}
x = {b} / {a}
Ответ: {b * a}
-----------------
	''')

	if (znak == "/"):
		print(f'''
x / {a} = {b}
x = {b} * {a}
Ответ = {b * a}
---------------
{a} / x = {b}
x = {b} * {a}
Ответ = {b * a}
''')


	
def step():
	podskaska()
	print('Степень (10 в 34)')
	a =int(float(input('Число: ')))
	b =int(float(input('В степени: ')))
	system('cls')
	print(f'Ответ: {a ** b}')

def fraction():
	podskaska()
	print(f'Пример: 1/2 одна вторая\n')
	a = Fraction(int(input('Первая дробь: ')))
	znak = str(input('Знак(* / + -): '))
	b = Fraction(int(input('Вторая дробь: ')))
	system('cls')
	if (znak == '+'):
		c()
		print(f'Ответ: {a + b}')
	if (znak == '-'):
		c()
		print(f'Ответ: {a - b}')
	if (znak == '/'):
		c()
		print(f'Ответ: {a / b}')
	if (znak == '*'):
		c()
		print(f'Ответ: {a * b}')
def calc():
	podskaska()
	a = int(input('Первое число: '))
	znak = str(input('Знак(- + / *): '))
	b = int(input('Второе число: '))
	system('cls')
	if (znak == '+'):
		c()
		print(f'Ответ: {a + b}')
	if (znak == '-'):
		c()
		print(f'Ответ: {a - b}')
	if (znak == '/'):
		c()
		print(f'Ответ: {a / b}')
	if (znak == '*'):
		c()
		print(f'Ответ: {a * b}')
#########Математика непосильная мне#####################
########################################################

 
if (vib == 1):
	fraction()
if (vib == 2):
	calc()
if (vib == 3):
	step()
if (vib == 4):
	x()
if(vib == 666):
	vremy()
if (vib == 5):
	c()
	bay()
	exit()
if (vib == 210908):
	print(hello)
else:
	c()
	print(error)
	system('python helper.py')
