count = 0

def bigWords(func):
    if count < 1: 
        print('What time is it?')
        func()     
        print('How does sugar taste?')
    else:
        func()
        func()
        
@bigWords 
def magic():
    print("HOW IS IT" * 20)