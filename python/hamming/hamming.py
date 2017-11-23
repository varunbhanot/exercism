def distance(strand_a, strand_b):
    if(len(strand_a) != len(strand_b)):
        raise ValueError
    count = 0
    loop = 0
    for c in strand_a:
        if strand_b[loop] != c:
            count+=1
        loop+=1
    return count

