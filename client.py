import requests

BASE_URL = "http://127.0.0.1:5000/api/bus"

class Command:
    def execute(self):
        pass

class GetBusStatusCommand(Command):
    def execute(self):
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            data = response.json()
            print("\n=== Status do Ônibus ===")
            print(f"Número: {data['busInfo']['busNumber']}")
            print(f"Linha: {data['busInfo']['busLine']}")
            print(f"Lugares ocupados: {data['busLotation']}")
            print(f"Status: {data.get('status', 'Indisponível')}")
        else:
            print("\nErro ao consultar status do ônibus.")

class UpdateBusLotationCommand(Command):
    def __init__(self, change):
        self.change = change

    def execute(self):
        response = requests.post(BASE_URL, json={"resert": self.change})
        if response.status_code == 200:
            data = response.json()
            print("\n=== Atualização ===")
            print(data["message"])
            print(f"Lugares ocupados: {data['busLotation']}")
            print(f"Status: {data.get('status', 'Indisponível')}")
        else:
            print("\nErro ao atualizar lotação do ônibus.")
            print(response.json().get("error", "Erro desconhecido"))

class Menu:
    def __init__(self):
        self.commands = {
            "1": GetBusStatusCommand().execute,
            "2": self.add_people,
            "3": self.remove_people
        }

    def display(self):
        print("\n=== Menu ===")
        print("1. Consultar status do ônibus")
        print("2. Adicionar pessoas ao ônibus")
        print("3. Remover pessoas do ônibus")
        print("0. Sair")

    def handle_input(self, choice):
        if choice in self.commands:
            self.commands[choice]()
            return True
        return False

    def add_people(self):
        try:
            change = int(input("Quantas pessoas adicionar? "))
            if change > 0:
                UpdateBusLotationCommand(change).execute()
            else:
                print("Por favor, insira um número positivo.")
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")

    def remove_people(self):
        try:
            change = int(input("Quantas pessoas remover? "))
            if change > 0:
                UpdateBusLotationCommand(-change).execute()
            else:
                print("Por favor, insira um número positivo.")
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")

def main():
    menu = Menu()
    while True:
        menu.display()
        choice = input("Escolha uma opção: ")
        if choice == "0":
            print("Saindo...")
            break
        if not menu.handle_input(choice):
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
