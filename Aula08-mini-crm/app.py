import control

from model import model_lead


def add_lead():
    name = input("Nome: ")
    company = input("Company: ")
    email = input("Email: ")
    stage = input("Stage: ")

    if not name or not email or "@" not in email:
        print("Nome e/ou e-mail inválidos")
        return

    print(name, company, email, stage)
    # precisar chamar model para modelar os dados

    print(model_lead(name, company, email, stage))

    # depois de modelado...
    # vou precisar chamar o model
    control.create_lead(model_lead(name, company, email, stage))

def list_leads():
    leads = control.read_leads()

    if not leads:
        print("Nenhum lead ainda")
        return

    print("\n# |  Nome  |   Empresa |   E-mail  ")
    for i, lead in enumerate(leads):
        print(f"{i:02d}| {lead['name']:<15} | {lead['company']:<15} | {lead['email']:<15}")

def search_leads():
    query = input("Buscar por:").strip().lower()

    if not query:
        print("Consulta vazia")
        return

    # Vamos enviar a busca para o control.py
    # o control.read_leads_search() irá retornar um array com os leads encontrados
    leads_finded = control.read_leads_search(query)

    print(f"\n# | {"Nome": <15} | {"Empresa": <15} | {"E-mail": <15} ")
    for i, lead in enumerate(leads_finded):
        print(f"{i:02d}| {lead['name']:<15} | {lead['company']:<15} | {lead['email']:<15}")


def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi posível exportar os leads para o CSV")
    else:
        print(F"CSV exportado para: {path_csv}")



def main():
    while True:
        print("\nMini CRM - Aula 01 - (adicionar\listar)")
        print("[1] - Adicionar lead")
        print("[2] - Listar leads")
        print("[3] - Buscar (nome/e-mail/empresa)")
        print("[4] - Exportar para CSV")
        print("[0] - Sair do programa")

        opt = input("Escolha uma ação: ").strip()
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
