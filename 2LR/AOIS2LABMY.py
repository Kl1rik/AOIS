import re
AlphabetArray = "ABCDEFGHIJKLMNOPPRSQWXYZ"

print(AlphabetArray)
def pdnf(expr):
    # Split the expression into terms and remove any spaces
    terms = [term.strip() for term in expr.split('+')]
    variables = set()

    # Determine the set of variables used in the expression
    for term in terms:
        for char in term:
            if char.isalpha():
                variables.add(char)

    # Generate all possible combinations of variable values
    combos = []
    for i in range(2**len(variables)):
        combo = {}
        for j, var in enumerate(variables):
            combo[var] = (i // 2**j) % 2
        combos.append(combo)

    # Evaluate the expression for each combination of variable values
    values = []
    for combo in combos:
        result = 1
        for term in terms:
            term_value = 0
            for char in term:
                if char.isalpha():
                    term_value |= combo[char]
            result &= term_value
        values.append(result)

    # Construct the PDNF string
    pknf_str = ''
    for i, combo in enumerate(combos):
        if values[i]:
            if pknf_str:
                pknf_str += ' + '
            pknf_str += '('
            for var, val in combo.items():
                if not val:
                    pknf_str += '~'
                pknf_str += var
            pknf_str += ')'

    return pknf_str

expr = '(A~B) + (A~C~D) + (~A~B~C)'
pdnf_str = pdnf(expr)
print(pdnf_str)


def pknf(expr):
    # Split the expression into terms and remove any spaces
    terms = [term.strip() for term in expr.split('+')]
    variables = set()

    # Determine the set of variables used in the expression
    for term in terms:
        for char in term:
            if char.isalpha():
                variables.add(char)

    # Generate all possible combinations of variable values
    combos = []
    for i in range(2**len(variables)):
        combo = {}
        for j, var in enumerate(variables):
            combo[var] = (i // 2**j) % 2
        combos.append(combo)

    # Evaluate the expression for each combination of variable values
    values = []
    for combo in combos:
        result = 1
        for term in terms:
            term_value = 0
            for char in term:
                if char.isalpha():
                    term_value |= combo[char]
            result &= term_value
        values.append(result)

    # Construct the PDNF string
    pknf_str = ''
    for i, combo in enumerate(combos):
        if values[i]:
            if pknf_str:
                pknf_str += ' * '
            pknf_str += '('
            for var, val in combo.items():
                if not val:
                    pknf_str += '~'
                pknf_str += var
            pknf_str += ')'

    return pknf_str

expr = '(A~B)+(A~C~D)+(~A~B~C)'
pknf_str = pknf(expr)
print(pknf_str)

    
def my_sknf():
    string = '(a∧!b)∨(b∧c))'       
    string = string.split('∧')
    for part in string:
        