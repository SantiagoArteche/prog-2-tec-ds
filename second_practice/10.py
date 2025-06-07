pieces_to_process = int(input("Insert the amount of pieces: "))

init = 0
valid_pieces = 0
while(init < pieces_to_process):
    piece_length = float(input("Insert the length of the chunk: "))
    if(piece_length >= 1.20 and piece_length <= 1.30):
        valid_pieces = valid_pieces + 1
    init += 1

print(f"The number of valid pieces is: {valid_pieces}")