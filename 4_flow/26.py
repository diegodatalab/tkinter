# 
# * 26. Match case

mood = 'bored'

match mood:
    case 'hungry':
        print('get some food')
    case 'thirsty':
        print('get some water')
    case 'tired':
        print('get some sleep')
    case _:
        print('any other mood')