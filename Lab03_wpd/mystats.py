def median(data):
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def trimmed_mean(data, p):
    if not data or not (0 <= p < 0.5):
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    k = int(n * p)
    trimmed_data = sorted_data[k : n - k]
    if not trimmed_data:
        return None
    return sum(trimmed_data) / len(trimmed_data)