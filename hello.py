import pyautogui
import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():
    app: QApplication = QApplication(sys.argv)

    window: QWidget = QWidget()

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
