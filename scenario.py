import math


class scenario:
    gBitSize = 9.875
    gSolidSG = 2.65
    gROP = 7.75
    gMW = 8.33
    rLiquid = 700
    gFormFluid = 0.9
    gFromIndRate = 0
    ra_fix1 = 0.0188
    gGasSG = 1
    rAir = 2000
    Temp = 80
    gTempGrad = 0.06
    rVDepth = [0, 205.71, 288.62, 378.84, 407.7]
    Temp = [540, 552.3425, 557.3171, 562.73303, 568.2418]
    rSP = []
    gPS = 2116.8
    rRoughness = 0.0188
    gGravity = 32.17405


    def cal_P_static(self):
        rPsi = self.gPS / 144
        rSP = rPsi
        MAX_ROW = len(self.Temp)
        tempRsp = []
        for n2 in range(0, MAX_ROW):
            rT = (self.Temp[0] + self.Temp[n2])
            ra = ((0.00139 * self.gBitSize * self.gBitSize * self.gSolidSG * self.gROP) +
                  (0.246 * self.gMW * self.rLiquid) + (1.43 * self.gFormFluid * self.gFromIndRate) +
                  self.ra_fix1 * self.gGasSG * self.rAir) / (rT / 2 * self.rAir)
            rb = ((0.033 * self.rLiquid) + (0.023 * self.gFromIndRate)) / (rT / 2 * self.rAir)
            rLeft = ra * self.rVDepth[n2]
            if n2 == 0:
                rSP = rPsi
            else:
                wIter = 0
                while (wIter < 100):
                    rRight = 144 * rb * (rSP - rPsi) + math.log(rSP / rPsi)
                    rDelta = abs(rRight - rLeft)
                    if rDelta < 0.000000001:
                        break
                    rDerif = 144 * rb + (1 / rSP)
                    rSP = rSP - (rRight - rLeft) / rDerif
                    wIter = wIter + 1
                tempRsp.append(rSP)
        self.rSP = tempRsp