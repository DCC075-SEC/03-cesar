# Cifra de César em Python

Projeto desenvolvido para a disciplina **DCC075 — Segurança em Sistemas de Computação**, com o objetivo de estudar a Cifra de César, uma técnica clássica de criptografia por substituição.

## 📌 Sobre o projeto

A Cifra de César é um método de criptografia que substitui cada letra de uma mensagem por outra letra deslocada um número fixo de posições no alfabeto.

Por exemplo, considerando um deslocamento de `3` posições:

| Letra original | Letra cifrada |
| -------------- | ------------- |
| A              | D             |
| B              | E             |
| C              | F             |
| X              | A             |
| Y              | B             |
| Z              | C             |

Quando o deslocamento chega ao final do alfabeto, a contagem retorna ao início. Esse comportamento é realizado por meio da operação módulo 26, considerando as 26 letras do alfabeto inglês.

O programa permite:

- **Encriptar:** transformar um texto original em um criptograma.
- **Decriptar:** recuperar o texto original **conhecendo a chave utilizada.**
- **Sair:** encerrar a execução do programa.

## ⚙️ Como funciona

### 1. Encriptação

A encriptação utiliza a fórmula:

[
C = (p + k) \bmod 26
]

Onde:

- (C): posição da letra cifrada.
- (p): posição da letra original.
- (k): chave de deslocamento.
- (26): quantidade de letras do alfabeto.

Cada letra é representada por um número entre 0 e 25, em que `a = 0`, `b = 1`, ..., `z = 25`.

**Exemplo:** encriptar `CASA` com chave `3`.

- C → F
- A → D
- S → V
- A → D

Resultado: `FDVD`.

### 2. Decriptação

A decriptação utiliza a fórmula inversa:

[
p = (C - k) \bmod 26
]

Ela desfaz o deslocamento aplicado durante a encriptação.

**Exemplo:** decriptar `FDVD` com chave `3`.

Resultado: `casa`.

### 3. Tratamento dos caracteres

A implementação possui algumas regras:

- Letras acentuadas são convertidas para suas versões sem acento. Por exemplo, `ação` torna-se `acao`.
- A encriptação transforma o resultado em letras maiúsculas.
- A decriptação retorna o resultado em letras minúsculas.
- Espaços, números e sinais de pontuação são preservados.
- A chave pode ser um inteiro positivo maior ou igual a 1.
- Chaves múltiplas de 26 não alteram as letras, pois representam deslocamentos completos pelo alfabeto.

**Importante:** o programa converte todas as letras para um padrão de caixa. Portanto, ele não preserva a diferença entre maiúsculas e minúsculas do texto original.

## 💻 Requisitos

- Python 3 instalado.
- Terminal, Prompt de Comando ou PowerShell.
- Editor de código opcional, como PyCharm ou Visual Studio Code.

O programa utiliza apenas bibliotecas da própria instalação do Python, não sendo necessária a instalação de dependências externas.

## 🚀 Como executar

### 1. Entre na pasta do projeto

```bash
cd NOME_DA_PASTA
```

Substitua `NOME_DA_PASTA` pelo nome da pasta que contém o arquivo Python.

### 2. Execute o programa

Se o arquivo se chamar `cifra_cesar.py`, utilize:

**Windows:**

```bash
python cifra_cesar.py
```

Se o comando `python` não funcionar, tente:

```bash
py cifra_cesar.py
```

**Linux ou macOS:**

```bash
python3 cifra_cesar.py
```

### 4. Utilize o menu interativo

Ao executar o programa, será exibido um menu semelhante a este:

```text
==================================================
   CIFRA DE CÉSAR - encriptação e criptoanálise
==================================================

O que deseja fazer?
  1) Encriptar um texto
  2) Decriptar um texto (conhecendo a chave)
  0) Sair
Opção:
```

Digite o número correspondente à operação desejada.

## 🧪 Exemplos de execução

### Exemplo 1 — Encriptação

```text
Opção: 1

Texto claro: CASA
Deslocamento k (1 a N): 3
Criptograma: FDVD
```

### Exemplo 2 — Decriptação

```text
Opção: 2

Criptograma: FDVD
Deslocamento k usado na encriptação: 3
Texto claro: casa
```

### Exemplo 3 — Texto com espaços e pontuação

Entrada:

```text
Texto claro: Ola, mundo!
Deslocamento k (1 a N): 3
```

Saída:

```text
Criptograma: ROD, PXQGR!
```

Os espaços e os sinais de pontuação permanecem inalterados.






