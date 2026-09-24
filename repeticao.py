## Avaliação de Atendimento
quantidade_excelente = 0
quantidade_ruim = 0

## Entrada de dados e repetção
for i in range(10, 56, 5):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
## Opinião e contagem
    opiniao = input("Qual sua opinião sobre o atendimento? (1 - Excelente, 2 - Bom, 3 - Ruim): ")
    print("Obrigado por participar da pesquisa! ",nome)

## Validação de opinião
    if opiniao not in ["1", "2", "3"]:
        print("Opinião inválida. Por favor, insira 1, 2 ou 3.")
        opiniao = input("Qual sua opinião sobre o atendimento? (1 - Excelente, 2 - Bom, 3 - Ruim): ")
        
## Contagem de opiniões
    if opiniao == "1":
        quantidade_excelente += 1
    elif opiniao == "3":
        quantidade_ruim += 1

## Resultado da pesquisa
print("A quantidade de pessoas que acharam o atendimento excelente é:", quantidade_excelente)
print("A quantidade de pessoas que acharam o atendimento ruim é:", quantidade_ruim)
