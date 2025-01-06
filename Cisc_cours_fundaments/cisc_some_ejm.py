var = 0
# mientras sea menor a 6
while var < 6:
    # aunmenta 1
    var += 1
    # si es par
    if var % 2 == 0:
        # continua y omite el resto
        continue
    # 1, 3, 5,
    print("#_-")

#
var = 1
while var < 10:
    print("#")
    # desplazamiento a la izq
    # multiplic x 2
    var = var << 1
    print(var)

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print('Valor de x', x)

a = 1
b = 0
# and
c = a & b
print(c, end=" _ ")
# or
d = a | b
print(d, end=" _ ")
# xor
e = a ^ b
print(e)

print(c + d + e)

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(sum(vals,))

nums = [1, 2, 3]
vals = nums
del vals[1:2]

print(vals)

nums = [1, 2, 3]
vals = nums[-1:-2]

print('replicacion',nums,vals)

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)


my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

my_list = [i for i in range(-1, 2)]

print(len(my_list), my_list)

# Matriz de 3 por 3 solo con numeros
matrix_pares = [[x+1 for x in range(3)] for y in range(3)]

for i in matrix_pares:
    print('fila', i)
    for j in i:
        print('col', j)


t = [[3-i for i in range (3)] for j in range (3)]
print('matriz 3x3', t)
s = 0
for i in range(3):
    # suma la diagonal
    s += t[i][i]
print(s)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[1][0])


def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))


def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)


def func(a, b):
    return a ** a


print(func(2,2))

def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))


def funcion_x(x):
    global y
    y = x * x
    return y


funcion_x(2)
print(y)


def any_var():
    print(var + 1, end='')


var = 1
any_var()
print(var)

my_list3 = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'


print(my_list(my_list3))


def fun_operacion(x, y, z):
    return x + 2 * y + 3 * z


print(fun_operacion(0, z=1, y=3))


def fun_inp_out(inp=2, out=3):
    return inp * out


print(fun_inp_out(out=2))


tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)













