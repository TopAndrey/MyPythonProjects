def calc():
    joke = 1
    def end():      # ШУТКА (Убирается, когда joke = 0)
        if joke == 1:
            print('ТУДУДУДУДУ! ТУ... ТУ! THE END')
            time.sleep(1.6)
            print('Да я ж пошутил! ХЕХЕ!')
            time.sleep(0.8)
            print('ПЕРЕЗАПУСКАЮ...')
            time.sleep(1)

    loop = True
    while loop == True:
        loop = False
        print('    КАЛЬКУЛЯТОР+')
        print('Выберете режим: NORMAL (N) / MULTI (M)')
        mode = str(input('> '))
        if mode.lower() == 'n':
            operat = str(input('Операция (+-*:√): '))
            if operat == '+':
                a = int(input('> '))
                b = int(input('> '))
                print(a+b)
            elif operat == '-':
                a = int(input('> '))
                b = int(input('> '))
                print(a-b)
            elif operat == '*':
                a = int(input('> '))
                b = int(input('> '))
                print(a*b)
            elif operat == ':':
                a = int(input('> '))
                b = int(input('> '))
                while a == 0 or b == 0:
                    err = 'Ошибка! На ноль делить нельзя! Мысли: походу за компом первоклашка'
                    if a == 0 and b != 0:
                        print(err)
                        a = int(input('> '))
                    elif b == 0 and a != 0:
                        print(err)
                        b = int(input('> '))
                    else:
                        print(err)
                        a = int(input('> '))
                        b = int(input('> '))
                print(a/b)
                q = str(input('Надо округлить? Y/N: '))
                if q == 'Y' or q == 'y':
                    ab = round((a/b), 0)
                    print('Ответ: '+str(ab))
            elif operat == '√' or operat.lower() == 'корень' or operat.lower() == 'sqrt':
                a = int(input('> '))
                if sqrt(a) == round(sqrt(a), 0):
                    a = str(sqrt(a))
                    print(a[0])
                else:
                    print(round(sqrt(a), 3))
            else:
                loop = True
                end()

                
        elif mode.lower() == 'm':
            operat = str(input('Операция (+-*:) '))
            if operat == '+':
                iput = int(input('Сколько слагаемых? (3-∞)'))
                result = 0
                if iput > 2:
                    for i in range(iput):
                        a = int(input('> '))
                        result = result + a
                    print(result)
                else:
                    print('Ошибка! В MULTI-моде минимум 3 слагаемых.')
            elif operat == '-':
                iput = int(input('Сколько вычитаемых? (2-∞)'))
                result = 0
                if iput > 1:
                    for i in range(iput+1):
                        a = int(input('> '))
                        if i == 0:
                            result = a
                        else:
                            result = result - a
                    print(result)
                else:
                    print('Ошибка! В MULTI-моде минимум 1 уменьшаемое и 2 вычитаемых.')
            elif operat == '*':
                iput = int(input('Сколько множителей? (3-∞)'))
                result = 1
                if iput > 2:
                    for i in range(iput):
                        a = int(input('> '))
                        result = result * a
                    print(result)
            elif operat == ':':
                iput = int(input('Сколько делителей? (2-∞): '))
                result = 0
                if iput > 1:
                    for i in range(iput+1):
                        a = int(input('> '))
                        if i == 0:
                            result = a
                        else:
                            while a == 0:
                                print('Ошибка! На ноль делить нельзя! Мысли: походу за компом первоклашка...')
                                a = int(input('> '))
                            result = result / a
                    print(result)
                    q = str(input('Надо округлить? Y/N: '))
                    if q.lower == 'y':
                        abc = round((result), 0)
                        print('Ответ: '+str(abc))                    
                else:
                    print('Ошибка! В MULTI-моде должно быть как минимум 1 делимое и 2 делителя.')
                
            else:
                loop = True
                end()
                
        else:
            loop = True
            end()

calc()
