
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:17:29 2023

@author: tranv
"""

import sys
import pygame
Car = 'img/carBD09.png'
class Setting:
    
    selected_car_text = ""
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
            'img/start_main.png')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.root.blit(background, (0, 0))

        # Tạo nút "Start"
        self.start_button_BD_09 = pygame.Rect(130, 15, 150, 0)
        self.button_color = pygame.Color("#FEB83C")
        self.hover_color = pygame.Color("#F1A011")

        # Tạo nút "1"
        self.one_button_BD_09 = pygame.Rect(65, 317, 30, 30)
        self.one_button_BD_09_color = pygame.Color("#FAFAFA")
        self.one_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "2"
        self.two_button_BD_09 = pygame.Rect(190, 317, 30, 30)
        self.two_button_BD_09_color = pygame.Color("#FAFAFA")
        self.two_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "3"
        self.three_button_BD_09 = pygame.Rect(307, 317, 30, 30)
        self.three_button_BD_09_color = pygame.Color("#FAFAFA")
        self.three_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "4"
        self.four_button_BD_09 = pygame.Rect(65, 568, 30, 30)
        self.four_button_BD_09_color = pygame.Color("#FAFAFA")
        self.four_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "5"
        self.five_button_BD_09 = pygame.Rect(190, 568, 30, 30)
        self.five_button_BD_09_color = pygame.Color("#FAFAFA")
        self.five_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "6"
        self.six_button_BD_09 = pygame.Rect(307, 568, 30, 30)
        self.six_button_BD_09_color = pygame.Color("#FAFAFA")
        self.six_hover_color = pygame.Color("#e8e8e8")
        
        # Tạo nút "Back"
        self.back_button_BD_09 = pygame.Rect(155, 35, 90, 40)
        self.back_button_BD_09_color = pygame.Color("#FEB83C")
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
                    global Car
                    if self.start_button_BD_09.collidepoint(mouse_pos):
                        pass
                    elif self.one_button_BD_09.collidepoint(mouse_pos): 
                        Car ='img/car1.png'
                        self.selected_car_text = "Car 1 is selected"  # Updated line
                    elif self.two_button_BD_09.collidepoint(mouse_pos):
                        Car ='img/car2.png'
                        self.selected_car_text = "Car 2 is selected"  # Updated line
                    elif self.three_button_BD_09.collidepoint(mouse_pos):
                        Car ='img/car3.png'
                        self.selected_car_text = "Car 3 is selected"  # Updated line
                    elif self.four_button_BD_09.collidepoint(mouse_pos):
                        Car ='img/car4.png'
                        self.selected_car_text = "car 4 is selected"  # Updated line
                    elif self.five_button_BD_09.collidepoint(mouse_pos):
                        Car ='img/car5.png'
                        self.selected_car_text = "car 5 is selected"  # Updated line
                    elif self.six_button_BD_09.collidepoint(mouse_pos):
                        Car ='img/carBD09.png'
                        self.selected_car_text = "car 6 is selected"  # Updated line
                    elif self.back_button_BD_09.collidepoint(mouse_pos):
                        background = pygame.image.load(
                            'img/start_main.png')
                        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
                        self.root.blit(background, (0, 0))
                        # Update the display
                        pygame.display.flip()
                        return
                        
                # Clear the screen with a background image or fill with a solid color
            background = pygame.image.load('img/Select_Car.png')
            background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
            self.root.blit(background, (0, 0))
                        
                
    

            # Lấy tọa độ chuột
            mouse_pos = pygame.mouse.get_pos()
            
            # Kiểm tra xem chuột có đang nằm trên nút "2" hay không
            if self.two_button_BD_09.collidepoint(mouse_pos):
                two_color = self.two_hover_color
            else:
                two_color = self.two_button_BD_09_color
            
            # Kiểm tra xem chuột có đang nằm trên nút "3" hay không
            if self.three_button_BD_09.collidepoint(mouse_pos):
                three_color = self.three_hover_color
            else:
                three_color = self.three_button_BD_09_color
            
            # Kiểm tra xem chuột có đang nằm trên nút "4" hay không
            if self.four_button_BD_09.collidepoint(mouse_pos):
                four_color = self.four_hover_color
            else:
                four_color = self.four_button_BD_09_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "5" hay không
            if self.five_button_BD_09.collidepoint(mouse_pos):
                five_color = self.five_hover_color
            else:
                five_color = self.five_button_BD_09_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "6" hay không
            if self.four_button_BD_09.collidepoint(mouse_pos):
                six_color = self.six_hover_color
            else:
                six_color = self.six_button_BD_09_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "back" hay không
            if self.back_button_BD_09.collidepoint(mouse_pos):
                back_color = self.back_hover_color
            else:
                back_color = self.back_button_BD_09_color
                
            # Kiểm tra xem chuột có đang nằm trên nút "Start" hay không
            if self.start_button_BD_09.collidepoint(mouse_pos):
                start_color = self.hover_color
            else:
                start_color = self.button_color

            # Kiểm tra xem chuột có đang nằm trên nút "Info" hay không
            if self.one_button_BD_09.collidepoint(mouse_pos):
                one_color = self.one_hover_color
            else:
                one_color = self.one_button_BD_09_color
            
            # Vẽ nút "2", "3", và "4" với màu hiện tại
            pygame.draw.rect(self.root, two_color, self.two_button_BD_09)
            pygame.draw.rect(self.root, three_color, self.three_button_BD_09)
            pygame.draw.rect(self.root, four_color, self.four_button_BD_09)
            pygame.draw.rect(self.root, five_color, self.five_button_BD_09)
            pygame.draw.rect(self.root, six_color, self.six_button_BD_09)
            pygame.draw.rect(self.root, back_color, self.back_button_BD_09)

            # Vẽ nút "Start" và "Info" với màu hiện tại
            pygame.draw.rect(self.root, start_color, self.start_button_BD_09)
            pygame.draw.rect(self.root, one_color, self.one_button_BD_09)

            # Vẽ văn bản "Start" và "Info" giữa nút
            start_text = self.font.render("---Select Car---", True, "#333333")
            one_text = self.font.render("1", True, "#333333")
            two_text = self.font.render("2", True, "#333333")
            three_text = self.font.render("3", True, "#333333")
            four_text = self.font.render("4", True, "#333333")
            five_text = self.font.render("5", True, "#333333")
            six_text = self.font.render("6", True, "#333333")
            back_text = self.font.render("Back", True, "#333333")

            start_text_rect = start_text.get_rect(center=self.start_button_BD_09.center)
            one_text_rect = one_text.get_rect(center=self.one_button_BD_09.center)
            two_text_rect = two_text.get_rect(center=self.two_button_BD_09.center)
            three_text_rect = three_text.get_rect(center=self.three_button_BD_09.center)
            four_text_rect = four_text.get_rect(center=self.four_button_BD_09.center)
            five_text_rect = five_text.get_rect(center=self.five_button_BD_09.center)
            six_text_rect = six_text.get_rect(center=self.six_button_BD_09.center)
            back_text_rect = back_text.get_rect(center=self.back_button_BD_09.center)

            self.root.blit(start_text, start_text_rect)
            self.root.blit(one_text, one_text_rect)
            self.root.blit(two_text, two_text_rect)
            self.root.blit(three_text, three_text_rect)
            self.root.blit(four_text, four_text_rect)
            self.root.blit(five_text, five_text_rect)
            self.root.blit(six_text, six_text_rect)
            self.root.blit(back_text, back_text_rect)
            
            # Vẽ văn bản "Car 1 is selected" khi nút "1" được nhấn
            self.selected_car_info_text = self.font.render(self.selected_car_text, True, "#333333")
            self.selected_car_info_rect = self.selected_car_info_text.get_rect(center=(self.WIDTH // 2, 100))
            self.root.blit(self.selected_car_info_text, self.selected_car_info_rect)
            
            

            pygame.display.flip()

        pygame.quit()
        sys.exit()
        
    # Function to get the selected car value
    def get_selected_car(self):
        return Car

if __name__ == "__main__":
    start_menu = Setting()
    start_menu.run_start_menu()