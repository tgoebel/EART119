#python2.7
"""
    - optimization fct for root finding and finding minima of fct.
      and data fitting
    --> also implemented in:
            scipy.optimize
"""
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                           data fitting
#===================================================================================
def lin_LS( aX, aY):
    """
    - linear least squares assuming normal distributed errors in Y, no errors in X

    :param aX: - independent variable
    :param aY: - measured dependent variable

    :return: { 'a' :  float( <intercept>),
               'b' :  float( <slope>),
               'R2 :  float(), #coefficient of variation = r_p**2 for lin. regre
               'r_p:  float(), # correlation coefficient (Pearson)

               'Y_hat' : np.array(), # modeled values of aY using a and b
            }

    example:   TODO:
    """
    dLS   = {}
    N     = len(aX)
    if len( aX) != len( aY):
        error_str = 'input variable need to have same dimensions %i, %i'%( len( aX), len( aY))
        raise ValueError, error_str
    meanX = aX.mean()
    meanY = aY.mean()
    # variance and co-variance - 1./N term omitted because it cancels in the following ratio
    VarX  = ( (aX - meanX)**2).sum()
    VarY  = ( (aY - meanY)**2).sum()
    CovXY = ( (aY-meanY)*(aX-meanX)).sum()

    # slope and intercept, and fit
    dLS['b'] = CovXY/VarX
    dLS['a'] = meanY - meanX*dLS['b']
    dLS['Y_hat'] = dLS['b']*aX + dLS['a']
    # goodness-of-fit
    ResSS    = ( ( dLS['Y_hat'] - aY)**2).sum()
    dLS['R2']= 1 - ResSS/VarY
    # correlation coefficient
    dLS['r_p'] = 1./N*CovXY/(aX.std()*aY.std())
    return dLS


def lin_MLE( aX, aY,  **kwargs):
    """ Maximum Likelihood for lin. model
    :Input
       aX - independent variable
       aY - observation with Gaussian uncertainty around best linear fit
       kwargs: b1_min, b1_max - bounds of slope for grid search
                              - default: 0.2 to 300
                sigma         - stdDev of Gaussian, default stdDev( aY)
              showPlot        - plot log likelihood fct.
    :output
         { 'b1'   : float - best-fitting slope 
           'b2'   : float - y-intercept
           'logL' : float - likelihood of best fit
           'uncer': np.array([2.5, 97.5]), - 2.5 and 97.5 confidence bound
         }  
    """
    #--------------------set params for grid search---------------------------------------------------------- 
    b1_min, b1_max = 0.2, 250
    b2_min, b2_max = -10, 10
    sigma          = 1  #aY.std()  # or 1?
    if 'b1_min' in kwargs.keys() and kwargs['b1_min'] is not None:
        b1_min = kwargs['b1_min']
    if 'b1_max' in kwargs.keys() and kwargs['b1_max'] is not None:
        b1_max = kwargs['b1_max']
    if 'b2_min' in kwargs.keys() and kwargs['b2_min'] is not None:
        b2_min = kwargs['b2_min']
    if 'b2_max' in kwargs.keys() and kwargs['b2_max'] is not None:
        b2_max = kwargs['b2_max']
    if 'sigma' in kwargs.keys() and kwargs['sigma'] is not None:
        sigma = kwargs['sigma']
    # make sure slope is not < 0
    if b1_min < 0:
        b1_min = 0
    if b1_max < 0:
        b1_max = 5
    if b2_max > 10:
        b2_max = 10
        b2_min = 0
    print b2_min, b2_max
    print b1_min, b1_max
    # range of expected slopes
    a_b1 = np.arange( b1_min, b1_max, .1)
    a_b2 = np.arange( b2_min, b2_max, .1) # in days
    print 'size of param vector for grid search: ', len( a_b1), 'x',len( a_b2)
    m_logL = np.zeros( ( len( a_b1), len(a_b2)), dtype = float)

    #--------------A--------------grid search to find MLE-------------------------------------------------- 
    for j in xrange( len( a_b2)):
        for i in xrange( len(a_b1)):
            # linear model expected value
            aY_hat =  a_b1[i]*( aX + a_b2[j])
            # log L of aY given b and sigma
            m_logL[i,j] = gauss1d_logL( aY, aY_hat, sigma)

    #--------------B solution and confidence---------------------------------------------------------------- 
    sel = m_logL == m_logL.max()
    mb2,mb1 = np.meshgrid( a_b2, a_b1)
    #TODO: confidence interval!!
    # find 2.5 and 97.5 confidence for each aY and plug into Gaussian logL 
    
    if 'showPlot' in kwargs.keys() and kwargs['showPlot'] == True:
        plt.figure()
        ax = plt.axes( [.15,.15,.8,.8])
        ax.set_title( 'b1=%.1f,b2=%.1f, logL = %.2f'%(mb1[sel][0], mb2[sel][0], m_logL.max()))
        plot1 = ax.pcolor( mb1, mb2, m_logL)
        cb1 = plt.colorbar(plot1, orientation = 'vertical')
        cb1.set_label( '$\log L$', rotation = 0, fontsize = 16,labelpad=-30, y=1.15)
        ax.set_ylabel( 'Intercept, b2')
        ax.set_xlabel( 'Slope, b1')
        plt.show()
    return { 'b1' : mb1[sel][0], 'b2' : mb2[sel][0],  'logL' : m_logL.max()}

def gauss1d_logL( aY, aY_hat, sigma):
    """ log likelihood fct for aY given parameters that lead to expected values, aMu
        input:   aY   - observation, e.g. distance or number of events
                aY_hat- expected value based on model and specific set of parameter choices
                sigma - stdDev of normal distribution, e.g. stdDev( aY) 
    """
    n = aY.shape[0]
    return -n/2*np.log10(2*np.pi) - n*np.log10( sigma) - 1/(2*sigma**2)*np.sum( (aY-aY_hat)**2)
#===================================================================================
#                            Newton and Secant method
#===================================================================================
def my_Newton( fct, df_dt, x0, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0
    """
    xn = float( x0)
    i  = 0
    while abs( fct( xn)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        x_next = xn - fct( xn)/df_dt( xn)
        print i, abs( fct( xn)), x_next
        xn = float( x_next)
        i += 1
    if abs( fct( xn)) > tol:# no solution found
        return None
    else:
        return float( x_next)

def my_Secant( fct, x0, x1, tol = 1e-4, N = 20):
    """
    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0, x1:  - interval for first secant estimate, with x0 close to root
    :param N:       - number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4

              x_n+1 = (x_n - f(x_n))*[( x_n - x_n-1) / (f(x_n) - f(x_n-1))]
        with: x_n+1 = x_next
              x_n   = x1
              x_n-1 = x0
    :return: f_r0 - root between x0 and x1
    """
    x0 = float( x0)
    x1 = float( x1)
    i  = 0
    while abs( fct( x1)) > tol and i < N: # could also set fct. to ~0 to find root instead of min.
        df_dt  = float(fct( x1)-fct( x0))/(x1-x0)
        x_next = x1 - fct( ( x1))/df_dt
        print i, abs( fct( x1)), x_next
        x0 = x1
        x1 = x_next
        # update variables at new step
        i += 1
    if abs( fct( x1)) > tol: # no solution found
        return None
    else:
        return float( x_next)

#===================================================================================
#                           finding minima and maxima
#===================================================================================

def my_fmin(  dfdx, x0, tol = 1e-5, N = 10000):
    """
    from https://en.wikipedia.org/wiki/Gradient_descent
      x_n+1 = x_n - gamma_n grad( f(xn))

    :param fct:     - find root of this fct. closes to x0
    :param dfct_dt: - derivatice of fct
    :param x0:      - initial guess of solution
    :param N:       - max. number of iterations, default = 20
    :param tol:     - tolerance, default = 1e-4
    :return: f_r0 - closest to x0

    benchmark:
        def fct( x):
            return x**4 - 3*x**3 + const
            #return x**2 - 9

        def dfdx( x):
            return 4 * x**3 - 9 * x**2

        return: ('Minimum at', 2.2499646074278457)
    """
    next_x = x0  # We start the search at x=6
    gamma  = 0.01  # Step size multiplier
    i      = 0
    step   = tol+1
    while abs(step) > tol and i <  N:
        current_x = next_x
        next_x = current_x - gamma * dfdx(current_x)
        step = next_x - current_x
        i += 1
    return next_x