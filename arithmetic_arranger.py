def arithmetic_arranger(problems, show_result=False):
    def clean_number(str_number):
        try:
            num = int(str_number)
            if len(str_number) > 4:
                raise Error("Numbers cannot be more than four digits")
            return num
        except ValueError:
            raise Error("Numbers must only contain digits")

    def valid_operator(operator):
        if operator not in ["+", "-"]:
            raise Error("Operator must be '+' or '-'")
        return operator

    def split_problem(problem):
        splited = problem.split()
        if len(problems) > 5:
            raise Error("Too many problems")
        operator = valid_operator(splited[1])
        num1 = clean_number(splited[0])
        num2 = clean_number(splited[2])
        result = num1 + num2 if operator == "+" else num1 - num2
        string_length = max(len(splited[0]), len(splited[2]))
        formatted_num1 = splited[0].rjust(string_length + 2)
        formatted_num2 = operator + " " + splited[2].rjust(string_length)
        separator = "-" * (string_length + 2)
        formatted_result = str(result).rjust(string_length + 2)
        return (formatted_num1, formatted_num2, separator, formatted_result)

    arranged_problems = "some"

    try:
        map = [split_problem(problem) for problem in problems]
        first = ""
        second = ""
        third = ""
        forth = ""
        for string1, string2, string3, string4 in map:
            first += string1 + "    "
            second += string2 + "    "
            third += string3 + "    "
            forth += string4 + "    "
        arranged_problems = (
            first.rstrip() + "\n" + second.rstrip() + "\n" + third.rstrip()
        )
        if show_result:
            arranged_problems += "\n" + forth.rstrip()
    except Error as e:
        return str(e)
    print(arranged_problems)
    return arranged_problems


class Error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Error: {self.message}."
