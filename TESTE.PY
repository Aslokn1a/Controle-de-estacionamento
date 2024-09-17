import numpy as np
import random

# Inicializar o estacionamento
def inicializar_estacionamento():
    setor_a = np.full(5, None)  # Setor A com 5 vagas
    setor_b = np.full(5, None)  # Setor B com 5 vagas
    setor_c = np.full(5, None)  # Setor C com 5 vagas
    return setor_a, setor_b, setor_c

# Função para encontrar um setor específico
def escolher_setor(setor):
    setores = {
        'A': setor_a,
        'B': setor_b,
        'C': setor_c
    }
    return setores.get(setor.upper())

# Função para ocupar uma vaga
def ocupar_vaga(setor_a, setor_b, setor_c, placa):
    for setor in [setor_a, setor_b, setor_c]:
        if placa in setor:
            print("O veículo já está estacionado.")
            return False
    
    setor = random.choice([setor_a, setor_b, setor_c])
    vagas_livres = np.where(setor == None)[0]
    
    if len(vagas_livres) == 0:
        print("Não há vagas disponíveis.")
        return False
    
    vaga_escolhida = random.choice(vagas_livres)
    setor[vaga_escolhida] = placa
    print(f"Veículo {placa} estacionado na vaga {vaga_escolhida}.")
    return True

# Função para liberar uma vaga
def liberar_vaga(setor_a, setor_b, setor_c, placa):
    for setor in [setor_a, setor_b, setor_c]:
        if placa in setor:
            vaga_ocupada = np.where(setor == placa)[0][0]
            setor[vaga_ocupada] = None
            print(f"Veículo {placa} removido da vaga {vaga_ocupada}.")
            return True
    
    print("Veículo não encontrado.")
    return False

# Função para exibir vagas disponíveis
def exibir_vagas(setor_a, setor_b, setor_c):
    def vagas_disponiveis(setor):
        vagas = np.where(setor == None)[0]
        return len(vagas)
    
    print("Vagas disponíveis por setor:")
    print(f"Setor A: {vagas_disponiveis(setor_a)}")
    print(f"Setor B: {vagas_disponiveis(setor_b)}")
    print(f"Setor C: {vagas_disponiveis(setor_c)}")

# Função para consultar veículo estacionado
def consultar_veiculo(setor_a, setor_b, setor_c, placa):
    for setor in [setor_a, setor_b, setor_c]:
        if placa in setor:
            print(f"Veículo {placa} está estacionado.")
            return
    print(f"Veículo {placa} não está estacionado.")

# Função principal
def main():
    setor_a, setor_b, setor_c = inicializar_estacionamento()
    
    # Exemplo de uso
    while True:
        print("\nMenu:")
        print("1. Ocupação de vaga")
        print("2. Liberação de vaga")
        print("3. Exibir vagas disponíveis")
        print("4. Consultar veículo")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            placa = input("Digite a placa do veículo: ")
            ocupar_vaga(setor_a, setor_b, setor_c, placa)
        elif escolha == '2':
            placa = input("Digite a placa do veículo: ")
            liberar_vaga(setor_a, setor_b, setor_c, placa)
        elif escolha == '3':
            exibir_vagas(setor_a, setor_b, setor_c)
        elif escolha == '4':
            placa = input("Digite a placa do veículo: ")
            consultar_veiculo(setor_a, setor_b, setor_c, placa)
        elif escolha == '5':
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
