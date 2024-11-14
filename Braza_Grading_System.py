grade_list = []
i = 1

while True:
    grades = input("Please input your grade here, input 'done' when finished.: ")
    
    if grades == 'done':
        break

    if grades.isdigit():
        final = int(grades)
        if (final) >= 40 or (final) >=100:
            grade_list.append(final)
            print(f"Grades: {grade_list} \nGrades inserted: {len(grade_list)}")
            i += 1
        else:
            print("Invalid Grade input. Please retry.")
            exit()

    else:
        print("Invalid Input.")
        exit()

average = sum(grade_list)
total = round((average) / len(grade_list), 2)

print(f"with the amount of {len(grade_list)} subjects, your average is {total}.")
    

