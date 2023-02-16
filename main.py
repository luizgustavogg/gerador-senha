import random

# Caracteres Usadas
min = 'abcdefghijklmnopqrstuvwxyz'
max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sybs = '[]{}()*#;/,-_%'

# Quantidade de caracteres
qnt = int(input('Digite qual tamanho da senha: '))

#fazendo senha com todos

all = min + max + num + sybs
passwordAll = "".join(random.sample(all,qnt))

#só maiúsculas e números

MAXnum = max + num
passwordMAXnum = "".join(random.sample(MAXnum,qnt))

#só minusculas e maiúsculas

MAXmin = max + min
passwordMAXmin = "".join(random.sample(MAXmin,qnt))

print(f'Senha sem 100% segura: {passwordAll} \n{10*("====") } \n'
        f'Senha Só maiúsculas e números: {passwordMAXnum} \n{10*("====") } \n'
        f'Senha Só minusculas e maiúsculas: {passwordMAXmin}')