import pandas as pd
import tkinter as tk
from scipy import stats
from sklearn import preprocessing
from tkinter import ttk, messagebox
from Algorithm_Display import Algorithm
import numpy as np
import pygame
from gtts import gTTS
from datetime import datetime
import pyttsx3
import time

class DataProcessor:
    @staticmethod
    def load_data(file_path):
        df_BD_09 = pd.read_csv(file_path)
        return df_BD_09
    
    @staticmethod
    def preprocess_data(df_BD_09):
        df_BD_09 = df_BD_09.dropna(how='any')

        return df_BD_09
    

class StudentPerformanceApp:
    def z_score(self):
        self.df_BD_09 = self.df_BD_09.dropna(how='any')
        self.df_BD_09 = self.df_BD_09.drop(columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'PreTest', \
                      'PracticeSport', 'NrSiblings', 'TransportMeans', 'Date', 'number oder', 'IsFirstChild'], axis=1)					

        z = np.abs(stats.zscore(self.df_BD_09._get_numeric_data()))
        self.df_BD_09 = self.df_BD_09[(z < 3).all(axis=1)]
        rr = preprocessing.MinMaxScaler()
        rr.fit(self.df_BD_09)
        self.df_BD_09 = pd.DataFrame(rr.transform(self.df_BD_09), index=self.df_BD_09.index, columns=self.df_BD_09.columns)
        self.df_BD_09.iloc[4:10]
        # Clear existing items in the TreeView
        self.tree.delete(*self.tree.get_children())
    
        # Repopulate the TreeView with the updated data
        for index, row in self.df_BD_09.iterrows():
            self.tree.insert("", index, values=tuple(row))
        
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
        engine.setProperty('rate', 130)  # Tốc độ phát lại (có thể điều chỉnh)
        engine.save_to_file(text, 'output.wav')
        engine.runAndWait()
    
        # Đợi một khoảng thời gian trước khi bắt đầu ghi âm để đảm bảo giọng nói đã bắt đầu
        time.sleep(2)
        
        pygame.mixer.music.load(f"output_{current_time}.mp3")
        pygame.mixer.music.play()
        
    def __init__(self, root):
        self.root = root
        self.root.title("Student Performance App")
        

        title_label = tk.Label(self.root, text="TRẦN VĂN BẢO DUY", font=("Helvetica", 16), pady=10, fg="white", bg="#0074ce")
        title_label.pack()
        title_label = tk.Label(self.root, text="EDA PHÂN TÍCH THĂM DÒ THÀNH TÍCH CỦA HỌC SINH TẠI MỘT TRƯỜNG CÔNG LẬP Ở MỸ NĂM 2022\n VỚI SỰ ẢNH HƯỞNG BỞI CÁC YẾU TỐ KHÁCH QUAN VÀ CHỦ QUAN", font=("Helvetica", 13, "bold"), pady=10, fg="white", bg="#0074ce")
        title_label.pack()

        load_data_button = tk.Button(self.root, text="Load Data", command=self.load_and_display_data)
        load_data_button.pack(padx=5, pady=5)

        self.canvas_frame = tk.Frame(self.root, bg='lightblue')
        self.canvas_frame.pack(side=tk.LEFT, padx=15, pady=15)
        

        self.root.geometry("1000x600")
        self.read_and_record_text_BD09("Hãy nhấn Load Data để hiển thị lên dữ liệu!")

    def load_and_display_data(self):
        self.df_BD_09 = DataProcessor.load_data('./StudentsPerformance.csv')
        self.read_and_record_text_BD09("Đã load dữ liệu thành công!")
        self.read_and_record_text_BD09("Hãy thực hiện xóa một số cột giá trị không có ích!")

        self.canvas_frame = tk.Frame(self.root, bg='lightblue')
        self.canvas_frame.pack(side=tk.LEFT, padx=15, pady=15)

        self.canvas_width = 1000
        self.canvas_height = 350
        self.canvas = tk.Canvas(self.canvas_frame, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        xsb = ttk.Scrollbar(self.canvas_frame, orient='horizontal', command=self.canvas.xview)
        xsb.pack(side=tk.BOTTOM, fill='x')
        self.canvas.configure(xscrollcommand=xsb.set)

        self.tree_frame = tk.Frame(self.canvas, bg='blue')
        self.canvas.create_window((10, 10), window=self.tree_frame, anchor=tk.NW)

        columns = list(self.df_BD_09.columns)
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')

        for i, row in self.df_BD_09.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.tree.pack(side=tk.LEFT)
        self.tree.bind("<Configure>", self.on_treeview_configure)

        refresh_frame = ttk.Frame(self.root)
        refresh_frame.place(relx=0.1, rely=0.85, anchor="s")
        refresh_frame.configure(borderwidth=15)

        refresh_button = tk.Button(refresh_frame, text="Z_score", command=self.z_score)
        refresh_button.pack(side=tk.TOP, padx=5)

        exit_frame = ttk.Frame(self.root)
        exit_frame.place(relx=0.9, rely=0.83, anchor="s")

        gray_button = tk.Button(exit_frame, text="Exit", command=self.root.destroy, fg="white", bg="red")
        gray_button.pack(side='left', padx=3, pady=3)
        
        preprocess_frame = ttk.Frame(self.root)
        preprocess_frame.place(relx=0.2, rely=0.83, anchor="s")

        self.preprocess_button_pressed = False
        self.pre_button = tk.Button(preprocess_frame, text="Pre-process", command=self.preprocess_and_refresh_data, fg="white", bg="green")
        self.pre_button.pack(side='left', padx=3, pady=3)
        self.pre_button.bind("<Button-1>", self.hide_button_after_click)
        
        # Create and configure a combobox
        combo_frame = ttk.Frame(self.root)
        combo_frame.place(relx=0.55, rely=0.825, anchor="s")

        combo_label = tk.Label(combo_frame, text="Data Analysis:", font=("Helvetica", 12, "bold"))
        combo_label.pack(side='left', padx=6)

        # Tạo danh sách giá trị bạn muốn hiển thị trong Combobox
        custom_values = ["Tổng kết đỗ/trượt theo học vấn của ba mẹ", "Thống kê điểm theo từng môn", "Thống kê phổ điểm trung bình cộng", \
                         "Điểm cho mỗi khóa học theo Race/Ethnicity", "Phân tích điểm khi có làm kiểm tra thử", "Thống kê học vấn gia đình", "Phân tích ảnh hưởng của chế độ ăn"]  # Thay đổi thành giá trị bạn muốn

        # Tạo Combobox với danh sách giá trị tùy chỉnh
        self.selected_value = tk.StringVar()
        combo = ttk.Combobox(combo_frame, textvariable=self.selected_value, values=custom_values, width=35)
        combo.pack(side='left', padx=8)
        # Nếu bạn muốn cập nhật giá trị Combobox tùy thuộc vào sự chọn lựa của người dùng, thêm sự kiện binding
        combo.bind("<<ComboboxSelected>>", self.on_combobox_selected)
        
        #============= XÓA CỘT =============#
        # Create and configure a combobox
        combo_col_frame = ttk.Frame(self.root)
        combo_col_frame.place(relx=0.9, rely=0.925, anchor="s")

        combo_col_label = tk.Label(combo_frame, text="Delete Col:", font=("Helvetica", 12, "bold"))
        combo_col_label.pack(side='left', padx=5)

        # Tạo danh sách giá trị bạn muốn hiển thị trong Combobox
        custom_col_values = ["TransportMeans", "NrSiblings", "IsFirstChild", \
                         "PracticeSport", "Date"]  # Thay đổi thành giá trị bạn muốn

        # Tạo Combobox với danh sách giá trị tùy chỉnh
        self.selected_col_value = tk.StringVar()
        combo = ttk.Combobox(combo_frame, textvariable=self.selected_col_value, values=custom_col_values, width=15)
        combo.pack(side='left', padx=5)
        
        combo.bind("<<ComboboxSelected>>", self.on_combobox_col_selected)
        
    def on_combobox_selected(self, event):
        # This function will be called when the combobox value changes
        selected_value = self.selected_value.get()
        
        # You can use the selected_value as needed, for example, print it
        print("Selected Column:", selected_value)
        if selected_value == "Tổng kết đỗ/trượt theo học vấn của ba mẹ":
            Algorithm.plot_pass_status_by_parental_education(self.df_BD_09, ['math', 'reading', 'writing'])
            time.sleep(3)
            self.read_and_record_text_BD09("Khi nói đến điểm kiểm tra của học sinh, có vẻ có mối quan hệ rõ ràng với học vị của Phụ Huynh.")
            self.read_and_record_text_BD09("Con cái của Phụ Huynh có học vị cao hơn thì điểm số cao hơn so với con cái của Phụ Huynh có học vị thấp hơn. Mô hình này được quan sát đều đặn với tất cả ba môn kiểm tra.")
            
        if selected_value == "Thống kê điểm theo từng môn":
            Algorithm.plot_subject_scores_count(self.df_BD_09, ['math', 'reading', 'writing'])
            
        if selected_value == "Thống kê phổ điểm trung bình cộng":
            Algorithm.plot_percentage_distribution(self.df_BD_09)
            time.sleep(3)
            self.read_and_record_text_BD09("Điểm trung bình cộng là điểm tổng 3 môn chia 3, thấy được sự phân bố phổ điểm tập trung nhiều ở tầm trung, ít ở phổ điểm thấp và khá ít ở điểm cao")
            
        if selected_value == "Điểm cho mỗi khóa học theo Race/Ethnicity":
            Algorithm.plot_scores_by_race(self.df_BD_09)
            
        if selected_value == "Phân tích điểm khi có làm kiểm tra thử":
            Algorithm.plot_scores_with_test_preparation(self.df_BD_09)
            time.sleep(3)
            self.read_and_record_text_BD09("Ngay cả khi không chuẩn bị bài kiểm tra, nhóm E vẫn hơn mọi nhóm khác ở điểm môn toán")
            self.read_and_record_text_BD09("và gần như vượt trội nhóm D & nhóm A ở điểm đọc bằng cách chuẩn bị bài kiểm tra. Do đó ta thấy dù có tố chất sẵn có nhưng nếu cần cù chuẩn bị trước thì việc có số điểm cao vẫn có thể đạt được.")
            
            
        if selected_value == "Thống kê học vấn gia đình":
            Algorithm.plot_parents_education(self.df_BD_09)
            
        if selected_value == "Phân tích ảnh hưởng của chế độ ăn":
            Algorithm.plot_performance_on_lunch(self.df_BD_09)
            time.sleep(3)
            self.read_and_record_text_BD09("Những học sinh đã ăn trưa sẽ có kết quả học tập tốt hơn những học sinh chưa ăn trưa trước đó. ")
            self.read_and_record_text_BD09("Qua đó chắc chắn có thể xác định rằng ăn uống rất quan trọng và góp phần không nhỏ vào sự hoạt động của cơ thể lẫn thể chất và trí não.")
        
    
        
    def on_combobox_col_selected(self, event):
        selected_column = self.selected_col_value.get()
        selected_col_value = self.selected_col_value.get()
        
        print("Selected Column:", selected_col_value)
        if selected_col_value == "TransportMeans":
            self.delete_column_and_refresh_data("TransportMeans")
            self.read_and_record_text_BD09("Đã xóa cột TransportMeans thành công!")
            self.refresh_data()
    
        if selected_col_value == "IsFirstChild":
            self.delete_column_and_refresh_data("IsFirstChild")
            self.read_and_record_text_BD09("Đã xóa cột IsFirstChild thành công!")
            self.refresh_data()
            
        if selected_col_value == "PracticeSport":
            self.delete_column_and_refresh_data("PracticeSport")
            self.read_and_record_text_BD09("Đã xóa cột PracticeSport thành công!")
            self.refresh_data()
            
        if selected_col_value == "Date":
            self.delete_column_and_refresh_data("Date")
            self.read_and_record_text_BD09("Đã xóa cột Date thành công!")
            self.refresh_data()
            
        if selected_col_value == "NrSiblings":
            self.delete_column_and_refresh_data("NrSiblings")
            self.read_and_record_text_BD09("NrSiblings")
            self.refresh_data()
        
    def delete_column_and_refresh_data(self, column_name):
        # Check if the column exists in the DataFrame
        if column_name in self.df_BD_09.columns:
            # Remove the specified column
            self.df_BD_09 = self.df_BD_09.drop(columns=[column_name], axis=1)
            
            # Refresh the displayed data
            self.refresh_data()
            
            # Optionally, update the TreeView's columns and data
            self.update_treeview_columns()

            # Optionally, you may want to handle any additional actions related to column deletion
            
        else:
            messagebox.showinfo("Column Not Found", f"Column '{column_name}' not found in the DataFrame.")

    def update_treeview_columns(self):
        # Clear existing columns in the TreeView
        for col in self.tree["columns"]:
            self.tree.heading(col, text="")
            self.tree.column(col, width=0)

        # Configure columns based on the updated DataFrame
        columns = list(self.df_BD_09.columns)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='center')
        # Automatically resize the canvas to fit the updated TreeView
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        
            
    def hide_button_after_click(self, event):
        if self.preprocess_button_pressed:
            self.pre_button.config(state=tk.DISABLED)

    def preprocess_and_refresh_data(self):
        self.preprocess_button_pressed = True
        self.hide_button_after_click(None)
        self.deleted_rows_label = tk.Label(self.root, text="", fg="yellow", font=("Helvetica", 13, "bold"), bg="#0074ce")
        self.deleted_rows_label.pack(pady=5)
        self.deleted_rows_label.place(relx=0.51, rely=0.239, anchor="n")
        self.original_shape = self.df_BD_09.shape
        self.df_BD_09 = DataProcessor.preprocess_data(self.df_BD_09)
        self.deleted_rows = self.original_shape[0] - self.df_BD_09.shape[0]
        self.shape = self.df_BD_09.shape
        self.deleted_rows_message = f"Đã xóa {self.deleted_rows} hàng có giá trị NULL\n còn lại {self.shape}"
        self.deleted_rows_label.config(text=self.deleted_rows_message)
        self.root.after(5000, self.remove_deleted_rows_message)
        self.refresh_data()
        self.read_and_record_text_BD09("Đã hoàn thành tiền xử lý! Hãy chọn các thống kê biểu đồ để xem phân tích dữ liệu")

    def remove_deleted_rows_message(self):
        self.deleted_rows_label.config(text="")

    def on_treeview_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def refresh_data(self):
        # Clear existing items in the TreeView
        self.tree.delete(*self.tree.get_children())
    
        # Repopulate the TreeView with the updated data
        for index, row in self.df_BD_09.iterrows():
            self.tree.insert("", index, values=tuple(row))
            

