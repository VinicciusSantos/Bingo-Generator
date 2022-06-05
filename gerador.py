from PIL import Image, ImageFont, ImageDraw
from random import randint
from time import sleep
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_molde1 = os.path.join(diretorio_principal, "Moldes", "molde1.png")
diretorio_molde2 = os.path.join(diretorio_principal, "Moldes", "molde2.png")
caminho_fonte = '/home/vinicius/Downloads/bebas_neue/BebasNeue-Regular.otf'
rgb_preto, rgb_branco = (0, 0, 0), (255, 255, 255)
pro = 'Gerador de Bingo'
arq = 'dadosrifa.txt'
contador = imagem = 0
ganhadores = []
pontuou = []
sorteados = []
conferir = []
geral = []
cartela = []
lgeral = []
lcartela = []
b = []
i = []
n = []
g = []
o = []


# Função que lê um número inteiro:
def leiaint(msg='Opção: '):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! por favor, digite um número inteiro válido.')
            continue
        else:
            return x


# Função que Sorteia os números de uma coluna no bingo:
def colbingo(lista, quantidade, primeiro, ultimo, cart):
    while True:
        x = randint(primeiro, ultimo)
        if x not in lista:
            lista.append(x)
        if len(lista) == quantidade:
            lista.sort()
            cart.append(lista[:])
            lista.clear()
            break


# Função que transforma um numero inteiro e coloca em uma lista:
def inteiro(numero, cart):
    if numero.isnumeric():
        numero = int(numero)
        cart.append(numero)


# Iniciando o Programa:
while True:
    esc = 0
    print("-=-=-=- GERADOR DE BINGO -=-=-=-")
    print("1 - Gerar \n2 - Ver Banco de Dados \n3 - Iniciar Sorteio")
    esc = leiaint()

    if esc == 1:
        mostrar = False
        print("-=-=- ESCOLHA UM MOLDE -=-=-")
        print("1 - Em Branco \n2 - Personalizado")
        qual = leiaint()
        quant = leiaint("Quantidade de Cartelas: ")

        print("-=-=-=- NOME DO EVENTO -=-=-=-")
        nome_evento = str(input("Nome: "))
        diretorio_resultados = os.path.join(diretorio_principal, f"Cartelas-{nome_evento}")
        os.mkdir(diretorio_resultados)

        # Sorteando os números para a cartela
        while True:
            colbingo(b, 5, 1, 15, cartela)
            colbingo(i, 5, 16, 30, cartela)
            colbingo(n, 4, 31, 45, cartela)
            colbingo(g, 5, 46, 60, cartela)
            colbingo(o, 5, 61, 75, cartela)

            # Evitar cartelas repetidas:
            if cartela not in geral:
                geral.append(cartela[:])
                contador += 1
            else:
                quant += 1
            cartela.clear()
            if contador == quant:
                break

        # Formatando os numeros menores que 10 para que fiquem com duas casas decimais:
        for k in range(0, len(geral)):
            for col in range(0, len(geral[k])):
                for num in range(0, len(geral[k][col])):
                    if geral[k][col][num] < 10:
                        geral[k][col][num] = str(f'0{geral[k][col][num]}')
                    else:
                        geral[k][col][num] = str(geral[k][col][num])

            # Formatando em uma string para ser colocado no molde:
            tabela = (f'{geral[k][0][0]:<3} {geral[k][1][0]:<3} {geral[k][2][0]:<3} {geral[k][3][0]:<3} {geral[k][4][0]:<3} \n'
                      f'{geral[k][0][1]:<3} {geral[k][1][1]:<3} {geral[k][2][1]:<3} {geral[k][3][1]:<3} {geral[k][4][1]:<3} \n'
                      f'{geral[k][0][2]:<3} {geral[k][1][2]:<3}        {geral[k][3][2]:<3} {geral[k][4][2]:<3} \n'
                      f'{geral[k][0][3]:<3} {geral[k][1][3]:<3} {geral[k][2][2]:<3} {geral[k][3][3]:<3} {geral[k][4][3]:<3} \n'
                      f'{geral[k][0][4]:<3} {geral[k][1][4]:<3} {geral[k][2][3]:<3} {geral[k][3][4]:<3} {geral[k][4][4]:<3} \n')


            # Gerador com molde em Branco:
            if qual == 1:
                coord_paint = (5, 5)
                imagem = Image.open(diretorio_molde1)
                font1 = ImageFont.truetype(caminho_fonte, 68)
                desenho = ImageDraw.Draw(imagem)
                desenho.text(coord_paint, tabela, font=font1, fill=rgb_preto)

            # Gerador com molde Personalizado:
            if qual == 2:
                # Colocar bingo principal:
                coord_paint = (173, 525)
                imagem = Image.open(diretorio_molde2)
                font2 = ImageFont.truetype(caminho_fonte, 93)
                desenho = ImageDraw.Draw(imagem)
                desenho.text(coord_paint, tabela, font=font2, fill=rgb_preto)

                # Colocar cópia menor para conferência:
                coord_paint = (664, 996)
                font3 = ImageFont.truetype(caminho_fonte, 27)
                desenho = ImageDraw.Draw(imagem)
                desenho.text(coord_paint, tabela, font=font3, fill=rgb_preto)

                # Colocar o número da rifa
                coord_paint = (695, 365)
                font = ImageFont.truetype(caminho_fonte, 37)
                desenho = ImageDraw.Draw(imagem)
                k += 1
                k = str(k)
                if len(k) == 1:
                    k = f'000{k}'
                elif len(k) == 2:
                    k = f'00{k}'
                elif len(k) == 3:
                    k = f'0{k}'
                desenho.text(coord_paint, f'N° {k}', font=font, fill=rgb_branco)
                k = int(k)
                k -= 1

            # Salvando a imagem e mostrando
            imagem.save(fr'{diretorio_resultados}\{nome_evento}_N{k+1}.png')
            #imagem.show()

        # Gerando um txt para armazenar os dados (Nota: Não é a melhor forma para se armazenar dados, mas foi a forma que eu pensei na época que estava criando):
        # O txt vai armazenar uma string, com os números de todas as cartela
        try:
            a = open(arq, 'rt')
            a.close()
        except FileNotFoundError:
            a = open(arq, 'wt+')
            print('-=-' * 14)
            print(f'Arquivo {arq} criado com sucesso!')
            print('-=-' * 14)
        else:
            print('-=-' * 10)
            print('Arquivo de Dados Encontrado')
            print('-=-' * 10)
        a = open(arq, 'at')
        a.write(str(geral))
        a.close()
        break
        

    # Mostrar o banco de dados:
    if esc == 2:
        a = open(arq, 'rt')
        print(a.read())

    # Iniciando Sorteio
    if esc == 3:
        try:
            a = open(arq, 'rt')
            a.close()
        except FileNotFoundError:
            print('Arquivo Não Encontrado!')
        a = open(arq, 'rt')
        txt = a.read()

        posb1 = 4

        while True:
            # Interpretando o txt:
            posb2 = posb1 + 6
            posb3 = posb2 + 6
            posb4 = posb3 + 6
            posb5 = posb4 + 6

            posi1 = posb5 + 8
            posi2 = posi1 + 6
            posi3 = posi2 + 6
            posi4 = posi3 + 6
            posi5 = posi4 + 6

            posn1 = posi5 + 8
            posn2 = posn1 + 6
            posn3 = posn2 + 6
            posn4 = posn3 + 6

            posg1 = posn4 + 8
            posg2 = posg1 + 6
            posg3 = posg2 + 6
            posg4 = posg3 + 6
            posg5 = posg4 + 6

            poso1 = posg5 + 8
            poso2 = poso1 + 6
            poso3 = poso2 + 6
            poso4 = poso3 + 6
            poso5 = poso4 + 6

            if poso5 > len(txt):
                break

            b1 = f'{txt[posb1]}{txt[posb1 + 1]}'
            inteiro(b1, lcartela)
            b2 = f'{txt[posb2]}{txt[posb2 + 1]}'
            inteiro(b2, lcartela)
            b3 = f'{txt[posb3]}{txt[posb3 + 1]}'
            inteiro(b3, lcartela)
            b4 = f'{txt[posb4]}{txt[posb4 + 1]}'
            inteiro(b4, lcartela)
            b5 = f'{txt[posb5]}{txt[posb5 + 1]}'
            inteiro(b5, lcartela)

            i1 = f'{txt[posi1]}{txt[posi1 + 1]}'
            inteiro(i1, lcartela)
            i2 = f'{txt[posi2]}{txt[posi2 + 1]}'
            inteiro(i2, lcartela)
            i3 = f'{txt[posi3]}{txt[posi3 + 1]}'
            inteiro(i3, lcartela)
            i4 = f'{txt[posi4]}{txt[posi4 + 1]}'
            inteiro(i4, lcartela)
            i5 = f'{txt[posi5]}{txt[posi5 + 1]}'
            inteiro(i5, lcartela)

            n1 = f'{txt[posn1]}{txt[posn1 + 1]}'
            inteiro(n1, lcartela)
            n2 = f'{txt[posn2]}{txt[posn2 + 1]}'
            inteiro(n2, lcartela)
            n3 = f'{txt[posn3]}{txt[posn3 + 1]}'
            inteiro(n3, lcartela)
            n4 = f'{txt[posn4]}{txt[posn4 + 1]}'
            inteiro(n4, lcartela)

            g1 = f'{txt[posg1]}{txt[posg1 + 1]}'
            inteiro(g1, lcartela)
            g2 = f'{txt[posg2]}{txt[posg2 + 1]}'
            inteiro(g2, lcartela)
            g3 = f'{txt[posg3]}{txt[posg3 + 1]}'
            inteiro(g3, lcartela)
            g4 = f'{txt[posg4]}{txt[posg4 + 1]}'
            inteiro(g4, lcartela)
            g5 = f'{txt[posg5]}{txt[posg5 + 1]}'
            inteiro(g5, lcartela)

            o1 = f'{txt[poso1]}{txt[poso1 + 1]}'
            inteiro(o1, lcartela)
            o2 = f'{txt[poso2]}{txt[poso2 + 1]}'
            inteiro(o2, lcartela)
            o3 = f'{txt[poso3]}{txt[poso3 + 1]}'
            inteiro(o3, lcartela)
            o4 = f'{txt[poso4]}{txt[poso4 + 1]}'
            inteiro(o4, lcartela)
            o5 = f'{txt[poso5]}{txt[poso5 + 1]}'
            inteiro(o5, lcartela)

            lgeral.append(lcartela[:])
            lcartela.clear()

            posb1 += 156

        sorteados.clear()
        conferir.clear()
        conferir = lgeral[:]

        while True:
            while True:
                z = leiaint('N° Sorteado: ')
                if 75 >= z >= 1:
                    break
                else:
                    print('Número Inválido!')
            if z not in sorteados:
                sorteados.append(z)
                sorteados.sort()
                print('-=-' * (5 + len(sorteados)))
                print(f'Números sorteados: \n{sorteados}')
                for pos in range(0, len(lgeral)):
                    if z in conferir[pos]:
                        conferir[pos].remove(z)
                        pontuou.append(pos + 1)
                        if len(conferir[pos]) == 0:
                            if conferir[pos] not in ganhadores:
                                print(f'A cartela número {pos + 1} Ganhou!')
                        if len(conferir[pos]) == 1:
                            print(f'A cartela {pos + 1} está somente com 1 número')
                pontuou.sort()
                print(f'As cartelas {pontuou} pontuaram')
                pontuou.clear()
                print('-=-' * (5 + len(sorteados)))
            else:
                print('Esse Número Já Foi Sorteado!')
