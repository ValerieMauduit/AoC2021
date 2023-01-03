def sliding_windows(data, size=3):
    # Returns the list of the sub-lists of a given span in an ordered list
    return [[data[n + p] for p in range(size)] for n in range(len(data) - size + 1)]
