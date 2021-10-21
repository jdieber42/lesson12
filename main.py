from functions import calc_number,multiply_number

def cal(a):
    return a + 10

def repeat_calc(function, num, times):
    result = num
    for n in range(times):
        result = function(result)
    return result

def print_parameter(liste_dict, function):
    for el in liste_dict:
        print(function(el))

def main():
    #print(calc_number(3,4))
    #print(multiply_number(3,4))

    # methode als variable = [lambda] arguments : expresssion
    x = lambda a: a+10

    #print(x(5))
    #print(cal(5))

    steps = lambda distance,step_size: print(distance/step_size)
    # print(steps(500,0.7))

    #steps(500, 0.7)

    score_list = [{"attempts": 5, "datetime": "1"}, {"attempts": 2, "datetime": "9"}, {"attempts": 1, "datetime": "3"},
                  {"attempts": 3, "datetime": "2"}]

    sorted_list = sorted(score_list, key=lambda k: k["datetime"])
    print(sorted_list)

    print_parameter(score_list, lambda k: k["datetime"])

    mult_num = lambda num: num*2
    #print(repeat_calc(mult_num,5,3))

    mult_num = lambda num: num * 3
    #print(repeat_calc(mult_num, 5, 3))

    mult_num = lambda num: num * 5
    #print(repeat_calc(mult_num, 5, 3))


if __name__ == "__main__":
    main()