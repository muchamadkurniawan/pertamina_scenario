# import math
#
# rPpsi = 0
# gBitSize = 9.875
# gSolidSG = 2.65
# gROP = 7.75
# gMW = 8.33
# rLiquid = 700
# gFormFluid = 0.9
# gFromInfluxRate = 0
# ra_fix1 = 0.00188
# gGasSG = 1
# rAir = 2000
# Temp = 80
# gTempGrad = 0.06
# rVDepth = [0, 205.71, 288.62, 378.84, 407.7]
# Temp = [540, 552.3425, 557.3171, 562.73303, 568.2418]
# gPS = 2116.8
#
# if __name__ == '__main__':
#     rPsi = gPS/144
#     rSP = rPsi
#     rPfr1x = 0
#     rPfr2x = 0
#     rP = gPS
#     rPfr1 = 0
#     rPfr2 = 0
#     rPpsi = 0
#     bFlag = 1
#     rDpx = 0
#     rDepth = 0
#     rAnnOD = 12.414
#     rAnnID = 5.00
#     rRoughness = 0.0018
#     gGravity = 32.17405
#     p_static = []
#     p_dynamic = []
#     rPressure = []
#     MAX_ROW = len(Temp)
#
#     for n2 in range(0, 5):
#         rDepth = rVDepth[n2]
#         rT = (Temp[0] + Temp[n2])
#         ra = (rAnnOD * rAnnOD - rAnnID * rAnnID)
#         rFlowArea = math.pi / 4 * ra
#         ra = ((0.00139 * gBitSize * gBitSize * gSolidSG * gROP) + (0.246 * gMW * rLiquid) + (
#                     1.43 * gFormFluid * gFromInfluxRate) +
#               ra_fix1 * gGasSG * rAir) / (rT / 2 * rAir)
#         #__STATIC__
#
#
#         rb = ((0.033*rLiquid)+(0.023*gFromInfluxRate))/(rT/2*rAir)
#         rc = 9.77*rT/2*rAir/rFlowArea
#         rd = ((0.33*rLiquid)+(0.22*gFromInfluxRate))/rFlowArea
#         rFlowDiameter = (rAnnOD - rAnnID) / 12
#
#         if rVDepth[n2] == 0:
#             p_static.append(rSP)
#             rPressure.append(gPS)
#         else:
#             rLeft = ra*rVDepth[n2]
#             wIter = 0
#             nbreak = 0
#             while(wIter<100):
#                 rRight = 144*rb*(p_static[n2-1]-rPpsi)+math.log(p_static[n2-1]/rPpsi)
#                 rDelta = abs(rRight - rLeft)
#                 if rDelta < 0.0000000001:
#                     break
#                 rDerif = 144 * rb+(1/p_static[n2-1])
#                 rSP = p_static[n2-1] - (rRight-rLeft)/rDerif
#                 wIter = wIter+1
#
#             # r3 = 4.07*rT*rAir
#             # r4 = (rLiquid/7.48)+(5.615*gFromInfluxRate/60)
#             # r5 = math.pow(1.74-(2*math.log10(2*rRoughness/rFlowDiameter)),2)
#             # # print("r5 = ",r5)
#             # r6 = 2*gGravity*rFlowDiameter
#             # # print("r6 = ", r6)
#             # r7 = 0.632447*math.log10(rVDepth[n2])-1.6499
#             # rx2 = ra*rc*rd*(rDepth-rDpx)
#             # rx3 = ra*rc*rc*(rDepth-rDpx)
#             # # rPfr1x = rPfr1+rPfr1x
#             # # rPfr2x = rPfr2+rPfr2x
#             # rPfr1 = 0
#             # rPfr2 = 0
#             # bFlag = 1
#             # nbreak_loop = False
#             # for nLoop in range(1,9):
#             #     wIter2 = 0
#             #     while (wIter2 < 100):
#             #         rP = 144*(p_static[n2-1]+rPfr1+rPfr1x+rPfr2+rPfr2x)
#             #         rGLR = r3 / ((gPS + rP) * r4)
#             #         rFLHU = math.pow(rGLR, r7)
#             #         rf = rFLHU / r5
#             #         re = rf / r6
#             #         print("rP" , rP/144)
#             #         # print("r7", r7)
#             #         if bFlag == 1:
#             #             rRight = 5184*rb*rPfr1*rPfr1*72*rPfr1
#             #             rLeft = rx2*re
#             #             rDerif = (rRight-rLeft)/((10368*rb*rPfr1)+72)
#             #         else:
#             #             rRight = 1000000*rb*math.pow(rPfr2,3)+10368*rPfr2*rPfr2
#             #             rLeft = rx3*re
#             #             rDerif = (rRight-rLeft)/(192*rPfr2*(15625*rb*rPfr2+108))
#             #         rDelta = abs(rRight-rLeft)
#             #         # print("delta  :",rDelta)
#             #         # print("rDERIF : ",rDerif)
#             #         if rDelta < 0.00000000001:
#             #             # print("TRUEEEEEEEEE")
#             #             wIter2 = 104
#             #         else:
#             #             if bFlag == 1:
#             #                 rPfr1 = rPfr1 - rDerif
#             #             else:
#             #                 rPfr2 = rPfr2 - rDerif
#             #             wIter2 = wIter2+1
#             #         # print("rPfr1 :", rPfr1, " rPfr2 :", rPfr2)
#             #     if nLoop == 1:
#             #         rPfr2 = rPfr1
#             #     bFlag = 3-bFlag
#             #     print("===================-------------------------------------=", nLoop)
#             p_static.append(rSP)
#             print("**************************************************************************", n2)
#         rPpsi = (rP) / 144
#         # p_dynamic.append(rPpsi)
#
#     print("P Dynamic : ",p_dynamic)
#     print("P Static :", p_static)
from scenario import scenario

if __name__ == '__main__':
    print("SCENARIO 1")
    gROP = 7.75
    rLiquid = 700
    gFormInfluxeRate = 0.9
    rAir = 2000
    gPS = 14.7

    sc = scenario()
    sc.cal_P_static(gROP, rLiquid, gFormInfluxeRate, rAir, gPS)
    print("static ", sc.rSP)
