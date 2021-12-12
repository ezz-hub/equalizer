# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eq1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq,ifft,fftshift,ifftshift
import cmath
from PyQt5.QtWidgets import QFileDialog
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import pandas as pd
from matplotlib.animation import FuncAnimation
import time
import numpy as np
from matplotlib.figure import Figure
Ts = 0
t = 0                   
x = 0
xcopy=0
freq_val=0
freq_valcpy=[]
frame_counter=0
flag_imp_aft=True
flag_imp_bef=True
flag_st=True
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.fig_before=Figure()
        self.canvas_before = FigureCanvas(self.fig_before)
        self.fig_after=Figure()
        self.canvas_after = FigureCanvas(self.fig_after)
        self.fig_spec=Figure()
        self.canvas_spec = FigureCanvas(self.fig_spec)
        MainWindow.setStyleSheet("background-color: rgb(72, 72, 72);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 320, 801, 221))
        self.groupBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(212, 212, 212);")
        self.groupBox.setObjectName("groupBox")
        self.start = QtWidgets.QPushButton(self.groupBox)
        self.start.setGeometry(QtCore.QRect(10, 160, 51, 34))
        self.start.setObjectName("start")
        self.res = QtWidgets.QPushButton(self.groupBox)
        self.res.setGeometry(QtCore.QRect(60, 160, 51, 34))
        self.res.setObjectName("res")
        self.back = QtWidgets.QPushButton(self.groupBox)
        self.back.setGeometry(QtCore.QRect(110, 160, 51, 34))
        self.back.setObjectName("back")
        self.forw = QtWidgets.QPushButton(self.groupBox)
        self.forw.setGeometry(QtCore.QRect(160, 160, 51, 34))
        self.forw.setObjectName("forw")
        self.zin = QtWidgets.QPushButton(self.groupBox)
        self.zin.setGeometry(QtCore.QRect(210, 160, 51, 34))
        self.zin.setObjectName("zin")
        self.zout = QtWidgets.QPushButton(self.groupBox)
        self.zout.setGeometry(QtCore.QRect(260, 160, 51, 34))
        self.zout.setObjectName("zout")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 60, 101, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        
        self.s1 = QtWidgets.QSlider(self.groupBox)
        self.s1.setGeometry(QtCore.QRect(400, 40, 22, 160))
        self.s1.setMaximum(50)
        self.s1.setValue(10)
        self.s1.setOrientation(QtCore.Qt.Vertical)
        self.s1.setObjectName("s2")
        self.s2 = QtWidgets.QSlider(self.groupBox)
        self.s2.setGeometry(QtCore.QRect(440, 40, 22, 160))
        self.s2.setMaximum(50)
        self.s2.setValue(10)
        self.s2.setOrientation(QtCore.Qt.Vertical)
        self.s2.setObjectName("s2")
        self.s3 = QtWidgets.QSlider(self.groupBox)
        self.s3.setGeometry(QtCore.QRect(480, 40, 22, 160))
        self.s3.setMaximum(50)
        self.s3.setValue(10)
        self.s3.setOrientation(QtCore.Qt.Vertical)
        self.s3.setObjectName("s3")
        self.s4 = QtWidgets.QSlider(self.groupBox)
        self.s4.setGeometry(QtCore.QRect(520, 40, 22, 160))
        self.s4.setMaximum(50)
        self.s4.setValue(10)
        self.s4.setOrientation(QtCore.Qt.Vertical)
        self.s4.setObjectName("s4")
        self.s5 = QtWidgets.QSlider(self.groupBox)
        self.s5.setGeometry(QtCore.QRect(560, 40, 22, 160))
        self.s5.setMaximum(50)
        self.s5.setValue(10)
        self.s5.setOrientation(QtCore.Qt.Vertical)
        self.s5.setObjectName("s5")
        self.s6 = QtWidgets.QSlider(self.groupBox)
        self.s6.setGeometry(QtCore.QRect(600, 40, 22, 160))
        self.s6.setMaximum(50)
        self.s6.setValue(10)
        self.s6.setOrientation(QtCore.Qt.Vertical)
        self.s6.setObjectName("s6")
        self.s7 = QtWidgets.QSlider(self.groupBox)
        self.s7.setGeometry(QtCore.QRect(640, 40, 22, 160))
        self.s7.setMaximum(50)
        self.s7.setValue(10)
        self.s7.setOrientation(QtCore.Qt.Vertical)
        self.s7.setObjectName("s7")
        self.s8 = QtWidgets.QSlider(self.groupBox)
        self.s8.setGeometry(QtCore.QRect(680, 40, 22, 160))
        self.s8.setMaximum(50)
        self.s8.setValue(10)
        self.s8.setOrientation(QtCore.Qt.Vertical)
        self.s8.setObjectName("s8")
        self.s9 = QtWidgets.QSlider(self.groupBox)
        self.s9.setGeometry(QtCore.QRect(720, 40, 22, 160))
        self.s9.setMaximum(50)
        self.s9.setValue(10)
        self.s9.setOrientation(QtCore.Qt.Vertical)
        self.s9.setObjectName("s9")
        self.s10 = QtWidgets.QSlider(self.groupBox)
        self.s10.setGeometry(QtCore.QRect(760, 40, 22, 160))
        self.s10.setMaximum(50)
        self.s10.setValue(10)
        self.s10.setOrientation(QtCore.Qt.Vertical)
        self.s10.setObjectName("s10")
        self.hor_s = QtWidgets.QSlider(self.groupBox)
        self.hor_s.setGeometry(QtCore.QRect(0, 20, 801, 22))
        self.hor_s.setMouseTracking(False)
        self.hor_s.setOrientation(QtCore.Qt.Horizontal)
        self.hor_s.setObjectName("hor_s")
        self.hor_s.setMinimum(25)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 92, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 110, 81, 19))
        self.label.setObjectName("label")
        self.labmin = QtWidgets.QLabel(self.groupBox)
        self.labmin.setGeometry(QtCore.QRect(100, 110, 61, 19))
        self.labmin.setObjectName("labmin")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(210, 110, 81, 19))
        self.label_3.setObjectName("label_3")
        self.labmax = QtWidgets.QLabel(self.groupBox)
        self.labmax.setGeometry(QtCore.QRect(300, 110, 81, 19))
        self.labmax.setObjectName("labmax")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.v1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.v1.setContentsMargins(0, 0, 0, 0)
        self.v1.setObjectName("v1")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 160, 551, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.v2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.v2.setContentsMargins(0, 0, 0, 0)
        self.v2.setObjectName("v2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(550, -1, 251, 321))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.v3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.v3.setContentsMargins(0, 0, 0, 0)
        self.v3.setObjectName("v3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuexport = QtWidgets.QMenu(self.menubar)
        self.menuexport.setObjectName("menuexport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionexport_pdf = QtWidgets.QAction(MainWindow)
        self.actionexport_pdf.setObjectName("actionexport_pdf")
        self.menufile.addAction(self.actionNew)
        self.menufile.addAction(self.actionOpen)
        self.menuexport.addAction(self.actionexport_pdf)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuexport.menuAction())

        self.start.clicked.connect(self.starting)
        self.res.clicked.connect(self.pb)
        self.back.clicked.connect(self.backword)
        self.forw.clicked.connect(self.forword)
        self.zin.clicked.connect(self.zoomin)
        self.zout.clicked.connect(self.zoomout)
        self.s1.valueChanged[int].connect(self.g1)
        self.s2.valueChanged[int].connect(self.g2)
        self.s3.valueChanged[int].connect(self.g3)
        self.s4.valueChanged[int].connect(self.g4)
        self.s5.valueChanged[int].connect(self.g5)
        self.s6.valueChanged[int].connect(self.g6)
        self.s7.valueChanged[int].connect(self.g7)
        self.s8.valueChanged[int].connect(self.g8)
        self.s9.valueChanged[int].connect(self.g9)
        self.s10.valueChanged[int].connect(self.g10)
        self.hor_s.valueChanged[int].connect(self.sl)

        self.actionOpen.triggered.connect(self.impoting)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.v1.addWidget(self.fig_before.canvas)
        self.v2.addWidget(self.fig_after.canvas)
        self.v3.addWidget(self.fig_spec.canvas)
        self.fig_spec.set_facecolor((0.29,0.29,0.29))
        self.fig_before.set_facecolor((0.29,0.29,0.29))
        self.fig_after.set_facecolor((0.29,0.29,0.29))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "controlling pad"))
        self.start.setText(_translate("MainWindow", "■"))
        self.start.setShortcut(_translate("MainWindow", "Q"))
        self.res.setText(_translate("MainWindow", "►"))
        self.res.setShortcut(_translate("MainWindow", "W"))
        self.back.setText(_translate("MainWindow", "<"))
        self.back.setShortcut(_translate("MainWindow", "E"))
        self.forw.setText(_translate("MainWindow", ">"))
        self.forw.setShortcut(_translate("MainWindow", "R"))
        self.zin.setText(_translate("MainWindow", "+"))
        self.zin.setShortcut(_translate("MainWindow", "T"))
        self.zout.setText(_translate("MainWindow", "-"))
        self.zout.setShortcut(_translate("MainWindow", "Y"))
        self.pushButton_7.setText(_translate("MainWindow", "change color"))
        self.pushButton_7.setShortcut(_translate("MainWindow", "U"))
        self.label.setText(_translate("MainWindow", "min value"))
        self.labmin.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "max value"))
        self.labmax.setText(_translate("MainWindow", "0"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuexport.setTitle(_translate("MainWindow", "export"))
        self.actionNew.setText(_translate("MainWindow", "New "))
        self.actionNew.setShortcut(_translate("MainWindow", "A"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "S"))
        self.actionexport_pdf.setText(_translate("MainWindow", "export pdf"))
        self.actionexport_pdf.setShortcut(_translate("MainWindow", "Ctrl+R"))
    def impoting(self):
        global Ts,t,x,xcopy,freq_valcpy,freq_val
        Ts = 1/240
        t = np.arange(0,10+Ts,Ts)                     
        x = np.sin(2*np.pi*2*t)+np.sin(2*np.pi*50*t)+np.cos(2*np.pi*100*t)
        xcopy=x.copy()
        freq_val=fft(x)
        freq_valcpy=list(freq_val).copy()
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(x, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
        self.fig_before.clear()
        lines_bef = [ax.plot([],[])[0] for ax in self.fig_before.axes]
        def update_bef(i):
            global flag_imp_bef
            if not flag_imp_bef:
                self.ani_bef.event_source.stop()
                self.fig_before.canvas.flush_events()
            else:
                global frame_counter,x,t,xcopy
                frame_counter=i
                range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
                xa=t[range_min:2*frame_counter]
                y1=x[range_min:2*frame_counter]
                ax=self.fig_before.gca()
                ax.cla()
                ax.set_ylim(min(x),max(x))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.plot(xa,y1,"yellow")
                ax.grid(True)
                self.fig_before.canvas.draw()
            self.fig_before.canvas.flush_events()
            return lines_bef
        self.ani_bef = FuncAnimation(self.fig_before, update_bef,interval=50,frames=np.arange(25,int((len(x)/2))),blit=True,repeat=False)
        
        self.fig_after.clear()
        lines_after = [ax.plot([],[])[0] for ax in self.fig_after.axes]
        def update_aft(i):
            global flag_imp_aft
            if not flag_imp_aft:
                self.ani_after.event_source.stop()
                self.fig_after.canvas.flush_events()
            else:
                global frame_counter,x,t,xcopy
                frame_counter=i
                range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
                xa=t[range_min:2*frame_counter]
                y1=np.real(xcopy[range_min:2*frame_counter])
                ax=self.fig_after.gca()
                ax.cla()
                ax.set_ylim(min(np.real(xcopy)),max(np.real(xcopy)))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.plot(xa,y1,"yellow")
                ax.grid(True)
                self.fig_after.canvas.draw()
            self.fig_after.canvas.flush_events()
            return lines_after
        self.ani_after = FuncAnimation(self.fig_after, update_aft,interval=50,frames=np.arange(25,int((len(x)/2))),blit=True,repeat=False)
    def starting(self):
        global Ts,t,x,xcopy,flag_imp_bef,flag_imp_aft,flag_st
        flag_imp_bef=False
        flag_imp_aft=False
        flag_st=True
        self.fig_before.clear()
        lines_bef = [ax.plot([],[])[0] for ax in self.fig_before.axes]
        def update_bef(i):
            global flag_st
            if not flag_st:
                self.ani_st_bef.event_source.stop()
                self.fig_before.canvas.flush_events()
            else:
                global frame_counter,x,t,xcopy
                frame_counter=i
                range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
                xa=t[range_min:2*frame_counter]
                y1=x[range_min:2*frame_counter]
                ax=self.fig_before.gca()
                ax.cla()
                ax.set_ylim(min(x),max(x))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.plot(xa,y1,"yellow")
                ax.grid(True)
                self.fig_before.canvas.draw()
            self.fig_before.canvas.flush_events()
            return lines_bef
        self.ani_st_bef = FuncAnimation(self.fig_before, update_bef,interval=50,frames=np.arange(25,int((len(x)/2))),blit=True,repeat=False)
        
        self.fig_after.clear()
        lines_after = [ax.plot([],[])[0] for ax in self.fig_after.axes]
        def update_aft(i):
            global flag_st
            if not flag_st:
                self.ani_st_after.event_source.stop()
                self.fig_after.canvas.flush_events()
            else:
                global frame_counter,x,t,xcopy
                frame_counter=i
                range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
                xa=t[range_min:2*frame_counter]
                y1=np.real(xcopy[range_min:2*frame_counter])
                ax=self.fig_after.gca()
                ax.cla()
                ax.set_ylim(min(np.real(xcopy)),max(np.real(xcopy)))
                ax.set_facecolor((0.29,0.29,0.29))
                ax.plot(xa,y1,"yellow")
                ax.grid(True)
                self.fig_after.canvas.draw()
            self.fig_after.canvas.flush_events()
            return lines_after
        self.ani_st_after = FuncAnimation(self.fig_after, update_aft,interval=50,frames=np.arange(25,int((len(x)/2))),blit=True,repeat=False)

    def pb(self):
        global Ts,t,x,xcopy,flag_imp_bef,flag_imp_aft,flag_st,frame_counter
        flag_imp_bef=False
        flag_imp_aft=False
        if flag_st == False:
            flag_st=True
            self.fig_before.clear()
            lines_bef = [ax.plot([],[])[0] for ax in self.fig_before.axes]
            c=frame_counter
            def update_bef(i):
                global flag_st,frame_counter,x,t,xcopy
                if not flag_st or frame_counter>=(int(len(x)/2)-25):
                    self.ani_st_bef.event_source.stop()
                    self.fig_before.canvas.flush_events()
                else:
                    frame_counter=i+c
                    range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
                    xa=t[range_min:2*frame_counter]
                    y1=x[range_min:2*frame_counter]
                    ax=self.fig_before.gca()
                    ax.cla()
                    ax.set_ylim(min(x),max(x))
                    ax.set_facecolor((0.29,0.29,0.29))
                    ax.plot(xa,y1,"yellow")
                    ax.grid(True)
                    self.fig_before.canvas.draw()
                self.fig_before.canvas.flush_events()
                return lines_bef
            self.ani_st_bef = FuncAnimation(self.fig_before, update_bef,interval=50,frames=np.arange(0,int((len(x)/2))-25),blit=True,repeat=False)

            self.fig_after.clear()
            lines_after = [ax.plot([],[])[0] for ax in self.fig_after.axes]
            def update_aft(i):
                global flag_st,frame_counter,x,t,xcopy
                if not flag_st or frame_counter>=(int(len(xcopy)/2)-26):
                    self.ani_st_after.event_source.stop()
                    self.fig_after.canvas.flush_events()
                else:
                    frame_counter=i+c
                    range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
                    xa=t[range_min:2*frame_counter]
                    y1=np.real(xcopy[range_min:2*frame_counter])
                    ax=self.fig_after.gca()
                    ax.cla()
                    ax.set_ylim(min(np.real(xcopy)),max(np.real(xcopy)))
                    ax.set_facecolor((0.29,0.29,0.29))
                    ax.plot(xa,y1,"yellow")
                    ax.grid(True)
                    self.fig_after.canvas.draw()
                self.fig_after.canvas.flush_events()
                return lines_after
            self.ani_st_after = FuncAnimation(self.fig_after, update_aft,interval=50,frames=np.arange(0,int((len(x)/2))-25),blit=True,repeat=False)
        else:
            flag_st=False

    def backword(self):
        global frame_counter
        global t,xcopy,x
        if frame_counter>35:
            frame_counter=frame_counter-10
            range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
            xa=t[range_min:2*frame_counter]
            ya=x[range_min:2*frame_counter]
            self.fig_before.clear()
            ax=self.fig_before.add_subplot(111)
            #ax.set_ylim(min(y_ecg),max(y_ecg))
            ax.set_ylim(min(x),max(x))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.plot(xa,ya,"yellow")
            self.fig_before.canvas.draw()
            self.fig_before.canvas.flush_events()
            #xa=t[range_min:2*frame_counter]
            yb=np.real(xcopy[range_min:2*frame_counter])
            self.fig_after.clear()
            ax=self.fig_after.add_subplot(111)
            ax.set_ylim(min(np.real(xcopy)),max(np.real(xcopy)))
            #ax.set_ylim(min(y_ecg),max(y_ecg))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.plot(xa,yb,"yellow")
            self.fig_after.canvas.draw()
            self.fig_after.canvas.flush_events()
        else:
            print("no enough points")
    def forword(self):
        global frame_counter
        global t,xcopy,x
        if frame_counter<(len(xcopy)/2-10):
            frame_counter=frame_counter+10
            range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
            xa=t[range_min:2*frame_counter]
            ya=x[range_min:2*frame_counter]
            self.fig_before.clear()
            ax=self.fig_before.add_subplot(111)
            #ax.set_ylim(min(y_ecg),max(y_ecg))
            ax.set_ylim(min(x),max(x))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.plot(xa,ya,"yellow")
            self.fig_before.canvas.draw()
            self.fig_before.canvas.flush_events()
            #xa=t[range_min:2*frame_counter]
            yb=np.real(xcopy[range_min:2*frame_counter])
            self.fig_after.clear()
            ax=self.fig_after.add_subplot(111)
            #ax.set_ylim(min(y_ecg),max(y_ecg))
            ax.set_ylim(min(np.real(xcopy)),max(np.real(xcopy)))
            ax.set_facecolor((0.29,0.29,0.29))
            ax.grid(True)
            ax.plot(xa,yb,"yellow")
            self.fig_after.canvas.draw()
            self.fig_after.canvas.flush_events()
        else:
            print("no enough points")
    
    def zoomin(self):
        global frame_counter
        global t,x,xcopy
        range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
        xa=t[range_min:2*frame_counter]
        ya=x[range_min:2*frame_counter]
        self.fig_before.clear()
        ax=self.fig_before.add_subplot(111)
        #ax.set_ylim(min(y_ecg),max(y_ecg))
        ax.margins(x=-0.3,y=0.05)
        #ax.set_ylim(min(x),max(x))
        ax.grid(True)
        ax.set_facecolor((0.29,0.29,0.29))
        ax.plot(xa,ya,"yellow")
        self.fig_before.canvas.draw()                
        self.fig_before.canvas.flush_events()
        yb=np.real(xcopy[range_min:2*frame_counter])
        self.fig_after.clear()
        ax=self.fig_after.add_subplot(111)
        #ax.set_ylim(min(y_ecg),max(y_ecg))
        ax.margins(x=-0.3,y=0.05)
        #ax.set_ylim(min(xcopy),max(xcopy))
        ax.grid(True)
        ax.set_facecolor((0.29,0.29,0.29))
        ax.plot(xa,yb,"yellow")
        self.fig_after.canvas.draw()                
        self.fig_after.canvas.flush_events()
    def zoomout(self):
        global frame_counter
        global t,x,xcopy
        range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
        xa=t[range_min:2*frame_counter]
        ya=x[range_min:2*frame_counter]
        self.fig_before.clear()
        ax=self.fig_before.add_subplot(111)
        #ax.set_ylim(min(y_ecg),max(y_ecg))
        ax.margins(x=0.05,y=1)
        #ax.set_ylim(min(xcopy),max(xcopy))
        ax.grid(True)
        ax.set_facecolor((0.29,0.29,0.29))
        ax.plot(xa,ya,"yellow")
        self.fig_before.canvas.draw()                
        self.fig_before.canvas.flush_events()
        yb=np.real(xcopy[range_min:2*frame_counter])
        self.fig_after.clear()
        ax=self.fig_after.add_subplot(111)
        #ax.set_ylim(min(y_ecg),max(y_ecg))
        ax.margins(x=0.05,y=1)
        ax.set_facecolor((0.29,0.29,0.29))
        #ax.set_ylim(min(xcopy),max(xcopy))
        ax.grid(True)
        ax.plot(xa,yb,"yellow")
        self.fig_after.canvas.draw()                
        self.fig_after.canvas.flush_events()
    def g1(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (0,int(n/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (19*int(n/20),n):
            freq_valcpy[i]=freq_val[i]
        print(19*int(n/20))
        print(value)
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[0:int(n/20)]=fabs[0:int(n/20)]*int(value/10)
        fabs[19*int(n/20):]=fabs[19*int(n/20):]*int(value/10)
        #print(len(fabs[9*int(len(x)/10)+1:]),len(fabs[0:int(len(x)/10)]))
        #print(len(fabs[int(len(x)/10):4*int(len(x)/10)]),len(fabs[6*int(len(x)/10):9*int(len(x)/10)]))
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g2(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (int(n/20),2*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (18*int(n/20),19*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[int(n/20):2*int(n/20)]=fabs[int(n/20):2*int(n/20)]*int(value/10)
        fabs[18*int(n/20):19*int(n/20)]=fabs[18*int(n/20):19*int(n/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g3(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (2*int(n/20),3*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (17*int(n/20),18*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[2*int(n/20):3*int(n/20)]=fabs[2*int(n/20):3*int(n/20)]*int(value/10)
        fabs[17*int(n/20):18*int(n/20)]=fabs[17*int(n/20):18*int(n/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g4(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (3*int(n/20),4*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (16*int(n/20),17*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[3*int(n/20):4*int(n/20)]=fabs[3*int(n/20):4*int(n/20)]*int(value/10)
        fabs[16*int(n/20):17*int(n/20)]=fabs[16*int(n/20):17*int(n/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g5(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (4*int(n/20),5*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (15*int(n/20),16*int(n/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[4*int(n/20):5*int(n/20)]=fabs[4*int(n/20):5*int(n/20)]*int(value/10)
        fabs[15*int(n/20):16*int(n/20)]=fabs[15*int(n/20):16*int(n/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g6(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (5*int(len(x)/20),6*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (14*int(len(x)/20),15*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[5*int(len(x)/20):6*int(len(x)/20)]=fabs[5*int(len(x)/20):6*int(len(x)/20)]*int(value/10)
        fabs[14*int(len(x)/20):15*int(len(x)/20)]=fabs[14*int(len(x)/20):15*int(len(x)/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g7(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (6*int(len(x)/20),7*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (13*int(len(x)/20),14*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[6*int(len(x)/20):7*int(len(x)/20)]=fabs[6*int(len(x)/20):7*int(len(x)/20)]*int(value/10)
        fabs[13*int(len(x)/20):14*int(len(x)/20)]=fabs[13*int(len(x)/20):14*int(len(x)/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g8(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (7*int(len(x)/20),8*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (12*int(len(x)/20),13*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[7*int(len(x)/20):8*int(len(x)/20)]=fabs[7*int(len(x)/20):8*int(len(x)/20)]*int(value/10)
        fabs[12*int(len(x)/20):13*int(len(x)/20)]=fabs[12*int(len(x)/20):13*int(len(x)/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g9(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (8*int(len(x)/20),9*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        for i in range (11*int(len(x)/20),12*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[8*int(len(x)/20):9*int(len(x)/20)]=fabs[8*int(len(x)/20):9*int(len(x)/20)]*int(value/10)
        fabs[11*int(len(x)/20):12*int(len(x)/20)]=fabs[11*int(len(x)/20):12*int(len(x)/20)]*int(value/10)
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def g10(self,value):
        global t,x,xcopy,freq_valcpy,freq_val
        #xcopy[0:int(len(x)/10)]=xcopy[0:int(len(x)/10)]*value
        n=len(x)
        #freqs=fftfreq(n)
        #plt.plot(freqs,np.angle(fftval))
        #plt.show()
        for i in range (9*int(len(x)/20),11*int(len(x)/20)):
            freq_valcpy[i]=freq_val[i]
        fabs= np.abs(freq_valcpy)
        fph=np.angle(freq_valcpy)
        fabs[9*int(len(x)/20):11*int(len(x)/20)]=fabs[9*int(len(x)/20):11*int(len(x)/20)]*int(value/10)
        
        fabs[0]=0 #boundary cond
        #ftheo= 2*(fabs/n)
        fc=[]
        #plt.plot(freqs,ftheo)
        #plt.show()
        for i in range(0,len(fabs)):
            fc.append(cmath.rect(fabs[i],fph[i]))
        freq_valcpy=fc
        xcopy=ifft(fc)
        self.fig_spec.clear()
        ax1 = self.fig_spec.add_subplot(111)
        ax1.specgram(xcopy, Fs=1/Ts,cmap="spring" , NFFT=256, noverlap=256/2,)        
        self.fig_spec.canvas.draw()
        self.fig_spec.canvas.flush_events()
    def sl(self,value):
        global frame_counter
        global t,xcopy,x
        self.hor_s.setMaximum(int(len(xcopy)/2)-1)
        frame_counter=value
        range_min=2*int(((frame_counter-25)+abs(frame_counter-25))/2)
        xa=t[range_min:2*frame_counter]
        ya=x[range_min:2*frame_counter]
        self.fig_before.clear()
        ax=self.fig_before.add_subplot(111)
        ax.set_ylim(min(x),max(x))
        ax.set_facecolor((0.29,0.29,0.29))
        ax.grid(True)
        ax.plot(xa,ya,"yellow")
        self.fig_before.canvas.draw()
        self.fig_before.canvas.flush_events()
        yb=np.real(xcopy[range_min:2*frame_counter])
        self.fig_after.clear()
        ax=self.fig_after.add_subplot(111)
        ax.set_ylim(min(np.real(xcopy)),max(np.real(xcopy)))
        ax.set_facecolor((0.29,0.29,0.29))
        ax.grid(True)
        ax.plot(xa,yb,"yellow")
        self.fig_after.canvas.draw()
        self.fig_after.canvas.flush_events()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())