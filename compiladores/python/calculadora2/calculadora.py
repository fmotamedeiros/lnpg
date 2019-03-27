import sys

def calcular(tokens):
  if len(tokens) == 3:
    if tokens[0][1] == 'DÍGITO' and tokens[1][1] == 'DÍGITO' and tokens[2][1] == 'SOMA':
      return int(tokens[0][0]) + int(tokens[1][0])
    
    if tokens[0][1] == 'DÍGITO' and tokens[1][1] == 'DÍGITO' and tokens[2][1] == 'SUB':
      return int(tokens[0][0]) - int(tokens[1][0])
    
    if tokens[0][1] == 'DÍGITO' and tokens[1][1] == 'DÍGITO' and tokens[2][1] == 'MULT':
      return int(tokens[0][0]) * int(tokens[1][0])
    
    if tokens[0][1] == 'DÍGITO' and tokens[1][1] == 'DÍGITO' and tokens[2][1] == 'DIVI':
      return int(tokens[0][0]) / int(tokens[1][0])

  sys.stderr.write('Problema no programa')
  sys.exit(1)