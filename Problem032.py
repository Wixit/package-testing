def main():
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    perm = '0123456789'
    specials = {}
    total = 0
    while True:
        # examine permutation
        for i in range(2, 9):
            a = int(perm[1:i])
            for j in range(i+1, 10):
                b = int(perm[i:j])
                c = int(perm[j:])
                if a * b == c and c not in specials:
                    specials[c] = 1
                    total += c
        # get next permutation
        for i in reversed(range(1, 10)):
            digit = int(perm[i])
            digits[digit] += 1
            if digits[digit:].count(1) > 1:
                next_index = digits[digit+1:].index(1) + digit + 1
                digits[next_index] = 0
                perm = perm[:i] + str(next_index) + perm[i+1:]
                j = i + 1
                while digits.count(1) > 0:
                    next_index = digits.index(1)
                    digits[next_index] = 0
                    perm = perm[:j] + str(next_index) + perm[j+1:]
                    j += 1
                break
        else:
            break
    print(total)

if __name__ == '__main__':
    main()
