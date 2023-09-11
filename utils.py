class Utils:
    def reversed(num):
        if type(num) is int:
            return int(str(num)[::-1])
        else:
            raise ValueError("Function input must be an integer")

    def formatter(num):
        if type(num) is int:
            return bin(num), oct(num)
        else:
            raise ValueError("Function input must be an integer")