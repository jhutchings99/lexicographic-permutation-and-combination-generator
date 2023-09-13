def generate_list_size_n(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    return lst

def generate_next_permutation_lexicographic_order(a):
    n = len(a)
    j = n - 2

    while j >= 0 and a[j] >= a[j+1]:
        j -= 1

    if j == -1:
        return None

    k = n - 1
    while a[j] >= a[k]:
        k -= 1

    a[j], a[k] = a[k], a[j]

    r = n - 1
    s = j + 1
    while r > s:
        a[r], a[s] = a[s], a[r]
        r -= 1
        s += 1

    return a

def get_user_input(input_prompt):
    getting_input = True
    while getting_input:
        try:
            user_input = int(input(input_prompt))
            if user_input < 1 or user_input > 9:
                print("User input must be an integer between 1 and 9")
            else:
                return user_input
        except:
            print("User input must be an integer")

def main():
    n = get_user_input("Enter an integer between 1 and 9: ")
    current_permutation = generate_list_size_n(n)
    total_permutations = 0

    while True:
        print(current_permutation)
        current_permutation = generate_next_permutation_lexicographic_order(current_permutation)
        total_permutations += 1
        if current_permutation == None:
            break

    print(f"Total permutations: {total_permutations}")


if __name__ == "__main__":
    main()