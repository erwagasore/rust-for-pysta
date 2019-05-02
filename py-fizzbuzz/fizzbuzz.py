for number in range(1, 101):
    fzb = ''

    if number % 3 == 0:
        fzb += 'Fizz'
    if number % 5 == 0:
        fzb += 'Buzz'
    if not fzb:
        fzb += '{}'.format(number)
    print(fzb)
