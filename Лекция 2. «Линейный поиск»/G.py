def input_read():
    inp_lst = [int(x) for x in input().split()]
    return inp_lst


def max_factors(sequence):
    if len(sequence) == 2:
        return tuple(sorted(sequence))
    max1 = max(sequence[0], sequence[1])
    max2 = min(sequence[0], sequence[1])
    min1, min2 = max2, max1
    for elem in sequence:
        if elem > max1:
            max2 = max1
            max1 = elem
        elif elem > max2:
            max2 = elem
        if elem < min1:
            min2 = min1
            min1 = elem
        elif elem < min2:
            min2 = elem
    if max1 * max2 >= min1 * min2:
        return max2, max1
    else:
        return min1, min2

def test():
    assert max_factors([1, 2]) == (1, 2)
    assert max_factors([2, 1]) == (1, 2)
    assert max_factors([1, 2, 3]) == (2, 3)
    assert max_factors([-1, -2, -3]) == (-3, -2)
    assert max_factors([4, 3, 5, 2, 5]) == (5, 5)
    assert max_factors([-4, -3, -5, -2, -5]) == (-5, -5)
    assert max_factors([-4, 3, -5, 2, 5]) == (-5, -4)
    assert max_factors([
        12288, -10075, 29710, 15686, -18900, -17715, 15992, 24431, 6220, 28403, -23148, 18480, -22905, 5411, -7602, 15560,
        -26674, 11109, -4323, 6146, -1523, 4312, 10666, -15343, -17679, 7284, 20709, -7103, 24305, 14334, -12281, 17314,
        26061, 25616, 17453, 16618, -24230, -19788, 21172, 11339, 2202, -22442, -20997, 1879, -8773, -8736, 5310, -23372,
        12621, -25596, -28609, -13309, -13, 10336, 15812, -21193, 21576, -1897, -12311, -6988, -25143, -3501, 23231, 26610,
        12618, 25834, -29140, 21011, 23427, 1494, 15215, 23013, -15739, 8325, 5359, -12932, 18111, -72, -12509, 20116,
        24390, 1920, 17487, 25536, 24934, -6784, -16417, -2222, -16569, -25594, 4491, 14249, -28927, 27281, 3297, 5998,
        6259, 4577, 12415, 3779, -8856, 3994, 19941, 11047, 2866, -24443, -17299, -9556, 12244, 6376, -13694, -14647,
        -22225, 21872, 7543, -6935, 17736, -2464, 9390, 1133, 18202, -9733, -26011, 13474, 29793, -26628, -26124, 27776,
        970, 14277, -23213, 775, -9318, 29014, -5645, -27027, -21822, -17450, -5, -655, 22807, -20981, 16310, 27605, -18393,
        914, 7323, 599, -12503, -28684, 5835, -5627, 25891, -11801, 21243, -21506, 22542, -5097, 8115, 178, 10427, 25808,
        10836, -11213, 18488, 21293, 14652, 12260, 42, 21034, 8396, -27956, 13670, -296, -757, 18076, -15597, 4135, -25222,
        -19603, 8007, 6012, 2704, 28935, 16188, -20848, 13502, -11950, -24466, 5440, 26348, 27378, 7990, -11523, -26393
    ]) == (29710, 29793)


def main():
    test()
    print(*max_factors(input_read()))


if __name__ == '__main__':
    main()
