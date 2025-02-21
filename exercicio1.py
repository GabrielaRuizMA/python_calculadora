# -*- coding: utf-8 -*-
"""Exercicio1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ywI8xCtmUx74_y7VkccIcZt4RvvX3pfV
"""

# Exibe opções ao usuário
print("Calculadora Financeira")
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

# Entrada da operação
operacao = input("Digite o número da operação desejada: ")

# Se a opção não for válida, exibe erro e encerra
if operacao not in ["1", "2", "3", "4", "5"]:
    print("Opção inválida. Reinicie o programa e escolha uma opção de 1 a 5.")
else:
    # Se a opção for "5", sai do programa
    if operacao == "5":
        print("Saindo...")
    else:
        # Entrada dos números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Executa a operação escolhida
        if operacao == "1":
            resultado = num1 + num2
            print(f"Resultado da soma: {resultado:.2f}")
        elif operacao == "2":
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado:.2f}")
        elif operacao == "3":
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado:.2f}")
        elif operacao == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado:.2f}")
            else:
                print("Erro: divisão por zero não é permitida.")