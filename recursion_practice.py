# input: [(1, 2)]
# [(W), (D), (L)]

# input: [(1,2), (3,4)]
# [(W, W), (D, W), (L, W), (W, D), (D, D), (L, D), (W, L), (D, L), (L, L)]

from typing import List

def solve(input):
    """ input is list of tuple with games
        return list of tuples contains possiblity of possiblity of games
    """
    if len(input) == 1:
        take = input.pop()
        return [[take, "W"], [take, "D"] ,[take, "L"]]
    else:
        current = input.pop()
        next_level = solve(input)
        result = []
        for each in next_level:
            a = each + [current, "W"]
            result.append(a)

        for each in next_level:
            a = each + [current, "D"]
            result.append(a)

        for each in next_level:
            a = each + [current, "L"]
            result.append(a)
    return result


if __name__ == "__main__":
    print(solve([(1,2), (3,4), (5, 6)]))