import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from Launcher_UI import Ui_OM

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_OM()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.launch_model)
        self.ui.pushButton_2.clicked.connect(self.close_app)
        self.ui.label_5.mousePressEvent = self.show_info
        self.ui.comboBox.mousePressEvent = self.open_file_dialog

        self.ui.comboBox.addItem("Select a model executable")

    def create_styled_messagebox(self, title, text, box_type="info"):

        box = QMessageBox(self)

        box.setWindowTitle(title)
        box.setText(text)
        if box_type == "error":
            box.setIcon(QMessageBox.Icon.Critical)
        elif box_type == "info":
            box.setIcon(QMessageBox.Icon.Information)

        ok_button = QPushButton("OK")
        ok_button.setStyleSheet(
            """
            QPushButton {
                background-color: #0078d7;  /* Classic blue color */
                color: white;
                font-weight: bold;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #003f73;
            }
            """
        )
        box.addButton(ok_button, QMessageBox.ButtonRole.AcceptRole)

        box.setStyleSheet(
            """
            QMessageBox {
                background-color: #f4f4f4;
                border: 1px solid #d3d3d3;
                border-radius: 8px;
            }
            QLabel {
                color: #333;
                font-size: 12pt;
            }
            """
        )
        box.exec()

    def launch_model(self):
        selected_model = self.ui.comboBox.currentText()
        start_time = self.ui.lineEdit_2.text()
        stop_time = self.ui.lineEdit.text()

        if selected_model == "Select a model executable" or not selected_model.endswith(".exe"):
            self.create_styled_messagebox("Error", "Please select a valid OpenModelica executable, start time and stop time.", box_type="error")
            return
        if not start_time.isdigit() or not stop_time.isdigit():
            self.create_styled_messagebox("Error", "Start time and Stop time must be numeric.", box_type="error")
            return

        try:
            subprocess.Popen([selected_model, f"-startTime={start_time}", f"-stopTime={stop_time}"])
            self.create_styled_messagebox("Success", "Model launched successfully!", box_type="info")
        except Exception as e:
            self.create_styled_messagebox("Error", f"Failed to launch the model: {str(e)}", box_type="error")

    def open_file_dialog(self, event):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Select OpenModelica Executable", "", "Executables (*.exe)")
        if file_path:
            self.ui.comboBox.clear()  # Clear placeholder
            self.ui.comboBox.addItem(file_path)

    def show_info(self, event):
        info_text = (
            "<h3>About OM Launcher</h3>"
            "<p>This OpenModelica Launcher helps you execute OpenModelica models with specified start and stop times.</p>"
            "<p><b>GitHub Repository:</b> "
            "<a href='https://github.com/Jeyapranov'>https://github.com/Jeyapranov</a></p>"
        )
        self.create_styled_messagebox("About OM Launcher", info_text, box_type="info")

    def close_app(self):

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
