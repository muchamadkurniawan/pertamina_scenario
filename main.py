from scenario import scenario
from matplotlib import pyplot as plt

import pandas as pd

if __name__ == '__main__':
    print("SCENARIO 1")
    gROP = 7.75
    rLiquid = 700
    gFormInfluxeRate = 0
    rAir = 2000
    gPS = 14.7
    gTemp = 80

    dataset = pd.read_excel('dataset.xlsx')

    mDepth = dataset['MDepth'].tolist()
    incDeg = dataset['IncDeg'].tolist()
    print("Data MDepth : ",mDepth, " len: ",len(mDepth))
    print("data IncDeg : ",incDeg, " len: ",len(incDeg))
    # ftTvd = dataset['ftTVD'].tolist()
    # EMW = dataset['EMW'].tolist()
    #
    #
    #
    sc = scenario(MDepth=mDepth, IncDeg=incDeg)

    sc.calc_rVDepth()
    sc.cal_Temperatur(gTemp)
    # sc.cal_P_static(gROP, rLiquid, gFormInfluxeRate, rAir, gPS)
    # sc.cal_p_dynamic(gROP, rLiquid, gFormInfluxeRate, rAir, gPS)
    # ECD = sc.cal_ECD()

    print("MDVepth       :", sc.rVDepth)
    # print("IncDeg       :", sc.incDeg)
    print("Temperature  :", sc.Temp)
    # print("ftTVD        :", sc.rVDepth)
    # print("P static     :", sc.rSP)
    # print("P Dynamic    :", sc.rPpsi)
    # print("ECD          :", ECD)
    # sc.plot_pore_pressure()
    # y = sc.rMDepth
    # x = sc.EMW
    # plt.plot(x, y)
    # plt.ylim((max(y), min(y)))
    # plt.plot(ECD, y)
    # plt.ylim((max(y), min(y)))
    # # plt.plot(ECD[1:], sc.rMDepth[1:])
    # # plt.gca().invert_yaxis()
    # plt.show()
    # sc.plot_pore_pressure()
