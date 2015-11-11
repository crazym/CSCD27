def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    print('a=',a)
    print('b=',b)
    print('p=',p)
    print('q=',q)
    print('pq=',p*q)
    return p, q

N=103591*104729
n = 160589551961873197828445495034570233363247818671691660589162331874420605817572168663844611732210826017325788763868930210440223836474839418256961011937199856444619784403234362611820562816346568692454930228130352012152251747388396591243103393766491148902701037590468059675856469998354735584903579056642573592659
fermat(n)
