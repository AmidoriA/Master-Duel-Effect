'''
Credit:
timelic from NexusMods: https://forums.nexusmods.com/index.php?/user/145588218-timelic

Original source:
https://bitbucket.org/timel/master-duel-chinese-translation-patch/src/master/%E5%8D%A1%E7%89%87CARD/c_CARD%E5%8E%8B%E7%BC%A9.py
'''

from typing import List
import json
import zlib

def ReadJSON(json_file_path: str) -> list or dict:
    with open(json_file_path, 'r', encoding='utf8') as f:
        dic: list = json.load(f)
    return dic
	
def getStringLen(s: str):
    return len(s.encode('utf-8'))
    res = 0
    for c in s:
        res += getCharLen(c)
    return res
	
def solve_P_desc(desc):
	
    res = ""
    res += monster_effect
    if p_effect != '':
        res += '\n'
        res += separator
        res += '\n'
        res += p_effect

    return res

CARD_Name_json: list = ReadJSON(f"CARD_Name.dec.json")
CARD_Desc_json: list = ReadJSON(f"CARD_Desc.dec.json")

name_merge_string = "\u0000" * 8  # There are eight blanks at the beginning
desc_merge_string = "\u0000" * 8

merge_string = {"name": "\u0000" * 8, "desc": "\u0000" * 8}

name_indx = [0]
desc_indx = [0]

for i in range(len(CARD_Name_json)):  # Here because of a strange bug in English desc is one less than name
    name = CARD_Name_json[i]
    desc = CARD_Desc_json[i]

    def helper(sentence: str, indx: List[int], name_or_desc: str,
               merge_string: dict):
        #    Cancel here first, but it shouldn't be a problem here.
        # Convert Chinese pendulum monster effects to Japanese format
        # if sentence.startswith('←'):
        #     sentence = solve_P_desc(sentence)
        length = getStringLen(sentence)
        if i == 0:
            length += 8
        space_len = 4 - length % 4  # It means getting the remainder
        indx.append(indx[-1] + length + space_len)  # Record indx
        if name_or_desc == "name":
            merge_string["name"] += sentence + '\u0000' * space_len
        else:
            merge_string["desc"] += sentence + '\u0000' * space_len

    helper(name, name_indx, "name", merge_string)
    helper(desc, desc_indx, "desc", merge_string)

# Compression
# Can't compress. Compression is a problem.

name_indx = [4, 8] + name_indx[1:]
desc_indx = [4, 8] + desc_indx[1:]

# print(name_indx)
# print(desc_indx)

card_indx = []
for i in range(len(name_indx)):
    card_indx.append(name_indx[i])
    card_indx.append(desc_indx[i])

print(card_indx)


def intTo4Hex(num: int) -> List[int]:
    res = []
    for _ in range(4):
        res.append(num % 256)
        num //= 256
    return res


card_indx_merge = []
for item in card_indx:
    card_indx_merge.extend(intTo4Hex(item))

# Direct Encryption
file_names = ['CARD_Name', 'CARD_Desc', 'CARD_Indx']


def encrypt(output_name, b: bytes):
    m_iCryptoKey = 0xDA  # Remember to change the key

    data = bytearray(zlib.compress(b))

    for i in range(len(data)):
        v = i + m_iCryptoKey + 0x23D
        v *= m_iCryptoKey
        v ^= i % 7
        data[i] ^= v & 0xFF

    with open(output_name, "wb") as f:
        f.write((data))
    f.close()


encrypt(f'CARD_Name',
        bytes(merge_string["name"], encoding='utf-8'))
encrypt(f'CARD_Desc',
        bytes(merge_string["desc"], encoding='utf-8'))
encrypt(f'CARD_Indx', bytes(card_indx_merge))