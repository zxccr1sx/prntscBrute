import string    
import random 
import time
import webbrowser


print('\033[31m')
print('\033[1m')
print('[✓]CREATED BY @true_wannacry in telegram')
print('[✓]CREATED BY @true_wannacry in telegram')
print('[✓]CREATED BY @true_wannacry in telegram')
print('\033[37m')

S = 2 
ran = ''.join(random.choices(string.ascii_lowercase, k = S))    
S2 = 4
ran2 = ''.join(random.choices(string.digits, k = S2))
result = f'https://prnt.sc/{ran}{ran2}'
choice = int(input('Enter num of links to generate '))
resultfull = webbrowser.open_new_tab(result)
i = 0

while True:
	print("link : " + f'resultfull')
	time.sleep(1)
	i += 1
	if i == choice:
		break
		
	result = f'https://prnt.sc/{ran}{ran2}'
	
	ran = ''.join(random.choices(string.ascii_lowercase, k = S))
	ran2 = ''.join(random.choices(string.digits, k = S2))
	resultfull = webbrowser.open(result)
