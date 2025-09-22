import streamlit as st
import random

class Player:
    def __init__(self, label, color):
        self.label = label
        self.color = color

class TicTacToeGame:
    def __init__(self, players, board_size=3):
        self.players = players
        self.board_size = board_size
        self.reset_game()

    def _get_winning_combos(self):
        rows = [[(r, c) for c in range(self.board_size)] for r in range(self.board_size)]
        cols = [[(r, c) for r in range(self.board_size)] for c in range(self.board_size)]
        diag1 = [(i, i) for i in range(self.board_size)]
        diag2 = [(i, self.board_size - 1 - i) for i in range(self.board_size)]
        return rows + cols + [diag1, diag2]

    def is_valid_move(self, row, col):
        return not self.has_winner and self.board[row][col] == ""

    def process_move(self, row, col, label):
        self.board[row][col] = label
        for combo in self.winning_combos:
            labels = [self.board[r][c] for r, c in combo]
            if len(set(labels)) == 1 and labels[0] != "":
                self.has_winner = True
                self.winner_combo = combo
                return

    def is_tied(self):
        return not self.has_winner and all(self.board[r][c] != "" for r in range(self.board_size) for c in range(self.board_size))

    def get_empty_cells(self):
        return [(r, c) for r in range(self.board_size) for c in range(self.board_size) if self.board[r][c] == ""]

    def reset_game(self):
        self.board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = self.players[0]
        self.has_winner = False
        self.winner_combo = []
        self.winning_combos = self._get_winning_combos()

    def toggle_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def find_best_move(self, label):
        opponent = "X" if label == "O" else "O"
        for r, c in self.get_empty_cells():
            self.board[r][c] = label
            if self.check_winner(label):
                self.board[r][c] = ""
                return r, c
            self.board[r][c] = ""
        for r, c in self.get_empty_cells():
            self.board[r][c] = opponent
            if self.check_winner(opponent):
                self.board[r][c] = ""
                return r, c
            self.board[r][c] = ""
        return random.choice(self.get_empty_cells()) if self.get_empty_cells() else None

    def check_winner(self, label):
        for combo in self.winning_combos:
            if all(self.board[r][c] == label for r, c in combo):
                return True
        return False

st.set_page_config(page_title="Tic Tac Toe", layout="centered")

st.markdown("""
    <style>
        body { background-color: #f9fafb; }
        .cell {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            border: 2px solid #ddd;
            border-radius: 12px;
            height: 90px;
            width: 90px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .winner {
            background-color: #ffc80 !important;
        }
        .stButton>button {
            height: 90px;
            width: 90px;
            font-size: 42px !important;
            font-weight: bold !important;
            border-radius: 12px;
        }
        .centered-button {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }
        .centered-button button {
            width: 50%;
            background-color: #1E88E5 !important;
            color: white !important;
            border-radius: 6px !important;
            font-size: 18px !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color:black; background:white; padding:7px; border-radius:6px;'> Tic-Tac-Toe (You(X) vs AI(O))</h1>", unsafe_allow_html=True)

if "game" not in st.session_state:
    st.session_state.game = TicTacToeGame([
        Player(label="X", color="#1E88E5"),
        Player(label="O", color="#E53935"),
    ])

game = st.session_state.game

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="centered-button">', unsafe_allow_html=True)
if st.button("Play Again"):
    game.reset_game()
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if game.has_winner:
    winner = game.current_player
    st.markdown(f"<h3 style='text-align:center; color:{winner.color};'>Player {winner.label} wins!</h3>", unsafe_allow_html=True)
elif game.is_tied():
    st.markdown("<h3 style='text-align:center; color:red;'>It's a tie!</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='text-align:center;'>{game.current_player.label}'s turn</h3>", unsafe_allow_html=True)

for row in range(game.board_size):
    cols = st.columns(game.board_size, gap="large")
    for col in range(game.board_size):
        cell_value = game.board[row][col]
        if cell_value == "":
            if cols[col].button(" ", key=f"{row}-{col}"):
                if game.is_valid_move(row, col):
                    game.process_move(row, col, game.current_player.label)
                    if game.has_winner or game.is_tied():
                        st.rerun()
                    game.toggle_player()
                    if game.current_player.label == "O" and not game.has_winner:
                        ai_move = game.find_best_move("O")
                        if ai_move:
                            ai_row, ai_col = ai_move
                            game.process_move(ai_row, ai_col, "O")
                            if game.has_winner or game.is_tied():
                                st.rerun()
                            game.toggle_player()
                    st.rerun()
        else:
            highlight = "winner" if (row, col) in game.winner_combo else ""
            cols[col].markdown(
                f"<div class='cell {highlight}' style='color:{'#1E88E5' if cell_value=='X' else '#E53935'};'>{cell_value}</div>",
                unsafe_allow_html=True
            )