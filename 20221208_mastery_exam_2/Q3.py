def reverse_lower(s: str) -> str:
    lower = [c for c in s if c.islower()]
    other = [c for c in s if not c.islower()]

    lower = lower[::-1]

    result = []
    for c in s:
        if c.islower():
            result.append(lower.pop(0))
        else:
            result.append(c)

    return "".join(result)


assert (reverse_lower('abc') == 'cba')
assert (reverse_lower('ABC') == 'ABC')
assert (reverse_lower('A123bc') == 'A123cb')
assert (reverse_lower('muic-2021') == 'cium-2021')
assert (reverse_lower('M-ahid--ol') == 'M-lodi--ha')
assert (reverse_lower('XJjHVzheiy') == 'XJyHViehzj')
assert (reverse_lower('L5bIgto2gv6W') == 'L5vIgot2gb6W')
assert (reverse_lower('sYmA5Poekfz0k9') == 'kYzA5Pfkeom0s9')
assert (reverse_lower('hDuAt5zqBSFg6-F3') == 'gDqAz5tuBSFh6-F3')
assert (reverse_lower('MreN13pdEbI28D1J3N') == 'MbdN13peErI28D1J3N')
