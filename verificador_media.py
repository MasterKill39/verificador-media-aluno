while True:
   NomeAluno = input("Entre com o nome do aluno: ")
   n1 = float(input("Entre com a nota 1: "))
   n2 = float(input("Entre com a nota 2: "))
   n3 = float(input("Entre com a nota 3: "))
   n4 = float(input("Entre com a nota 4: "))
   MA= (n1+n2+n3+n4)/4
   print("A sua nota final foi", MA)
   if MA <=3:
     print("Voce foi reprovado")
   else:
     MA >=7
     print("Voce foi aprovado")
     op=input("Mais aluno(s) (S/N)")
     if op.upper()=='S':
      continue
     else:
       break
print("Fim da média")