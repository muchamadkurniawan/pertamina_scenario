import math


class scenario:
    gBitSize = 9.875
    gSolidSG = 2.65
    gMW = 8.33
    gFormFluid = 0.9
    ra_fix1 = 0.0188
    gGasSG = 1
    TempAbs = 80
    gTempGrad = 0.06
    incDeg = [0, 0.38, 0.32, 0.28, 0.76, 1.53]
    rVDepth = [0, 205.71, 288.62, 378.84, 407.7]
    rMDepth = [0, 205.71, 288.62, 378.84, 407.7]
    # Temp = [540, 552.3425, 557.3171, 562.73303, 568.2418]
    Temp = []
    rSP = []
    rPpsi = []
    rRoughness = 0.0188
    gGravity = 32.17405
    rAnnOD = 12.414
    rAnnID = 5.00
    MAX_ITER = 100
    MARGIN = 1e-9

    def cal_Temperatur(self, AbsTemp):
        MAX_ROW = len(self.rVDepth)
        temperatur = []
        for i in range(MAX_ROW):
            if i == 0:
                temperatur.append(460 + AbsTemp)
            else:
                tempe1 = (self.rMDepth[i]-self.rMDepth[i-1])
                tempe2 = math.cos(math.radians((self.incDeg[i]+self.incDeg[i-1])/2))
                tempe3 = tempe1*tempe2+self.rVDepth[i-1]
                tempe4 = tempe3 * self.gTempGrad+540
                temperatur.append(tempe4)
        self.Temp = temperatur

    def cal_P_static(self,gROP, rLiquid, gFormInfluxRate, rAir, gPS):
        gPS = gPS * 144
        rPsi = gPS / 144
        rSP = rPsi
        MAX_ROW = len(self.rVDepth)
        tempRsp = []
        for n2 in range(0, MAX_ROW):
            rT = (self.Temp[0] + self.Temp[n2])
            ra = ((0.00139 * self.gBitSize * self.gBitSize * self.gSolidSG * gROP) +
                  (0.246 * self.gMW * rLiquid) + (1.43 * self.gFormFluid * gFormInfluxRate) +
                  self.ra_fix1 * self.gGasSG * rAir) / (rT / 2 * rAir)
            rb = ((0.033 * rLiquid) + (0.023 * gFormInfluxRate)) / (rT / 2 * rAir)
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

    def cal_p_dynamic(self,gROP, rLiquid, gFormInfluxRate, rAir, gPS):
        gPS = gPS * 144
        rPsi = gPS / 144
        rSP = self.rSP
        rPfr1X = 0
        rPfr2X = 0
        rPfr1 = 0
        rPfr2 = 0
        rP = gPS

        rDpx = 0
        rPpsi = 0
        temp0 = self.TempAbs + 460

        for i in range (len(self.rVDepth)):
            rDepth = self.rMDepth[i]
            rT = temp0 + self.Temp[i]
            # print("rT :", rT, self.Temp[i])
            ra = (self.rAnnOD*self.rAnnOD-self.rAnnID*self.rAnnID)
            rFlowArea = math.pi / 4 * ra
            rFlowDiameter = (self.rAnnOD-self.rAnnID)/12
            ra = ((0.00139 * self.gBitSize * self.gBitSize * self.gSolidSG * gROP) + (0.246 * self.gMW * rLiquid) + (
                1.43 * self.gFormFluid * gFormInfluxRate)+(self.ra_fix1 * self.gGasSG * rAir)) / (rT / 2 * rAir)
            rb = ((0.033*rLiquid)+(0.023*gFormInfluxRate))/rT*2/rAir
            rc = 9.77 * rT / 2 * rAir /rFlowArea
            rd = ((0.33*rLiquid)+(0.22*gFormInfluxRate))/rFlowArea

            if self.rVDepth[i] != 0:
                r3 = 4.07*rT*rAir
                r4 = (rLiquid/7.48)+(5.615*gFormInfluxRate/60)
                if r4 == 0:
                    break
                r5 = math.pow(1.74-2*math.log10(2*self.rRoughness/rFlowDiameter),2)
                if r5 == 0:
                    break
                r6 = 2*self.gGravity*rFlowDiameter
                if r6 == 0:
                    break
                r7 = 0.632447*math.log10(self.rVDepth[i])-1.6499
                rx2 = ra*rc*rd*(rDepth-rDpx)
                rx3 = ra*rc*rc*(rDepth-rDpx)

                rPfr1 = 0
                rPfr2 = 0

                bFlag = 1
                for nloop in range(1,8):
                    wIter = 0
                    while (wIter<self.MAX_ITER):
                        rP = 144 * (self.rSP[i]+rPfr1+rPfr1X+rPfr2+rPfr2X)
                        rGLR = r3 /((gPS+rP)*r4)
                        rFLHU = math.pow(rGLR, r7)
                        rf = rFLHU/r5
                        re = rf / r6

                        if bFlag == 1:
                            rRight = 5184 * rb * rPfr1 * rPfr1 + 72 * rPfr1
                            rLeft = rx2 * re
                            rDerif = (rRight-rLeft)/((10368*rb*rPfr1)+72)
                        else:
                            rRight = 1e6 * rb * math.pow(rPfr2, 3) + 10368 * rPfr2 * rPfr2
                            rLeft = rx3*re
                            rDerif = (rRight-rLeft)/(192*rPfr2*(15625*rb*rPfr2+108))
                        rDelta = abs(rRight - rLeft)
                        if rDelta < self.MARGIN:
                            break
                        if bFlag == 1:
                            rPfr1 = rPfr1 - rDerif
                        else:
                            rPfr2 = rPfr2 -rDerif
                        wIter = wIter + 1
                    if nloop == 1:
                        rPfr2 = rPfr1
                    bFlag = 3 - bFlag
            rPpsi = rP / 144
            self.rPpsi.append(rPpsi)

    def cal_ECD(self):
        MAX_ROW = len(self.rVDepth)
        rECD = []
        for i in range (MAX_ROW):
            if self.rVDepth[i] == 0:
                rECD.append(0)
            else:
                rECD.append(self.rPpsi[i]/(0.052*self.rVDepth[i]))
        return rECD