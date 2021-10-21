def calculate_sum(num1, num2):
    return num1 + num2

def cube_number(num):
    return num*num*num

def calc_steps(distance_meter, step_meter):
    return int(distance_meter/step_meter)


def main():
    # exercise 1 - caclulate numbers
    result1 = calculate_sum(2,5)
    print(result1)

    # exercise 2 - calculate cube
    result2 = cube_number(3)
    print(result2)

    # exercise 3 - steps calculator
    print(calc_steps(500,0.7))

if __name__ == "__main__":
    main()