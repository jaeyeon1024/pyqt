import sys
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton , QMessageBox, QMainWindow, QAction,QMenu, qApp, QDesktopWidget
from PyQt5.QtCore import QCoreApplication # 이벤트에 대한 처리
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import QDate
class Exam(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("dkssuyd")# 상태줄

        menu = self.menuBar() # 메뉴 생성
        menu.setNativeMenuBar(False)
        menu_file = menu.addMenu("File")
        menu_Edit = menu.addMenu("Edit")

        file_exit = QAction('Exit',self) # 메뉴 객체 생성
        
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("bye")
        file_exit.triggered.connect(qApp.quit)

        file_new = QMenu("New",self)

        file_new_saves = QAction("save",self)

        menu_file.addAction(file_exit) # 메뉴 등록
        menu_file.addMenu(file_new)
        file_new.addAction(file_new_saves)

        tools_exit = QAction('Exit',self) # 툴바 관련

        tools_exit.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(tools_exit)

        btn1 = QPushButton("hello",self)
        btn1.resize(btn1.sizeHint())
        btn1.setToolTip("툴팁입니다 <b>안녕하세요<b/>")
        btn1.move(300,250)
        
        btn1.clicked.connect(QCoreApplication.instance().quit)
        
        self.resize(700,500)# 이걸로 하면 자동으로 정 가운데 창
        #self.setGeometry(300,300,700,500) # 이걸로 하면 위치랑 크기 지정 가능
        self.setWindowTitle("버튼 학습")
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft)

    def closeEvent(self, event: QEvent) -> None:
        ans = QMessageBox.question(self,"a","whd",
                                   QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        #return super().closeEvent(event)

now = QDate.currentDate()
print(now.toString())

app = QApplication(sys.argv) #application 객체 생성
w = Exam()
sys.exit(app.exec_())# 이벤트 처리를 위한 루프 생성

