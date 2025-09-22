# Tic-Tac-Toe-Game-
 Tic-Tac-Toe Game built with Streamlit in Python.   Play classic Tic Tac Toe (X vs AI O) directly in your browser with a modern web interface.   Includes automatic win/draw detection, highlighted winning cells, and a restart option.   Deployable on Streamlit Cloud .
 
 # Live Play: https://tic-tac-toe-game1.streamlit.app/

# Tic-Tac-Toe-Game-using-Streamlit
#  Tic Tac Toe Game  

An interactive **Tic-Tac-Toe game** built with **Streamlit** in Python.  
It allows a **human player (X)** to play against a simple **AI opponent (O)** on a 3x3 board.  
The game runs directly in the **browser** and is deployable on **Streamlit Cloud**.  

---

##  Table of Contents

- [Project Overview](#project-overview)  
- [Game Rules](#game-rules)  
- [Features](#features)  
- [How to Play](#how-to-play)  
- [Screenshots](#screenshots)  
- [Project Structure](#project-structure)  


---

##  Project Overview

This project aims to:

- Provide a **classic Tic Tac Toe** experience in the browser.  
- Let a human player (**X**) compete against an **AI opponent (O)**.  
- Detect **win, loss, or draw** automatically.  
- Deliver a **clean and responsive UI** built with Streamlit.  

---

##  Game Rules

1. The game is played on a **3x3 grid**.  
2. Player is always **X**, AI is **O**.  
3. Players take turns placing their symbols.  
4. First to align **3 in a row** (horizontal, vertical, or diagonal) wins.  
5. If all 9 cells are filled and no winner → **Draw**.  

---

##  Features

-  odern **UI with Streamlit buttons**  
-  **Player vs AI** gameplay  
-  Detects **win or draw automatically**  
-  **Highlighted winning cells**  
-  **Restart button** to reset the game  


---

##   Screenshots

###  Game Start  


![Game Start](/Tic_Tac_Toe_Game/screenshots/game_start.png)

###  Game Play 


![Game Play](/Tic_Tac_Toe_Game/screenshots/game_play.png)

###  Game Over


![Game Over](/Tic_Tac_Toe_Game/screenshots/game_over.png)



---

##  Project Structure

Tic_Tac_Toe_Game/
- ├── tic_tac_toe.py        
- ├── requirements.txt                     
- └── screenshots/          
    - ├── game_start.png
    - ├── game_play.png
    - └── game_over.png

---

##  How to Play

Run the app locally with:

```bash
streamlit run tic_tac_toe.py

