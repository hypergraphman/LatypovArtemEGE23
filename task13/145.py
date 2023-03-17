g = {
    'А': 'ГД',
    'Б': 'АВЖ',
    'В': 'А',
    'Г': 'ЕД',
    'Д': 'Е',
    'Е': 'БВЖЗ',
    'Ж': 'ЗИ',
    'З': 'И',
    'К': 'ЕЛ',
    'Л': 'ЕД',
    'И': 'КЛ',
}


def f(s, p):
    if len(p) > 1 and p[-1] == p[0]:
        return 1
    if len(p) != len(set(p)):
        return 0
    return sum([f(v, p + v) for v in g[s]])


print(f('Е', 'Е'))