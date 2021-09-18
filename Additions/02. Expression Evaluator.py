from collections import deque

expression = deque(input().split())

numbers_and_final_result = deque()

while expression:
    if expression[0].isdigit():
        numbers_and_final_result.append(int(expression.popleft()))
    else:
        action = expression.popleft()
        result = numbers_and_final_result.popleft()
        if action == "*":
            while numbers_and_final_result:
                next_num = numbers_and_final_result.popleft()
                if (result < 0 and next_num < 0) or (result > 0 and next_num > 0):
                    result = result * next_num
                else:
                    result = - (result * next_num)

        elif action == "+":
            while numbers_and_final_result:
                next_num = numbers_and_final_result.popleft()
                result = result + next_num

        elif action == "-":
            while numbers_and_final_result:
                result = result - numbers_and_final_result.popleft()
        elif action == "/":
            while numbers_and_final_result:
                result = result / numbers_and_final_result.popleft()

        numbers_and_final_result.append(int(result))

print(*numbers_and_final_result)
