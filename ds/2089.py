def num_sys(num):
    q, r = divmod(num, -2)
    return num_sys(q) + str(-r) if q else str(-r)


print(num_sys(-int(input())))

# TODO: 이해못함
