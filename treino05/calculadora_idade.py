import datetime
def calculadoraIdade(dia, mes, ano):
    data_hoje = datetime.datetime.now().date()
    data_nascimento = datetime.date(ano, mes, dia)
    idade = int((data_hoje - data_nascimento).days / 365.25)
    print('A idade é:', idade)

calculadoraIdade(12, 12, 1994)



