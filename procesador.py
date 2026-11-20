import re
from collections import Counter

def contar_palabras(texto):
    """Cuenta las palabras en un texto."""
    palabras = texto.strip().split()
    return len(palabras)

def frecuencia_palabras(texto, top=5):
    """Retorna las top N palabras mas frecuentes."""
    palabras = re.findall(r'\w+', texto.lower())
    return dict(Counter(palabras).most_common(top))

def resumen(texto, max_chars=100):
    """Genera un resumen truncado del texto."""
    if len(texto) <= max_chars:
        return texto
    return texto[:max_chars].rsplit(' ', 1)[0] + '...'
