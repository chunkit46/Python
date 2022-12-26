def check_tetris(grid: list[list[str]], expected_output, exception: bool):
    def tetris(grid: list[list[str]]) -> int:
        # check if the grid is non-rectangle
        num_cols = len(grid[0])
        for row in grid:
            if len(row) != num_cols:
                raise ValueError('non-rectangle grid is invalid')

        # count completed lines
        count = 0
        for row in grid:
            if all(c == 'x' for c in row):
                count += 1

        return count

    try:
        assert tetris(grid) == expected_output
    except ValueError:
        return exception
    if exception:
        return False
    return True


assert check_tetris([
    ['x', 'x'],
    ['x', 'x'],
    ['x', 'x'],
    ['x', 'x']], 4, False)
assert check_tetris([
    [' ', ' ', ' '],
    ['x', 'x', 'x'],
    ['x', ' ', ' '],
    ['x', 'x', 'x'],
    [' ', ' ', ' '],
    [' ', ' ', ' ']], 2, False)
assert check_tetris([
    ['x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x']], 7, False)
assert check_tetris([
    [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x'],
    ['x', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' '],
    [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ']], 2, False)
assert check_tetris([
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x'],
    [' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x'],
    ['x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x'],
    ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']], 1, False)
assert check_tetris([
    [' ', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'x', ' '],
    ['x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    [' ', ' ', ' ', ' ', ' '],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', ' ', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x'],
    ['x', 'x', ' ', 'x', ' '],
    [' ', ' ', ' ', 'x', 'x']], 10, False)
assert check_tetris([
    ['x', 'x', 'x', ' ', ' ', 'x', 'x', 'x'],
    [' ', ' ', ' ', 'x', ' '],
    ['x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
    ['x', ' ', 'x', 'x', 'x', ' '],
    ['x'],
    [' ', 'x'],
    [' ', ' ', ' ', 'x', 'x', ' ', 'x', 'x'],
    [' ', ' '],
    ['x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', 'x', ' ']], 0, True)  # Non-rectangle
assert check_tetris([
    [' ', 'x', 'x', ' ', ' ', ' ', 'x'],
    ['x', 'x', ' ', ' ', ' ', ' '],
    ['x', 'x', ' ', 'x', 'x', ' ', 'x'],
    [' ', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', ' ', ' '],
    ['x', 'x', ' ', 'x']], 0, True)  # Non-rectangle