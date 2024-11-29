import requests

BASE_URL = "http://127.0.0.1:5000/api/bus"

def display_menu():
    print("\n=== Menu ===")
    print("1. Consultar status do ônibus")
    print("2. Adicionar pessoas ao ônibus")
    print("3. Remover pessoas do ônibus")
    print("0. Sair")

def get_bus_status():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        print("\n=== Status do Ônibus ===")
        print(f"Número: {data['busInfo']['busNumber']}")
        print(f"Linha: {data['busInfo']['busLine']}")
        print(f"Lugares ocupados: {data['busLotation']}")
        print(f"Status: {data['status']}")
    else:
        print("\nErro ao consultar status do ônibus.")

def update_bus_lotation(change):
    response = requests.post(BASE_URL, json={"resert": change})
    if response.status_code == 200:
        data = response.json()
        print("\n=== Atualização ===")
        print(data["message"])
        print(f"Lugares ocupados: {data['busLotation']}")
        print(f"Status: {data['status']}")
    else:
        print("\nErro ao atualizar lotação do ônibus.")
        print(response.json().get("error", "Erro desconhecido"))

def main():
    while True:
        display_menu()
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            get_bus_status()
        elif choice == "2":
            try:
                change = int(input("Quantas pessoas adicionar? "))
                if change > 0:
                    update_bus_lotation(change)
                else:
                    print("Por favor, insira um número positivo.")
            except ValueError:
                print("Entrada inválida. Insira um número inteiro.")
        elif choice == "3":
            try:
                change = int(input("Quantas pessoas remover? "))
                if change > 0:
                    update_bus_lotation(-change)
                else:
                    print("Por favor, insira um número positivo.")
            except ValueError:
                print("Entrada inválida. Insira um número inteiro.")
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
