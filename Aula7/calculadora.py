import math

from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if num1 < 0 and operacao == "sqrt" // operacao == "log":
        resultado = "Erro: número negativo"
        etapas = f"Não há possibiidade de calcular com {num1}."
    else:
        num2_valor = request.form.get("num2", "").strip()
        if operacao != "sqrt" and operacao != "log" and not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        
        num2 = float(num2_valor)

        match operacao:
            case "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"
                return etapas 
            case "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"
                return etapas 
            case "*":
                resultado = num1 * num2
                etapas = f"{num1} * {num2} = {resultado}"
                return etapas 
            case "/":
                if num2 != 0:
                    resultado = num1 / num2
                    etapas = f"{num1} / {num2} = {resultado}"
                else:
                    resultado = "Erro: Divisão por zero"
                    etapas = "Não é possível dividir por zero."
                return etapas 
            case "**":
                resultado = num1 ** num2
                etapas = f"{num1} ** {num2} = {resultado}"
                return etapas 
            case "log":
                resultado = round(math.log(num1, 10),2)
                etapas = f"{num1} = {resultado}"
                return etapas 
            case "sqrt":
                resultado = round(math.sqrt(num1), 2) 
                etapas = f"√{num1} = {resultado}"
                return etapas 

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)