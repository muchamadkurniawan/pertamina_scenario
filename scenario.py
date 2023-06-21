import math


class scenario:
    gBitSize = 9.875
    gSolidSG = 2.65
    gROP = 7.75
    gMW = 8.33
    rLiquid = 700
    gFormFluid = 0.9
    gFromIndRate = 0
    ra_fix1 = 0.0018
    gGasSG = 1
    rAir = 2000
    Temp = 80
    gTempGrad = 0.06
    rVDepth = [0, 205.71, 288.62, 378.84, 407.7]
    Temp = [540, 552.3425, 557.3171, 562.73303, 568.2418]
    rSP = []
    gPS = 2116.8


    def cal_P_static(self):
        rPsi = self.gPS / 144
        rSP = rPsi
        rPfr1x = 0
        rPfr2x = 0
        rP = self.gPS
        rPfr1 = 0
        rPfr2 = 0
        rPpsi = 0
        bFlag = 1
        rDpx = 0
        rDepth = 0
        rAnnOD = 12.414
        rAnnID = 5.00
        rRoughness = 0.00188
        gGravity = 32.17405

        MAX_ROW = len(self.Temp)
        tempRsp = []
        for n2 in range(0, MAX_ROW):
            rDpx = rDepth
            rDepth = self.rVDepth[n2]
            rT = (self.Temp[0] + self.Temp[n2])
            ra = (rAnnOD * rAnnOD - rAnnID * rAnnID)
            rFlowArea = math.pi / 4 * ra
            rPfr1x = rPfr1x + rPfr1
            rPfr2x = rPfr2x + rPfr2
            ra = ((0.00139 * self.gBitSize * self.gBitSize * self.gSolidSG * self.gROP) +
                  (0.246 * self.gMW * self.rLiquid) + (1.43 * self.gFormFluid * self.gFromIndRate) +
                  self.ra_fix1 * self.gGasSG * self.rAir) / (rT / 2 * self.rAir)
            rb = ((0.033 * self.rLiquid) + (0.023 * self.gFromIndRate)) / (rT / 2 * self.rAir)
            rc = 9.77 * rT / 2 * self.rAir / rFlowArea
            rd = ((0.33 * self.rLiquid) + (0.22 * self.gFromIndRate)) / rFlowArea
            rFlowDiameter = (rAnnOD - rAnnID) / 12

            if self.rVDepth[n2] == 0:
                rPpsi = rP / 144
            else:
                rLeft = ra * self.rVDepth[n2]
                wIter = 0
                while (wIter < 100):
                    rRight = 144 * rb * (rSP - rPsi) + math.log(rSP / rPsi)
                    rDelta = abs(rRight - rLeft)
                    if rDelta < 0.000000001:
                        break
                    rDerif = 144 * rb + (1 / rSP)
                    rSP = rSP - (rRight - rLeft) / rDerif
                    wIter = wIter + 1
            print("rSP end :", rSP)
            tempRsp.append(rSP)
        self.rSP = tempRsp