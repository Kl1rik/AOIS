from enum import Enum
from dataclasses import dataclass
from itertools import product


class UnrecognisableToken(Exception):
    pass


class ImpossibleSolve(Exception):
    pass


class TokenType(Enum):
    VARIABLE = 0
    LEFT_BRACKET = 1
    RIGHT_BRACKET = 2
    INVERSION = 3
    CONJUNCTION = 4
    DISJUNCTION = 5
    IMPLICATION = 6
    EQUIVALENCE = 7


@dataclass
class Token:
    type: TokenType
    value: str
    order: int


@dataclass
class FullLogicalInterpretation:
    logical_interpretation: dict
    formula_value: int


class LogicalFormulaSolver:
    one_sym_tokens: dict = {'(': TokenType.LEFT_BRACKET, ')': TokenType.RIGHT_BRACKET, '!': TokenType.INVERSION,
                            '¬': TokenType.INVERSION, '&': TokenType.CONJUNCTION, '∧': TokenType.CONJUNCTION,
                            '∨': TokenType.DISJUNCTION, '⇒': TokenType.IMPLICATION, '→': TokenType.IMPLICATION,
                            '↔': TokenType.EQUIVALENCE, '⇔': TokenType.EQUIVALENCE, '≡': TokenType.EQUIVALENCE,
                            '~': TokenType.EQUIVALENCE}
    token_orders: dict = {TokenType.VARIABLE: -1, TokenType.LEFT_BRACKET: -1, TokenType.RIGHT_BRACKET: -1,
                          TokenType.INVERSION: 0, TokenType.CONJUNCTION: 1, TokenType.DISJUNCTION: 2,
                          TokenType.IMPLICATION: 3, TokenType.EQUIVALENCE: 4}

    def __init__(self, raw_formula: str):
        self.token_list: list[Token] = []
        self.raw_formula: str = raw_formula
        self.variables: set[str] = set()
        self.element: list[Token] = []
        self.val: list[int] = []

    def __replace_special_syms(self):
        self.raw_formula = self.raw_formula.replace('->', '→')
        self.raw_formula = self.raw_formula.replace('=>', '→')
        self.raw_formula = self.raw_formula.replace('<->', '↔')
        self.raw_formula = self.raw_formula.replace('<=>', '↔')
        self.raw_formula = self.raw_formula.replace('^', '∧')
        self.raw_formula = self.raw_formula.replace('&', '∧')
        self.raw_formula = self.raw_formula.replace('*', '∧')
        self.raw_formula = self.raw_formula.replace('+', '∨')
        self.raw_formula = self.raw_formula.replace('|', '∨')

    def __divide_into_tokens(self):
        self.__replace_special_syms()
        raw_token = ''
        for sym in self.raw_formula:
            if sym.isdigit() and len(raw_token) == 0:
                raise UnrecognisableToken('Numbers can go only after letters')
            elif sym.isalpha() or sym.isdigit():
                raw_token += sym
            elif sym.isspace():
                continue
            elif self.one_sym_tokens.get(sym, None):
                if not raw_token == '':
                    self.token_list.append(Token(TokenType.VARIABLE, raw_token, self.token_orders[TokenType.VARIABLE]))
                    self.variables.add(raw_token)
                raw_token = ''
                new_type = self.one_sym_tokens[sym]
                self.token_list.append(Token(new_type, sym, self.token_orders[new_type]))
            else:
                raise UnrecognisableToken('Forbidden symbol. Logical formula contains only:\n1. Letters\n'
                                          '2. Spaces\n'
                                          '3. Numbers after letters\n'
                                          '4. Logical operations symbols')
        if not raw_token == '':
            self.token_list.append(Token(TokenType.VARIABLE, raw_token, self.token_orders[TokenType.VARIABLE]))
            self.variables.add(raw_token)
        self.variables = sorted(self.variables)

    def __solve_operation(self):
        if self.element[len(self.element) - 1].type == TokenType.INVERSION:
            self.val.append(int(not self.val.pop()))
            self.element.pop()
            return
        first_value: int = self.val.pop()
        second_value: int = self.val.pop()
        if self.element[len(self.element) - 1].type == TokenType.CONJUNCTION:
            self.val.append(first_value & second_value)
        elif self.element[len(self.element) - 1].type == TokenType.DISJUNCTION:
            self.val.append(first_value | second_value)
        elif self.element[len(self.element) - 1].type == TokenType.IMPLICATION:
            self.val.append(int(not second_value) | first_value)
        elif self.element[len(self.element) - 1].type == TokenType.EQUIVALENCE:
            self.val.append((int(not second_value) & int(not first_value)) | (second_value & first_value))
        self.element.pop()

    def __solve_for_interpretation(self, logical_interpretation):
        for token in self.token_list:
            if token.type == TokenType.VARIABLE:
                self.val.append(logical_interpretation[token.value])
            elif token.type == TokenType.LEFT_BRACKET:
                self.element.append(token)
            elif token.type in (TokenType.INVERSION, TokenType.CONJUNCTION, TokenType.DISJUNCTION,
                                      TokenType.IMPLICATION, TokenType.EQUIVALENCE):
                if len(self.element) == 0 or self.element[len(self.element) - 1].type == \
                        TokenType.LEFT_BRACKET:
                    self.element.append(token)
                else:
                    while (not token.order < self.element[len(self.element) - 1].order) and \
                            (self.element[len(self.element) - 1].type != TokenType.LEFT_BRACKET):
                        self.__solve_operation()
                    self.element.append(token)
            elif token.type == TokenType.RIGHT_BRACKET:
                while not self.element[len(self.element) - 1].type == TokenType.LEFT_BRACKET:
                    self.__solve_operation()
                self.element.pop()
        while len(self.element) != 0:
            self.__solve_operation()
        # print(FullLogicalInterpretation(logical_interpretation, self.val.pop()))
        return FullLogicalInterpretation(logical_interpretation, self.val.pop())

    def solve_formula(self):
        self.__divide_into_tokens()
        possible_var_combs = sorted(list(product([0, 1], repeat=len(self.variables))))
        raw_truth_table: list[FullLogicalInterpretation] = list()
        for combo in possible_var_combs:
            logical_interpretation = dict(zip(self.variables, combo))
            raw_truth_table.append(self.__solve_for_interpretation(logical_interpretation))
        return raw_truth_table

    def beautiful_result_print(self):
        raw_truth_table = self.solve_formula()
        for var in self.variables:
            print(var.center(len(var) + 2, ' ') + '|', end='')
        print(self.raw_formula.center(len(self.raw_formula) + 2, ' '))
        for interpretation in raw_truth_table:
            for var, value in interpretation.logical_interpretation.items():
                print(str(value).center(len(var) + 2, ' ') + '|', end='')
            print(str(interpretation.formula_value).center(len(self.raw_formula) + 2, ' '))



class FcnfFdnfFormConverter:
    def __init__(self, raw_formula ):
        self.truth_table = LogicalFormulaSolver(raw_formula).solve_formula()
        self.fcnf = ''
        self.fdnf = ''
        self.fcnf_num_form = ''
        self.fdnf_num_form = ''
        table_values = [element.formula_value for element in self.truth_table]
        self.formula_index = int(''.join([str(value) for value in table_values]), 2)

    def build_fcnf(self):
        fcnf_show = []
        fcnf_num = 0
        disj_set = []
        for element in self.truth_table:
            if element.formula_value == 0:
                disjunction_set  = []
                fcnf_show.append(str(fcnf_num))
                for var, value in element.logical_interpretation.items():
                    disjunction_set.append(var if value == 0 else '!'+var)
                disj_set.append('('+' ∨ '.join(disjunction_set)+')')
            fcnf_num += 1
        self.fcnf = ' ∧ '.join(disj_set)
        self.fcnf_num_form = '∧(' + ', '.join(fcnf_show) + ')'

    def build_fdnf(self):
        fdnf_fcnf_nums = []
        fcnf_num = 0
        conj_set = []
        for element in self.truth_table:
            if element.formula_value == 1:
                conjunction_set =  []
                fdnf_fcnf_nums.append(str(fcnf_num))
                for var, value in element.logical_interpretation.items():
                    conjunction_set.append(var if value == 1 else '!' + var)
                conj_set.append('(' + ' ∧ '.join(conjunction_set) + ')')
            fcnf_num += 1
        self.fdnf = ' ∨ '.join(conj_set)
        self.fdnf_num_form = '∨(' + ', '.join(fdnf_fcnf_nums) + ')'


def test():
    formula = '(!((!x1+!x2)&!(x1&x3)))'
    formula_solver = LogicalFormulaSolver(formula)
    formula_solver.beautiful_result_print()
    fknf_fdnf_show = FcnfFdnfFormConverter(formula)
    fknf_fdnf_show.build_fcnf()
    fknf_fdnf_show.build_fdnf()
    print(f'FCNF: {fknf_fdnf_show.fcnf}\n'
          f'FCNF number form: {fknf_fdnf_show.fcnf_num_form}\n'
          f'FDNF: {fknf_fdnf_show.fdnf}\n'
          f'FDNF number form: {fknf_fdnf_show.fdnf_num_form}\n'
          f'Formula index: {fknf_fdnf_show.formula_index}')


test()


        