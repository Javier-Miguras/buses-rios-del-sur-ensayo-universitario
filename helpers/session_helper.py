import builtins

# Inicializa una variable global en el módulo builtins
if not hasattr(builtins, "session"):
    builtins.session = {}

def set_session(key, value):
    builtins.session[key] = value

def get_session(key):
    return builtins.session.get(key)

def clear_session():
    builtins.session.clear()
