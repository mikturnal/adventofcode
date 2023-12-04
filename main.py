def analyse_document(file_path):
    combined_digits_list = []
    written_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nice"]

    with open(file_path, 'r') as file:
        for line in file:
            found_written_numbers = []
            # Extracting digits from the line
            digits = [int(digit) for digit in line.strip() if digit.isdigit()]

            for substring in written_numbers:
                if substring in line:
                    found_written_numbers.append(substring)

            # Combining the first and last digits
            if digits:
                combined_digits = int(str(digits[0]) + str(digits[-1]))
                combined_digits_list.append(combined_digits)
            print(found_written_numbers)
    return sum(combined_digits_list)


file_path = 'test.txt'
result = analyse_document(file_path)
# print(result)
