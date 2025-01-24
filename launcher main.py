import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from Launcher_UI import Ui_OM  # Replace with the actual name of your .py file converted from .ui


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_OM()
        self.ui.setupUi(self)

        # Connect buttons and interactive elements
        self.ui.pushButton.clicked.connect(self.launch_model)  # Launch button
        self.ui.pushButton_2.clicked.connect(self.close_app)   # Cancel button
        self.ui.label_5.mousePressEvent = self.show_info       # "i" icon click event (fixed here)
        self.ui.comboBox.mousePressEvent = self.open_file_dialog  # ComboBox click to select exe file

        # Initialize ComboBox placeholder
        self.ui.comboBox.addItem("Select a model executable")  # Initial placeholder

    def create_styled_messagebox(self, title, text, box_type="info"):
        """Create a custom-styled QMessageBox."""
        box = QMessageBox(self)

        # Set the title, text, and icon based on the box type
        box.setWindowTitle(title)
        box.setText(text)
        if box_type == "error":
            box.setIcon(QMessageBox.Icon.Critical)
        elif box_type == "info":
            box.setIcon(QMessageBox.Icon.Information)

        # Custom style for the OK button
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

        # Custom style for the box itself
        box.setStyleSheet(
            """
            QMessageBox {
                background-color: 
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
        """Launch the selected model with the specified parameters."""
        selected_model = self.ui.comboBox.currentText()
        start_time = self.ui.lineEdit_2.text()
        stop_time = self.ui.lineEdit.text()

        # Validation
        if selected_model == "Select a model executable" or not selected_model.endswith(".exe"):
            self.create_styled_messagebox("Error", "Please select a valid OpenModelica executable, Start time and Stop time.", box_type="error")
            return
        if not start_time.isdigit() or not stop_time.isdigit():
            self.create_styled_messagebox("Error", "Start time and Stop time must be numeric.", box_type="error")
            return

        # Launch the executable
        try:
            subprocess.Popen([selected_model, f"-startTime={start_time}", f"-stopTime={stop_time}"])
            self.create_styled_messagebox("Success", "Model launched successfully!", box_type="info")
        except Exception as e:
            self.create_styled_messagebox("Error", f"Failed to launch the model: {str(e)}", box_type="error")

    def open_file_dialog(self, event):
        """Open a file dialog to select the executable."""
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Select OpenModelica Executable", "", "Executables (*.exe)")
        if file_path:
            self.ui.comboBox.clear()  # Clear placeholder
            self.ui.comboBox.addItem(file_path)

    def show_info(self, event):
        """Display information about the launcher."""
        info_text = (
            "<h3>About OM Launcher</h3>"
            "<p>This OpenModelica Launcher helps you execute OpenModelica models with specified start and stop times.</p>"
            "<p><b>GitHub Repository:</b> "
            "<a href='https://github.com/Jeyapranov'>https://github.com/Jeyapranov</a></p>"
        )
        self.create_styled_messagebox("About OM Launcher", info_text, box_type="info")

    def close_app(self):
        """Close the application."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
