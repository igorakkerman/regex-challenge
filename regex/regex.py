def matches(string, pattern):
    return match(string, 0, pattern, 0) \
        if pattern != "" else string == ""


def match(string, string_index, pattern, pattern_index):
    if string_index >= len(string) and pattern_index >= len(pattern):
        return True

    if pattern_index >= len(pattern):
        return False

    if pattern_index + 1 < len(pattern) and pattern[pattern_index + 1] == '*':
        return match_star(string, string_index, pattern, pattern_index)

    if string_index >= len(string):
        return False

    pattern_char = pattern[pattern_index]

    if 'a' <= pattern_char <= 'z':
        if len(string) <= string_index or string[string_index] != pattern_char:
            return False

    elif pattern_char == '.':
        pass

    else:
        raise ValueError("Illegal regex pattern character")

    return match(string, string_index + 1, pattern, pattern_index + 1)


def match_star(string, string_index, pattern, pattern_index):
    star_char = pattern[pattern_index]

    # if rest after star matches, then c* matched ""
    if match(string, string_index, pattern, pattern_index + 2):
        return True

    # advance by one in the string
    return (string_index < len(string) and (string[string_index] == star_char or star_char == '.')) and \
        match_star(string, string_index + 1, pattern, pattern_index)
