

def twoPtForwardDiff(x,y):
    """ This function takes the derivative of a segment of 
    points in the manner that if you pick a point 
    move to the next opint to the right this function will 
    take those points and gie you the derivative aka the slope """

    
    
    
   
    
    dy = np.diff(y)
    dx = np.diff(x)
    
    dydx = np.zeros(y.shape,float) # this makes the arrays the same size
    
    dydx[0:-1] = dy/dx
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx


def twoPtCenteredDiff(x,y):
    """ this function takes an initial point and takes the points 
    on either side of it and takes the derivative of the three points
    giving you the slope for the function at the chosen point"""

    
    
    
    dy = np.diff(y)  # array
    dy = np.diff(x)   #array
    dydx = np.zeros(y.shape,float)   # this makes the arrays the same size
    
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])  #center difference
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward dfference
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference

    
    
    return dydx
    
    

def fourPtCenteredDiff(x,y):
    """ the way this function works is ittakes a chosen point and then takes two 
    points in front of it and two points behind it and then takes the dirivitive 
    or the  slope of the line of best fit of the 5 points"""
    #dy = np.diff(y)
    #dx = np.diff(x)
    dydx = np.zeros(y.shape,float) # this makes the arrays the same size
    
    dydx[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/ (12*(x[2]-x[1]))
    
    
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward dfference
    dydx[1] = (y[2]-y[1])/(x[2]-x[1]) #forward dfference
   
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    dydx[-2] = (y[-2] - y[-3])/(x[-2] - x[-3]) #backward difference
    
    
    
   
    return dydx