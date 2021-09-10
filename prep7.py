a=input('Drink Size:\n')
b=input('Drink type:\n')
if a=='large':
      if b=='regular':
            print('300 calories')
      elif b=='diet':
            print("100 calories")
      else: 
            print('0 calories')
elif a=='small':
      if b=='regular':
            print('150 calories')
      elif b=='diet':
            print('50 calories')
      else:
            print('0 calories')
