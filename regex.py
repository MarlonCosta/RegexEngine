# Project 1
def compare_regex_char(regex: str, string: str):
    """"Checks if a 1-character regex matches a 1-character string"""
    if (regex == "." and string != "") or regex == "":
        return True
    elif regex != ".":
        return regex == string
    else:
        return False


# Project 2
def compare_regex_same_length(regex: str, string: str):
    """Checks if a regex matches a string of the same length"""
    if not regex:
        return True
    if not string:
        return False
    if compare_regex_char(regex[0], string[0]):
        return compare_regex_same_length(regex[1:], string[1:])


# Project 3
def compare_regex_variable_length(regex: str, string: str):
    """Checks if a regex matches a string of variable length"""
    if regex == "":
        return True
    elif string:
        if compare_regex_same_length(regex, string):
            return True
        else:
            return compare_regex_variable_length(regex, string[1:])
    else:
        return False


if __name__ == '__main__':
    regex_input, string_input = input().split("|")
    print(compare_regex_variable_length(regex_input, string_input))
