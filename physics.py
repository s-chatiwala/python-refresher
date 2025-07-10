import math

def calculate_buoyancy(V, density_fluid):
    """Calculate buoyance by multiplying V, the volume of the fluid in cubic meters, the density of the fluid in kg/m^3, and the constant force of gravity at 9.81 m/s^2."""
    g = 9.81
    buoyancy_force = V * density_fluid * g
    return buoyancy_force

def will_it_float(V, mass):
    """Determines whether an object will float or sink"""
    if mass // V < 1:
        return True
    return False

def calculate_pressure(depth):
    """Return pressure in pascals."""
    g = 9.81
    return 9.81 * 1000 * depth

def calculate_angular_acceleration(tau, I):
    """Calculate the angular acceleration of an object."""
    return tau / I

def calculate_torque(F_magnitude, F_direction, r):
    """Calculate torque applied to an object."""
    return F_magnitude * r * sin(F_direction)




