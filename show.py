import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Mode show'
        self.left = 200
        self.top = 200
        self.width = 320
        self.height = 100
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        self.createHorizontalLayout()

        #設定圖示，QIcon物件接收一個我們要顯示的圖片路徑作為引數。
        # self.setWindowIcon(QIcon('web3.png'))

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("Showing")
        
        layout = QHBoxLayout()

        buttonBlue = QPushButton('rest', self)
        buttonBlue.clicked.connect(self.on_click)
        layout.addWidget(buttonBlue) 

        buttonRed = QPushButton('keyboard', self)
        buttonRed.clicked.connect(self.on_click)
        layout.addWidget(buttonRed) 

        buttonGreen = QPushButton('mouse', self)
        buttonGreen.clicked.connect(self.on_click)
        layout.addWidget(buttonGreen) 

        self.horizontalGroupBox.setLayout(layout)

    
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


"""
a:0 >>休息
delete.py :250 行
"""