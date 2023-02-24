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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from mapclientplugins.pointcloudpartitionerstep.view.zincpointcloudpartitionerwidget import ZincPointCloudPartitionerWidget

class Ui_PointCloudPartitionerWidget(object):
    def setupUi(self, PointCloudPartitionerWidget):
        if not PointCloudPartitionerWidget.objectName():
            PointCloudPartitionerWidget.setObjectName(u"PointCloudPartitionerWidget")
        PointCloudPartitionerWidget.resize(884, 640)
        self.horizontalLayout = QHBoxLayout(PointCloudPartitionerWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(PointCloudPartitionerWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonContinue = QPushButton(self.groupBox_5)
        self.pushButtonContinue.setObjectName(u"pushButtonContinue")

        self.horizontalLayout_3.addWidget(self.pushButtonContinue)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonViewAll = QPushButton(self.groupBox_4)
        self.pushButtonViewAll.setObjectName(u"pushButtonViewAll")

        self.horizontalLayout_2.addWidget(self.pushButtonViewAll)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.spinBoxPointSize = QSpinBox(self.groupBox)
        self.spinBoxPointSize.setObjectName(u"spinBoxPointSize")
        self.spinBoxPointSize.setMinimum(1)

        self.horizontalLayout_9.addWidget(self.spinBoxPointSize)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButtonDeleteNode = QPushButton(self.groupBox)
        self.pushButtonDeleteNode.setObjectName(u"pushButtonDeleteNode")

        self.horizontalLayout_8.addWidget(self.pushButtonDeleteNode)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.widgetZinc = ZincPointCloudPartitionerWidget(PointCloudPartitionerWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.widgetZinc)


        self.retranslateUi(PointCloudPartitionerWidget)

        QMetaObject.connectSlotsByName(PointCloudPartitionerWidget)
    # setupUi

    def retranslateUi(self, PointCloudPartitionerWidget):
        PointCloudPartitionerWidget.setWindowTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Point Cloud Partitioner", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Point Cloud Partitioner", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"File", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Continue", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"View All", None))
        self.groupBox.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Points", None))
        self.label.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Size:", None))
        self.pushButtonDeleteNode.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Delete", None))
    # retranslateUi

