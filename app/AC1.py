class Matematica:


#Exercício 01
#Faça uma função que efetua o cálculo do salário líquido de um professor. Os dados fornecidos serão: valor hora aula, número de aulas dadas e o percentual de desconto do INSS.
    def salario_liquido(nmr_aulas, vlr_hora, inss):
        aulas = int(nmr_aulas)
        valor = float(vlr_hora)
        desconto = float(inss)
        desconto_total = aulas * valor * (desconto / 100)
        salario_final = aulas * valor - desconto_total
        return round(salario_final, 2)


#Exercício 02
#Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto aos clientes. Faça uma função que receba um valor de um produto e devolva um novo valor tendo em vista que o desconto foi de 9%.
    def DescontoDoProduto(vlr_produto):
        valor = float(vlr_produto)
        desconto = (9 / 100) * valor
        novoValor = valor - desconto
        return (novoValor, desconto)
    

#Exercício 03
#Faça uma função que leia dois números reais, um será o valor de um produto e o outro o valor do desconto que esse produto está recebendo. Devolva quantos reais o produto custa na promoção.
    def ValorPromocao(vlr_original, descont):
        valor = float(vlr_original)
        desconto = float(descont)
        return valor - desconto


#Exercício 04
#Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% de comissão para o garçom. Faça uma função que receba o valor gasto com despesas realizadas em um restaurante e devolva o valor total da conta e o valor da gorjeta. 
    def ValorTotal(vlr_despesa):
        valorDespesa = float(vlr_despesa)
        valorGorjeta = float(valorDespesa / 10)
        valorTotal = valorDespesa + valorGorjeta
        return round(valorTotal, 2), round(valorGorjeta, 2)



    






    



