def slices(series, length):
    if len(series) < length or length < 1 :
        raise ValueError
    else :
        return list([int(x) for x in series[i:i+length]]
                      for i in range(len(series) - length + 1))


if __name__ == '__main__':
    print(slices('97867564',2))