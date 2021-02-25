// program to calculate simple interest



def simple_interest(p,t,r):
    print('Principal Amount is', p)
    print('Total Time ', t)
    print('Interest Rste',r)

    si = (p * t * r)/100

    print('Simple Interest ', si)
    return si

# Driver code
simple_interest(8, 6, 8)
