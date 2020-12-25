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

    def split_and_format_problem(problem):
        splited = problem.split()
        if len(problems) > 5:
            raise Error("Too many problems")
        operator = valid_operator(splited[1])
        num1 = clean_number(splited[0])
        num2 = clean_number(splited[2])
        string_length = max(len(str(num1)), len(str(num2)))
        formatted = dict()
        formatted["first_number"] = str(num1).rjust(string_length + 2)
        formatted["second_number"] = operator + " " + str(num2).rjust(string_length)
        formatted["separator"] = "-" * (string_length + 2)
        if show_result:
            result = num1 + num2 if operator == "+" else num1 - num2
            formatted["result"] = str(result).rjust(string_length + 2)

        return formatted

    def combine_strings(problem, strings):
        splitted_problem = split_and_format_problem(problem)
        keys = ["first_number", "second_number", "separator"]
        if show_result:
            keys.append("result")
        for key in keys:
            strings[key] = strings.get(key, []) + [splitted_problem[key]]
        return strings

    try:
        my_dict = dict()
        for problem in problems:
            my_dict = combine_strings(problem, my_dict)
        return "\n".join(["    ".join(v) for v in my_dict.values()])
    except Error as e:
        return str(e)


class Error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Error: {self.message}."
