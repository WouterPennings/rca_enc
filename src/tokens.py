charToken = dict({
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
    27: ' ',
    28: "0",
    29: "1",
    30: "2",
    31: "3",
    32: "4",
    33: "5",
    34: "6",
    35: '7',
    36: "8",
    37: "9"
})

def getKeyByValue(value):
    key_list = list(charToken.keys())
    val_list = list(charToken.values())
    return key_list[val_list.index(value)]
