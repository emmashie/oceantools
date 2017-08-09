import numpy as np


def _dens0(S, T):
    """Density of seawater at zero pressure"""

    S = np.asarray(S)
    T = np.asarray(T)

    # --- Define constants ---
    a0 = 999.842594
    a1 = 6.793952e-2
    a2 = -9.095290e-3
    a3 = 1.001685e-4
    a4 = -1.120083e-6
    a5 = 6.536332e-9

    b0 = 8.24493e-1
    b1 = -4.0899e-3
    b2 = 7.6438e-5
    b3 = -8.2467e-7
    b4 = 5.3875e-9

    c0 = -5.72466e-3
    c1 = 1.0227e-4
    c2 = -1.6546e-6

    d0 = 4.8314e-4

    # --- Computations ---
    # Density of pure water
    SMOW = a0 + (a1 + (a2 + (a3 + (a4 + a5 * T) * T) * T) * T) * T

    # More temperature polynomials
    RB = b0 + (b1 + (b2 + (b3 + b4 * T) * T) * T) * T
    RC = c0 + (c1 + c2 * T) * T

    return SMOW + RB * S + RC * (S**1.5) + d0 * S * S



def dens(S, T, P=0):
    """Compute density of seawater from salinity, temperature, and pressure
    Usage: dens(S, T, [P])
    Input:
        S = Salinity,     [PSS-78]
        T = Temperature,  [°C]
        P = Pressure,     [dbar = 10**4 Pa]
    P is optional, with default value zero
    Output:
        Density,          [kg/m**3]
    Algorithm: UNESCO 1983
    """

    S = np.asarray(S)
    T = np.asarray(T)
    P = np.asarray(P)

    P = 0.1 * P  # Convert to bar
    return _dens0(S, T) / (1 - P / _seck(S, T, P))
