def bit_string(N):
    L = 2**N
    count = L
    final_list = []

    for o in range(N):
        count = count/2
        bit_op = 1

        for index in range(L):
            if (index) % count == 0:
                if bit_op:
                    bit_op =0
                else:
                    bit_op = 1
            if o == 0:
                final_list.append([bit_op])
            else:
                final_list[index].append(bit_op)
    return final_list

print bit_string(3)
