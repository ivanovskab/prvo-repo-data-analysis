from database import sesija, Employee, Product, Sale

def insert_employee(session, full_name, email, age, position, salary, years_in_company):

    emp1 = Employee(full_name = "File Tom",
                email = "tom@example.com",
                age = 60,
                position = 'technical support',
                salary = 75000,
                years_in_company = 15)
    sesija.add(emp1)
    sesija.commit() # commit izvrsuva
    print(f"Vraboteniot {full_name} e vnesen! ")
    return emp1

def insert_product(sesija, name, price):
    prod1 = Product(name = name,price= price )
    sesija.add(prod1)
    sesija.commit()
    print(f"Produktot: {name} e dodaden ")
    return prod1

def insert_sale(sesija, employee_id, product_id):
    sale1 = Sale(employee_id = employee_id, product_id=product_id)
    sesija.add(sale1)
    sesija.commit()
    print("Prodazbata e zabelezana. ")
    return sale1

print("Novi promeni vo nov brach")
ime = input("Vnesete ime: ")
print(f"Zdravo {ime}")
'''
p = insert_product(sesija, 'banani', '100')
e = insert_employee(sesija, "Teo", 'teo@gmail.com', 25, 'software developer', 30000, 5)


# e i p se objekti
# debugger to check what the program is doing in the background
# F5 -> python debugger -> python file

s  = insert_sale(sesija, 1, 1)'''

#########################################
## Zemanje podatoci


'''
#################### Update
'''
employees.salary = 80000 
sesija.commit()'''

# filter by ID or full_name
###########################
# DELETE
'''
employee = sesija.query(Employee).filter_by(id=17).first()
sesija.delete(employee)
sesija.commit()'''

