# write your code here
user_input = input()
input_list = user_input.split(" ")
number_1 = int(input_list[0])
number_2 = int(input_list[2])
if input_list[1] == "+":
    print(number_1 + number_2)
elif input_list[1] == "*":
    print(number_1 * number_2)
elif input_list[1] == "-":
    print(number_1 - number_2)
