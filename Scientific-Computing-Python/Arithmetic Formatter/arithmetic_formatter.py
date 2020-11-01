def arithmetic_arranger(problems,show=False):
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  arranged_problems = ''

  if len(problems) > 5:
    return "Error: Too many problems."
    
    
  for i in range(len(problems)):
    strip_problem = problems[i].split()
    num1 = strip_problem[0]
    num2 = strip_problem[2]
    operator = strip_problem[1]
    if operator != '+' and operator != '-':
        return "Error: Operator must be '+' or '-'."
    elif num1.isnumeric() == False or num2.isnumeric() == False:
        return "Error: Numbers must only contain digits."
    elif len(num1) > 4 or len(num2) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
        if operator == '+':
            result = str(int(num1) + int(num2))
        else:
            result = str(int(num1) - int(num2))
        length = max(len(num1),len(num2)) + 2
        line1 = line1 + num1.rjust(length)              + '    ' 
        line2 = line2 + (operator.ljust(1) + num2.rjust(length-1)) + '    ' 
        line3 = line3 + '-'*length                      + '    '
        line4 = line4 + result.rjust(length)            + '    '
    

  if show == False:
      arranged_problems =  line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip()
  else:
      arranged_problems =  line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + '\n' + line4.rstrip() 


  return arranged_problems
