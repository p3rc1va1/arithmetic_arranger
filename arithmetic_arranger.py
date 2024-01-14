def arithmetic_arranger(array: list, show_answer: bool = False) -> str:
  first_numbers = []
  second_numbers = []
  operations = []
  sizes = []
  answers = []
  #split them into corresponding lists to organize them in a better way
  for i in range(len(array)):
    f, o, s = array[i].split()
    if o != '+' and o != '-':
      return "Error: Operator must be '+' or '-'."
    if f.isdigit() == False or s.isdigit() == False:
      return "Error: Numbers must only contain digits."
    if len(f) > 4 or len(s) > 4:
      return "Error: Numbers cannot be more than four digits."
    first_numbers.append(f)
    second_numbers.append(s)
    operations.append(o)

    if len(f) > len(s):
      sizes.append(len(f) * '-' + '--')
    else:
      sizes.append(len(s) * '-' + '--')
    if o == '-':
      answers.append(str(int(f) - int(s)))

    if o == '+':
      answers.append(str(int(f) + int(s)))

  if len(first_numbers) > 5 or len(second_numbers) > 5:
    return 'Error: Too many problems.'

  arranged_first_line = (len(sizes[0]) -
                         len(first_numbers[0])) * ' ' + first_numbers[0]
  for i in range(1, len(first_numbers)):
    arranged_first_line = arranged_first_line + '    ' + (
        len(sizes[i]) - len(first_numbers[i])) * ' ' + first_numbers[i]

  arranged_second_line = operations[0] + (
      len(sizes[0]) - len(second_numbers[0]) - 1) * ' ' + second_numbers[0]
  for i in range(1, len(first_numbers)):
    arranged_second_line = arranged_second_line + '    ' + operations[i] + (
        len(sizes[i]) - len(second_numbers[i]) - 1) * ' ' + second_numbers[i]

  arranged_third_line = '    '.join(sizes)
  ultimate_answer = arranged_first_line + '\n' + arranged_second_line + '\n' + arranged_third_line

  if show_answer:
    arranged_fourth_line = (len(sizes[0]) - len(answers[0])) * ' ' + answers[0]
    for i in range(1, len(answers)):
      arranged_fourth_line = arranged_fourth_line + '    ' + (
          len(sizes[i]) - len(answers[i])) * ' ' + answers[i]
    ultimate_answer = ultimate_answer + '\n' + arranged_fourth_line
    return ultimate_answer
  return ultimate_answer


print(
    arithmetic_arranger(
        ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
