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
        self.text_edit.setPlaceholderText("Enter new comment text")
        layout.addWidget(self.text_edit)
        
        self.btn_select = QPushButton("Select ZIP and RAR files", self)
        self.btn_select.clicked.connect(self.select_archive_files)
        layout.addWidget(self.btn_select)
        
        self.btn_apply = QPushButton("Apply Changes", self)
        self.btn_apply.clicked.connect(self.apply_comments)
        layout.addWidget(self.btn_apply)
        
        self.setLayout(layout)
        self.setWindowTitle("Edit ZIP and RAR File Comments")
        self.resize(400, 200)
    
    def select_archive_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select ZIP or RAR files", "", "Archive Files (*.zip *.rar)")
        if files:
            self.archive_files = files
            QMessageBox.information(self, "Selected", f"{len(files)} files selected.")
    
    def apply_comments(self):
        new_comment = self.text_edit.toPlainText()
        if not self.archive_files:
            QMessageBox.warning(self, "Error", "No files selected!")
            return
        
        for archive_path in self.archive_files:
            try:
                if archive_path.endswith('.zip'):
                    with zipfile.ZipFile(archive_path, 'a') as zipf:
                        zipf.comment = new_comment.encode("utf-8")
                elif archive_path.endswith('.rar'):
                    self.set_rar_comment(archive_path, new_comment)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error modifying comment for {archive_path}: {str(e)}")
                return
        
        QMessageBox.information(self, "Done", "Comments updated for all selected ZIP and RAR files.")
        self.archive_files = []
    
    def set_rar_comment(self, rar_path, comment):
        try:
            subprocess.run(["rar", "c", f"-z{comment}", rar_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "RAR program is not installed on your system!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error setting RAR comment: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArchiveCommentEditor()
    window.show()
    sys.exit(app.exec())
