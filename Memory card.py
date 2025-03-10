import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")
        
        self.level = 1
        self.score = 0
        self.max_level = 5  # Changed to 5 levels
        
        self.cards = []
        self.buttons = []
        self.first_selection = None
        self.second_selection = None
        
        self.create_level()

        # Scoreboard
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.grid(row=0, column=0, columnspan=4)
        
        # Level label
        self.level_label = tk.Label(self.root, text=f"Level: {self.level}", font=("Arial", 14))
        self.level_label.grid(row=0, column=4, columnspan=4)
    
    def create_level(self):
        """Creates a new level with more cards"""
        self.buttons = []
        self.first_selection = None
        self.second_selection = None
        
        # Increase grid size with each level
        grid_size = self.level + 3  # Starting from 4x4 at level 1 to 8x8 at level 5
        card_count = grid_size * grid_size // 2
        self.cards = list(range(1, card_count + 1)) * 2  # Create pairs of numbers
        random.shuffle(self.cards)

        # Create the buttons (cards) based on the grid size
        for i in range(grid_size):
            row = []
            for j in range(grid_size):
                btn = tk.Button(self.root, text="", width=8, height=4, font=("Arial", 14),
                                command=lambda i=i, j=j: self.reveal_card(i, j))
                btn.grid(row=i + 1, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)
    
    def reveal_card(self, i, j):
        """Reveals the card when clicked"""
        if self.buttons[i][j]["text"] == "" and self.first_selection is None:
            self.first_selection = (i, j)
            self.buttons[i][j]["text"] = str(self.cards[i * len(self.buttons) + j])
        elif self.buttons[i][j]["text"] == "" and self.second_selection is None:
            self.second_selection = (i, j)
            self.buttons[i][j]["text"] = str(self.cards[i * len(self.buttons) + j])
            self.root.after(1000, self.check_match)
    
    def check_match(self):
        """Checks if the two selected cards match"""
        i1, j1 = self.first_selection
        i2, j2 = self.second_selection
        
        if self.cards[i1 * len(self.buttons) + j1] == self.cards[i2 * len(self.buttons) + j2]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            
            # Check if level is completed
            if self.score == len(self.cards) // 2:
                if self.level < self.max_level:
                    self.level += 1
                    self.level_label.config(text=f"Level: {self.level}")
                    self.create_level()
                else:
                    self.level_label.config(text="Max Level Reached!")
        
        else:
            self.buttons[i1][j1]["text"] = ""
            self.buttons[i2][j2]["text"] = ""
        
        self.first_selection = None
        self.second_selection = None

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()