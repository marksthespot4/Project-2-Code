import math as m
#iceberg simulator 2000
#constants
SWATERDENSITY = 1025 #kg / m^3 
AIRDENSITY = 1.290 #kg / m^3
BOXDRAG = 2.1
CAPETOWNTOANTARCTICA = 3500 #km
WAVESPEED = 0.56 #m/s
#account for all forces
iceNeededPerDay = 1860000 #m^3
#shape = rectangular prism
heightIce = 75 #m
widthIce = 200 #m
lengthIce = 200 #m
iceLossMaximumPercentage =  1 - iceNeededPerDay / (heightIce * widthIce * lengthIce)

#BUOYANT FORCE -> DRAG
def buoyForceHeight(volIce,l,w):
    #height = mass / (density * length * width)
    massIce = volIce * 900
    height = massIce / (SWATERDENSITY * l * w)
    return height
#DRAG FORCE 
def dragForce(h, w, veloc):
    airDrag = 0.5 * AIRDENSITY * (heightIce - h) * w * abs(veloc) * veloc * BOXDRAG
    waterDrag = 0.5 * SWATERDENSITY * h * w * abs(veloc) * veloc * BOXDRAG
    return airDrag + waterDrag

#tester
h = buoyForceHeight(iceNeededPerDay, lengthIce, widthIce)
d = dragForce(h, widthIce, 10.2819)
print(d)