
def bisection_method(f,xi,xf,tol):

    if ( f(xi)*f(xf)>=0 ) :
        return "Choose correct initial values" 
    while( (xf-xi)> tol):
        m=(xi+xf)/2.0

        if ( f(m)*f(xi) > 0 ):
            xi=m

        if (  f(m)*f(xi) < 0 ):
            xf=m

        if ( f(m)*f(xi) == 0 ):
            break
    return m


def false_position_method(f,xi,xf,tol):
    if ( f(xi)*f(xf)>=0 ) :
        return "Choose correct initial values" 
    xr=1
    while(1):
        xr= (xi*f(xf) - xf*f(xi))/(f(xf)-f(xi))

        if( f(xr)>0 ):
            xf=xr
        if( f(xr)<0 ):
            xi=xr
        if( f(xr)==0 or abs(f(xr))<tol ):
            break 
    return xr


def calculate_percent_error(calculated,real):
    return (abs(calculated-real)/real)*100


def f(x):
    return x*x-3



tolerance=1e-6
#i choose initial values 0 and 5
a=0 
b=5
exact_solution= float(f"{3**0.5:.6}")  # to become 6 significant figure

bisection_solution = bisection_method(f,a,b,tolerance)

print(f"Bisection Solution: {bisection_solution}",)

false_position_solution= false_position_method( f,a,b,tolerance )

print(f"False Method Solution: {false_position_solution}",)

bisection_error = calculate_percent_error(bisection_solution,exact_solution)
false_position_error = calculate_percent_error(false_position_solution,exact_solution)

print(f"Error in bisection : % {bisection_error}")

print(f"Error in false position : % {false_position_error}")
