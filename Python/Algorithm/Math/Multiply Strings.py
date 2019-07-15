class Solution:
    def multiply(self, num1, num2):
        product = [0] * (len(num1) + len(num2))
        i = len(product) - 1
        for n1 in reversed(num1):
            j = i
            for n2 in reversed(num2):
                product[j] += int(n1) * int(n2)
                product[j-1] += product[j] // 10
                product[j] %= 10
                j -= 1
            i-= 1
        # count digits
        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1
        return ''.join(map(str, product[pt:]))