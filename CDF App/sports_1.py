from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pylab as plt
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(250, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/istockphoto-1300314773-170667a-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_3.setStyleSheet("font: 24pt \"Wide Latin\";\n"
"font: 20pt \"Poor Richard\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.Mean_Velocity = QtWidgets.QLabel(self.groupBox)
        self.Mean_Velocity.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mean_Velocity.sizePolicy().hasHeightForWidth())
        self.Mean_Velocity.setSizePolicy(sizePolicy)
        self.Mean_Velocity.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.Mean_Velocity.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.Mean_Velocity.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Mean_Velocity.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.Mean_Velocity.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Mean_Velocity.setMidLineWidth(2)
        self.Mean_Velocity.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.Mean_Velocity.setObjectName("Mean_Velocity")
        self.verticalLayout_5.addWidget(self.Mean_Velocity)
        self.Dial = QtWidgets.QDial(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dial.sizePolicy().hasHeightForWidth())
        self.Dial.setSizePolicy(sizePolicy)
        self.Dial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Dial.setObjectName("Dial")
        self.verticalLayout_5.addWidget(self.Dial)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Initial_Velocity = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Initial_Velocity.sizePolicy().hasHeightForWidth())
        self.Initial_Velocity.setSizePolicy(sizePolicy)
        self.Initial_Velocity.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.Initial_Velocity.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.Initial_Velocity.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Initial_Velocity.setObjectName("Initial_Velocity")
        self.horizontalLayout_4.addWidget(self.Initial_Velocity)
        self.Final_Velocity_330 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Final_Velocity_330.sizePolicy().hasHeightForWidth())
        self.Final_Velocity_330.setSizePolicy(sizePolicy)
        self.Final_Velocity_330.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.Final_Velocity_330.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";\n"
"")
        self.Final_Velocity_330.setScaledContents(False)
        self.Final_Velocity_330.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Final_Velocity_330.setWordWrap(False)
        self.Final_Velocity_330.setObjectName("Final_Velocity_330")
        self.horizontalLayout_4.addWidget(self.Final_Velocity_330)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addWidget(self.groupBox)
        #self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        #self.graphicsView.setEnabled(False)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(200)
        #sizePolicy.setVerticalStretch(200)
        #sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        #self.graphicsView.setSizePolicy(sizePolicy)
        #self.graphicsView.setMinimumSize(QtCore.QSize(200, 200))
        #self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 16777213))
        #self.graphicsView.setSizeIncrement(QtCore.QSize(0, 0))
        #self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        #self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.graphicsView.setAutoFillBackground(False)
        #self.graphicsView.setAlignment(QtCore.Qt.AlignCenter)
        #self.graphicsView.setRenderHints(QtGui.QPainter.TextAntialiasing)
        #self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        #self.graphicsView.setObjectName("graphicsView")
        #self.horizontalLayout_5.addWidget(self.graphicsView)
        self.Parameters_GroupBox = QtWidgets.QGroupBox(self.splitter)
        self.Parameters_GroupBox.setStyleSheet("font: 25pt \"Playbill\";\n"
"font: 63 12pt \"Segoe UI Semibold\";")
        self.Parameters_GroupBox.setObjectName("Parameters_GroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Parameters_GroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.Parameters_GroupBox)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.label_7.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Parameters_GroupBox)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Mean_Value = QtWidgets.QLabel(self.groupBox_4)
        self.Mean_Value.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.Mean_Value.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.Mean_Value.setObjectName("Mean_Value")
        self.verticalLayout.addWidget(self.Mean_Value)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.Parameters_GroupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_5.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.Parameters_GroupBox)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Probability = QtWidgets.QLabel(self.groupBox_3)
        self.Probability.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.Probability.setObjectName("Probability")
        self.verticalLayout_4.addWidget(self.Probability)
        self.Probability_Value = QtWidgets.QLabel(self.groupBox_3)
        self.Probability_Value.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.Probability_Value.setStyleSheet("font: 63 12pt \"Segoe UI Semibold\";")
        self.Probability_Value.setObjectName("Probability_Value")
        self.verticalLayout_4.addWidget(self.Probability_Value)
        self.verticalLayout_10.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_7.addWidget(self.splitter)
        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #canvas for plotting
        self.Canvas_for_pdf = MplCanvas2(self)
        self.horizontalLayout_5.addWidget(self.Canvas_for_pdf)

        self.Canvas_for_pdf.setMinimumSize(QtCore.QSize(200, 200))
        self.Canvas_for_pdf.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.Canvas_for_pdf.setSizeIncrement(QtCore.QSize(0, 0))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.Canvas_for_pdf.sizePolicy().hasHeightForWidth())
        self.Canvas_for_pdf.setSizePolicy(sizePolicy)

        #dial settings
        self.Dial.setMinimum(0)
        self.Dial.setMaximum(330)
        self.Dial.setValue(160)

        self.cdf_plotting()
        self.cdf_calculating()
        self.Dial.valueChanged.connect(self.sliderMoved)

    def sliderMoved(self):
        self.cdf_plotting()
        self.cdf_calculating()
        
       


    def cdf_plotting(self):
        self.Canvas_for_pdf.axes.clear()
        velocity = np.arange(0,320,2)
        pdf = norm.pdf(velocity , loc = 160 , scale = 20 )
        self.Canvas_for_pdf.axes.plot(velocity, pdf)
        #self.Canvas_for_pdf.axes.set_title("Normal Dist. with mean=160, std_dv=20")
        self.Canvas_for_pdf.axes.set_xlabel('Velocity-values')
        self.Canvas_for_pdf.axes.set_ylabel('PDF(Velocity)')
        self.Canvas_for_pdf.axes.tick_params(colors='white', which='both')
        self.Canvas_for_pdf.axes.spines['left'].set_color('white')
        self.Canvas_for_pdf.axes.spines['bottom'].set_color('white')
        self.Canvas_for_pdf.axes.spines['top'].set_color('white')
        self.Canvas_for_pdf.axes.spines['right'].set_color('white')
        self.Canvas_for_pdf.axes.xaxis.label.set_color('white')
        self.Canvas_for_pdf.axes.yaxis.label.set_color('white')


        velocity_range=np.arange(0, self.Dial.value(), 0.01)
        self.Canvas_for_pdf.axes.fill_between(velocity_range,norm.pdf(velocity_range, loc=160, scale=20), alpha=0.5, color='c')
        self.Canvas_for_pdf.draw()


    def cdf_calculating(self):
        cdf_upper_limit = norm(loc = 160 , scale = 20).cdf(self.Dial.value())
        cdf_lower_limit = norm(loc = 160 , scale = 20).cdf(0)
        prob = cdf_upper_limit - cdf_lower_limit
        self.Probability_Value.setText(str(round(prob,2)))
        self.Probability_Value.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignHCenter)

        self.label_7.setText(str(self.Dial.value()))
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignHCenter)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Cumulative Distribution Probability", "Cumulative Distribution Probability"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Cumulative Gaussian Probability Distribution </span></p></body></html>"))
        self.Mean_Velocity.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">160</span></p></body></html>"))
        self.Initial_Velocity.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.Initial_Velocity.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">0</span></p></body></html>"))
        self.Final_Velocity_330.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"right\">0</p></body></html>"))
        self.Final_Velocity_330.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">330</span></p></body></html>"))
        self.Parameters_GroupBox.setTitle(_translate("Form", "Graph Parameter"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\">Final Velocity</p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p align=\"center\">330</p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Mean</span></p></body></html>"))
        self.Mean_Value.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">160</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Standard Deviation</p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">20</p></body></html>"))
        self.Probability.setText(_translate("Form", "<html><head/><body><p align=\"center\">Probabity</p></body></html>"))
        self.Probability_Value.setText(_translate("Form", "<html><head/><body><p align=\"center\">123</p></body></html>"))


class MplCanvas2(FigureCanvasQTAgg):
   def __init__(self, parent=None, width=3.5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        
        self.fig.tight_layout()      
        self.axes = self.fig.add_subplot(111)
        self.axes.set_facecolor('#19232d')
        self.fig.set_facecolor('#19232d')
        super(MplCanvas2, self).__init__(self.fig) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    Form.show()
    sys.exit(app.exec_())

