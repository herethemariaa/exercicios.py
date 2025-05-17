#Lógica em Python de uma lista de alunos com suas respectivas notas, utilizando os dicionários:

list_students = []

while True:
    print("====== PORTAL DO ALUNO ======")
    
    print("====== INFORMAÇÕES BÁSICAS ======")
    name_var = str(input("Nome do Aluno: "))
    age_var = int(input("Idade do Aluno: "))
    
    print("====== NOTAS DO ALUNO =====")
    
    grade_math = float(input("Nota de Matemática: "))
    grade_science = float(input("Nota de Ciências: "))
    grade_history = float(input("Nota de História: "))
    
    grade_var = (grade_math, grade_science, grade_history)
    
    student = {
        "name": name_var,
        "age": age_var,
        "grade": grade_var        
    }
    
    list_students.append(student)
    
    next = str(input("Deseja continuar? (Escreva 'S' para Sim e 'N' para Não)" ).lower())
    
    if next != 's':
        break
