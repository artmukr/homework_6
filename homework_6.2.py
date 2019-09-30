
def calculator(first_number, second_number, action):
    result = {
              "+": float(first_number) + float(second_number),
              "-": float(first_number) - float(second_number),
              "/": float(first_number) / float(second_number),
              "*": float(first_number) * float(second_number)
          }
    return result[action]


print(calculator(5, 4, '*'))
