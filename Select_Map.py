# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:17:29 2023

@author: tranv
"""

import sys
import pygame
Map = 'img/1.png'
class Setting:
    
    selected_map_text = ""
    def __init__(self):
        pygame.init()
        self.WIDTH = 400
        self.HEIGHT = 620
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.timer = pygame.time.Clock()
        self.fps = 60

        # Icon của các cửa sổ
        icon = pygame.image.load(
            'Graphics/Icon_Snake.png')
        pygame.display.set_icon(icon)

        pygame.display.set_caption("Car Racing - 21110155 - 09 Bao Duy")

        # CỬA SỔ START
        self.root = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        background = pygame.image.load(
            'img/Select_Map.png')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.root.blit(background, (0, 0))

        # Tạo nút "Start"
        self.start_button = pygame.Rect(130, 30, 150, 0)
        self.button_color = pygame.Color("#FEB83C")
        self.hover_color = pygame.Color("#F1A011")

        # Tạo nút "1"
        self.one_button = pygame.Rect(100, 315, 30, 30)
        self.one_button_color = pygame.Color("#FAFAFA")
        self.one_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "2"
        self.two_button = pygame.Rect(267, 315, 30, 30)
        self.two_button_color = pygame.Color("#FAFAFA")
        self.two_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "3"
        self.three_button = pygame.Rect(100, 568, 30, 30)
        self.three_button_color = pygame.Color("#FAFAFA")
        self.three_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "4"
        self.four_button = pygame.Rect(267, 568, 30, 30)
        self.four_button_color = pygame.Color("#FAFAFA")
        self.four_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "Back"
        self.back_button = pygame.Rect(155, 575, 90, 40)
        self.back_button_color = pygame.Color("#FEB83C")
        self.back_hover_color = pygame.Color("#F1A011")

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
                    global Map
                    if self.start_button.collidepoint(mouse_pos):
                        pass
                    elif self.one_button.collidepoint(mouse_pos): 
                        Map ='img/1.png'
                        self.selected_map_text = "Map 1 is selected"  # Updated line
                    elif self.two_button.collidepoint(mouse_pos):
                        Map ='img/2.png'
                        self.selected_map_text = "Map 2 is selected"  # Updated line
                    elif self.three_button.collidepoint(mouse_pos):
                        Map ='img/3.png'
                        self.selected_map_text = "Map 3 is selected"  # Updated line
                    elif self.four_button.collidepoint(mouse_pos):
                        Map ='img/4.png'
                        self.selected_map_text = "Map 4 is selected"  # Updated line
                    elif self.back_button.collidepoint(mouse_pos):
                        background = pygame.image.load(
                            'img/start_main.png')
                        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
                        self.root.blit(background, (0, 0))
                    
                        # You may need to redraw other elements on the screen as well
                    
                        # Update the display
                        pygame.display.flip()
                        return
                        
                # Clear the screen with a background image or fill with a solid color
            background = pygame.image.load('img/Select_Map.png')
            background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
            self.root.blit(background, (0, 0))
                        
                
    

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()
            
            # Kiểm tra xem chuột có đang nằm trên nút "2" hay không
            if self.two_button.collidepoint(mouse_pos):
                two_color = self.two_hover_color
            else:
                two_color = self.two_button_color
            
            # Kiểm tra xem chuột có đang nằm trên nút "3" hay không
            if self.three_button.collidepoint(mouse_pos):
                three_color = self.three_hover_color
            else:
                three_color = self.three_button_color
            
            # Kiểm tra xem chuột có đang nằm trên nút "4" hay không
            if self.four_button.collidepoint(mouse_pos):
                four_color = self.four_hover_color
            else:
                four_color = self.four_button_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "back" hay không
            if self.back_button.collidepoint(mouse_pos):
                back_color = self.back_hover_color
            else:
                back_color = self.back_button_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "Start" hay không
            if self.start_button.collidepoint(mouse_pos):
                start_color = self.hover_color
            else:
                start_color = self.button_color

            # Kiểm tra xem chuột có đang nằm trên nút "Info" hay không
            if self.one_button.collidepoint(mouse_pos):
                one_color = self.one_hover_color
            else:
                one_color = self.one_button_color
            
            # Vẽ nút "2", "3", và "4" với màu hiện tại
            pygame.draw.rect(self.root, two_color, self.two_button)
            pygame.draw.rect(self.root, three_color, self.three_button)
            pygame.draw.rect(self.root, four_color, self.four_button)
            pygame.draw.rect(self.root, back_color, self.back_button)

            # Vẽ nút "Start" và "Info" với màu hiện tại
            pygame.draw.rect(self.root, start_color, self.start_button)
            pygame.draw.rect(self.root, one_color, self.one_button)

            # Vẽ văn bản "Start" và "Info" giữa nút
            start_text = self.font.render("---Select Map---", True, "#333333")
            one_text = self.font.render("1", True, "#333333")
            two_text = self.font.render("2", True, "#333333")
            three_text = self.font.render("3", True, "#333333")
            four_text = self.font.render("4", True, "#333333")
            back_text = self.font.render("Back", True, "#333333")

            start_text_rect = start_text.get_rect(center=self.start_button.center)
            one_text_rect = one_text.get_rect(center=self.one_button.center)
            two_text_rect = two_text.get_rect(center=self.two_button.center)
            three_text_rect = three_text.get_rect(center=self.three_button.center)
            four_text_rect = four_text.get_rect(center=self.four_button.center)
            back_text_rect = back_text.get_rect(center=self.back_button.center)

            self.root.blit(start_text, start_text_rect)
            self.root.blit(one_text, one_text_rect)
            self.root.blit(two_text, two_text_rect)
            self.root.blit(three_text, three_text_rect)
            self.root.blit(four_text, four_text_rect)
            self.root.blit(back_text, back_text_rect)
            
            # Vẽ văn bản "Map 1 is selected" khi nút "1" được nhấn
            self.selected_map_info_text = self.font.render(self.selected_map_text, True, "#333333")
            self.selected_map_info_rect = self.selected_map_info_text.get_rect(center=(self.WIDTH // 2, 100))
            self.root.blit(self.selected_map_info_text, self.selected_map_info_rect)
            
            

            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
    # Function to get the selected map value
    def get_selected_map(self):
        return Map
