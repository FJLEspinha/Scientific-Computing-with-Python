def arithmetic_arranger(problems, show_answers=False):
    if len(problems) >5:
        return 'Error: Too many problems.'
    
    operation = list(map(lambda sign: sign.split()[1], problems))
    if '*'  in operation or '/' in operation:
        return "Error: Operator must be '+' or '-'."
    
    first_number = list(map(lambda number: number.split()[0],problems))
    second_number = list(map(lambda number:number.split()[2],problems))

    if not all(map(lambda number: number.isdigit(),first_number)) or not all(map(lambda number:number.isdigit(),second_number)):
        return "Error: Numbers must only contain digits."
    
    if not all(map(lambda number:len(number)<5,first_number)) or not all(map(lambda number:len(number)<5,second_number)):
        return 'Error: Numbers cannot be more than four digits.'
    solution= []
    spaces = 4
    for i in range(len(first_number)):
        num1 = int(first_number[i])
        num2 = int(second_number[i])
        op = operation[i]
        result=0

        if op =='+':
            result = num1+num2
            solution.append(result)
        else:
            result= num1-num2
            solution.append(result)
    
    first_line=[]
    second_line=[]
    dash_line=[]
    result_line=[]
    for i in range(len(first_number)):
        if len(first_number[i]) > len(second_number[i]):
            first_line.append(" "*2+first_number[i])
        else:
            first_line.append(" "*(len(second_number[i])-len(first_number[i])+2)+first_number[i])

    for i in range(len(second_number)):
        if len(second_number[i])>len(first_number[i]):
            second_line.append(operation[i]+" "+second_number[i])
        else:
            second_line.append(operation[i]+" "*(len(first_number[i])-len(second_number[i])+1)+second_number[i])
    
    for i in range(len(first_number)):
        dash_line.append("-"*(max(len(first_number[i]),len(second_number[i]))+2))
    
    for i in range(len(first_number)):
        if len(str(solution[i])) > max(len(first_number[i]),len(second_number[i])):
            result_line.append(" "+str(solution[i]))
        else:
            result_line.append(" "*(max(len(first_number[i]),len(second_number[i]))-len(str(solution[i]))+2)+str(solution[i]))
    if show_answers==False:
        sol=(" "*spaces).join(first_line)+"\n"+(" "*spaces).join(second_line)+"\n"+(" "*spaces).join(dash_line)
    else:
        sol=(" "*spaces).join(first_line)+"\n"+(" "*spaces).join(second_line)+"\n"+(" "*spaces).join(dash_line)+"\n"+(" "*spaces).join(result_line)
    return sol

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print('**********************************************')
print(arithmetic_arranger(["3801 - 2", "123 + 49"],True)) #V
print('**********************************************')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49","123 + 49","123 + 49"])}') # V


