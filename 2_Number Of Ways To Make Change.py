def numberOfWaysToMakeChange(n, denoms):
    times = 0
    zero = 0
    for i in range(len(denoms)):
        if n%denoms[i]==0:
                times +=1
                zero +=1
        elif n%denoms[i] in denoms:
                times +=1
    if zero == 2:
        times +=1
    if sum(denoms) == n:
        times +=1
    return times


print(numberOfWaysToMakeChange(6, [1, 5]))











