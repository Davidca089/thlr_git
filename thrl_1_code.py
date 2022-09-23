
#[Q9]

def union(E,F):
    res = set() 
    for x in E:
        res.add(x)

    for y in F:
        res.add(y)

    return res

#[/Q9]

#[Q10]


def intersection(E,F):
    res = set() 
    for x in E:
        if x in F:
            res.add(x)

    for y in F:
        if y in E:
            res.add(y)

    return res
#[/Q10]

#[Q11]


def subtraction(E,F):
    res = set() 
    for x in E:
        if x not in F:
            res.add(x)

    return res

#[/Q11]

#[Q12]

def diff(E,F):
    res = set() 
    for x in E:
        if x not in F:
            res.add(x)

    for y in F:
        if y not in E:
            res.add(y)
    return res

#[/Q12]

#[Q13]

def sublists(L):

    res = []
    if L == []:
        return [[]]
    
    S = sublists(L[1:])
    for s in S:
        res.append(s)
        res.append([L[0]] + s)

    return res 



#[/Q13]

#[Q14]

def power_set(E):
    s = sublists(list(E))
    return [set(i) for i in s] 


#[/Q14]


