paths = [["B", "C"], ["D", "B"], ["C", "A"]]
paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]


if len(paths) == 1:
    print(paths[0][-1])
else:
    from_list = set()
    to_list = set()
    for path in paths:
        from_list.add(path[0])
        to_list.add(path[1])

    res = to_list - from_list
    res.pop()


sources = set([path[0] for path in paths])
for path in paths:
    if path[1] not in sources:
        print(path[1])
