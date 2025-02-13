g_terra = 9.8
g_lua = 1.6

def pesoLua(massa):
    p_lua = g_lua*massa
    return p_lua

def pesoTerra(massa):
    p_terra = g_terra*massa
    return p_terra