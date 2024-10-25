for i in range(1, 16):  # range(1, 15+1)과 동일하지만 간결하게 수정
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
