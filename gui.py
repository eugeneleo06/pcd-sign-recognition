import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 800)
    w.move(450, 450)
    w.setWindowTitle('Hand Written-Signature Verification')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()