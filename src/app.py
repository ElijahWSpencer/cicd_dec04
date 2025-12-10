def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    return a/b

def log (a, tolerance=1e-3, max_iterations=1000):
    if a <= 0:
        raise ValueError("ERROR: ln(a) undefined for a <= 0")
    
    b = a - 1
    
    for i in range(max_iterations):
        e_to_b = 1
        term = 1
        
        for n in range(1, 100):
            term *= b / n
            e_to_b += term
            
        b_new = b - (e_to_b - a) / e_to_b
        
        if abs(b_new - b) < tolerance:
            return b_new
        b = b_new
        
    raise RuntimeError("ERROR: Could not converge")

def square(a):
    return a*a

def sin(a, terms=20):
    pi = 3.141592
    a = ((a + pi) % (2 * pi)) - pi
    
    sine = 0
    num = a
    denom = 1
    sign = 1
    
    for n in range(terms):
        term = sign * num / denom
        sine += term
        sign *= -1
        num *= a * a
        denom *= (2 * n + 2) * (2 * n + 3)
    
    return sine

def cos(a, terms=20):
    pi = 3.141592
    a = ((a + pi) % (2 * pi)) - pi
    
    cosine = 0
    num = 1
    denom = 1
    sign = 1
    
    for n in range(terms):
        term = sign * num / denom
        cosine += term
        sign *= -1
        num *= a * a
        denom *= (2 * n + 1) * (2 * n + 2)
        
    return cosine

def sqrt (a, tolerance=1e-10, max_iterations=1000):
    if a < 0:
        raise ValueError("ERROR: Cannot calculate square root of negative number")
    if a == 0:
        return 0
    
    guess = a / 2
    
    for n in range(max_iterations):
        new_guess = 0.5 * (guess + a / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
        
    raise RuntimeError("ERROR: Could not converge")
    
def percent (a, b):
    return a / b * 100