# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/query.ui'
#
# Created: Wed Jul  8 21:09:15 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ui_query(object):
    def setupUi(self, ui_query):
        ui_query.setObjectName(_fromUtf8("ui_query"))
        ui_query.resize(603, 871)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ui_query)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.scrollArea = QtGui.QScrollArea(ui_query)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 595, 863))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(self.scrollAreaWidgetContents)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_9.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.textEdit_query = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_query.setAcceptRichText(False)
        self.textEdit_query.setObjectName(_fromUtf8("textEdit_query"))
        self.verticalLayout.addWidget(self.textEdit_query)
        self.groupBox = gui.QgsCollapsibleGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(_fromUtf8("{{geocodeArea:}}"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_nominatim = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_nominatim.setObjectName(_fromUtf8("lineEdit_nominatim"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_nominatim)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.radioButton_extentMapCanvas = QtGui.QRadioButton(self.groupBox)
        self.radioButton_extentMapCanvas.setChecked(True)
        self.radioButton_extentMapCanvas.setObjectName(_fromUtf8("radioButton_extentMapCanvas"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.radioButton_extentMapCanvas)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_7)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setText(_fromUtf8("Points"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_4.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBox_points = QtGui.QCheckBox(self.groupBox)
        self.checkBox_points.setText(_fromUtf8(""))
        self.checkBox_points.setChecked(True)
        self.checkBox_points.setObjectName(_fromUtf8("checkBox_points"))
        self.horizontalLayout_4.addWidget(self.checkBox_points)
        self.lineEdit_csv_points = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_points.setInputMask(_fromUtf8(""))
        self.lineEdit_csv_points.setText(_fromUtf8(""))
        self.lineEdit_csv_points.setPlaceholderText(_fromUtf8("col1,col2,col3"))
        self.lineEdit_csv_points.setObjectName(_fromUtf8("lineEdit_csv_points"))
        self.horizontalLayout_4.addWidget(self.lineEdit_csv_points)
        self.formLayout_4.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setText(_fromUtf8("Lines"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_4.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkBox_lines = QtGui.QCheckBox(self.groupBox)
        self.checkBox_lines.setText(_fromUtf8(""))
        self.checkBox_lines.setChecked(True)
        self.checkBox_lines.setObjectName(_fromUtf8("checkBox_lines"))
        self.horizontalLayout_6.addWidget(self.checkBox_lines)
        self.lineEdit_csv_lines = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_lines.setObjectName(_fromUtf8("lineEdit_csv_lines"))
        self.horizontalLayout_6.addWidget(self.lineEdit_csv_lines)
        self.formLayout_4.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setText(_fromUtf8("Multilinestrings"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_4.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_14)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.checkBox_multilinestrings = QtGui.QCheckBox(self.groupBox)
        self.checkBox_multilinestrings.setText(_fromUtf8(""))
        self.checkBox_multilinestrings.setChecked(True)
        self.checkBox_multilinestrings.setObjectName(_fromUtf8("checkBox_multilinestrings"))
        self.horizontalLayout_7.addWidget(self.checkBox_multilinestrings)
        self.lineEdit_csv_multilinestrings = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_multilinestrings.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_csv_multilinestrings.setObjectName(_fromUtf8("lineEdit_csv_multilinestrings"))
        self.horizontalLayout_7.addWidget(self.lineEdit_csv_multilinestrings)
        self.formLayout_4.setLayout(7, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setText(_fromUtf8("Multipolygons"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_4.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_12)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.checkBox_multipolygons = QtGui.QCheckBox(self.groupBox)
        self.checkBox_multipolygons.setText(_fromUtf8(""))
        self.checkBox_multipolygons.setChecked(True)
        self.checkBox_multipolygons.setObjectName(_fromUtf8("checkBox_multipolygons"))
        self.horizontalLayout_8.addWidget(self.checkBox_multipolygons)
        self.lineEdit_csv_multipolygons = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_csv_multipolygons.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_csv_multipolygons.setObjectName(_fromUtf8("lineEdit_csv_multipolygons"))
        self.horizontalLayout_8.addWidget(self.lineEdit_csv_multipolygons)
        self.formLayout_4.setLayout(8, QtGui.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_extentLayer = QtGui.QRadioButton(self.groupBox)
        self.radioButton_extentLayer.setObjectName(_fromUtf8("radioButton_extentLayer"))
        self.horizontalLayout_3.addWidget(self.radioButton_extentLayer)
        self.comboBox_extentLayer = QtGui.QComboBox(self.groupBox)
        self.comboBox_extentLayer.setObjectName(_fromUtf8("comboBox_extentLayer"))
        self.horizontalLayout_3.addWidget(self.comboBox_extentLayer)
        self.pushButton_refreshLayers = QtGui.QPushButton(self.groupBox)
        self.pushButton_refreshLayers.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refreshLayers.setIcon(icon)
        self.pushButton_refreshLayers.setObjectName(_fromUtf8("pushButton_refreshLayers"))
        self.horizontalLayout_3.addWidget(self.pushButton_refreshLayers)
        self.formLayout_4.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_browseDir = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_browseDir.setObjectName(_fromUtf8("lineEdit_browseDir"))
        self.horizontalLayout.addWidget(self.lineEdit_browseDir)
        self.pushButton_browse_output_file = QtGui.QPushButton(self.groupBox)
        self.pushButton_browse_output_file.setObjectName(_fromUtf8("pushButton_browse_output_file"))
        self.horizontalLayout.addWidget(self.pushButton_browse_output_file)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_filePrefix = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_filePrefix.setObjectName(_fromUtf8("lineEdit_filePrefix"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_filePrefix)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_generateQuery = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_generateQuery.setObjectName(_fromUtf8("pushButton_generateQuery"))
        self.horizontalLayout_2.addWidget(self.pushButton_generateQuery)
        self.pushButton_runQuery = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_runQuery.setDefault(True)
        self.pushButton_runQuery.setObjectName(_fromUtf8("pushButton_runQuery"))
        self.horizontalLayout_2.addWidget(self.pushButton_runQuery)
        self.pushButton_saveQuery = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_saveQuery.setObjectName(_fromUtf8("pushButton_saveQuery"))
        self.horizontalLayout_2.addWidget(self.pushButton_saveQuery)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_progress = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_progress.sizePolicy().hasHeightForWidth())
        self.label_progress.setSizePolicy(sizePolicy)
        self.label_progress.setText(_fromUtf8("progress text"))
        self.label_progress.setObjectName(_fromUtf8("label_progress"))
        self.verticalLayout.addWidget(self.label_progress)
        self.progressBar_execution = QtGui.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar_execution.setProperty("value", 0)
        self.progressBar_execution.setObjectName(_fromUtf8("progressBar_execution"))
        self.verticalLayout.addWidget(self.progressBar_execution)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_overpassTurbo = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_overpassTurbo.setText(_fromUtf8("Overpass Turbo"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/QuickOSM/resources/turbo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_overpassTurbo.setIcon(icon1)
        self.pushButton_overpassTurbo.setObjectName(_fromUtf8("pushButton_overpassTurbo"))
        self.horizontalLayout_5.addWidget(self.pushButton_overpassTurbo)
        self.pushButton_documentation = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_documentation.setObjectName(_fromUtf8("pushButton_documentation"))
        self.horizontalLayout_5.addWidget(self.pushButton_documentation)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtGui.QSpacerItem(20, 71, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(ui_query)
        QtCore.QObject.connect(self.checkBox_points, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_points.setEnabled)
        QtCore.QObject.connect(self.checkBox_lines, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_lines.setEnabled)
        QtCore.QObject.connect(self.checkBox_multilinestrings, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_multilinestrings.setEnabled)
        QtCore.QObject.connect(self.checkBox_multipolygons, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_csv_multipolygons.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ui_query)

    def retranslateUi(self, ui_query):
        ui_query.setWindowTitle(_translate("ui_query", "QuickOSM - Query", None))
        self.label.setText(_translate("ui_query", "Overpass query", None))
        self.groupBox.setTitle(_translate("ui_query", "Advanced", None))
        self.lineEdit_nominatim.setPlaceholderText(_translate("ui_query", "Can be overridden", None))
        self.label_5.setText(_translate("ui_query", "{{bbox}} or {{center}}", None))
        self.radioButton_extentMapCanvas.setText(_translate("ui_query", "Extent of the map canvas", None))
        self.label_3.setText(_translate("ui_query", "Outputs", None))
        self.lineEdit_csv_lines.setPlaceholderText(_translate("ui_query", "or let empty", None))
        self.radioButton_extentLayer.setText(_translate("ui_query", "Extent of a layer", None))
        self.label_4.setText(_translate("ui_query", "Directory", None))
        self.lineEdit_browseDir.setPlaceholderText(_translate("ui_query", "Save to temporary file", None))
        self.pushButton_browse_output_file.setText(_translate("ui_query", "Browse", None))
        self.label_6.setText(_translate("ui_query", "File prefix", None))
        self.pushButton_generateQuery.setText(_translate("ui_query", "Generate query", None))
        self.pushButton_runQuery.setText(_translate("ui_query", "Run query", None))
        self.pushButton_saveQuery.setText(_translate("ui_query", "Save query", None))
        self.pushButton_documentation.setText(_translate("ui_query", "Documentation", None))

from qgis import gui
from QuickOSM import resources_rc
