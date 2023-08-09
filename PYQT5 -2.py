import sys
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton , QMessageBox, QDesktopWidget 
from PyQt5.QtCore import QCoreApplication # 이벤트에 대한 처리
from PyQt5.QtCore import QEvent
class Exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    def initUI(self):
        
        
        btn1 = QPushButton("hello",self)
        btn1.resize(btn1.sizeHint())
        btn1.setToolTip("툴팁입니다 <b>안녕하세요<b/>")
        btn1.move(300,250)
        
        btn1.clicked.connect(QCoreApplication.instance().quit)
        
        #self.resize(700,500)
        self.setGeometry(300,300,700,500)
        self.setWindowTitle("버튼 학습")
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event: QEvent) -> None:
        ans = QMessageBox.question(self,"a","whd",
                                   QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        #return super().closeEvent(event)

app = QApplication(sys.argv) #application 객체 생성
w = Exam()
sys.exit(app.exec_())# 이벤트 처리를 위한 루프 생성