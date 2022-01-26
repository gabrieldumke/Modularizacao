import requests
import replit
from menu import menu


def sistema():
    lista_livros = dict()
    while True:
      retorno = menu(lista_livros)
      replit.clear()  # comando para apagar console
      if retorno is True:
        return
    else:
        lista_livros = retorno


sistema()