n1 = float(input("Entre com a nota 1: "))
n2 = float(input("Entre com a nota 2: "))
n3 = float(input("Entre com a nota 3: "))
n4 = float(input("Entre com a nota 4: "))

MA= (n1+n2+n3+n4)/4

print("A sua nota final foi", MA)

if MA <3:
  print("Vc foi reprovado")

else: 
  if MA <=7:
    print("Vc foi aprovado")

  else:
      print("AF")

print("fim da media")