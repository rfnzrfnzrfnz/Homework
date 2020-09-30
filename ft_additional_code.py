def ft_additional_code(num):
    result = ""
    if num >= 0:
        while num:
            digit = num % 2
            if digit == 0:
                result = "0" + result
            else:
                result = "1" + result
            num = num // 2
        while len(result) < 8:
            result = "0" + result
        print(result)

    else:
        num = num * (-1)
        while num:
            digit = num % 2
            if digit == 0:
                result = "1" + result
            else:
                result = "0" + result
            num = num // 2
        while len(result) < 8:
            result = "1" + result
        print(result)
