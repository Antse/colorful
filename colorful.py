class Colorful:
    def is_colorful(self, number):
        digits = []
        for n in str(number):
            digits.append(int(n))

        if len(digits) == 2:
            digits.append(digits[0] * digits[1])
            return len(set(digits)) == len(digits)
        elif len(digits) == 3:
            digits.append(digits[0] * digits[1])
            digits.append(digits[1] * digits[2])
            digits.append(digits[2] * digits[1] * digits[0])
            return len(set(digits)) == len(digits)
        else:
            # TODO: implement for all numbers
            return False

#  2, ou 3 digits.
