from math import log, exp

def MMQlin(x, y):
    n = len(x)
    xy = [x[i]*y[i] for i in range(len(x))]
    x2 = [i**2 for i in x]
    sx = sum(x)
    sy = sum(y)
    sxy = sum(xy)
    sx2 = sum(x2)
    a = ((n*sxy)-(sx*sy))/((n*sx2)-(sx)**2)
    b = ((sxy*sx)-(sy*sx2))/((sx**2)-(n*sx2))
    return f'{a}*x {"+" if b >= 0 else "-"} {abs(b)}'

def MMQlog(x, y):
    n = len(x)
    sy = sum(y)
    lnx = [log(i) for i in x]
    slnx = sum(lnx)
    ylnx = [y[i]*lnx[i] for i in range(n)]
    sylnx = sum(ylnx)
    ln2x = [i**2 for i in lnx]
    sln2x = sum(ln2x)
    a = ((n*sylnx)-(slnx*sy))/((n*sln2x)-(slnx)**2)
    b = ((sylnx*slnx)-(sy*sln2x))/((slnx**2)-(n*sln2x))
    return f'{a}*ln(x) {"+" if b >= 0 else "-"} {abs(b)}'

def MMQexp(x, y):
    n = len(x)
    x2 = [i**2 for i in x]
    lny = [log(i) for i in y]
    xlny = [x[i]*lny[i] for i in range(n)]
    sx = sum(x)
    sx2 = sum(x2)
    slny = sum(lny)
    sxlny = sum(xlny)
    a = ((n*sxlny)-(sx*slny))/((n*sx2)-(sx)**2)
    b = ((sxlny*slny)-(slny*sx2))/((sx**2)-(n*sx2))
    eb = exp(b)
    return f'{eb}*exp({a}*x)'

def MMQpot(x, y):
    n = len(x)
    lnx = [log(i) for i in x]
    slnx = sum(lnx)
    lny = [log(i) for i in y]
    slny = sum(lny)
    xy = [lnx[i]*lny[i] for i in range(n)]
    slnxlny = sum(xy)
    ln2x = [i**2 for i in lnx]
    sln2x = sum(ln2x)
    a = ((n*slnxlny)-(slnx*slny))/((n*sln2x)-(slnx**2))
    b = ((slnx*slnxlny)-(slny*sln2x))/((slnx**2)-n*sln2x)
    eb = exp(b)
    return f'{eb}*x^{a}'