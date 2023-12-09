import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Algorithm:
    @staticmethod
    def plot_subject_scores_count(df_BD_09, subjects):
        for i, subject in enumerate(subjects):
            
            new_window = tk.Toplevel()
            new_window.title(f"{subject} Scores Count")
            
            # Thêm văn bản vào cửa sổ mới
            info_label = tk.Label(new_window, text=f"Biểu đồ thống kê điểm số môn {subject}", font=("Helvetica", 12))
            info_label.pack(pady=10)
    
            fig, ax = plt.subplots(figsize=(6, 4))
            p = sns.countplot(x=f'{subject} score', data=df_BD_09, palette="muted", ax=ax)
            _ = plt.setp(p.get_xticklabels(), rotation=90)
    
            canvas = FigureCanvasTkAgg(fig, master=new_window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        
    @staticmethod
    def plot_pass_status_by_parental_education(df_BD_09, subjects):
        new_window = tk.Toplevel()
        new_window.title("Pass Status by Parental Education")

        fig, axes = plt.subplots(1, len(subjects), figsize=(6 * len(subjects), 4), sharey=True)

        total_pass_counts = 0
        total_fail_counts = 0
        
        # Thêm văn bản vào cửa sổ mới
        info_label = tk.Label(new_window, text="Biểu đồ thể hiện số lượng sinh viên Pass và Fail môn Math, Reading, Writing", font=("Helvetica", 12))
        info_label.pack(pady=10)

        for i, subject in enumerate(subjects):
            pass_status_column = f"{subject} PassStatus"
            df_BD_09[pass_status_column] = np.where(df_BD_09[f'{subject} score'] < 40, 'F', 'P')
            df_BD_09[pass_status_column].value_counts()

            p = sns.countplot(x='parental level of education', data=df_BD_09, hue=pass_status_column, palette='bright', ax=axes[i])
            _ = plt.setp(p.get_xticklabels(), rotation=90)

            # Đếm số lượng 'P' và 'F'
            pass_status_counts = df_BD_09[pass_status_column].value_counts()

            # In thông tin vào cửa sổ
            info_text = f"{subject} - Số lượng đã PASS: {pass_status_counts.get('P', 0)}\nSố lượng đã FAIL: {pass_status_counts.get('F', 0)}"
            pass_info_label = tk.Label(new_window, text=info_text, font=("Helvetica", 10))
            pass_info_label.pack(pady=5)

            # Update total counts
            total_pass_counts += pass_status_counts.get('P', 0)
            total_fail_counts += pass_status_counts.get('F', 0)

        # Display total pass/fail counts
        total_info_label = tk.Label(new_window, text=f"\nTổng số lượng đã PASS: {total_pass_counts}\nTổng số lượng đã FAIL: {total_fail_counts}", font=("Helvetica", 10))
        total_info_label.pack(pady=10)

        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
    @staticmethod    
    def plot_percentage_distribution(df_BD_09):
        df_BD_09['Total_Marks'] = df_BD_09['math score'] + df_BD_09['reading score'] + df_BD_09['writing score']
        df_BD_09['Percentage'] = df_BD_09['Total_Marks'] / 3
    
        new_window = tk.Toplevel()
        new_window.title("Percentage Distribution")
    
        fig, ax = plt.subplots(figsize=(8, 6))
        p = sns.countplot(x="Percentage", data=df_BD_09, palette="muted", ax=ax)
        _ = plt.setp(p.get_xticklabels(), rotation=0)
    
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    @staticmethod
    def plot_scores_by_race(df):
        fig, ax = plt.subplots(1, 3, figsize=(12, 6))
    
        # Set the titles for each axis
        ax[0].set_title('Maths score')
        ax[1].set_title('Reading score')
        ax[2].set_title('Writing score')
    
        # Bar plotting
        sns.barplot(ax=ax[0], data=df, x='math score', y='race/ethnicity', palette='inferno')
        sns.barplot(ax=ax[1], data=df, x='reading score', y='race/ethnicity', palette='inferno')
        sns.barplot(ax=ax[2], data=df, x='writing score', y='race/ethnicity', palette='inferno')
    
        plt.xlim(40)
        plt.tight_layout()
        
        new_window = tk.Toplevel()
        new_window.title("Scores by Race/Ethnicity")
        
        # Thêm văn bản vào cửa sổ mới
        info_label = tk.Label(new_window, text="Điểm cho mỗi khóa học theo Race/Ethnicity", font=("Helvetica", 12))
        info_label.pack(pady=10)
        
        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    @staticmethod
    def plot_scores_with_test_preparation(df):
        fig, ax = plt.subplots(1, 3, figsize=(12, 6))

        # Set the titles for each axis
        ax[0].set_title('Maths score')
        ax[1].set_title('Reading score')
        ax[2].set_title('Writing score')

        # Bar plotting (hue set to "test_preparation")
        sns.barplot(ax=ax[0], data=df, x='math score', y='race/ethnicity', palette='inferno', hue='test preparation course')
        sns.barplot(ax=ax[1], data=df, x='reading score', y='race/ethnicity', palette='inferno', hue='test preparation course')
        sns.barplot(ax=ax[2], data=df, x='writing score', y='race/ethnicity', palette='inferno', hue='test preparation course')

        plt.xlim(50)
        plt.tight_layout()

        new_window = tk.Toplevel()
        new_window.title("Scores with Test Preparation")
        
        # Thêm văn bản vào cửa sổ mới
        info_label = tk.Label(new_window, text="Scores for each course with test preparation", font=("Helvetica", 12))
        info_label.pack(pady=10)

        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    @staticmethod
    def plot_parents_education(df):
        plt.figure(figsize=(12, 8))
        plt.title('Parents education')
        sns.countplot(x='parental level of education', data=df, hue='race/ethnicity', palette='mako')

        new_window = tk.Toplevel()
        new_window.title("Parents Education Count")
        
        # Thêm văn bản vào cửa sổ mới
        info_label = tk.Label(new_window, text="Thống kê học vấn gia đình", font=("Helvetica", 12))
        info_label.pack(pady=10)

        canvas = FigureCanvasTkAgg(plt.gcf(), master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    @staticmethod
    def plot_performance_on_lunch(df):
        fig, ax = plt.subplots(1, 3, figsize=(12, 6))
        # Set the titles for each axis
        ax[0].set_title('Maths score')
        ax[1].set_title('Reading score')
        ax[2].set_title('Writing score')

        # Bar plotting (hue set to "lunch")
        sns.barplot(ax=ax[0], data=df, x='math score', y='race/ethnicity', palette='inferno', hue='lunch')
        sns.barplot(ax=ax[1], data=df, x='reading score', y='race/ethnicity', palette='inferno', hue='lunch')
        sns.barplot(ax=ax[2], data=df, x='writing score', y='race/ethnicity', palette='inferno', hue='lunch')

        plt.xlim(50)
        plt.tight_layout()

        new_window = tk.Toplevel()
        new_window.title("Performance on Lunch")
        
        # Thêm văn bản vào cửa sổ mới
        info_label = tk.Label(new_window, text="Phân tích ảnh hưởng của chế độ ăn", font=("Helvetica", 12))
        info_label.pack(pady=10)

        canvas = FigureCanvasTkAgg(plt.gcf(), master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        
