import sys
import zipfile
import rarfile
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog, QMessageBox

class ArchiveCommentEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.archive_files = []

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("متن کامنت جدید را وارد کنید")
        layout.addWidget(self.text_edit)
        
        self.btn_select = QPushButton("انتخاب فایل‌های ZIP و RAR", self)
        self.btn_select.clicked.connect(self.select_archive_files)
        layout.addWidget(self.btn_select)
        
        self.btn_apply = QPushButton("اعمال تغییرات", self)
        self.btn_apply.clicked.connect(self.apply_comments)
        layout.addWidget(self.btn_apply)
        
        self.setLayout(layout)
        self.setWindowTitle("ویرایش کامنت فایل‌های ZIP و RAR")
        self.resize(400, 200)
    
    def select_archive_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "انتخاب فایل ZIP یا RAR", "", "Archive Files (*.zip *.rar)")
        if files:
            self.archive_files = files
            QMessageBox.information(self, "انتخاب شد", f"{len(files)} فایل انتخاب شد.")
    
    def apply_comments(self):
        new_comment = self.text_edit.toPlainText()
        if not self.archive_files:
            QMessageBox.warning(self, "خطا", "هیچ فایلی انتخاب نشده است!")
            return
        
        for archive_path in self.archive_files:
            try:
                if archive_path.endswith('.zip'):
                    with zipfile.ZipFile(archive_path, 'a') as zipf:
                        zipf.comment = new_comment.encode("utf-8")
                elif archive_path.endswith('.rar'):
                    self.set_rar_comment(archive_path, new_comment)
            except Exception as e:
                QMessageBox.critical(self, "خطا", f"مشکلی در تغییر کامنت {archive_path} پیش آمد: {str(e)}")
                return
        
        QMessageBox.information(self, "انجام شد", "کامنت تمامی فایل‌های ZIP و RAR تغییر یافت.")
        self.archive_files = []
    
    def set_rar_comment(self, rar_path, comment):
        try:
            subprocess.run(["rar", "c", f"-z{comment}", rar_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            QMessageBox.critical(self, "خطا", "برنامه RAR روی سیستم شما نصب نیست!")
        except Exception as e:
            QMessageBox.critical(self, "خطا", f"خطا در تنظیم کامنت RAR: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArchiveCommentEditor()
    window.show()
    sys.exit(app.exec())
