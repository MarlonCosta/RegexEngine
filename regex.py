def match(regex, string):
    """match characters in input pattern and string one by one recursively"""
    if not regex:
        return True
    elif not string:
        return False
    elif '?' in regex[1:] and regex[1] == '?' and regex[0] != "\\":
        return rep_zero_to_once(regex, string)
    elif '*' in regex[1:] and regex[1] == '*' and regex[0] != "\\":
        return rep_zero_to_many(regex, string)
    elif '+' in regex[1:] and regex[1] == '+' and regex[0] != "\\":
        return rep_once_to_many(regex, string)
    elif regex[0] == "\\":
        return match(regex[1:], string)
    elif regex[0] in ('.', string[0]):
        return match(regex[1:], string[1:])
    return False


def rep_zero_to_once(regex, string):
    """regex pattern's first character may appear once or zero times"""
    if regex[0] not in (string[0]):
        return match(regex[2:], string)
    return match(regex[2:], string[1:])


def rep_zero_to_many(regex, string):
    """regex pattern's first character may appear zero or multiple times"""
    if regex[0] not in (string[0], '.'):
        return match(regex[2], string)
    elif regex[-1] == '*' and len(string) == 1:
        return True
    elif regex[:2] == '.*' and regex[-1] == string[0]:
        return True
    return match(regex, string[1:])


def rep_once_to_many(regex, string):
    """regex pattern's first character may appear once or multiple times"""
    if regex[0] not in (string[0], '.'):
        return False
    elif len(regex) - len(string) == 1:
        return match(regex[:1] + regex[2:], string)
    return match(regex, string[1:])


def bounded_match(regex, string):
    """regex pattern is only searched at the beginning or at the end of a string"""
    if regex[0] == '^' and regex[-1] == '$':
        res = match(regex[1:-1], string)
        if res and len(regex) - 2 == len(string):
            return True
        elif res and {'*', '?', '+'} & set(regex):
            return True
        return False
    elif regex[0] == '^':
        return match(regex[1:], string[:len(regex) - 1])
    elif regex[-1] == '$':
        return match(regex[:-1], string[-len(regex) + 1:])


def entry_point(regex, string):
    if not regex:
        return True
    elif not string:
        return False
    elif regex[0] == '^' or regex[-1] == '$':
        return bounded_match(regex, string)
    elif match(regex, string):
        return True
    return entry_point(regex, string[1:])


def main():
    r, s = input().split('|')
    print(entry_point(r, s))


if __name__ == '__main__':
    main()
