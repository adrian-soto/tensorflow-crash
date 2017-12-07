import numpy as np




def torus(theta, phi, R, r):
    '''
    
    '''

    if R<=r:
        print "ERROR: R must be larger than r"
        pass
    
    else:
        x = (R + r*np.cos(theta))*np.cos(phi)
        y = (R + r*np.cos(theta))*np.sin(phi)
        z = r*np.sin(phi)
        return (x,y,z)




def inside_torus(point, R=3, r=2):
        
    # distance to z-axis
    u = np.sqrt(point[0]**2 + point[1]**2)
    
    if u < 1.0E-07:
        # point is along z-axis
        return 0
    
    else:
        # project point to point-z plane: (u,v)
        v = point[2]
        
        # translate u by R
        u = u - R
        
        # Check if (u,v) inside circle of radius r
        if u**2 + v**2 > r**2:
            return 0
        else:
            return 1
    


# ### Umbilic torus

# In[12]:

def umbilic_torus(u,v):
    
    x = np.sin(u)*(
    7 + np.cos((u/3.0)-2.0*v) + 2.0*np.cos((u/3.0)+v)
    )
    
    y = np.cos(u)*(
    7 + np.cos((u/3.0)-2.0*v) + 2.0*np.cos((u/3.0)+v)
    )
    
    z = np.sin((u/3.0)-2.0*v) + 2.0*np.cos((u/3.0)+v)
    
    return (x,y,z)
