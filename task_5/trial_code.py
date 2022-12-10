infix_ex = input().replace("^--","^").replace("/--","/").replace("+-- ", "+")  .replace("*--","*").replace("---","-").replace("+- ", "-")
for i in range(len(infix_ex)):
    if infix_ex[:2] == "--":
        infix_ex = infix_ex[2:]
    else:
        infix_ex = infix_ex.replace("--",'+')

print(infix_ex)