"""
Cifra de César + Criptoanálise por frequência de letras
DCC075 - Segurança em Sistemas de Computação

Menu interativo:
  1) Encriptar     -> C = (p + k) mod 26
  2) Decriptar     -> p = (C - k) mod 26
"""

import string
import unicodedata

ALFABETO = string.ascii_lowercase  # a..z  ->  0..25

# Frequências (%) de cada letra, conforme Wikipédia:
# https://pt.wikipedia.org/wiki/Frequência_de_letras
FREQ_PT = {
    "a": 14.63, "b": 1.04, "c": 3.88, "d": 4.99, "e": 12.57, "f": 1.02,
    "g": 1.30, "h": 1.28, "i": 6.18, "j": 0.40, "k": 0.02, "l": 2.78,
    "m": 4.74, "n": 5.05, "o": 10.73, "p": 2.52, "q": 1.20, "r": 6.53,
    "s": 7.81, "t": 4.34, "u": 4.63, "v": 1.67, "w": 0.01, "x": 0.21,
    "y": 0.01, "z": 0.47,
}
FREQ_EN = {
    "a": 8.167, "b": 1.492, "c": 2.782, "d": 4.253, "e": 12.702, "f": 2.228,
    "g": 2.015, "h": 6.094, "i": 6.966, "j": 0.153, "k": 0.772, "l": 4.025,
    "m": 2.406, "n": 6.749, "o": 7.507, "p": 1.929, "q": 0.095, "r": 5.987,
    "s": 6.327, "t": 9.056, "u": 2.758, "v": 0.978, "w": 2.360, "x": 0.150,
    "y": 1.974, "z": 0.074,
}


# ----------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------
def remover_acentos(texto):
    """'ação' -> 'acao'. A cifra trabalha só com as 26 letras a-z."""
    decomposto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in decomposto if unicodedata.category(c) != "Mn")


def ler_inteiro_positivo(mensagem):
    """Pergunta até o usuário digitar um inteiro >= 1."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit() and int(entrada) >= 1:
            return int(entrada)
        print("  Valor inválido. Digite um número inteiro maior ou igual a 1.")


def ler_texto(mensagem):
    """Pergunta até o usuário digitar algo."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("  O texto não pode ser vazio.")


# ----------------------------------------------------------------------
# Parte 1: Cifra de César
# ----------------------------------------------------------------------
def deslocar(texto, k):
    """Desloca cada letra do texto em k posições (k negativo = decriptar).

    - Letras: C = (p + k) mod 26
    - Espaços, números e pontuação ficam como estão.
    """
    resultado = []
    for caractere in remover_acentos(texto).lower():
        if caractere in ALFABETO:
            p = ALFABETO.index(caractere)   # letra -> número (a=0 ... z=25)
            c = (p + k) % 26                # fórmula da cifra
            resultado.append(ALFABETO[c])   # número -> letra
        else:
            resultado.append(caractere)
    return "".join(resultado)


def encriptar(texto, k):
    return deslocar(texto, k).upper()   # criptograma em maiúsculas (como nos slides)


def decriptar(criptograma, k):
    return deslocar(criptograma, -k)    # p = (C - k) mod 26


# ----------------------------------------------------------------------
# Menu interativo
# ----------------------------------------------------------------------
def menu():
    print("=" * 50)
    print("   CIFRA DE CÉSAR - encriptação e criptoanálise")
    print("=" * 50)

    while True:
        print("\nO que deseja fazer?")
        print("  1) Encriptar um texto")
        print("  2) Decriptar um texto (conhecendo a chave)")
        print("  0) Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            texto = ler_texto("\nTexto claro: ")
            k = ler_inteiro_positivo("Deslocamento k (1 a N): ")
            if k % 26 == 0:
                print("  Atenção: k múltiplo de 26 não altera o texto!")
            print(f"Criptograma: {encriptar(texto, k)}")

        elif opcao == "2":
            texto = ler_texto("\nCriptograma: ")
            k = ler_inteiro_positivo("Deslocamento k usado na encriptação: ")
            print(f"Texto claro: {decriptar(texto, k)}")

        elif opcao == "0":
            print("Até mais!")
            break

        else:
            print("  Opção inválida.")


if __name__ == "__main__":
    menu()