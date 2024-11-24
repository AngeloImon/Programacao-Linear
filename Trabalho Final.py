import gurobipy as gp

# Function to read data from Tab_Func.txt
def read_tab_func_data(filename):
    tab_func_data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            identifier = int(parts[0])
            hour_time = parts[1]
            min_employee_amount = int(parts[2])
            salary_multiplier = float(parts[3])
            tab_func_data.append((identifier, hour_time, min_employee_amount, salary_multiplier))
    return tab_func_data

# Read data from Tab_Func.txt
tab_func_data = read_tab_func_data('Tab_Func.txt')

# Print the parsed data
for identifier, hour_time, min_employee_amount, salary_multiplier in tab_func_data:
    print(f"Período: {identifier}, Horário: {hour_time}, NMA: {min_employee_amount}, Salário: {salary_multiplier}")

# Creating an optimization model
modelo = gp.Model()

# Creating decision variables
x = modelo.addVars(len(tab_func_data), name="x")  # Create variables for each hour
Q = modelo.addVars(len(tab_func_data), name="x")  # Create variables for each hour

# Objective function
modelo.setObjective(gp.quicksum(Q[i]*tab_func_data[i][3] for i in range(len(tab_func_data))), sense=gp.GRB.MINIMIZE
)

# Constraints
R1 = modelo.addConstrs(
    (gp.quicksum(x[j%24] for j in range(i-5, i+1)) == Q[i] for i in range(len(tab_func_data))), name="R"
)

R1 = modelo.addConstrs(
    (Q[i] >= tab_func_data[i][2] for i in range(len(tab_func_data))), name="R"
)
# Suppress terminal output
modelo.setParam("OutputFlag", 0)

# Solving the model
modelo.optimize()

# Print the solution
for i in range(len(tab_func_data)):
    if x[i].x > 0:
        print(f'Horario de entrada: {tab_func_data[i][1]}:00 - Quantidade Empregados: {x[i].x:.0f}')

print(f'Obj: {modelo.objVal}')