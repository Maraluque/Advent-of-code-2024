import re
if __name__ == '__main__':
    mult_result = 0
    regex_enabled_options = r"do\(\)([\s\S]*?)don't\(\)"
    regex_mult = r"mul\(\d{1,3},\d{1,3}\)"
    regex_values = r"\d{1,3}"

    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = f"do(){lines}don't()" # HACK: To take the first occurrences as do()
        results = []
        result = re.findall(regex_enabled_options, lines)
        for item in result:
            result_mult = re.findall(regex_mult, item)
            for mult in result_mult:
                result_values = re.findall(regex_values, mult)
                result_values = list(map(int,result_values))
                local_mult = result_values[0] * result_values[1]
                mult_result += local_mult
    print(mult_result)
