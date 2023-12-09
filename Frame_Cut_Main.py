
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 05 22:15:18 2023

@author: tranv
"""
import tkinter as tk_BD09
from tkinter import filedialog, scrolledtext
from tkinter import messagebox
import cv2
from gtts import gTTS
import pyttsx3
import time
import pygame
from datetime import datetime
from PIL import Image
import pygame.mixer
import speech_recognition as srBD09
import numpy as np
import os


class VideoProcessor:
    def __init__(self):
        self.save_name_BD09 = "..."
        self.file_image_BD09 = "..."
        self.create_gui()

    def read_and_record_text_BD09(self, text):
        pygame.mixer.init()
        # Chuyển đoạn văn bản thành giọng nói và lưu vào file âm thanh
        tts = gTTS(text=text, lang='vi')  # Bạn có thể thay đổi 'en' thành ngôn ngữ mong muốn
         # Tạo một chuỗi thời gian dựa trên ngày và giờ hiện tại
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Lưu tệp âm thanh với tên duy nhất dựa trên thời gian
        tts.save(f"output_{current_time}.mp3")
    
        # Phát lại giọng nói
        engine = pyttsx3.init()
        engine.setProperty('rate', 100)  # Tốc độ phát lại (có thể điều chỉnh)
        engine.save_to_file(text, 'output.wav')
        engine.runAndWait()
    
        # Đợi một khoảng thời gian trước khi bắt đầu ghi âm để đảm bảo giọng nói đã bắt đầu
        time.sleep(2)
        
        pygame.mixer.music.load(f"output_{current_time}.mp3")
        pygame.mixer.music.play()

    def record(self):
        try:
            recognizer = srBD09.Recognizer()
            self.intro_record()
            with srBD09.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)
    
                self.window.update()
                audio = recognizer.record(source, duration=7)
            # Perform speech recognition
            text = recognizer.recognize_google(audio, language='vi')
            return text
        except Exception as e:
            messagebox.showerror("Lỗi khi nghe âm thanh", str(e))

    def intro_record(self):
        self.log_text.insert(tk_BD09.END, "\n")
        self.log_text.insert(tk_BD09.END, "Đang điều chỉnh tiếng ồn xung quanh...\n")
        time.sleep(2)
        self.log_text.insert(tk_BD09.END, "Thời gian thu âm là 5 giây\n")
        self.log_text.insert(tk_BD09.END, "Đang nghe...\n")

    def intro(self):
        self.read_and_record_text_BD09("Vui lòng lựa chọn file muốn sử dụng và nhập số vào ô trống phía dưới ")
        self.log_text.insert(tk_BD09.END, "Chọn file video muốn cắt frame:\n")
        self.log_text.insert(tk_BD09.END, "1. 09BaoDuy_Bird1\n")
        self.log_text.insert(tk_BD09.END, "2. 09BaoDuy_Bird2\n")
        self.log_text.insert(tk_BD09.END, "3. 09BaoDuy_Bird3\n")
        self.log_text.insert(tk_BD09.END, "4. 09BaoDuy_Bird4\n")
        self.log_text.insert(tk_BD09.END, "5. 09BaoDuy_Bird5\n")

    def select_video(self):
        option_BD09 = int(self.choose_entry.get())

        if option_BD09 == 1:
            self.file_name = "09BaoDuy_Bird1.mp4"
        elif option_BD09 == 2:
            self.file_name = "09BaoDuy_Bird2.mp4"
        elif option_BD09 == 3:
            self.file_name = "09BaoDuy_Bird3.mp4"
        elif option_BD09 == 4:
            self.file_name = "09BaoDuy_Bird4.mp4"
        elif option_BD09 == 5:
            self.file_name = "09BaoDuy_Bird5.mp4"
        else:
            messagebox.showerror("Lỗi mở file")
            self.log_text.insert(tk_BD09.END, "Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")
        self.process_video(self.file_name)

    def process_video(self, filename):
        self.log_text.insert(tk_BD09.END, " \n")
        self.log_text.insert(tk_BD09.END, " \n")
        self.read_and_record_text_BD09("Đang tiến hành cắt frame, vui lòng đợi!")
        cap_BD09 = cv2.VideoCapture(filename)
        count = 0
        while cap_BD09.isOpened():
            ret, frame = cap_BD09.read()
            if not ret:
                break
            cv2.imshow('Processing...', frame)
            folder = str(self.save_name_BD09)
            # Đường dẫn đầy đủ cho ảnh mới
            image_path = f"{folder}/frame{count}.jpg"
    
            # Lưu ảnh vào đường dẫn được chọn
            cv2.imwrite(image_path, frame)
            count += 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap_BD09.release()
        cv2.destroyAllWindows()
        self.log_text.insert(tk_BD09.END, f"Đã cắt được {count} ảnh")
        self.read_and_record_text_BD09(f"Đã cắt được {count} ảnh")
        messagebox.showinfo("Thành công", f"Đã cắt được {count} ảnh")

    def text_to_speech(self, text, lang='vi'):
        # Tạo đối tượng gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        # Lưu file âm thanh
        tts.save("output.mp3")
        # Phát file âm thanh
        os.system("start output.mp3")

    def select_save_folder(self):
        self.read_and_record_text_BD09("Hãy chọn đường dẫn bạn muốn lưu ảnh")
        folder_path = filedialog.askdirectory()
        if folder_path:
            save_folder_path = folder_path
            self.save_name_BD09 = save_folder_path
            self.read_and_record_text_BD09("Đã chọn được nơi lưu ảnh")
            messagebox.showinfo("Thành công", f"Đã chọn thư mục: {save_folder_path}")

    def update_label(self):
        # Xóa nội dung hiện tại của Label
        self.save_file_label.config(text="")
        # Thêm nội dung mới từ biến save_name_BD09
        self.save_file_label.config(text=self.save_name_BD09)
        
    
        self.image_file_label.config(text="")
        self.image_file_label.config(text=self.file_image_BD09)

    def select_image(self):
        # Chọn ảnh từ hộp thoại
        self.read_and_record_text_BD09("Hãy chọn ảnh muốn xử lý")
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.read_and_record_text_BD09("Đã chọn được file ảnh")
        messagebox.showinfo("Thành công", f"Đã chọn ảnh từ: {file_path}")
        self.file_image_BD09 = file_path
    
    def gray_scale(self):
        # Mở ảnh từ đường dẫn
        anh = Image.open(self.file_image_BD09)
        # Chuyển đổi thành ảnh đen trắng
        anh_den_trang = anh.convert('L')
        # Lưu ảnh mới vào đường dẫn đích
        anh_den_trang.save(self.file_image_BD09)
        image = cv2.imread(self.file_image_BD09)  # Đọc ảnh từ đường dẫn
        cv2.imshow("Gray Image", image)  # Hiển thị ảnh trong cửa sổ với tên "Image"
        cv2.waitKey(0)  # Đợi cho đến khi có phản hồi từ người dùng (ấn phím bất kỳ)
        cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ hiển thị
    
    def rotate(self):
        # Mở ảnh từ đường dẫn
        anh = Image.open(self.file_image_BD09)
        self.read_and_record_text_BD09("Hãy đọc lên góc muốn quay, chỉ đọc số")
        angle = int(self.record())
        self.log_text.insert(tk_BD09.END, f"Số góc bạn đọc là: {angle}")
        time.sleep(3)
        # Quay ảnh theo góc quay
        rotate_image = anh.rotate(angle, expand=True)
        # Lưu ảnh mới vào đường dẫn đích
        rotate_image.save(self.file_image_BD09)
        image = cv2.imread(self.file_image_BD09)  # Đọc ảnh từ đường dẫn
        cv2.imshow("Rotated Image", image)  # Hiển thị ảnh trong cửa sổ với tên "Image"
        cv2.waitKey(0)  # Đợi cho đến khi có phản hồi từ người dùng (ấn phím bất kỳ)
        cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ hiển thị
        
    
    def predict_bird(self):
        # Mở ảnh từ đường dẫn
        image = cv2.imread('D:/temp/frameDetected.jpg')  # Đọc ảnh từ đường dẫn
        cv2.imshow("Bird Detecting", image)  # Hiển thị ảnh trong cửa sổ với tên "Image"
        cv2.waitKey(0)  # Đợi cho đến khi có phản hồi từ người dùng (ấn phím bất kỳ)
        cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ hiển thị


    def Thoat(self):
        # hàm thoát 
        traloi = messagebox.askquestion("Xác nhận", "Bạn có muốn thoát không (Y/N)?")
        if traloi == "yes": self.window.destroy() #wn.quit()

    def create_gui(self):
        # Tạo tk_BD09inter window
        self.window = tk_BD09.Tk()
        self.window.title("Xử lý video")
        self.window.geometry("400x400")

        # Tạo labels và entry fields cho input
        choose_label = tk_BD09.Label(self.window, text="Chọn video số (chỉ nhập 1, 2, 3):")
        choose_label.pack()

        self.choose_entry = tk_BD09.Entry(self.window)
        self.choose_entry.pack()

        # Tạo nút "Chọn thư mục lưu ảnh"
        save_file_button = tk_BD09.Button(self.window, text="Chọn thư mục lưu ảnh",
                                          command=lambda: [self.select_save_folder(), self.update_label()])
        save_file_button.pack()

        save_file_label_intro = tk_BD09.Label(self.window, text="Đường dẫn thư mục đã chọn: ")
        save_file_label_intro.pack()
        self.save_file_label = tk_BD09.Label(self.window, text=self.save_name_BD09)
        self.save_file_label.pack()

        # Tạo một scrolledtext widget để hiển thị log messages
        self.log_text = scrolledtext.ScrolledText(self.window, width=40, height=10)
        self.log_text.pack()

        start_button = tk_BD09.Button(self.window, text="Tiến hành cắt frame", command=self.select_video, fg="white",
                                      bg="green")
        start_button.pack()

        # Nút để chọn ảnh
        select_image_button = tk_BD09.Button(self.window, text="Xử lí ảnh", command=lambda: [self.select_image(),
                                                                                            self.update_label()])
        select_image_button.pack()

        image_file_label_intro = tk_BD09.Label(self.window, text="Đường dẫn ảnh đã chọn: ")
        image_file_label_intro.pack()
        self.image_file_label = tk_BD09.Label(self.window, text=self.file_image_BD09)
        self.image_file_label.pack()

        gray_button = tk_BD09.Button(self.window, text="Trắng Đen", command=self.gray_scale, fg="blue", bg="white")
        gray_button.pack(side='left', padx=3, pady=3)

        rotate_button = tk_BD09.Button(self.window, text="Quay ảnh", command=self.rotate, fg="blue", bg="white")
        rotate_button.pack(side='left', padx=3, pady=3)

        AI_button = tk_BD09.Button(self.window, text="Nhận diện loài chim", command=self.predict_bird, fg="blue",
                                   bg="white")
        AI_button.pack(side='left', padx=3, pady=3)

        exit_button = tk_BD09.Button(self.window, text="Thoát", command=self.Thoat, fg="white", bg="red")
        exit_button.pack(side='right', padx=3, pady=3)

        self.intro()
        # Bắt đầu vòng lặp sự kiện tk_BD09inter
        self.window.mainloop()


