#!/bin/bash

echo "Escolha uma operação:"
echo "1. Adição"
echo "2. Subtração"
echo "3. Multiplicação"
echo "4. Divisão"

# Coletar os números
read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

# Coletar a operação desejada
read -p "Escolha a operação (1/2/3/4): " op

# Realizar a operação
case $op in
  1)
    resultado=$((num1 + num2))
    echo "Resultado da adição: $resultado"
    ;;
  2)
    resultado=$((num1 - num2))
    echo "Resultado da subtração: $resultado"
    ;;
  3)
    resultado=$((num1 * num2))
    echo "Resultado da multiplicação: $resultado"
    ;;
  4)
    if [ $num2 -ne 0 ]; then
      resultado=$((num1 / num2))
      echo "Resultado da divisão: $resultado"
    else
      echo "Erro: Divisão por zero não permitida."
    fi
    ;;
  *)
    echo "Opção inválida."
    ;;
esac
