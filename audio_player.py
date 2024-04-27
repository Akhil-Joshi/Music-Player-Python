import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):

        self.master = master
        master.title("Python Music Player")
        self.playlist = []
        self.current_index = 0
        self.isPlaying = False

        self.label = tk.Label(master, text="Music Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(master, width=50, font=("Helvetica", 12), selectbackground="#87CEEB", selectforeground="Blue")
        self.listbox.pack(pady=5)

        self.button_select = tk.Button(master, text="Select Folder", command=self.select_folder)
        self.button_select.pack(pady=5)

        self.button_play = tk.Button(master, text="Play", command=self.toggle_play)
        self.button_play.pack(pady=5)

        self.button_stop = tk.Button(master, text="Stop", command=self.stop)
        self.button_stop.pack(pady=5)

        pygame.init()

    # Open a dialog to select a folder and load the MP3 files from the selected folder.
    def select_folder(self):

        folder_path = filedialog.askdirectory()
        if folder_path:
            self.load_files(folder_path)

    # Clear the playlist and load the MP3 files from the given folder path.
    def load_files(self, folder_path):

        self.playlist.clear()
        self.listbox.delete(0, tk.END)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.mp3'):
                    full_path = os.path.join(root, file)
                    self.playlist.append(full_path)
                    self.listbox.insert(tk.END, os.path.basename(full_path))

    # Toggle between play and pause states.
    def toggle_play(self):
        
        if not self.playlist:
            return

        if not self.isPlaying:
            self.play()
            self.isPlaying = True
            self.button_play.config(text="Pause")
        else:
            self.pause()
            self.isPlaying = False
            self.button_play.config(text="Play")

    def play(self):

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            selected_index = self.listbox.curselection()
            if selected_index:
                self.current_index = selected_index[0]
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self): 
        pygame.mixer.music.stop()
        self.isPlaying = False
        self.button_play.config(text="Play")

def main():
    root = tk.Tk()
    root.geometry("400x400")
    MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()