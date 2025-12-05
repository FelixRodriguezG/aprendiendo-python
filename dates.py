# 10. Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.

from datetime import datetime
def get_current_date():
    return datetime.now()

def date_difference(date1, date2):
    return abs((date2 - date1).days)