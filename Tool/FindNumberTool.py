''' This tool find the quantity of iteration to find number in the natural numbers range '''

left_range_side = int(input("Enter number equal to left side of the numbers range: "))
right_range_side = int(input("Enter number equal to right side of the numbers range: "))

run_status = True
run_iteration = True
iteration = 0
true_state = True
false_state = False

while run_status == true_state:
    number = int(input(f"Enter number between {left_range_side} and {right_range_side}: "))
    if left_range_side < number < right_range_side:
        print("Correct number!!! Super!!!")
        if number == left_range_side:
            print("Answer:")
            print(f"Your number is {left_range_side}.")
            run_status = false_state
        elif number == right_range_side:
            print("Answer:")
            print(f"Your number is {right_range_side}.")
            run_status = false_state
        else:
            while run_iteration == true_state:
                iteration += 1
                required_number = int((left_range_side + right_range_side)/2)
                if required_number == number:
                    print("Answer:")
                    print(f"Your number is {required_number}.")
                    print(f"The quantity of iteration(s) is(are) {iteration}.")
                    #next_number = input(f"Would you like to find one more in the selected range?, yes/no")
                    #if next_number == "no":
                    #    next_number = input(f"Would you like to change the range?, yes/no")
                    #    if next_number == "no":
                    run_iteration = false_state
                    run_status = false_state
                elif required_number < number:
                    left_range_side = required_number
                else:
                    right_range_side = required_number
    else:
        print("Not correct number!!!")
