def inputArray():
    n = int(input("Enter number of elements : "))
    ip_arr = list(map(int, input(f'Enter {n} elements separating with space : ').strip().split()))[:n]
    return ip_arr