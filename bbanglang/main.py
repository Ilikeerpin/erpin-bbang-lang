import re
def cs(n: int) -> str:
    return f"+{n}" if n > 0 else str(n)
def pe(expression):
    expression = expression.replace(" ", "")
    tokens = []
    token = ""
    ah_group = {"ㅋ": [], "*": [], "&": []}

    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit() or (char == '-' and (i == 0 or expression[i - 1] in "+-*/")):
            token += char
        elif char == "ㅋ": 
            start = i
            while i < len(expression) and expression[i] == "ㅋ":
                i += 1
            count = i - start
            group_key = "ㅋ" * count
            ah_group["ㅋ"].append(group_key)
            tokens.append(group_key)
            continue
        elif char == "*":
            start = i
            while i < len(expression) and expression[i] == "*":
                i += 1
            count = i - start
            group_key = "*" * count
            ah_group["*"].append(group_key)
            tokens.append(group_key)
            continue
        elif char == "&": 
            start = i
            while i < len(expression) and expression[i] == "&":
                i += 1
            count = i - start
            group_key = "&" * count
            ah_group["&"].append(group_key)
            tokens.append(group_key)
            continue
        else:
            if token:
                tokens.append(token)
                token = ""
            tokens.append(char)
        i += 1
    
    if token:
        tokens.append(token)

    return tokens
def cn(expression):
    expression = expression.replace(" ", "")
    if not expression:
        return 0 

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    operator_stack = []
    operand_stack = []
    tokens = []
    token = ""
    
    for i, char in enumerate(expression):
        if char.isdigit() or (char == '-' and (i == 0 or expression[i - 1] in "+-*/")):
            token += char
        else:
            if token:
                tokens.append(token)
                token = ""
            tokens.append(char)
    if token:
        tokens.append(token)

    for token in tokens:
        if token.lstrip('-').isdigit():
            operand_stack.append(int(token))
        elif token in "+-*/":
            while operator_stack and precedence[operator_stack[-1]] >= precedence[token]:
                operator = operator_stack.pop()
                if len(operand_stack) < 2:
                    operand1 = 0 if not operand_stack else operand_stack.pop()
                    operand2 = 0 if not operand_stack else operand_stack.pop()
                else:
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()

                if operator == "+":
                    operand_stack.append(operand1 + operand2)
                elif operator == "-":
                    operand_stack.append(operand1 - operand2)
                elif operator == "*":
                    operand_stack.append(operand1 * operand2)
                elif operator == "/":
                    operand_stack.append(operand1 / operand2 if operand2 != 0 else float('inf'))
            operator_stack.append(token)

    while operator_stack:
        operator = operator_stack.pop()
        if len(operand_stack) < 2:
            operand1 = 0 if not operand_stack else operand_stack.pop()
            operand2 = 0 if not operand_stack else operand_stack.pop()
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

        if operator == "+":
            operand_stack.append(operand1 + operand2)
        elif operator == "-":
            operand_stack.append(operand1 - operand2)
        elif operator == "*":
            operand_stack.append(operand1 * operand2)
        elif operator == "/":
            operand_stack.append(operand1 / operand2 if operand2 != 0 else float('inf'))

    return operand_stack[0] if operand_stack else 0

def run(file1):
    with open(file1, "r", encoding="utf-8") as file:
        han = file.read()
        hanl = han.splitlines()
        global val
        val = {}
        end="\n"
        for j in hanl:
            j.replace("빵","")
            al = ""
            if j.startswith("빠"):
                hcount = j.count("아")
                if j[hcount + 1] == "앙":
                    if j[hcount + 2:].startswith("당떨어져서그래~"):
                        ins2 = j[hcount + 10:]
                        ins2 = pe(''.join(ins))
                        for i in ins2:
                            if  "*" in i:
                                if not al:
                                    al += cs(i.count("*"))
                                elif (al[-1] == "/" or al[-1] == "*"):
                                    al += str(i.count("*"))
                                else:
                                    al += cs(i.count("*"))
                            elif "&" in i:
                                if not al:
                                    al += cs(i.count("&"))
                                elif (al[-1] == "/" or al[-1] == "*"):
                                    al += str(i.count("&"))
                                else:
                                    al += cs(i.count("&"))
                            elif i == "@":
                                al = al + "*"
                            elif i == "!":
                                al = al + "/"
                            elif i == "^":
                                al = al+"+"
                            elif i =="#":
                                al = al+"-"
                        val[hcount] = chr(cn(al[1:]))
                        al=""
                        continue
                global last
                last = ""
                acount = 0
                j = j[2:]
                j2 = j
                j = pe("".join(j))
                for i in j:
                    if "배고파~" in j2:
                        inp = int(input())
                        al += cs(inp)
                        break
                    if  "*" in i:
                        if not al:
                            al += cs(i.count("*"))
                        elif (al[-1] == "/" or al[-1] == "*"):
                            al += str(i.count("*"))
                        else:
                            al += cs(i.count("*"))
                    if "&" in i:
                        if not al:
                            al += cs(i.count("&"))
                        elif (al[-1] == "/" or al[-1] == "*"):
                            al += str(i.count("&"))
                        else:
                            al += cs(i.count("&"))
                    if i == "@":
                        al = al + "*"
                    if i == "!":
                        al = al + "/"
                    if i == "^":
                        al = al+"+"
                    if i =="#":
                        al = al+"-"
                    if "ㅋ" in i:
                        aacount = i.count("ㅋ")
                        al+=str(val[aacount])
                val[hcount] = cn(al)
                al=""
            elif j.startswith("교주~"):
                ins = j[3:]
                ins = pe("".join(ins))
                al1 = ""
                for i in ins:
                    if  "*" in i:
                        if not al:
                            al += cs(i.count("*"))
                        elif (al[-1] == "/" or al[-1] == "*"):
                            al += str(i.count("*"))
                        else:
                            al += cs(i.count("*"))
                    if "&" in i:
                        if not al:
                            al += cs(i.count("&"))
                        elif (al[-1] == "/" or al[-1] == "*"):
                            al += str(i.count("&"))
                        else:
                            al += cs(i.count("&"))
                    if i == "@":
                        al1 = al1 + "*"
                    if i == "!":
                        al1 = al1 + "/"
                    if i == "^":
                        al1+="+"
                    if i =="#":
                        al1 = al1+"-"
                    if "ㅋ" in i:
                        aacount = i.count("ㅋ")
                        al1+=str(val[aacount])
                print(cn(al1),end=end)
                end="\n"
            elif j.startswith("배고파~"):
                inp = input()
            elif j.startswith("당떨어져서그래~"):
                ins = j[7:]
                ins = pe(''.join(ins))
                if ins:
                    al1 = ""
                    for i in ins:
                        if  "*" in i:
                            if not al1:
                                al1 += cs(i.count("*"))
                            elif (al1[-1] == "/" or al1[-1] == "*"):
                                al1 += str(i.count("*"))
                            else:
                                al1 += cs(i.count("*"))
                        if "&" in i:
                            if not al1:
                                al1 += cs(i.count("&"))
                            elif (al1[-1] == "/" or al1[-1] == "*"):
                                al1 += str(i.count("&"))
                            else:
                                al1 += cs(i.count("&"))
                        if i == "@":
                            al1 = al1 + "*"
                        if i == "!":
                            al1 = al1 + "/"
                        if i == "^":
                            al1+="+"
                        if i =="#":
                            al1 = al1+"-"
                        if "ㅋ" in i:
                            aacount = i.count("ㅋ")
                            al1+=str(val[aacount])
                    print(chr(cn(al1)),end=end)
                    # print(chr(cn(al1)),end=end)
                    end="\n"
            elif j.startswith("네르~"):
                end = ""
            elif not j.startswith("당떨어져서그래~") and not j.startswith("배고파~") and not j.startswith("교주~") and not j.startswith("빠") and j.startswith("네르~") and j:
                raise RuntimeError("이게 어떻게 빠아앙이냐!")
