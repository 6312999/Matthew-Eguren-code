import math
def polar_to_cartesian(r, theta):
    x=r*math.cos(math.radians(theta))
    y=r*math.sin(math.radians (theta))
    return (round (x,5), round (y,5))

r=float(input('what R value would you like to use'))
theta=float(input("At what angle"))
print(f"The coordinates {polar_to_cartesian(r,theta)} in the cartesian plane")

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).

def cartesian_to_polar(x, y):
    r=math.sqrt(x**2 + y**2)
    theta= math.atan(math.degrees(y/x)) 
    return (r,theta)
x=float(input('what x value would you like to use'))
y=float(input('what y value would you like to use'))
print(f"the coordinates are {cartesian_to_polar(x,y)} in the cartesian plane")

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.

def pendulum_position(A, f, phi, t):
    x_t=A*math.cos(2*math.pi*f*t+ math.radians(phi))
    return x_t
    
A=float(input("What is the amplitude"))
f= float(input("What is the frequency"))
phi= float(input("What is the phase factor"))
t=float(input("What is the time"))
print(f"The position is:", {pendulum_position(A, f, phi, t)})
    