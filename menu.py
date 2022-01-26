def adicionar_livro(lista):  
  titulo = input('Título : ').strip()
  titulo = titulo.lower()
  quantidade = int(input('quantidade : '))
  lista[titulo] = quantidade
  return lista

def remover_livro(lista):
  titulo = input('Título : ').strip()
  titulo = titulo.lower()
  if titulo in lista:
      resposta = input(f'Você tem certeza que deseja remover {titulo}? ')
      if resposta == 'sim':
        del lista[titulo]
      else:
        return lista
  else:
    print('Livro não encontrado.')
    return lista


  return lista

def alterar_livro(lista):
  titulo = input('Título : ').strip()
  titulo = titulo.lower()
  if titulo in lista:
    print(f'Quantidade atual: {lista[titulo]}')
  else:
    print('Livro não encontrado.')
  try:
    novaquantidade = int(input('Nova quantidade : '))
  except: print('Digite um valor válido')
  else: lista[titulo] = novaquantidade
  return lista

def listar_livros(lista):
  # Formatação para impressão
  print(f'{"Título".ljust(20)} Quantidade')
  # Laço para impressão do dicionário
  for k, v in lista.items():
      print(f'{k.ljust(25)} {v}')

  input()   # Após imprimir a lista clique em enter para que o programa continue a execução
  return lista
 

def menu(lista):

  #Adicionar nas opções a opção para listar
  print('-=-=-=-=-=-=-=-=-=-=-=')
  print(f'{"MENU".rjust(13)}')
  print('-=-=-=-=-=-=-=-=-=-=-=')
  print('1-Adicionar Livro')
  print('2-Remover livro')
  print('3-Alterar estoque')
  print('4-Listar Livros')

  escolha_menu = input("Escolha: ").strip()

  if escolha_menu == '1':
    return adicionar_livro(lista)  
  elif escolha_menu == '2':
    return remover_livro(lista)
  elif escolha_menu == '3':
    return alterar_livro(lista)
  elif escolha_menu == '4':
    return listar_livros(lista)
  elif escolha_menu == 's':
    return True
  else: 
    print('Você não informou um comando correto.')
    return lista