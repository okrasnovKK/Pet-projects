# Шифр Цезаря

def questions():
    task = int(input('Задайте направление шифрования (0-зашифровать, 1-дешифровать). Выход - 2: '))
    if task not in [0, 1, 2]:
        print('Введено неверное значение')
        questions()
    elif task == 2:
        print('До свидания!')
        exit()

    language = int(input('Выберите язык (0-русский, 1-английский): '))
    if language not in [0, 1]:
        print('Введено неверное значение')
        questions()
    elif language == 0:
        step = int(input('Выберите шаг сдвига (1 до 32(включительно): '))
        if step < 1 or step > 32:
                print('Введено неверное значение')
                questions()
    else:
        step = int(input('Выберите шаг сдвига (1 до 25(включительно)): '))
        if step < 1 or step > 25:
            print('Введено неверное значение')
            questions()
    return task, language, step

def sentence():
    massage = input('Введите сообщение: ')
    if massage.isdigit():
        print('Данное сообщение нельзя за(де-)шифровать')
        sentence()
    else:
        mas_1= massage
        for i in mas_1:
            if i in [*string.punctuation]:
                mas_1 = mas_1.replace(i, '')
    if mas_1 in ['', ' ']:
        print('Данное сообщение нельзя за(де-)шифровать')
        sentence()
    return massage

def re_de_cryption():
    task, language, step = questions()
    massage = sentence()
    if task == 0:
        '''Шифровка'''

        encrypted_massage = ''
        for j in massage:
            if j in [*string.punctuation, ' ']:
                encrypted_massage = encrypted_massage + j
            else:
                if j.isupper():
                    if language == 1:
                        if 65 <= ord(j) + step <= 90:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step)
                        else:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step - 26)
                    else:
                        if 1040 <= ord(j) + step <= 1071:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step)
                        else:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step - 32)
                else:
                    if language == 1:
                        if 97 <= ord(j) + step <= 122:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step)
                        else:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step - 26)
                    else:
                        if 1072 <= ord(j) + step <= 1103:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step)
                        else:
                            encrypted_massage = encrypted_massage + chr(ord(j) + step - 32)

        return encrypted_massage
    elif task == 1:
            #'''Дешифровка'''


        decrypted_massage = ''
        for j in massage:
            if j not in [*string.punctuation, ' ']:
                if j.isupper():
                    if language == 1:
                        if 65 <= ord(j) - step <= 90:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step)
                        else:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step + 26)
                    else:
                        if 1040 <= ord(j) - step <= 1071:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step)
                        else:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step + 32)
                else:
                    if language == 1:
                        if 97 <= ord(j) - step <= 122:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step)
                        else:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step + 26)
                    else:
                        if 1072 <= ord(j) - step <= 1103:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step)
                        else:
                            decrypted_massage = decrypted_massage + chr(ord(j) - step + 32)
            else:
                decrypted_massage = decrypted_massage + j
        return decrypted_massage
    else:
        print('До свидания!')
        exit()


for i in range(25):
    print(re_de_cryption())
import string
text = input().split()

encrypted_massage = ''
for i in text:
    k = len(i)
for a in i:
    if a in [*string.punctuation]:
        k -= 1
for j in i:
    if j in [*string.punctuation, ' ']:
        encrypted_massage = encrypted_massage + j
    else:
        if j.isupper():
            if 65 <= ord(j) + k <= 90:
                encrypted_massage = encrypted_massage + chr(ord(j) + k)
            else:
                encrypted_massage = encrypted_massage + chr(ord(j) + k - 26)
        else:
            if 97 <= ord(j) + k <= 122:
                encrypted_massage = encrypted_massage + chr(ord(j) + k)
            else:
                encrypted_massage = encrypted_massage + chr(ord(j) + k - 26)
encrypted_massage = encrypted_massage + ' '
print(encrypted_massage)