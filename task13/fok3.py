g = {
    'А': 'Б',
    'Б': 'ДВ',
    'В': 'АГЕ',
    'Г': 'АЖ',
    'Д': 'ИВ',
    'Е': 'ДИКЖ',
    'Ж': 'В',
    'К': 'ВЖ',
    'Л': 'ИК',
    'И': 'К',
}


def f(s, p):
    if len(p) > 1 and p[-1] == p[0]:
        return 1
    if len(p) != len(set(p)):
        return 0
    return sum([f(v, p + v) for v in g[s]])


print(f('В', 'В'))