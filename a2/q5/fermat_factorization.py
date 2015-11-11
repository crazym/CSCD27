import math
import gmpy2
def FermatFacotorization(n):
    # a = math.ceil(math.sqrt(N))
    N = gmpy2.mpz(n)
    gmpy2.get_context().precision = 2048
    a = gmpy2.sqrt(N)
    # print a
    b2 = a**2 - N
    # print b2
    while not is_sqr(b2):
        a += 1
        b2 = a**2 - N
	print a
    print "a is " + str(a)
    print "b2 is " + str(b2)
    # a = math.sqrt(a2)
    b = math.sqrt(b2)
    return (a+b, a-b)
def is_sqr(integer):
    return gmpy2.sqrt(integer) %1 == 0

def is_square(integer):
    itg = gmpy2.mpz(integer)
    gmpy2.get_context().precision = 2048
    root = gmpy2.sqrt(itg)
    # root = math.sqrt(integer)
    if int(root) ** 2 == integer: 
        return True
    else:
        return False

n = 160589551961873197828445495034570233363247818671691660589162331874420605817572168663844611732210826017325788763868930210440223836474839418256961011937199856444619784403234362611820562816346568692454930228130352012152251747388396591243103393766491148902701037590468059675856469998354735584903579056642573592659

N = 5959
print FermatFacotorization(n)
