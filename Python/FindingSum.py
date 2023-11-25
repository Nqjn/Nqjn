from typing import Optional

def play(board_size: int, pos: str) -> Optional[list[str]]:
    board = create_Board(board_size)
    x, y = translator(pos, board)
    path = [pos]
    result = Knight_move(x, y, path, board)
    if result:
        return final
    else:
        return None

def create_Board(board_size: int):
    return [[ f"{chr(97+x)}{board_size-y}" for x in range(board_size)] for y in range(board_size)]

def translator(pos: str, board: list[list[str]]):
    return next(((x, y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y] == pos[2:]), None)

final = []
def Knight_move(x: int, y: int, path: list[str], board: list[list[str]]):
    moves = [(2, 1), (2, -1),(-2, 1), (-2, -1), (1, 2), (1, -2),(-1,2), (-2, -1)]
    if is_final(board):
        final.append(path.copy())
        return final
    


    for i in range(len(moves)):
        dx, dy = moves[i]
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, board):

            for l in range(len(moves)):
                if l+1 < len(moves):
                    sdx, sdy = moves[l + 1]
                    snew_x, snew_y = x + sdx, y + sdy
                    if is_valid(snew_x, snew_y, board) and new_x != snew_x and new_y != snew_y:
                        new_path = path.copy() + [f"{board[x][y]}qK{board[new_x][new_y]}&{board[snew_x][snew_y]}"]
                        original_value = board[new_x][new_y]
                        soriginal_value = board[snew_x][snew_y]

                        board[x][y] = "bK" 
                        board[snew_x][snew_y] = "bK"
                        # board[new_x][new_y] = "bK"

                        if Knight_move(new_x, new_y, new_path, board):
                            return True
                        board[new_x][new_y] = original_value
                        board[snew_x][snew_y] = soriginal_value

    return None

def is_final(board: list[list[str]] ):
    return not any(posit != "bK" for row in board for posit in row)
    
def is_valid(
            x: int,
            y: int,
            board: list[list[str]]
            ) -> bool:
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != "bK"
    

print(play(8, "qKa1"))

