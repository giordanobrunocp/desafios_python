import math
ang=int(input('Digite um angulo: '))
sen=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))

print('O Seno do ângulo {}º é {:.2f}'.format(ang,sen))
print('O Cosseno do ângulo {}º é {:.2f}'.format(ang,cos))
print('A Tangente do àngulo {}º é {:.2f}' .format(ang,tan))
