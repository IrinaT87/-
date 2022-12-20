with open ('file/data.txt') as file:
    departments=[]  #список отделов
    for line in file:
        department_name=line.strip()
        employees_count=int(file.readline().strip())
        employees=[]
        for i in range(employees_count):
            employee=file.readline().strip()
            name, surname, date, city=employee.split(' | ')
            employees.append({
                'name': name,
                'surname': surname,
                'date':date,
                'city':city
            })
        file.readline()
        departments.append({
        'name':department_name,
        'elployees_count':employees_count,
        'employees':employees})
       
print(departments)