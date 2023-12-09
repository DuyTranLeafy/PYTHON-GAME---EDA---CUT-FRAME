# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:17:29 2023

@author: tranv
"""

import sys
import pygame
import GameRacingCar
import Select_Map 
import Select_Car
import time
import Main_Playout_Project

class PacmanStartMenu:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("audio/play_main.mp3")
        pygame.mixer.music.play()
        pygame.init()
        self.WIDTH = 400
        self.HEIGHT = 620
        self.screen = pygame.display.set_mode([400, 620])
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Icon của các cửa sổ
        icon = pygame.image.load(
            'Graphics/Icon_Snake.png')
        pygame.display.set_icon(icon)

        pygame.display.set_caption("Car Racing - 21110155 - 09 Bao Duy")

        # CỬA SỔ START
        self.root = pygame.display.set_mode((400, 620))
        background = pygame.image.load(
            'img/start_main.png')
        background = pygame.transform.scale(background, (400, 620))
        self.root.blit(background, (0, 0))

        # Tạo nút "Start"
        self.start_button_BD_09 = pygame.Rect(20, 149, 150, 40)
        self.button_color_BD_09 = pygame.Color("#FEB83C")
        self.hover_color = pygame.Color("#F1A011")

        # Tạo nút "Info"
        self.info_button_BD_09 = pygame.Rect(20, 234, 150, 40)
        self.info_button_BD_09_color = pygame.Color("#FEB83C")
        self.info_hover_color = pygame.Color("#F1A011")
        
        # Tạo nút "Car"
        self.car_button_BD_09 = pygame.Rect(20, 324, 150, 40)
        self.car_button_BD_09_color = pygame.Color("#FEB83C")
        self.car_hover_color = pygame.Color("#F1A011")
        
        # Tạo nút "Exit"
        self.exit_button_BD_09 = pygame.Rect(20, 414, 150, 40)
        self.exit_button_BD_09_color = pygame.Color("#FEB83C")
        self.exit_hover_color = pygame.Color("#F1A011")

        self.font = pygame.font.Font(
            "INVASION2000.ttf", 30)
    
    def run_start_menu(self):
        running = True
        while running:
            self.timer.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.start_button_BD_09.collidepoint(mouse_pos):
                        pygame.mixer.music.pause()
                        time.sleep(1)
                        pygame.mixer.init()
                        pygame.mixer.music.load("audio/game_start.mp3")
                        pygame.mixer.music.play()
                        racing_game = GameRacingCar.GameRunner()
                        racing_game.run_game()
                        
                    elif self.info_button_BD_09.collidepoint(mouse_pos):
                        select_map = Select_Map.Setting()
                        select_map.run_start_menu()
                    elif self.car_button_BD_09.collidepoint(mouse_pos):
                        select_car = Select_Car.Setting()
                        select_car.run_start_menu()
                    elif self.exit_button_BD_09.collidepoint(mouse_pos):
                        pygame.mixer.music.pause()
                        custom_menu = Main_Playout_Project.CustomStartMenu()
                        custom_menu.run_custom_menu()
                        """background = pygame.image.load(
                            'Main_Playout.png')
                        background = pygame.transform.scale(background, (940, 540))
                        self.root_main = pygame.display.set_mode((940, 540))
                        self.root_main.blit(background, (0, 0))
                        # Update the display
                        pygame.display.flip()
                        return"""
                                   

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()

            # Kiểm tra xem chuột có đang nằm trên nút "Start" hay không
            if self.start_button_BD_09.collidepoint(mouse_pos):
                start_color = self.hover_color
            else:
                start_color = self.button_color_BD_09

            # Kiểm tra xem chuột có đang nằm trên nút "Info" hay không
            if self.info_button_BD_09.collidepoint(mouse_pos):
                info_color = self.info_hover_color
            else:
                info_color = self.info_button_BD_09_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "Car" hay không
            if self.car_button_BD_09.collidepoint(mouse_pos):
                car_color = self.car_hover_color
            else:
                car_color = self.car_button_BD_09_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "Exit" hay không
            if self.exit_button_BD_09.collidepoint(mouse_pos):
                exit_color = self.exit_hover_color
            else:
                exit_color = self.exit_button_BD_09_color

            # Vẽ nút "Start" và "Info" với màu hiện tại
            pygame.draw.rect(self.root, start_color, self.start_button_BD_09)
            pygame.draw.rect(self.root, info_color, self.info_button_BD_09)
            pygame.draw.rect(self.root, car_color, self.car_button_BD_09)
            pygame.draw.rect(self.root, exit_color, self.exit_button_BD_09)

            # Vẽ văn bản "Start" và "Info" giữa nút
            start_text = self.font.render("Start", True, "#333333")
            info_text = self.font.render("Map", True, "#333333")
            car_text = self.font.render("Car", True, "#333333")
            exit_text = self.font.render("Exit", True, "#333333")

            start_text_rect = start_text.get_rect(center=self.start_button_BD_09.center)
            info_text_rect = info_text.get_rect(center=self.info_button_BD_09.center)
            car_text_rect = car_text.get_rect(center=self.car_button_BD_09.center)
            exit_text_rect = exit_text.get_rect(center=self.exit_button_BD_09.center)

            self.root.blit(start_text, start_text_rect)
            self.root.blit(info_text, info_text_rect)
            self.root.blit(exit_text, exit_text_rect)
            self.root.blit(car_text, car_text_rect)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
"""
if __name__ == "__main__":
    start_menu = PacmanStartMenu()
    start_menu.run_start_menu()"""