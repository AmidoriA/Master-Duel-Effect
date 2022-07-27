'''
Credits:
- akintos from GitHub: https://gist.github.com/akintos/04e2494c62184d2d4384078b0511673b
- timelic from NexusMods for the new crypto key: https://bitbucket.org/timel/master-duel-chinese-translation-patch/src/master/%E5%8D%A1%E7%89%87CARD/a_CARD%E8%A7%A3%E5%AF%86.py
'''

import zlib

file_names = ['CARD_Desc', 'CARD_Indx', 'CARD_Name']

m_iCryptoKey = 0xda


def Decrypt(file_name):
    with open(f'{file_name}', "rb") as f:
        data = bytearray(f.read())

    for i in range(len(data)):
        v = i + m_iCryptoKey + 0x23D
        v *= m_iCryptoKey
        v ^= i % 7
        data[i] ^= v & 0xFF

    with open(f'{file_name}' + ".dec", "wb") as f:
        f.write(zlib.decompress(data))


for name in file_names:
    Decrypt(name)