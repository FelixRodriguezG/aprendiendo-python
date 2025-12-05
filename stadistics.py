# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.

def average(list_numbers):
    """Calcula la media de una lista de números."""
    if not list_numbers:
        return 0
    return sum(list_numbers) / len(list_numbers)

def median(list_numbers):
    """Calcula la mediana de una lista de números."""
    sorted_numbers = sorted(list_numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]