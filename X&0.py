def print_mat(matrix):
    for line in range(0, 3):
        line_output = "|".join(matrix[line][:])
        print(line_output)


def find_coords(user):
    match user:
        case "1":
            return 0, 0
        case "2":
            return 0, 1
        case "3":
            return 0, 2
        case "4":
            return 1, 0
        case "5":
            return 1, 1
        case "6":
            return 1, 2
        case "7":
            return 2, 0
        case "8":
            return 2, 1
        case "9":
            return 2, 2


def check(matrix):
    ok = False
    for line in matrix:
        if line.count("X") == 3:
            print("You won!")
            ok = True
        if line.count("0") == 3:
            print("Laptop won! :(")
            ok = True

    col1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
    col2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
    col3 = [matrix[0][2], matrix[1][2], matrix[2][2]]
    if col1.count("X") == 3 or col2.count("X") == 3 or col3.count("X") == 3:
        print("You won!")
        ok = True

    if col1.count("0") == 3 or col2.count("0") == 3 or col3.count("0") == 3:
        print("Laptop won! :(")
        ok = True

    fst_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
    snd_diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]
    if fst_diagonal.count("X") == 3 or snd_diagonal.count("X") == 3:
        print("You won!")
        ok = True
    if fst_diagonal.count("0") == 3 or snd_diagonal.count("0") == 3:
        print("Laptop won! :(")
        ok = True

    return ok


def solve():
    mat = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    count = 1

    while count != 10:
        if count % 2 == 1:
            user = input("Choose a space: ")

            if user < "1" or user > "9" or len(user) != 1:
                print("Invalid choice! Try another: ")
                continue
            else:
                coords = find_coords(user)
                if mat[coords[0]][coords[1]] == " ":
                    mat[coords[0]][coords[1]] = "X"
                    count += 1
                else:
                    print("It's unavailable!")
                    continue
        else:
            print("Laptop's turn: ")
            if mat[1][1] == " ":
                mat[1][1] = "0"
            elif mat[0][0] == " ":
                mat[0][0] = "0"
            elif mat[0][2] == " ":
                mat[0][2] = "0"
            elif mat[2][0] == " ":
                mat[2][0] = "0"
            elif mat[2][2] == " ":
                mat[2][2] = "0"
            elif mat[0][1] == " ":
                mat[0][1] = "0"
            elif mat[1][0] == " ":
                mat[1][0] = "0"
            elif mat[1][2] == " ":
                mat[1][2] = "0"
            elif mat[2][1] == " ":
                mat[2][1] = "0"
            count += 1
        print_mat(mat)
        if check(mat):
            return
    print("Tie!")


solve()
