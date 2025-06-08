from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Stałe fizyczne
R = Q_(8.314, "J/(mol*K)")
M_v = Q_(18e-3, "kg/mol")
rho_water = Q_(1000, "kg/m^3")
eta_air = Q_(1.8e-5, "kg/(m*s)")
D_vap = Q_(2.5e-5, "m^2/s")

SIGMA_WATER_AIR = 0.073 #* ureg.newton / ureg.meter
GRAVITY = 9.81 #* ureg.meter / ureg.second**2
RHO_AIR = 1.205 #* ureg.kilogram / ureg.meter**3
AIR_VISCOSITY = 1.81e-5