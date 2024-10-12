import itertools as it


def find_str(iterator: list) -> list:
    return list(filter(lambda x: isinstance(x, str), iterator))


def fix_wiring(cables: list, sockets: list, plugs: list) -> list:
    return [f"plug {c} into {s} using {p}" if p else f"weld {c} into {s} without plug"
            for c, s, p in it.zip_longest(find_str(cables), find_str(sockets), find_str(plugs)) if all([c, s])]


if __name__ == "__main__":
    # case 1
    plugs1 = ['plug1', 'plug2', 'plug3']
    sockets1 = ['socket1', 'socket2', 'socket3', 'socket4']
    cables1 = ['cable1', 'cable2', 'cable3', 'cable4']
    for c in fix_wiring(cables1, sockets1, plugs1):
        print(c)

    print("------")

    # case 2
    plugs2 = ['plugZ', None, 'plugY', 'plugX']
    sockets2 = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables2 = ['cable2', 'cable1', False]
    for line in fix_wiring(cables2, sockets2, plugs2):
        print(line)


