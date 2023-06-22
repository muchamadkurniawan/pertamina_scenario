from scenario import scenario
from matplotlib import pyplot as plt

if __name__ == '__main__':
    print("SCENARIO 1")
    gROP = 7.75
    rLiquid = 700
    gFormInfluxeRate = 0.9
    rAir = 2000
    gPS = 14.7
    gTemp = 80

    sc = scenario()
    sc.cal_Temperatur(gTemp)
    sc.cal_P_static(gROP, rLiquid, gFormInfluxeRate, rAir, gPS)
    sc.cal_p_dynamic(gROP, rLiquid, gFormInfluxeRate, rAir, gPS)
    ECD = sc.cal_ECD()
    print("Temperature  :", sc.Temp)
    print("P static     :", sc.rSP)
    print("P Dynamic    :",sc.rPpsi)
    print("ECD          :", ECD)
    plt.plot(ECD[1:4],sc.rVDepth[1:4])
    plt.show()

