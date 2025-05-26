def solution(sides):
    s_sides = sorted(sides)
    if s_sides[-1] < s_sides[0] + s_sides[1]:
        return 1
    else:
        return 2