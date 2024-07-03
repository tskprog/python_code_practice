def inputArray():
    n = int(input("Enter number of elements : "))
    ip_arr = []
    # ip_arr = [-4,-2,0,5,6]
    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        # adding the element
        ip_arr.append(ele)
    return ip_arr