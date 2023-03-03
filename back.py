class Rule:
    def __init__(self, rule):
        self.rule = self.dec_to_bin(rule)

    def dec_to_bin(self, n):
        number = []
        while n != 0 and len(number) <= 32:
            number.append(n % 2)
            n //= 2
        while len(number) != 32:
            number.append(0)
        number.reverse()
        return number

    def bin_to_dec(self, number):
        number.reverse()
        n = 0
        for i in range(len(number)):
            n += number[i]*pow(2, i)
        return n

    def calculate_res(self, number): # number: base, up, down, left, right
        return self.rule[self.bin_to_dec(number)] == 1
