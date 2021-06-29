import numpy as np

def get_fen(board, turn):
    fen = ""
    fen_notation = {1:"p",2:"r",6:"n",4:"b",5:"q",3:"k",
                    11:"P",12:"R",13:"N",14:"B",15:"Q",16:"K",
                    0:None}
    empty = 0
    for row in board:
        for letter in row:
            if fen_notation[letter] is not None:
                if empty != 0:
                    fen += str(empty)
                fen += str(fen_notation[letter])
                empty = 0
            else:
                empty += 1
        if empty != 0:
            fen += str(empty)
        empty = 0
        fen += "/"
    fen = fen[:-1]
    fen += " "+turn+" KQkq - 0 1"
    return fen, turn


def string_to_numpy(fen_string):
    fen_list = fen_string.split(",")
    fen_dict = {}

    fen_notation = {"bp":1,"bt":2,"bh":3,"bb":4,"bk":5,"bq":6,
                    "wp":11,"wt":12,"wh":13,"wb":14,"wk":15,"wq":16}


    for i in range(0,len(fen_list),2):
        if (fen_list[i+1] != "-"):
            fen_dict[str(int(fen_list[i+1])-11)] = fen_list[i]
    array = np.zeros((8,8))

    for k,v in fen_dict.items():
        k = "0" + str(k) if len(k) == 1 else k
        array[int(k[0])][int(k[1])] = fen_notation[v[:2]]
    return array


board = string_to_numpy('bt1,11,bh1,12,bb1,13,bk1,14,bq1,15,bb2,16,bh2,17,bt2,18,bp1,21,bp2,22,bp3,23,bp4,24,bp5,25,bp6,26,bp7,27,bp8,28,wp1,71,wp2,72,wp3,73,wp4,74,wp5,55,wp6,76,wp7,77,wp8,78,wt1,81,wh1,82,wb1,83,wk1,84,wq1,85,wb2,86,wh2,87,wt2,88')
fen,turn = get_fen(board,"w")
print(fen)
