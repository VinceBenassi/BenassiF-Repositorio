def CODE(sTxt,nKey):
    sMsg = ''
    for xE in sTxt:
        nXOR = ord(xE) ^ nKey
        nLSB = nXOR & 0xf
        nMSB = nXOR >> 0x4
        nAux = nLSB<<4 | nMSB
        sMsg += str(nAux) + ','
    return sMsg


def DECO(aCODE,nKey):
    sMsg = ""
    for elementos in aCODE:
        nLSB = elementos & 0xf
        nMSB = elementos >> 0x4
        nAux = nLSB << 4 | nMSB
        sMsg += chr(nAux ^ nKey)
    return sMsg

aMSG = [118,103,215,71,199,51,7,39,22,39,51,54,103,54,167,215,199]
nKey = [7,13,19,21]

print(DECO(aMSG, 19))
