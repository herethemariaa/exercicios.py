contacts_list = []

while True:
    print("====== LISTA DE CONTATOS ======")
    
    name_var = str(input("Nome Completo: "))
    tell_var = str(input("Telefone: "))
    email_var = str(input("E-mail: "))
    
    contact = {
        "name": name_var,
        "tellphone": tell_var,
        "email": email_var
    }
    
    contacts_list.append(contact)
    
    next = input("Deseja adicionar mais um contato? (Escreva 'S' para Sim e 'N' para Não): ").lower()
    
    if next != 's':
        break
    
print("\nContatos cadastrados:")
for contato in contacts_list:
    print(contato)