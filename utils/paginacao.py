import math


def make_pagination_range(
        range_pagina,
        qtd_paginas,
        pagina_atual,
):
    range_meio = math.ceil(qtd_paginas / 2)
    range_inicial = pagina_atual - range_meio
    range_final = pagina_atual + range_meio
    total_paginas = len(range_pagina)

    range_inicial_offset = abs(range_inicial) if range_inicial < 0 else 0

    if range_inicial < 0:
        range_inicial = 0
        range_final += range_inicial_offset

    if range_final > total_paginas:
        range_inicial = range_inicial = abs(total_paginas - range_final)

    paginacao = range_pagina[range_inicial:range_final]

    return {
        'paginacao': paginacao,
        'range_pagina': range_pagina,
        'qtde_paginas': qtd_paginas,
        'pagina_atual': pagina_atual,
        'total_paginas': total_paginas,
        'range_inicial': range_inicial,
        'range_final': range_final,
        'primeira_pagina_fora_do_range': pagina_atual > range_meio,
        'ultima_pagina_fora_do_range': range_final < total_paginas
    }
