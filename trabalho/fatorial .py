
# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)

# ---------------------------------------------

def test_factorial(Numero):

    NumeroRecebido = Numero
    Resultado = Numero

     while NumeroRecebido >1:
     Resultado*= NumeroRecebido -1
     NumeroRecebido -=1

         return Resultado
