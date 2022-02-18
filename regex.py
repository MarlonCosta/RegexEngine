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
    if regex == "$":
        return string == ""
    if not string:
        return False
    if not compare_regex_char(regex[0], string[0]):
        return False
    else:
        return compare_regex_same_length(regex[1:], string[1:])


# Project 3
def compare_regex_variable_length(regex: str, string: str):
    """Checks if a regex matches a string of variable length"""
    if not regex:
        return True
    elif string:
        if compare_regex_same_length(regex, string):
            return True
        else:
            return compare_regex_variable_length(regex, string[1:])
    else:
        return False


#   Project 4
def compare_regex_beginning_end(regex: str, string: str):
    """Adds the wildcard characters ^ and $ to the regex engine"""
    if not regex:
        return True
    if regex[0] == "^" and regex[-1] == "$":
        return compare_regex_same_length(regex[1:], string)
    if regex[0] == "^":
        return compare_regex_same_length(regex[1], string)
    if regex[-1] == "$":
        return compare_regex_variable_length(regex, string)

    return compare_regex_variable_length(regex, string)


def entry_point(input_string):
    """Method to make simpler unit tests"""
    regex, string = input_string.split("|")
    return compare_regex_beginning_end(regex, string)


if __name__ == '__main__':
    print(entry_point(input()))
