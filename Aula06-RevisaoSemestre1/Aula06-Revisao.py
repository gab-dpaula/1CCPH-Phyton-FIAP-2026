

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


# função qur valida na lista de requisições se tem dois erros seguidos

def erros_seguidos(respostas_http):
    for i in range(len(respostas_http) - 1):
        codigo_atual = respostas_http[i]
        prox_codigo = respostas_http[i + 1]

        if not ver_sucesso(codigo_atual) and not ver_sucesso(prox_codigo):
            return True
    return False

def analisar_endpoint(respostas_http):
    quantidade_sucessos = 0

    for cod_http in respostas_http:
        if ver_sucesso(cod_http):
            quantidade_sucessos += 1

    qtd_total_req = len(respostas_http)
    quantidade_erros = qtd_total_req - quantidade_sucessos

    percentual_sucessos = quantidade_sucessos / qtd_total_req * 100

    tem_erros_seguidos = erros_seguidos(respostas_http)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucessos >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return(quantidade_sucessos, quantidade_erros, percentual_sucessos, classificacao)

# Percorrendo toda a matriz

maior_qtd_erros = -1
endpoin_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    respostas_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(respostas_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Respostas http: {respostas_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucessos: {percentual}")
    print(f"Classificacao: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        endpoint_maior_erro = erros
        emdpoint_maior_erro = nome_endpoint

    print(f"Endpoint com mais erros é: {endpoint_maior_erro} ({maior_qtd_erros} erros)")