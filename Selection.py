import random 

#Generating temperature using random function between 1 to 400
temperature = random.randint(1, 400)
if temperature > 100:
    print(f'temperature: {temperature} --temperature above boiling point')
if temperature >  320:
    print(f'temperature: {temperature} --temperature above smoke point')
if temperature < 100:
    print(f'temperature: {temperature} --temperature is not very high')