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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

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
        self.groupBox.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Point Cloud Partitioner", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"Group Points", None))
        self.pushButtonCreateGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Create Group", None))
        self.pushButtonRemoveGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Remove Group", None))
        self.pushButtonAddToGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Add Selected Points to Group", None))
        self.pushButtonRemoveFromGroup.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Remove Selected Points from Group", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"View", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"View All", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("PointCloudPartitionerWidget", u"File", None))
        self.pushButtonContinue.setText(QCoreApplication.translate("PointCloudPartitionerWidget", u"Continue", None))
    # retranslateUi

