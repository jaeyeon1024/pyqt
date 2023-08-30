import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QBoxLayout, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import cv2

class Video_player(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setWindowTitle("Video Player")
        self.setGeometry(600,300,800,500)
        self.setAcceptDrops(True)
        
        self.mainBoxLayout = QVBoxLayout()
        
        self.Drag_Drop()

        bottomBoxLayout = QVBoxLayout()
        self.mainBoxLayout.addLayout(bottomBoxLayout)
        
        self.setLayout(self.mainBoxLayout)

        self.show()

    def Drag_Drop(self):
        self.drop_Label = QLabel("Drop")
        self.or_label = QLabel("or")
        self.drop_button = QPushButton("Select Image")
        self.drop_button.setFixedSize(150,50)
        self.drop_button.clicked.connect(self.selectVideoFile)

        label_v_box = QVBoxLayout()
        label_v_box.addStretch(1)
        label_v_box.addWidget(self.drop_Label,30,Qt.AlignCenter)
        label_v_box.addWidget(self.or_label,40,Qt.AlignCenter)
        label_v_box.addWidget(self.drop_button,50,Qt.AlignCenter)
        label_v_box.addStretch(1)
        self.mainBoxLayout.addLayout(label_v_box)

    def selectVideoFile(self):
        video_file, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "MP4 Files(*.mp4);;AVI Files(*.avi);;MKV Files(*.mkv);; WMV Files(*.wmv)")
        if video_file:
            self.setvisiable()
            self.run_video(video_file)
            
    def run_video(self,video_file):
        cnt = 0
        frame_lists = []
        index = -1
        cap = cv2.VideoCapture(video_file)
        while(cap.isOpened()):
            

            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (800,500))

            frame_lists.append(frame)
            index += 1

            if cnt:
                cnt -= 1
                continue
            # h, w, ch = frame.shape
            # qimg = QtGui.QImage(frame.data, w, h, ch*w, QtGui.QImage.Format_RGB888)
            # pixmap = QtGui.QPixmap.fromImage(qimg)
            # self.drop_Label.setPixmap(pixmap)
            cv2.imshow('frame',frame_lists[index])
            key = cv2.waitKey(25)
            special_key = cv2.waitKeyEx(25)
            if key == ord('q'):
                break
            if key == ord(' '):
                while True:
                    key = cv2.waitKey(25)
                    if key == ord(' '):
                        break
            if special_key == 0x270000:
                cnt = 50
            if special_key == 0x250000:
                index -= 50
        cap.release()          
        cv2.destroyAllWindows()

    def dragEnterEvent(self,event) -> None:
        if event.mimeData().hasUrls():
            event.setAccepted(True)
        else:
            event.setAccepted(False)

    def dropEvent(self,event) -> None:
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            video_file = event.mimeData().urls()[0].toLocalFile()
            self.setVideo(video_file)
            event.setAccepted(True)
        else:
            event.setDropAction(Qt.IgnoreAction)

    def setVideo(self, video_file):
        self.drop_Label.setPixmap(QPixmap(video_file))
        self.drop_Label.setScaledContents(True)
        self.setvisiable()
        self.run_video(video_file)

    def setvisiable(self):
        self.or_label.setVisible(False)
        self.drop_button.setVisible(False)
        self.drop_button.setDisabled(True)
        self.drop_Label.setVisible(False)
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Video_player()
    sys.exit(app.exec_())