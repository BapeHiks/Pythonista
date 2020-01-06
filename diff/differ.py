import argparse
import difflib
import hashlib
from sys import argv
import webbrowser

def diff(from_, to_, wrap_col):
  '''
   Создайте diff и запишите его в файл, чтобы его можно было открыть в браузере.
  '''
   # Так как from_ и to_ приходят как списки слов, нам нужно
   # собрать их обратно в предложения, а затем
   # разбить на разрывы строк, чтобы получить список строк для сравнения.
  from_ = ' '.join(from_).splitlines()
  to_ = ' '.join(to_).splitlines()
  
  delta_html = difflib.HtmlDiff(wrapcolumn=wrap_col).make_file(from_, to_, fromdesc='from text', todesc='to text')
  
  with open('diff_table.html', 'w') as file:
    file.write(delta_html)

  webbrowser.open('diff_table.html')

def parse_input(data):
  '''
  Parse input from Drafts command-line-like.
  '''
  parser = argparse.ArgumentParser(description='diff two texts.')

  parser.add_argument('-f', '--f', '-from', '--from',
                        dest='from_',
                        metavar='STRING',
                        nargs='+',
                        help='the first text to compare')

  parser.add_argument('-t', '--t', '-to', '--to',
                        dest='to_',
                        metavar='STRING',
                        nargs='+',
                        help='the second text to compare')
    
  parser.add_argument('-wc', '--wc', '-wrapcolumn', '--wrapcolumn',
                        dest='wrap_col',
                        default=50,
                        metavar='INT',
                        type=int,
                        help='number of characters each column in diff should wrap to')
                        
  args = parser.parse_args(data)
  diff(args.from_, args.to_, args.wrap_col)
 
if __name__ == '__main__':
  parse_input(argv[1].split(' '))
