while (True):
    print("--------------------")
    print("Aritmetika dasar")
    print("------------------\n")
    print("1. Kalkulator")
    print("2. Keluar(Y/N)")
    print("------------------\n")
    inpData: int
    inpData = input("Pilih menu: ")
    if inpData == "1":
        a: int
        b: int
        operator: str
        hitung: float
        a = float(input("Nilai a: "))
        b = float(input("Nilai b: "))

        operator = input("Operator(+ - * /): ")

        if operator == "+":
            hitung = a + b
            print("hasilnya = ", hitung)
        elif operator == "-":
            hitung = a - b
            print("hasilnya = ", hitung)
        elif operator == "*":
            hitung = a * b
            print("hasilnya = ", hitung)
        elif operator == "/":
            hitung = a / b
            print("hasilnya = ", hitung)    

    elif (inpData == "Y" or inpData == "y"):
        print("Bye")
        break
    elif (inpData == "N" or inpData == "n"):
        continue
