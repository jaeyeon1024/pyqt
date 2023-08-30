import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class practice(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    def initUI(self):

        self.statusBar()
        self.statusBar().showMessage("hi")# 상태줄

        menu = self.menuBar() # 메뉴 생성
        menu_file = menu.addMenu("File")
        menu_save = menu.addMenu("save")
        
        file_exit = QAction('Exit',self) # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("bye")

        file_exit.triggered.connect(qApp.quit)

        file_save = QAction('save',self)
        file_save.setShortcut('Ctrl+S')
        file_save.setStatusTip("save")

        file_new = QMenu("New",self)
        
        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit) # 메뉴 등록
        menu_save.addAction(file_save)


        self.resize(450,400)
        self.show()



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = practice() 

    sys.exit(app.exec_())