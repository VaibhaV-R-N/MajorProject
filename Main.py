import cv2 as cv
import subprocess
import time
import HandState as hs
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from PyQt5.QtGui import QImage, QPixmap
from MPUtility import Utility
from ConfigHandler import Handler 


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.ut = Utility()
        self.state = {"stop": True,
                      "start": False
                      }
        self.cHandler = Handler()
        self.last = []
        self.prevG = None
        self.buttoncss = "background-color:#FFED00;color:#000000;"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setStyleSheet(
        #     "background-color:#000000;color:#FFED00;")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 390))

        self.groupBox.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(630, 320, 150, 150))
        self.groupBox_3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setTitle("Gesture")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 51, 310))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(59, 9, 291, 320))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.t1 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.t1.setObjectName("t1")
        self.verticalLayout_2.addWidget(self.t1)
        self.t2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.t2.setObjectName("t2")
        self.verticalLayout_2.addWidget(self.t2)
        self.t3 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.t3.setObjectName("t3")
        self.verticalLayout_2.addWidget(self.t3)
        self.t4 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.t4.setObjectName("t4")
        self.verticalLayout_2.addWidget(self.t4)
        self.t5 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.t5.setObjectName("t5")
        self.verticalLayout_2.addWidget(self.t5)
        self.execKeyLabel = QtWidgets.QLabel(self.groupBox)
        self.execKeyLabel.setText("ExeKey : ")
        self.execKeyLabel.setGeometry(QtCore.QRect(10, 340, 100, 41))
        self.t6 = QtWidgets.QTextEdit(self.groupBox)
        self.t6.setGeometry(QtCore.QRect(60, 340, 60, 41))
        self.update = QtWidgets.QPushButton(self.groupBox)
        self.update.setText("Update")
        self.update.setGeometry(QtCore.QRect(245, 340, 101, 41))
        self.update.clicked.connect(self.updateConfig)
        # self.update.setStyleSheet(self.buttoncss)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 430, 171, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 440, 57, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 10, 391, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.videocam = QtWidgets.QLabel(self.groupBox_2)
        self.videocam.setGeometry(QtCore.QRect(16, 25, 361, 251))
        self.videocam.setText("")
        self.videocam.setPixmap(QtGui.QPixmap("index.png"))
        self.videocam.setScaledContents(True)
        self.videocam.setObjectName("videocam")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(400, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.startF)
        self.start.setStyleSheet(self.buttoncss)

        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setText("stop")
        self.stop.setGeometry(QtCore.QRect(505, 330, 101, 41))
        self.stop.clicked.connect(self.stopF)
        self.stop.setEnabled(False)
        self.stop.setStyleSheet(self.buttoncss)

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(50, 1, 145, 145))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.tList = [self.t1, self.t2, self.t3, self.t4, self.t5, self.t6]
        cmds = self.cHandler.getAllCommands()
        for i, t in enumerate(self.tList):
            t.setText(cmds[i])

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Scripts"))
        self.label.setText(_translate("MainWindow", "One :"))
        self.label_4.setText(_translate("MainWindow", "Two :"))
        self.label_5.setText(_translate("MainWindow", "Three :"))
        self.label_3.setText(_translate("MainWindow", "Four :"))
        self.label_2.setText(_translate("MainWindow", "FIve :"))
        self.comboBox.setItemText(0, _translate(
            "MainWindow", "ANN (Recommended)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ALGO"))
        self.label_6.setText(_translate("MainWindow", "Model : "))
        self.groupBox_2.setTitle(_translate("MainWindow", "VideoCam"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.label_8.setText(_translate("MainWindow", ""))

    def capture(self):
        vidsrc = cv.VideoCapture(0)

        while True:

            if self.state["start"] == True:
                s, img = vidsrc.read()
                if s:
                    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

                    self.img = self.ut.draw(img)

                    h, w, _ = self.img.shape
                    bytesPerL = w * 3
                    Qimg = QImage(self.img.data, w, h, bytesPerL,
                                  QImage.Format_RGB888)

                    pixMap = QPixmap.fromImage(Qimg)

                    self.videocam.setPixmap(pixMap)

            elif self.exitEvent.is_set():
                self.videocam.setPixmap(QtGui.QPixmap("index.png"))
                break

            else:
                time.sleep(1)

    def updateGesture(self):

        while True:

            if self.state["start"] == True:

                if self.ut.startT2:

                    if self.model == "ANN (Recommended)":
                        gesture = self.ut.predictGesture()

                    elif self.model == "ALGO":
                        gesture = hs.stateToGesture(
                            hs.getState(self.ut.getResult()))

                    if gesture not in [0, 6, None]:
                        if self.prevG == None:
                            self.prevG = gesture
                            subprocess.run(
                                ["notify-send", "-t", "1", f"Gesture = {self.gesture}"])
                        self.gesture = gesture
                        self.label_8.setText(str(gesture))
                        if self.prevG != self.gesture:
                            subprocess.run(
                                ["notify-send", "-t", "1", f"Gesture = {self.gesture}"])
                            self.prevG = self.gesture

                    else:
                        self.label_8.setText("")

            elif self.exitEvent.is_set():
                break

            else:
                time.sleep(1)

    def updateConfig(self):

        commands = []
        for t in self.tList:
            commands.append(str(t.toPlainText()))
        self.cHandler.updateCommands(commands)
        subprocess.run(['notify-send', 'Config Updated Successfully'])

    def setFalse(self, state):

        for k in self.state.keys():
            if k != state:
                self.state[k] = False

    def startF(self):

        self.state["start"] = True
        self.setFalse("start")
        self.exitEvent = threading.Event()
        self.camthread = Thread(target=self.capture, daemon=True)
        self.gesturethread = Thread(target=self.updateGesture, daemon=True)
        self.camthread.start()
        self.gesturethread.start()
        self.model = str(self.comboBox.currentText())

        self.stop.setEnabled(True)
        self.start.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.update.setEnabled(False)

    def stopF(self):

        self.state["stop"] = True
        self.setFalse("stop")
        self.exitEvent.set()

        self.start.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.update.setEnabled(True)
        self.stop.setEnabled(False)

    def execF(self, key):

        try:
            if key.char == self.cHandler.getCommand("exec"):
                cmd = self.cHandler.getCommand(str(self.gesture))
                if cmd != "":
                    cmd = cmd.split(" ")
                    subprocess.run(cmd)

        except AttributeError:
            if key.name == self.cHandler.getCommand("exec"):
                cmd = self.cHandler.getCommand(str(self.gesture))
                print(cmd)
                if cmd != "":
                    cmd = cmd.split(" ")
                    subprocess.run(cmd)

        except Exception:
            pass


if __name__ == "__main__":
    import sys
    from pynput import keyboard
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(800, 500)
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    listener = keyboard.Listener(on_press=ui.execF)
    listener.start()
    sys.exit(app.exec_())
