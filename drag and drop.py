import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QBoxLayout, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

style_sheet = '''
    Qlabel#TargetLabel{
    color: darkgray;
    border: 2px dashed darkgray;
    font: 24px 'helvetica';
    qproperty-alignment: AlignCenter;
    }
    QLabel{
    color: darkgray;
    font: 18px 'helvetica';
    qpriperty-alignment: AlignCenter;
    }
    QPushButton{
    border: 1px solid;
    border-radius: 3px;
    font: 18px 'helvetica';
    }
    QPushButton:pressed{
    background-color: skyblue;
    }
        '''

class TargetLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Drag and Drop")
        self.setObjectName("TargetLabel")

        self.or_label = QLabel("or")
        self.select_image_button = QPushButton("Select Image")
        self.select_image_button.setFixedSize(150,50)
        self.select_image_button.clicked.connect(self.selectImageFile)

        label_v_box = QVBoxLayout()
        label_v_box.addStretch(3)
        label_v_box.addWidget(self.or_label)
        label_v_box.addWidget(self.select_image_button,0,Qt.AlignCenter)
        label_v_box.addStretch(1)

        self.setLayout(label_v_box)

    def setPixmap(self, image):
        super().setPixmap(image)
        self.or_label.setVisible(False)
        self.select_image_button.setVisible(False)

    def selectImageFile(self):
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "JPG Files(*.jpg);;PNG Files(*.png);;Bitmap Files(*.bmp);; GIF Files(*.gif)")
        if image_file:
            self.setPixmap(QPixmap(image_file))
            self.setScaledContents(True)

class DropTargetEx(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setMinimumSize(500,400)
        self.setWindowTitle("Drag and Drop")   
        self.setAcceptDrops(True)
        TargetLabel()
        self.setupWidgets()
        self.show()
    def setupWidgets(self):
        self.target_label = QLabel(self)
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.target_label)

        self.setLayout(main_v_box)

    def dragEnterEvent(self,event) -> None:
        if event.mimeData().hasImage:
            event.setAccepted(True)
        else:
            event.setAccepted(False)
    def dropEvent(self,event) -> None:
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            image_path = event.mimeData().urls()[0].toLocalFile()
            self.setImage(image_path)
            event.setAccepted(True)
        else:
            event.setAccepted(False)
    def setImage(self, image_file):
        self.target_label.setPixmap(QPixmap(image_file))
        self.target_label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = DropTargetEx()
    sys.exit(app.exec_())
    