

endpoints = ["/login", "/produtos", "/pedidos"]

status = [
    [200,200,401,200,500],
    [200,200,200,200,200],
    [201,500,502,201,500]
]


# função para detectar se um status é sucesso

def ver_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

print(ver_sucesso(status [0][1]))


# função para contar requisicoes validas e falhas

def contar_requisicoes(codigo):
    sucessos = 0
    falhas = 0

    for codigo in codigo:
        if 200 <= codigo <= 299:
            sucessos += 1
        else:
            falhas += 1
    return sucessos, falhas

sucessos, falhas = contar_requisicoes()