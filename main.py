nums_arr = list(range(10))
ops_arr = ["*", "/", "+", "-"]


def eval_oper(ops, nums):
    op = ops.pop()
    n1 = nums.pop()
    n2 = nums.pop()

    if op == "+":
        nums.append(n1 + n2)
    elif op == "-":
        nums.append(n2 - n1)
    elif op == "*":
        nums.append(n1 * n2)
    elif op == "/":
        if n1 == 0:
            raise ZeroDivisionError("error: divided by 0")
        nums.append(n2 / n1)

def priority(op):
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    return 0

def calculate(expr):
    expr = expr.replace(" ", "")

    nums = []
    ops = []
    k = 0

    while k < len(expr):
        if expr[k].isdigit() or expr[k] == ".":
            i = k

            while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                i += 1
            num = expr[k:i]

            try:
                if "." in num:
                    nums.append(float(num))

                else:
                    nums.append(int(num))

            except ValueError:
                raise ValueError(f"error: {num} - is not a number")

            k = i

            continue

        elif expr[k] == "(":
            ops.append(expr[k])

        elif expr[k] == ")":
            while ops and ops[-1] != "(":
                eval_oper(ops, nums)
            if ops and ops[-1] == "(":
                ops.pop()
            else:
                raise ValueError("error: expected '('")

        elif expr[k] in ops_arr:
            if expr[k] == "-" and (k == 0 or expr[k - 1] == "("):
                i = k + 1

                while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
                    i += 1
                num = expr[k:i]

                try:
                    if "." in num:
                        nums.append(float(num))
                    else:
                        nums.append(int(num))

                except ValueError:
                    raise ValueError(f"error: {num} - is not a number")

                k = i

                continue

            ops.append(expr[k])

            while ops != [] and ops[-1] != "(" and priority(ops[-1]) >= priority(expr[k]) and len(nums) >= len(ops) + 1:
                eval_oper(ops, nums)

        else:
            raise ValueError(f"error: {expr[k]} - is not recognised")

        k += 1

    while ops:
        if ops[-1] == "(":
            raise ValueError("error: expected ')'")
        eval_oper(ops, nums)

    if len(nums) != 1:
        raise ValueError("error: whole expression is not recognised")

    return nums[0]

expr = input("Enter expression: ").strip()

print(f"{expr} = {calculate(expr)}")
