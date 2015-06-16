# ----------------------------------------- Connectedness of a network ---------------------------------------- #
#                                                                                                               #
#       Here are the records from a busy telephone system with one million users:                               #
#                                                                                                               #
#                                       RecNr	Caller	Called                                                  #
#                                       1	200007	100053                                                  #
#                                       2	600183	500439                                                  #
#                                       3	600863	701497                                                  #
#                                       ...	...	...                                                     #
#                                                                                                               #
#       The telephone number of the caller and the called number in record n are Caller(n) = S2n-1 and          #
#       Called(n) = S2n where S1,2,3,... come from the "Lagged Fibonacci Generator":                            #
#                                                                                                               #
#                       For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)                     #
#                       For 56 ≤ k, Sk = [Sk-24 + Sk-55] (modulo 1000000)                                       #
#                                                                                                               #
#       If Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails;                #
#       otherwise the call is successful.                                                                       #
#                                                                                                               #
#       From the start of the records, we say that any pair of users X and Y are friends if X calls Y or        #
#       vice-versa. Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z;     #
#       and so on for longer chains.                                                                            #
#                                                                                                               #
#       The Prime Minister's phone number is 524287. After how many successful calls, not counting misdials,    #
#       will 99% of the users (including the PM) be a friend, or a friend of a friend etc.,                     #
#       of the Prime Minister?                                                                                  #
# ------------------------------------------------------------------------------------------------------------- #
import time

def genLaggedFibNumber():
    S = [0 for i in range(55)]
    
    for k in range(1, 55 + 1):
        S[k - 1] = (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000
        yield S[k - 1]

    while (1):
        k += 1
        Sk = (S[0] + S[31]) % 1000000
        S = S[1:] + [Sk]
        
        yield Sk

def telephone():
    g = genLaggedFibNumber()

    while (1):
        caller = next(g)
        called = next(g)

        while (caller == called):
            caller = next(g)
            called = next(g)

        yield caller, called

class Node(object):
    def __init__(self, v):
        self._value = v
        self._leader = self
        self._rank = 1
        self._size = 1

    @property
    def value(self):
        return self._value

    @property
    def leader(self):
        if (self._leader != self._leader._leader):
            self._leader = self._leader.leader
            
        return self._leader        

    @leader.setter
    def leader(self, l):
        self._leader = l

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, r):
        self._rank = r

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        self._size = s

def union(a, b):
    leaderA = a.leader
    leaderB = b.leader

    if (leaderA == leaderB):
        return

    if (leaderA.rank <= leaderB.rank):
        leaderA._leader = leaderB
        leaderB.size += leaderA.size
        leaderB.rank += 1
    else:
        leaderB._leader = leaderA
        leaderA.size += leaderB.size
        leaderA.rank += 1
    
def eu186():
    PM = 524287
    users = [Node(i) for i in range(10 ** 6)]

    i = 1

    p = telephone()
    
    while(1):
        caller, called = next(p)
        union(users[caller], users[called])

        if (users[PM].leader.size >= 0.99 * 10 ** 6):
            return i

        i += 1

if __name__ == "__main__":
    startTime = time.clock()
    print (eu186())
    elapsedTime = time.clock() - startTime
    print ("Time spent in (", __name__, ") is: ", elapsedTime, " sec")
