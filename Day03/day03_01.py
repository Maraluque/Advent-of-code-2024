import re
if __name__ == '__main__':
    mult_result = 0
    regex_mult = r"mul\(\d{1,3},\d{1,3}\)"
    regex_values = r"\d{1,3}"

    with open("input.txt", "r") as f:
        lines = f.readlines()
        results = []
        for line in lines:
            result = re.findall(regex_mult, line)
            for item in result:
                result_values = re.findall(regex_values, item)
                result_values = list(map(int,result_values))
                local_mult = result_values[0] * result_values[1]
                mult_result += local_mult
    print(mult_result)
