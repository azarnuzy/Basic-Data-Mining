a = 2 
b = 3
print('a+b adalah {}'.format(a+b))

c = not((a * b > 5) and (a + b < 5))
print(c)

# CASTING TIPE DATA
data_int = 9
print('data= ', data_int, 'type = ', type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika int = 0

print('data= ', data_float, 'type = ', type(data_float))
print('data= ', data_str, 'type = ', type(data_str))
print('data= ', data_bool, 'type = ', type(data_bool))
