def hello_world():
    print("Hello World!")
    print("Hello again!")

def write_name(name):
    print(f"Hallo {name}")

def calc_number(num1, num2):
    result = num1 + num2
    return result

def multiply_number(num1=2,num2=2):
    return num1 * num2

def tests():
    write_name("Hans")
    write_name("Kathi")

    #result1 = calc_number("1","1")
    #result2 = calc_number(4,4)

    #print(f"{result1} - {result2}")

    multi_result = multiply_number(num1=5,num2=4)

    print(multi_result)

    multi_result = multiply_number(num1=3,num2=4)

    print(multi_result)

if __name__ == "__main__":
    tests()
