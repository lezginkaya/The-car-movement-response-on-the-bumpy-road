import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter

def par_vel():
   m=1200 # weight of car
   v=np.arange(0,200,5) # km/h
   k=400000 #N/m stiffenss of the damper
   c=0.5 #damping ratio
   y=0.05 # m , bump of the road
   t= 6 #m, period

   # excitation frequency of the road
   w=0.290889*v

   #natural freq of the car
   wn=np.sqrt(k/m) #rad/s
   wn_hz=wn/(2*np.pi) #hz
   r=w/wn # frequency ratio
   A= np.sqrt((1+(2*c*r)**2)/(((1-r**2)**2)+((2*c*r)**2)))
   x=A*y # amplitude response
   return  x

def par_mass():
    m = np.arange(500,2000,5)  # weight of car
    v = 90  # km/h
    k = 400000  # N/m stiffenss of the damper
    c = 0.5  # damping ratio
    y = 0.05  # m , bump of the road
    t = 6  # m, period

    # excitation frequency of the road
    w = 0.290889 * v

    # natural freq of the car
    wn = np.sqrt(k / m)  # rad/s
    wn_hz = wn / (2 * np.pi)  # hz
    r = w / wn  # frequency ratio
    A = np.sqrt((1 + (2 * c * r) ** 2) / (((1 - r ** 2) ** 2) + ((2 * c * r) ** 2)))
    x = A * y  # amplitude response
    return x
def par_road():
    m = 1200  # weight of car
    v = 90  # km/h
    k = 400000  # N/m stiffenss of the damper
    c = 0.5  # damping ratio
    y = np.arange(0.01,0.2,0.002)  # m , bump of the road
    t = 6  # m, period

    # excitation frequency of the road
    w = 0.290889 * v

    # natural freq of the car
    wn = np.sqrt(k / m)  # rad/s
    wn_hz = wn / (2 * np.pi)  # hz
    r = w / wn  # frequency ratio
    A = np.sqrt((1 + (2 * c * r) ** 2) / (((1 - r ** 2) ** 2) + ((2 * c * r) ** 2)))
    x = A * y  # amplitude response
    return x
def par_stiffness():
    m = 1200  # weight of car
    v = 90  # km/h
    k = np.arange(100000,800000,100)  # N/m stiffenss of the damper
    c = 0.5  # damping ratio
    y = 0.05  # m , bump of the road
    t = 6  # m, period

    # excitation frequency of the road
    w = 0.290889 * v

    # natural freq of the car
    wn = np.sqrt(k / m)  # rad/s
    wn_hz = wn / (2 * np.pi)  # hz
    r = w / wn  # frequency ratio
    A = np.sqrt((1 + (2 * c * r) ** 2) / (((1 - r ** 2) ** 2) + ((2 * c * r) ** 2)))
    x = A * y  # amplitude response
    return x


fig,axs=plt.subplots(2,2, figsize=(12,9.5))
axs[0,0].plot(np.arange(0,200,5),par_vel())
axs[0,0].set_title("Velocity Effects on Amplitude", fontsize=10)
axs[0,0].set_ylabel("Amplitude")
axs[0,0].set_xlabel("Velocity(km/h)")
axs[0,1].plot(np.arange(500,2000,5),par_mass())
axs[0,1].set_title("Weight Effects on Amplitude",fontsize=10)
axs[0,1].set_ylabel("Amplitude")
axs[0,1].set_xlabel("Weight(kg)")
axs[1,0].plot(np.arange(0.01,0.2,0.002),par_road())
axs[1,0].set_title("Bump Height  Effects on Amplitude",fontsize=10)
axs[1,0].set_ylabel("Amplitude")
axs[1,0].set_xlabel("Bump Height(m)")
axs[1,1].plot(np.arange(100000,800000,100),par_stiffness())
axs[1,1].set_title("Stiffness Of The Car Effects on Amplitude",fontsize=10)
axs[1,1].set_ylabel("Amplitude")
axs[1,1].set_xlabel("Stiffness(N/m)")
plt.show()




