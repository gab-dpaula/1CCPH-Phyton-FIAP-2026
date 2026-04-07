# programa para a leitura de quatro notas parciais de um aluno.

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))

media_final = (nota1 + nota2 + nota3 + nota4) / 4
if media_final >= 7:
    print(f'Aluno aprovado.')
elif 5 <= media_final < 7:
    print(f'Aluno em recuperação.')
else:
    print(f'Aluno reprovado.')