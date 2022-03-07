'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocacao, Depois mostre:
A- Apenas os 5 primeiros colocados.
B- Os ultimos 4 colocados da tabela.
C- Uma lista com os times em ordem alfabetica.
D- Em que posicao na tabela estao time da Chapecoense.'''

from time import time


timesingleses='Manchester City', 'Liverpool', 'Chelsea', 'Manchester United', 'West Ham', 'Arsenal', 'Wolverhampton', 'Tottenham', 'Brighton', 'Southampton', 'Crystal Palace', 'Leicester', 'Aston Villa', 'Brentford', 'Leeds United', 'Everton', 'Newcastle', 'Burnley', 'Watford', 'Norwich'
print(timesingleses[:5])
print('-='*30)
print(timesingleses[16:])
print('-='*30)
print(sorted(timesingleses))
print('-='*30)
print(f'O Leicester esta na {timesingleses.index("Leicester")+1} posicao da tabela.')
