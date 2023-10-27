
def main():
    lines = open('day08.txt', 'r').read().splitlines()
    register = {}

    for l in lines:
        key, _ = l.split(maxsplit=1)
        register[key] = 0

    for l in lines:
        key, rest = l.replace('inc ', '+= (').replace('dec ', '-= (').split(maxsplit=1)
        for curKey in register.keys():
            rest = rest.replace(f' {curKey} ', f' register["{curKey}"] ')

        toEval = 'register["' + key + '"] ' + rest + ' else 0)'

        exec(toEval, {}, {'register': register})

    print(max(register.values()))


if __name__ == "__main__":
    main()
