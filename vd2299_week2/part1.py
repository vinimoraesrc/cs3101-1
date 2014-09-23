employees = [('Bob ', 40, 18.25), ('Mary ', 10, 20.00), ('John ', 0, 100.90),\
              ('Carl ', 19, 17.21), ('Meg ', 60, 22.10), ('Yu ', 0, 8585.00),\
              ('Test ', 50, 50.0)]

length = len(employees)

def total_pay(l):
    """Produces tuples in the format (name, total_pay).

    Argument:
    l -- list of tuples in the format (name, hours_week, hourly_wage)

    - 'l[i][0]' stands for the employees' name in ith the tuple
    - 'l[i][1] * l[i][2]' is the computation of the total weekly pay
    - 'l[i][1] > 0' checks if the employee worked this week
    """
    x = [(l[i][0], (l[i][1] * l[i][2])) for i in range(length) if l[i][1] > 0]
    print (x)

total_pay(employees)