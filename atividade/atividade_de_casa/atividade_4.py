# Atividade 4 - Estrutura Condicional Composta

# int() converte o valor digitado para número inteiro
valor = int(input("Digite um valor: "))

# Verifica se o valor é maior que 70
if valor > 70:
    print("Destino: Marte")

# Verifica se o valor está entre 30 e 70
elif valor >= 30 and valor <= 70:
    print("Destino: Lua")

# Caso o valor seja menor que 30
else:
    print("Permanece na órbita da Terra")

# if: Usado para verificar uma condição e executar um bloco de código se a condição for verdadeira.

# elif: Usado para verificar uma condição adicional se a condição anterior for falsa.

# else: Usado para executar um bloco de código se todas as condições anteriores forem falsas.

# > : Maior que
# >= : Maior ou igual a
# < : Menor que
# <= : Menor ou igual a
# and: Operador lógico que retorna True se ambas as condições forem verdadeiras.