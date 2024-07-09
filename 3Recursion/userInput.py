def inputInt(comment):
    n = int(input(comment+' : '))
    return n


def inputStr(comment):
    return input(comment+' : ')


def inputArray():
    n = inputInt("Enter number of elements")
    ip_arr = list(map(int, input(f'Enter {n} elements separating with space : ').strip().split()))[:n]
    return ip_arr