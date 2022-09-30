def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):

    # interprete estas variaveis como quais cartas cada um vai dar em troca da outra
    maria_gives = []
    joao_gives = []

    for figurinha_maria in figurinhas_da_maria:
        # caso joao ja tenha a figurinha da maria, pule
        if (figurinha_maria in figurinhas_do_joao):
            continue

        # caso algum dos dois ja tenha dado esta carta
        if (figurinha_maria in maria_gives or figurinha_maria in joao_gives):
            continue

        for figurinha_joao in figurinhas_do_joao:
            # caso maria ja tenha a figurinha do joao, pule
            if (figurinha_joao in figurinhas_da_maria):
                continue
            
            # caso algum dos dois ja tenha dado esta carta
            if (figurinha_joao in joao_gives or figurinha_joao in maria_gives):
                continue

            maria_gives.append(figurinha_maria)
            joao_gives.append(figurinha_joao)
            break

    return len(maria_gives)

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))
