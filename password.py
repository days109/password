x = 4
while True:
	password = input('請輸入密碼: ')
	x = x -1
	if password == 'a1234':
		print('登入成功')
		break
	elif x == 0:
		print('超過次數禁止登入')
		break
	elif password != 'a1234':
		print('密碼錯誤!還有')
		print(x)
		print('機會')
	
	