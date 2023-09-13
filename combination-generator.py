def generate_list_size_n(r):
    lst = []
    for i in range(1, r+1):
        lst.append(i)
    return lst

def generate_next_permutation_lexicographic_order(a, n, r):
    i = r - 1
    while a[i] == n - r + i:
        i -= 1

    if i == -1:
        return
    
    a[i] += 1

    for j in range(i+1, r):
        a[j] = a[i] + j - i

    return a

def main():
    pass

if __name__ == "__main__":
    main()