# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:17:29 2023

@author: tranv
"""
import tkinter as tk
import sys
import pygame
from EDA_Main_Version import StudentPerformanceApp
import Start_Main
import Frame_Cut_Main

class CustomStartMenu:
    def __init__(self, width=940, height=540):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.timer = pygame.time.Clock()
        self.fps = 60

        # CỬA SỔ START
        self.root = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        background = pygame.image.load('Main_Playout.png')  # Update with your background image
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.root.blit(background, (0, 0))

        # Tạo nút "Data"
        self.data_button = pygame.Rect(371, 411, 190, 40)
        self.data_button_color = pygame.Color("#4857A4")
        self.data_hover_color = pygame.Color("#243172")

        # Tạo nút "Game"
        self.game_button = pygame.Rect(150, 411, 190, 40)
        self.game_button_color = pygame.Color("#4857A4")
        self.game_hover_color = pygame.Color("#243172")

        # Tạo nút "CutFrame"
        self.cutframe_button = pygame.Rect(592, 411, 190, 40)
        self.cutframe_button_color = pygame.Color("#4857A4")
        self.cutframe_hover_color = pygame.Color("#243172")

        # Font
        self.font = pygame.font.Font(None, 36)

    def run_custom_menu(self):
        running = True
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.data_button.collidepoint(mouse_pos):
                        root = tk.Tk()
                        root.configure(background='#0074ce')
                        app = StudentPerformanceApp(root)
                        root.mainloop()
                    elif self.game_button.collidepoint(mouse_pos):
                        # Handle Game button click
                        start_menu = Start_Main.PacmanStartMenu()
                        start_menu.run_start_menu()
                    elif self.cutframe_button.collidepoint(mouse_pos):
                        frame = Frame_Cut_Main.VideoProcessor()
                        

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()

            # Kiểm tra xem chuột có đang nằm trên nút "Data" hay không
            if self.data_button.collidepoint(mouse_pos):
                data_color = self.data_hover_color
            else:
                data_color = self.data_button_color

            # Kiểm tra xem chuột có đang nằm trên nút "Game" hay không
            if self.game_button.collidepoint(mouse_pos):
                game_color = self.game_hover_color
            else:
                game_color = self.game_button_color

            # Kiểm tra xem chuột có đang nằm trên nút "CutFrame" hay không
            if self.cutframe_button.collidepoint(mouse_pos):
                cutframe_color = self.cutframe_hover_color
            else:
                cutframe_color = self.cutframe_button_color

            # Vẽ nút "Data" và "Game" với màu hiện tại
            pygame.draw.rect(self.root, data_color, self.data_button)
            pygame.draw.rect(self.root, game_color, self.game_button)
            pygame.draw.rect(self.root, cutframe_color, self.cutframe_button)

            # Vẽ chữ lên nút
            data_text = self.font.render("START", True, pygame.Color("white"))
            game_text = self.font.render("START", True, pygame.Color("white"))
            cutframe_text = self.font.render("START", True, pygame.Color("white"))

            data_text_rect = data_text.get_rect(center=self.data_button.center)
            game_text_rect = game_text.get_rect(center=self.game_button.center)
            cutframe_text_rect = cutframe_text.get_rect(center=self.cutframe_button.center)

            self.root.blit(data_text, data_text_rect)
            self.root.blit(game_text, game_text_rect)
            self.root.blit(cutframe_text, cutframe_text_rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
        

if __name__ == "__main__":
    custom_menu = CustomStartMenu()
    custom_menu.run_custom_menu()
