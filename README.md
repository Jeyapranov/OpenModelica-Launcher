# OpenModelica Launcher

This project is a simple app to help run OpenModelica models with start and stop times directly from a user-friendly interface. The GUI is built with PyQt6, and you can select an executable, input times, and launch the model easily.

---

# Features
1) Launch open modelica models easily with customizable start and stop time
2) user friendly and ease to access
3) dynamic colour adjuctment for dark and light modes

---

## Project Layout

Here’s how the project is organized:

```
OpenModelica-Launcher/
│
├── model                 # model with exe files and dependent files
├── dist                  # contains .exe file for GUI
├── Launcher_UI.py        # Python code converted from the .ui file
├── Launcher_main.py      # Main application logic
├── .gitignore            # contains images and cache files and .ui code(QT designer)
└── README.md             # This file
```

---

## How to Use the App
1. Open the app (by run the Launcher_main.py or open the exe file in the dist folder).
2. Select an OpenModelica executable file (`.exe` from model folder).
3. Enter the start and stop times in the input fields.
4. Click the **Launch Model** button to run the simulation.
5. To view app info, click on the info label.

---

## Steps to Run the Project

### Development Mode
1. Clone this repo:
   ```bash
   git clone https://github.com/YourUsername/OpenModelica-Launcher.git
   cd OpenModelica-Launcher
   ```

2. Set up your Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install PyQt6
   ```

3. Convert the `.ui` file to Python if needed:
   ```bash
   pyuic6 -o Launcher_UI.py Launcher_UI.ui
   ```

4. Run the app:
   ```bash
   python Launcher_main.py
   ```

### Creating an Executable
I already add the .exe file in dist folder but If you want to package the app as an `.exe` file:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Use the provided `.spec` file to build the executable:
   ```bash
   pyinstaller --onefile --windowed OpenModelicaLauncher.spec
   ```

3. After building, you’ll find the executable in the `dist/` folder:
   - On **Windows**: `dist/Launcher_main.exe`
   - On **Linux/macOS**: `dist/Launcher_main`

4. Run the executable:
   - **Windows**: Double-click it.
   - **Linux/macOS**:
     ```bash
     ./Launcher_main
     ```
---

<img src="E:\om\OpenModelica-Launcher\images\UI.png" alt="UI Image" style="width: 100%;"/>

---


## Notes on Qt Designer
The GUI was designed using **Qt Designer**. If you want to tweak the layout:
1. Open the `Launcher_UI.ui` file in Qt Designer.
2. Make your changes visually.
3. Convert it to Python:
   ```bash
   pyuic6 -o Launcher_UI.py Launcher_UI.ui
   ```

---

## Credits
- **Qt Designer** for the GUI.
- **PyQt6** for the Python GUI framework.
- **OpenModelica** for simulation.
- **PyInstaller** for creating standalone executables.

---
