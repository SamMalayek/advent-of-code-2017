
def main():
    lines = open('day08.txt', 'r').read().splitlines()
    register = {}
    values = []

    # eval() does not like undefined dict keys, even if using defaultdict.
    # It must only be used for evaluating expressions.
    for l in lines:
        key, _ = l.split(maxsplit=1)
        register[key] = 0

    for l in lines:
        key, operator, rest = l.split(maxsplit=2)
        for curKey in register.keys():
            rest = rest.replace(f' {curKey} ', f' register["{curKey}"] ')

        toEval = f'({rest} else 0)'

        # eval() does not like += and -= because they are augmented assignment statements.
        # It must only be used for evaluating expressions.
        if operator == 'inc':
            register[key] += eval(toEval)
        else:
            register[key] -= eval(toEval)

        eval(toEval, {}, {'register': register})
        values.append(max(register.values()))

    print(max(values))


if __name__ == "__main__":
    main()
