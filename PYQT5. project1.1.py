import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLCDNumber,QPushButton,QLabel,QLineEdit,QGroupBox,QTabWidget,QVBoxLayout,QHBoxLayout)
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QIcon
#from PomodoroStyleSheet import style_sheet

POMODORO_TIME = 1500000
SHORT_BREAK_TIME = 300000
LONG_BREAK_TIME = 900000

class PomodoroTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setMinimumSize(500,400)
        self.setWindowTitle("1.1 - Pomodoro Timer")
        self.setWindowIcon(QIcon("images/tomato.png"))

        self.pomodoro_limit = POMODORO_TIME
        self.short_break_limit = SHORT_BREAK_TIME
        self.long_break_limit = LONG_BREAK_TIME

        self.setupTabsAndWidgets()

        self.current_tab_selected = 0
        self.current_start_button = self.pomodoro_start_button
        self.current_stop_button = self.pomodoro_stop_button
        self.current_reset_button = self.pomodoro_reset_button
        self.current_time_limit = self.pomodoro_limit
        self.current_lcd = self.pomodoro_lcd
        self.task_is_set = False
        self.number_of_tasks = 0
        self.task_complete_counter = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)

        self.show()

    def setupTabsAndWidgets(self):
        self.tab_bar = QTabWidget(self)
        self.pomodoro_tab =QWidget()
        self.pomodoro_tab.setObjectName("Pomodoro")
        self.short_break_tab = QWidget()
        self.short_break_tab.setObjectName("ShortBreak")
        self.long_break_tab = QWidget()
        self.long_break_tab.setObjectName("LongBreak")

        self.tab_bar.addTab(self.pomodoro_tab, "Pomodoro")
        self.tab_bar.addTab(self.short_break_tab,"Short Break")
        self.tab_bar.addTab(self.long_break_tab,"Long Break")

        self.tab_bar.currentChanged.connect(self.tabsSwitched)

        self.pomodoroTab()
        self.shortBreakTab()
        self.longBreakTab()

        self.enter_task_lineedit = QLineEdit()
        self.enter_task_lineedit.setClearButtonEnabled(True)
        self.enter_task_lineedit.setPlaceholderText("Enter Your Current Task")

        confirm_task_button = QPushButton(QIcon("images/plus.pnh"),None)
        confirm_task_button.setObjectName("ConfirmButton")
        confirm_task_button.clicked.connect(self.addTaskToTaskbar)

        task_entry_h_box = QHBoxLayout()
        task_entry_h_box.addWidget(self.enter_task_lineedit)
        task_entry_h_box.addWidget(confirm_task_button)

        self.tasks_v_box = QVBoxLayout()

        task_v_box = QVBoxLayout()
        task_v_box.addLayout(task_entry_h_box)
        task_v_box.addLayout(self.tasks_v_box)

        task_bar_gb = QGroupBox("Tasks")
        task_bar_gb.setLayout(task_v_box)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.tab_bar)
        main_v_box.addWidget(task_bar_gb)
        self.setLayout(main_v_box)

    def pomodoroTab(self):
        start_time = self.calculateDisplayTime(self.pomodoro_limit)

        self.pomodoro_lcd = QLCDNumber()
        self.pomodoro_lcd.setObjectName("PomodoroLCD")
        self.pomodoro_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.pomodoro_lcd.display(start_time)

        self.pomodoro_start_button = QPushButton("Start")
        self.pomodoro_start_button.clicked.connect(self.startCountDown)

        self.pomodoro_stop_button = QPushButton("Stop")
        self.pomodoro_stop_button.clicked.connect(self.stopCountDown)

        self.pomodoro_reset_button = QPushButton("Reset")
        self.pomodoro_reset_button.clicked.connect(self.resetCountDown)

        button_h_box = QHBoxLayout()
        button_h_box.addWidget(self.pomodoro_start_button)
        button_h_box.addWidget(self.pomodoro_stop_button)
        button_h_box.addWidget(self.pomodoro_reset_button)

        v_box = QVBoxLayout()
        v_box.addWidget(self.pomodoro_lcd)
        v_box.addLayout(button_h_box)
        self.pomodoro_tab.setLayout(v_box)

    def shortBreakTab(self):
        start_time = self.calculateDisplayTime(self.short_break_limit)

        self.short_break_lcd = QLCDNumber()
        self.short_break_lcd.setObjectName("ShortLCD")
        self.short_break_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.short_break_lcd.display(start_time)

        self.short_start_button = QPushButton("start")
        self.short_start_button.clicked.connect(self.startCountDown)

        self.short_stop_button = QPushButton("stop")
        self.short_stop_button.clicked.connect(self.stopCountDown)

        self.short_reset_button = QPushButton("reset")
        self.short_reset_button.clicked.connect(self.resetCountDown)
        
        button_h_box = QHBoxLayout()
        button_h_box.addWidget(self.short_start_button)
        button_h_box.addWidget(self.short_stop_button)
        button_h_box.addWidget(self.short_reset_button)

        v_box = QVBoxLayout()
        v_box.addWidget(self.short_break_lcd)
        v_box.addLayout(button_h_box)
        self.short_break_tab.setLayout(v_box)

    def longBreakTab(self):
        start_time = self.calculateDisplayTime(self.long_break_limit)

        self.long_break_lcd = QLCDNumber()
        self.long_break_lcd.setObjectName("LongLCD")
        self.long_break_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.long_break_lcd.display(start_time)
        
        self.long_start_button = QPushButton("Start")
        self.long_start_button.clicked.connect(self.startCountDown)

        self.long_stop_button = QPushButton("Stop")
        self.long_stop_button.clicked.connect(self.stopCountDown)
        
        self.long_reset_button = QPushButton("Reset")
        self.long_reset_button.clicked.connect(self.resetCountDown)

        button_h_box = QHBoxLayout()
        button_h_box.addWidget(self.long_start_button)
        button_h_box.addWidget(self.long_stop_button)
        button_h_box.addWidget(self.long_reset_button)
        
        v_box = QVBoxLayout()
        v_box.addWidget(self.long_break_lcd)
        v_box.addLayout(button_h_box)
        self.long_break_tab.setLayout(v_box)

    def startCountDown(self):
        self.current_start_button.setEnabled(False)

        if self.task_is_set == True and self.task_complete_counter == 0:
            self.counter_label.setText("{}/4".format(self.task_complete_counter))
        
        remaining_time = self.calculateDisplayTime(self.current_time_limit)
        if remaining_time == "00:00":
            self.resetCountDown()
            self.timer.start(1000)
        else:
            self.timer.start(1000)
    def stopCountDown(self):
        if self.timer.isActive() != False:
            self.timer.stop()
            self.current_start_button.setEnabled(True)
    
    def resetCountDown(self):
        self.stopCountDown()

        if self.current_tab_selected == 0:
            self.pomodoro_limit = POMODORO_TIME
            self.current_time_limit = self.pomodoro_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
        elif self.current_tab_selected == 1:
            self.short_break_limit = SHORT_BREAK_TIME
            self.current_time_limit = self.short_break_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
        elif self.current_tab_selected == 2:
            self.long_break_limit = LONG_BREAK_TIME
            self.current_time_limit = self.long_break_limit
            reset_time = self.calculateDisplayTime(self.current_time_limit)
        self.current_lcd.display(reset_time)

    def updateTimer(self):
        remaing_time = self.calculateDisplayTime(self.current_time_limit)

        if remaing_time == "00:00":
            self.stopCountDown()
            self.current_lcd(remaing_time)
            
            if self.current_tab_selected == 0:
                self.task_complete_counter += 1
                if self.task_complete_counter == 4:
                    self.counter_label.setText("Time for a long break. {}/4".format(self.task_complete_counter))
                    self.task_complete_counter = 0
                elif self.task_complete_counter < 4:
                    self.counter_laber.setText("{}4".format(self.task_complete_counter))
        else:
            self.current_time_limit -= 100
            self.current_lcd.display(remaing_time)
    
    def tabsSwitched(self, index): # pomodoro , shortbreak, longbreak 탭 마다 실행
        self.current_tab_selected = index
        self.stopCountDown()

        if self.current_tab_selected == 0:
            self.current_start_button = self.pomodoro_start_button
            self.current_stop_button = self.pomodoro_stop_button
            self.current_reset_button = self.pomodoro_reset_button
            self.pomodoro_limit = POMODORO_TIME
            self.current_time_limit = self.pomodoro_limit

            reset_time = self.calculateDisplayTime(self.current_time_limit)
            self.current_lcd = self.pomodoro_lcd
            self.current_lcd.display(reset_time)

        elif self.current_tab_selected == 1:
            self.current_start_button = self.short_start_button
            self.current_stop_button = self.short_stop_button
            self.current_reset_button = self.short_reset_button
            self.short_break_limit = SHORT_BREAK_TIME
            self.current_time_limit = self.short_break_limit

            reset_time = self.calculateDisplayTime(self.current_time_limit)
            self.current_lcd = self.short_break_lcd
            self.current_lcd.display(reset_time)

        elif self.current_tab_selected == 2:
            self.current_start_button = self.long_start_button
            self.current_stop_button = self.long_stop_button
            self.current_reset_button = self.long_reset_button
            self.long_break_limit = LONG_BREAK_TIME
            self.current_time_limit = self.long_break_limit

            reset_time = self.calculateDisplayTime(self.current_time_limit)
            self.current_lcd = self.long_break_lcd
            self.current_lcd.display(reset_time)

    def addTaskToTaskbar(self): # task 추가
        text = self.enter_task_lineedit.text()
        self.enter_task_lineedit.clear()

        if text != ""and self.number_of_tasks != 1:
            self.enter_task_lineedit.setReadOnly(True)
            self.task_is_set = True
            new_task = QLabel(text)

            self.counter_label = QLabel("{}/4".format(self.task_complete_counter))
            self.counter_label.setAlignment(Qt.AlignRight)
                
            cancel_task_button = QPushButton(QIcon("images/minus.png"),None)
            cancel_task_button.setMaximumWidth(24)
            cancel_task_button.clicked.connect(self.clearCurrentTask)

            self.new_task_h_box = QHBoxLayout()
            self.new_task_h_box.addWidget(new_task)
            self.new_task_h_box.addWidget(self.counter_label)
            self.new_task_h_box.addWidget(cancel_task_button)

            self.tasks_v_box.addLayout(self.new_task_h_box)
            self.number_of_tasks += 1

    def clearCurrentTask(self): # 현재 task 삭제
        self.new_task.setParent(None)
        self.counter_label.setParent(None)
        self.cancel_task_button.setParent(None)

        self.number_of_tasks -= 1
        self.task_is_set = False
        self.task_complete_counter = 0 

        self.enter_task_lineedit.setReadOnly(False)

    def convertTotalTime(self,time_in_milli):
        minutes = (time_in_milli / (1000 * 60)) % 60
        seconds = (time_in_milli / 1000) % 60
        return int(minutes), int(seconds)
        
    def calculateDisplayTime(self,time):
        minutes, seconds = self.convertTotalTime(time)
        amount_of_time = "{:02d} : {:02d}".format(minutes,seconds)
        return amount_of_time
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QLineEdit { background-color: white }")
    window = PomodoroTimer()
    sys.exit(app.exec_())