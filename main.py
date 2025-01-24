import os
import sys
import logging as logger


logger.basicConfig(filename='log.log', level=logger.DEBUG, encoding='utf-8', format='%(asctime)s - %(levelname)s || %(message)s')


def read_file(path:str):
  '''
  Função que trata a leitura do arquivo, e, caso o mesmo exista no caminho passado, retorna o texto contido no mesmo.
  '''

  if not os.path.exists(path):
    raise FileNotFoundError('Arquivo não encontrado, favor verificar se o caminho passado está correto.')

  try:
    with open(path, 'r') as f:
        file_text = f.read()
  except Exception as e:
    logger.error(f'ERRO INESPERADO!!\n\n{e}')
    raise Exception('Ocorreu um erro inesperado durante a execução do problema.')
  return file_text.replace('.', '').replace(',', '').replace('\n',' ').replace('  ', ' ').strip()


def count_words_in_str_to_dict(string:str):
  '''
  Cria um dicionário com as palavras existentes no texto e conta quantas vezes cada palavra aparece
  '''

  words_dict = {}
  split_file_text = string.split(' ')
  for word in split_file_text:
    if word == '':
      continue
    if word in words_dict:
      words_dict[word] += 1
    else:
      words_dict[word] = 1
  return words_dict


def create_sorted_words_report(file_name:str, words_dict:dict):
  '''
  Cria o arquivo de relatório e escreve nele o total de palavras encontradas em cada arquivo e 
  cada palavra do arquivo seguida da quantidade de repetições ordenadas da maior quantidade para a menor.
  '''

  with open('relatório.txt', 'w', encoding='utf-8') as f:
    f.write(f'Relatório do arquivo {file_name}.\n\n')
    total_words = 0
    while len(words_dict) > 0:
      most_frequent = ('', 0)
      for word, count in words_dict.items():
        if most_frequent[0] == '' or most_frequent[1] < count:
          most_frequent = (word, count)
      f.write(f'"{most_frequent[0]}": {most_frequent[1]}\n')
      total_words += most_frequent[1]
      words_dict.pop(most_frequent[0])
    f.write(f'\n\nNÚMERO TOTAL DE PALAVRAS NO ARQUIVO: {total_words}')


def main():
  # Verificando se o número de argumentos passados está correto
  if len(sys.argv) != 2:
    print('Não foi indicado qual o caminho para o arquivo a ser analisado.')
    return
  
  path = sys.argv[1]
  file_name = path.split('/')[-1]
  print(f'Analisando o arquivo {file_name}')

  # Tratando os caracteres especiais que não fazem parte de nenhuma palavra
  file_text = read_file(path)
  
  words_dict = count_words_in_str_to_dict(file_text)
    
  create_sorted_words_report(file_name, words_dict)
  

if __name__ == '__main__':
  main()