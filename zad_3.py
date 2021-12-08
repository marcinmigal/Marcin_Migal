def if_even(number) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


even = if_even(5)

if even == True:
    print('Liczba Parzysta')
else:
    print("Liczba Nieparzysta")
