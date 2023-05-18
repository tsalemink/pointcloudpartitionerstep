# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pointcloudpartitionerwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from mapclientplugins.pointcloudpartitionerstep.view.zincpointcloudpartitionerwidget import ZincPointCloudPartitionerWidget

class Ui_PointCloudPartitionerWidget(object):
    def setupUi(self, PointCloudPartitionerWidget):
        if not PointCloudPartitionerWidget.objectName():
            PointCloudPartitionerWidget.setObjectName(u"PointCloudPartitionerWidget")
        PointCloudPartitionerWidget.resize(884, 640)
        self.horizontalLayout = QHBoxLayout(PointCloudPartitionerWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(PointCloudPartitionerWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButtonCreateGroup = QPushButton(self.groupBox_2)
        self.pushButtonCreateGroup.setObjectName(u"pushButtonCreateGroup")

        self.verticalLayout_4.addWidget(self.pushButtonCreateGroup)

        self.pushButtonRemoveGroup = QPushButton(self.groupBox_2)
        self.pushButtonRemoveGroup.setObjectName(u"pushButtonRemoveGroup")

        self.verticalLayout_4.addWidget(self.pushButtonRemoveGroup)

        self.pushButtonAddToGroup = QPushButton(self.groupBox_2)
        self.pushButtonAddToGroup.setObjectName(u"pushButtonAddToGroup")

        self.verticalLayout_4.addWidget(self.pushButtonAddToGroup)

        self.pushButtonRemoveFromGroup = QPushButton(self.groupBox_2)
        self.pushButtonRemoveFromGroup.setObjectName(u"pushButtonRemoveFromGroup")

        self.verticalLayout_4.addWidget(self.pushButtonRemoveFromGroup)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBoxSelectionMode = QComboBox(self.groupBox_5)
        self.comboBoxSelectionMode.setObjectName(u"comboBoxSelectionMode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxSelectionMode.sizePolicy().hasHeightForWidth())
        self.comboBoxSelectionMode.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.comboBoxSelectionMode, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBoxSelectionType = QComboBox(self.groupBox_5)
        self.comboBoxSelectionType.setObjectName(u"comboBoxSelectionType")

        self.gridLayout_2.addWidget(self.comboBoxSelectionType, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.pushButtonSelectPointsOnSurface = QPushButton(self.groupBox_5)
        self.pushButtonSelectPointsOnSurface.setObjectName(u"pushButtonSelectPointsOnSurface")

        self.verticalLayout_7.addWidget(self.pushButtonSelectPointsOnSurface)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBoxSurfacesVisibility = QCheckBox(self.groupBox_6)
        self.checkBoxSurfacesVisibility.setObjectName(u"checkBoxSurfacesVisibility")
        self.checkBoxSurfacesVisibility.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBoxSurfacesVisibility)

        self.checkBoxPointsVisibility = QCheckBox(self.groupBox_6)
        self.checkBoxPointsVisibility.setObjectName(u"checkBoxPointsVisibility")
        self.checkBoxPointsVisibility.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBoxPointsVisibility)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pointSizeSpinBox = QDoubleSpinBox(self.groupBox_6)
        self.pointSizeSpinBox.setObjectName(u"pointSizeSpinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pointSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.pointSizeSpinBox.setSizePolicy(sizePolicy3)
        self.pointSizeSpinBox.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.pointSizeSpinBox, 0, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonViewAll = QPushButton(self.groupBox_3)
        self.pushButtonViewAll.setObjectName(u"pushButtonViewAll")

        self.verticalLayout.addWidget(self.pushButtonViewAll)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButtonContinue = QPushButton(self.groupBox_4)
        self.pushButtonContinue.setObjectName(u"pushButtonContinue")

        self.verticalLayout_3.addWidget(self.pushButtonContinue)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.horizontalLayout.addWidget(self.groupBox)

        self.widgetZinc = ZincPointCloudPartitionerWidget(PointCloudPartitionerWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.widgetZinc)


        self.retranslateUi(PointCloudPartitionerWidget)

        QMetaObject.connectSlotsByName(PointCloudPartitionerWidget)
    # setupUi

    def retranslateUi(self, PointCloudPartitionerWidget):
        PointCloudPartitionerWidget.setWindowTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Point Cloud Partitioner", None))
        self.groupBox.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Point Cloud Partitioner", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Group Points", None))
        self.pushButtonCreateGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Create Group", None))
        self.pushButtonRemoveGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Remove Group", None))
        self.pushButtonAddToGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Add Selected Points to Group", None))
        self.pushButtonRemoveFromGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Remove Selected Points from Group", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Selection", None))
        self.label_2.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Selection Mode:", None))
        self.label_3.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Selection Type:", None))
        self.pushButtonSelectPointsOnSurface.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Select Points on Surface", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Visibility", None))
        self.checkBoxSurfacesVisibility.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Surfaces", None))
        self.checkBoxPointsVisibility.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Points", None))
        self.label.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Point Size:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"View All", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"File", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Continue", None))
    # retranslateUi

