import re   # Regular Expression
from sympy import Matrix, lcm   # Matrix and least common multiple

element_list = []
element_matrix = []

# Get the chemical equation
print("Enter your chemical equation")
print("e.g. Fe3O4+HNO3->Fe(NO3)2+Fe(NO3)3+H2O")
equation = input()
equation = re.sub(r"[ \[\]]", "", equation).split("->")

# Get the reactants and products from the equation
reactants = equation[0].split("+")
products = equation[1].split("+")

# Add the elements to the matrix
def add_to_matrix(element, index, side, count):
    if index == len(element_matrix):
        element_matrix.append([0] * len(element_list))

    if element not in element_list:
        element_list.append(element)
        for i in range(len(element_matrix)):
            element_matrix[i].append(0)

    column = element_list.index(element)
    element_matrix[index][column] += count * side

# Find the elements in a decomposed group
def find_elements(group, index, side, multiplier):
    elements = re.split("([A-Z][a-z]?)", group)
    # Filter out empty strings
    # re.split produces empty strings at the beginning and end of the list
    elements = [element for element in elements if element]
    elements.append('')

    i = 0
    while i < len(elements) and elements[i]:
        count = multiplier
        if elements[i + 1].isdigit():
            count *= int(elements[i + 1])
        
        add_to_matrix(elements[i], index, side, count)

        i += 2 if elements[i + 1].isdigit() else 1

# Decompose the compound into elements and their respective count 
def decompose_compound(compound, index, side):
    groups = re.split(r"(\([A-Za-z0-9]*\)[0-9]*)", compound)
    groups = [group for group in groups if group]

    for group in groups:
        multiplier = 1
        if group.startswith("("):
            group = re.split(r"\)([0-9]*)", group)
            if group[1].isdigit():
                multiplier = int(group[1])
            group = group[0][1:]

        find_elements(group, index, side, multiplier)

for i in range(len(reactants)):
    decompose_compound(reactants[i], i, 1)
for i in range(len(products)):
    decompose_compound(products[i], i + len(reactants), -1)

# Balance the equation
element_matrix = Matrix(element_matrix).transpose()
solution = element_matrix.nullspace()[0]    # Get the nullspace of the matrix (Solve the system of equations)
multiple = lcm([val.q for val in solution])
solution *= multiple    # Make all the coefficients integers

# Print the balanced equation
coefficients = solution.tolist()
result = ""

for i in range(len(reactants)):
    result += str(coefficients[i][0]) + reactants[i]
    if i < len(reactants) - 1:
        result += " + "

result += " -> "

for i in range(len(products)):
    result += str(coefficients[i + len(reactants)][0]) + products[i]
    if i < len(products) - 1:
        result += " + "

print(result)