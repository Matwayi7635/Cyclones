import netCDF4
import numpy as np
from matplotlib import pyplot as plt

def ncdump(nc_fid, verb=True):
    '''
    ncdump outputs dimensions, variables and their attribute information.
    The information is similar to that of NCAR's ncdump utility.
    ncdump requires a valid instance of Dataset.

    Parameters
    ----------
    nc_fid : netCDF4.Dataset
        A netCDF4 dateset object
    verb : Boolean
        whether or not nc_attrs, nc_dims, and nc_vars are printed

    Returns
    -------
    nc_attrs : list
        A Python list of the NetCDF file global attributes
    nc_dims : list
        A Python list of the NetCDF file dimensions
    nc_vars : list
        A Python list of the NetCDF file variables
    '''
    def print_ncattr(key):
        """
        Prints the NetCDF file attributes for a given key

        Parameters
        ----------
        key : unicode
            a valid netCDF4.Dataset.variables key
        """
        try:
            print ("\t\ttype:"), repr(nc_fid.variables[key].dtype)
            #print '\t\ttype:', repr(nc_fid.variables[key].dtype)
            for ncattr in nc_fid.variables[key].ncattrs():
                print ('\t\t%s:') % ncattr,\
                      repr(nc_fid.variables[key].getncattr(ncattr))
        except KeyError:
            print ("\t\tWARNING: %s does not contain variable attributes") % key

    # NetCDF global attributes
    nc_attrs = nc_fid.ncattrs()
    if verb:
        print ("NetCDF Global Attributes:")
        for nc_attr in nc_attrs:
            print ('\t%s:') % nc_attr, repr(nc_fid.getncattr(nc_attr))
    nc_dims = [dim for dim in nc_fid.dimensions]  # list of nc dimensions
    # Dimension shape information.
    if verb:
        print ("NetCDF dimension information:")
        for dim in nc_dims:
            print ("\tName:"), dim 
            print ("\t\tsize:"), len(nc_fid.dimensions[dim])
            print_ncattr(dim)
    # Variable information.
    nc_vars = [var for var in nc_fid.variables]  # list of nc variables
    if verb:
        print ("NetCDF variable information:")
        for var in nc_vars:
            if var not in nc_dims:
                print ('\tName:'), var
                print ("\t\tdimensions:"), nc_fid.variables[var].dimensions
                print ("\t\tsize:"), nc_fid.variables[var].size
                print_ncattr(var)
    return nc_attrs, nc_dims, nc_vars


def wrf_unstagger( grid, dim ):
    """ Unstagger a staggered WRF grid in the X, Y, or Z (U, V, or W) direction.
        ---------------------
        grid (numpy.ndarray): The 2D, 3D, 4D, or 5D array to be unstaggered.
        dim (str): A string specifying what dimension to unstagger. Must be
        X, Y, Z, U, V or W.
        ---------------------
        returns:
        numpy.ndarray unstaggered grid (dim-1)
        ---------------------
        EXAMPLE:
        import numpy as np

        arr = np.random.randint( low=1, high=10, size=( 9,10,9 ) ) ## create a random array staggered in the Y direction
        arr_unstaggered = wrf_unstagger( arr, 'Y' )
        """
    nd = len( grid.shape )
    if dim == 'X' or dim == 'U':
        if nd == 4:
            gridout = ( grid[ :, :, :, :-1 ] + grid[ :, :, :, 1: ] ) / 2.
        else: pass
    if dim == 'Y' or dim == 'V':
        if nd == 4:
            gridout = ( grid[ :, :, :-1, : ] + grid[ :, :, 1:, : ] ) / 2.
        else: pass
    if dim == 'Z' or dim == 'W':
        if nd == 4:
            gridout = ( grid[ :, :-1, :, : ] + grid[ :, 1:, :, : ] ) / 2.
        else: pass
    return gridout



def wrf_pres(P,PB):
    return (P+PB) #in Pa

def wrf_height(PH,PHB):
    return (PH+PHB)/9.81

def wrf_theta(PTEMP):
    return (PTEMP+300.)

def wrf_temp(THETA,PRES):
    return (THETA)*(PRES/1000.)**(.2854) # in hPa


def wrf_rh(TEMP,PRES,MXRAT):
    A= 6.11*100. #Pa
    Rv = 461.495 #J/kg/K
    Lv = 2.453*10**6 #J/Kg
    
    ES = A*np.exp((Lv/Rv)*((1./273.)-(1./TEMP))) #in Pa
    SMXRAT = ((621.97*ES)/(PRES-ES))/1000.
    return (MXRAT/SMXRAT)*100.



def get_wrf_var(var,file_path):
    '''
    Requirements: 
    import netCDF4
    
    This function will read in a wrf file and the desired variable 
    The input is the variable name and the location of the file
    The output is an array of the desired variable in the native units
    example: get_wrf_var('PSFC','/location/to/file')    
    '''
    ncfile = netCDF4.Dataset(file_path,mode='r')
    ncvar = ncfile.variables[var][:]
    ncfile.close()
    return ncvar



def pres_interp(var,surface,new_height): 
    '''
    Takes a wrf variable like u,v,w, and/or mixing ratios and linearly interpolates it to pressure surfaces
    
    input: variable with 4D (time, height, x, y), the pressure surface as the same 4D variable, and the pressure
    levels that you want to interpolate to
    output: variable with 4D (time, new height, x, y)
    
    import numpy as np
    
    Note: np.interp requires the arrays to be increasing, so since we are interpolating to pressure coords
    we have to reverse the direction
    '''
    
    #######################
    #These are the pressure levels to interpolate to if you want to define them here
    #new_height = np.array([1000,850,700,500,200,100]) 
    #######################
    
    new_surf = np.empty((var.shape[0],new_height.shape[0],var.shape[2],var.shape[3]))

    for TIM in np.arange(var.shape[0]): #Loop over all the time periods
        for IDX, VAL in np.ndenumerate(var[0][0]): #Loop over all the points
            new_val = np.interp(new_height,surface[TIM,::-1,IDX[0],IDX[1]],var[TIM,::-1,IDX[0],IDX[1]], right=np.nan)
            new_surf[TIM,:,IDX[0],IDX[1]]=new_val[:] #put the interpolated profile into the new array
    return new_surf
filename = 'wrfout_d01_2019-03-08:00:00:00'
######################################################wrfout_d01_2019-03-08:00:00:00##########


ncfile = netCDF4.Dataset(filename,'r')

#Get the horizontal grid
LAT = ncfile.variables['XLAT'][:]
LON = ncfile.variables['XLONG'][:]

#Get Base Pressure, Perturbation Pressure, and combine them
P = ncfile.variables['P'][:]
PB = ncfile.variables['PB'][:]
PRES = wrf_pres(P,PB)/100. #Divide by 100 to get hPa

#Get perturbation potential temperature, add 300K, and convert to temperature
THETA = ncfile.variables['T'][:]
THETA = wrf_theta(THETA)
TEMP = wrf_temp(THETA,PRES)


#Get some variables
WVMIX = ncfile.variables['QVAPOR'][:]
U = ncfile.variables['U'][:]
V = ncfile.variables['V'][:]
#W = ncfile.variables['W'][:]

#Because of the C-staggered grid in WRF we need to get the velocities centered at the mass points of the grid boxes
#We can do this by averaging the 2 closest grid points to get an estimate of the center
U = wrf_unstagger(U, 'X' )
V = wrf_unstagger(V, 'Y' )
#W = wrf_unstagger(W, 'Z' )


#Get the landmask
LM = ncfile.variables['LANDMASK'][:]


ncfile.close() #Close the file




#Can calculate other variables as needed
RH = wrf_rh(TEMP,PRES*100.,WVMIX) #Needs to be in Pascals instead of hPa



####################################
# Specify what pressure levels you want to interpolate to, Note that you will get NaNs near the surface of strong lows
PLevels = np.array([1000,850,700,500,200,100]) 


#Interpolate RH,U,V to those pressure levels
RH_ = pres_interp(RH,PRES,PLevels)
U_ = pres_interp(U,PRES,PLevels)
V_ = pres_interp(V,PRES,PLevels)
#If you forget a variable you may need
TIMES = get_wrf_var('Times',filename)

Time_Index = 0
Height_Index = 3


fig = plt.figure(figsize=(10,10))
ax = plt.subplot(111)


clev = np.arange(0,110,5) #Contour levels

#Plot the RH at the specified pressure level and time
im = ax.contourf(LON[Time_Index],LAT[Time_Index],RH_[Time_Index,Height_Index],clev,cmap=plt.cm.BrBG)

#Add the landmask
ax.contour(LON[Time_Index],LAT[Time_Index],LM[Time_Index],colors='red',linewidths=2)

#For barbs you may need to fiddle with the sampling frequency depending on your resolution and plot size
xsf=15
ysf=15
ax.barbs(LON[Time_Index,::xsf,::ysf],LAT[Time_Index,::xsf,::ysf],U_[Time_Index,Height_Index,::xsf,::ysf],V_[Time_Index,Height_Index,::xsf,::ysf],color='k')

#Set the limits based on  min/max lat/lon. May need to modify for southern hemisphere and near the equator
ax.set_xlim(LON[Time_Index].min(),LON[Time_Index].max())
ax.set_ylim(LAT[Time_Index].min(),LAT[Time_Index].max())


#Add the title which will change based on the chosen Plevel
ax.set_title('%s RH, Winds at %s hPa'%(''.join(TIMES[Time_Index]),PLevels[Height_Index]),fontsize=16)

#Add the colorbar
cb_ax = fig.add_axes([.91,.124,.04,.756])
cbar = fig.colorbar(im,orientation='vertical',cax=cb_ax)
cbar.set_label('RH (%)',size=18)


#Save the figure
plt.savefig('WRF_RH_Barbs_TI_%2.2d_PLEV_%2.2d.png'%(Time_Index,Height_Index),bbox_inches='tight')



plt.show()#Show the plot

###############################################55

Time_Index = 0
Height_Index = 3


fig = plt.figure(figsize=(10,10))
ax = plt.subplot(111)

#Calculate the wind speed magnitudes
WSPD = np.sqrt(U**2 + V**2)

clev = np.arange(0,60,2) #Contour levels

#Plot the wind speeds at the specified pressure level and time
im = ax.contourf(LON[Time_Index],LAT[Time_Index],WSPD[Time_Index,Height_Index],clev,cmap=plt.cm.rainbow,alpha=.8)

#Add the landmask
ax.contour(LON[Time_Index],LAT[Time_Index],LM[Time_Index],colors='red',linewidths=2)

ax.streamplot(LON[Time_Index],LAT[Time_Index],U_[Time_Index,Height_Index],V_[Time_Index,Height_Index],color='k')
#More info on streamplots here: https://matplotlib.org/gallery/images_contours_and_fields/plot_streamplot.html

#Set the limits based on  min/max lat/lon. May need to modify for southern hemisphere and near the equator
ax.set_xlim(LON[Time_Index].min(),LON[Time_Index].max())
ax.set_ylim(LAT[Time_Index].min(),LAT[Time_Index].max())


#Add the title which will change based on the chosen Plevel
ax.set_title('%s Wind Speed, Streamlines at %s hPa'%(''.join(TIMES[Time_Index]),PLevels[Height_Index]),fontsize=16)


#Add the colorbar
cb_ax = fig.add_axes([.91,.124,.04,.756])
cbar = fig.colorbar(im,orientation='vertical',cax=cb_ax)
cbar.set_label('Wind Speed (m s$^{-1}$)',size=18)


#Save the figure
plt.savefig('WRF_WSPD_STREAM_TI_%2.2d_PLEV_%2.2d.png'%(Time_Index,Height_Index),bbox_inches='tight')



plt.show()#Show the plot
