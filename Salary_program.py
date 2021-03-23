salaries = []
num_members = 3

for i in range(num_members):
    salary = int(input("Введите вашу зарплату: "))
    salaries.append(salary)

#  Складываем все зарплаты
avg_salary = 0

for i in range(num_members):
    avg_salary += salaries[i]

print(avg_salary/num_members)