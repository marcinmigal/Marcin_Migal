def say_hi(name: str, surname: str) -> str:
    return f'Cześć {name} {surname}'

prompt = say_hi('Marcin','Migal')
print(prompt)