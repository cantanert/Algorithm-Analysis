fibb(0) = 0, fibb(1) = 1; fibb(n) = fibb(n-1) + fibb(n-2)

Obvious algorithm:
Code (precondition: n ≥ 0):
    fibb(n)
        if n < 2
            return n
        else
            return fibb(n-1) + fibb(n-2)
    

//T(n)=Θ(fibb(n)
//fibb(n)≃1.6n
//---------------------------------------------------------------
//Recursive uses memoization

        fib(n):
            A: Array(0..n) of Natural := (0=>0, 1=>1, others=>0);
            return fib-aux(n, A)

        fib-aux(n, A: in out array):
                if A(n) = 0 and then n /= 0 then       -- Check if A(n) is calculated yet

                    A(n) := fib-aux(n-1, A) + A(n-2);  -- Store solution

                end if;
            end if
            return A(n)                                -- Return solution

        client:
            put(fib(5));
        
//We arrange the recursion so that A(n-2) is calculated before it is needed
