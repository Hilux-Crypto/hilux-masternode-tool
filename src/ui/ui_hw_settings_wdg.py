# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_hw_settings_wdg.ui
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WdgHwSettings(object):
    def setupUi(self, WdgHwSettings):
        WdgHwSettings.setObjectName("WdgHwSettings")
        WdgHwSettings.resize(536, 359)
        self.verticalLayout = QtWidgets.QVBoxLayout(WdgHwSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wdgHwSettings = QtWidgets.QWidget(WdgHwSettings)
        self.wdgHwSettings.setObjectName("wdgHwSettings")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wdgHwSettings)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, 0, 4, 0)
        self.gridLayout_3.setSpacing(8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblPinStatus = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblPinStatus.setObjectName("lblPinStatus")
        self.gridLayout_3.addWidget(self.lblPinStatus, 1, 1, 1, 1)
        self.lblSDCardProtectionStatus = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblSDCardProtectionStatus.setObjectName("lblSDCardProtectionStatus")
        self.gridLayout_3.addWidget(self.lblSDCardProtectionStatus, 6, 1, 1, 1)
        self.lblSDCardProtectionLabel = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblSDCardProtectionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSDCardProtectionLabel.setObjectName("lblSDCardProtectionLabel")
        self.gridLayout_3.addWidget(self.lblSDCardProtectionLabel, 6, 0, 1, 1)
        self.btnEnDisPin = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnEnDisPin.setAutoDefault(False)
        self.btnEnDisPin.setObjectName("btnEnDisPin")
        self.gridLayout_3.addWidget(self.btnEnDisPin, 1, 2, 1, 1)
        self.lblWipeCodeStatus = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblWipeCodeStatus.setObjectName("lblWipeCodeStatus")
        self.gridLayout_3.addWidget(self.lblWipeCodeStatus, 5, 1, 1, 1)
        self.lblFirmwareVersion = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblFirmwareVersion.setMinimumSize(QtCore.QSize(128, 0))
        self.lblFirmwareVersion.setOpenExternalLinks(True)
        self.lblFirmwareVersion.setObjectName("lblFirmwareVersion")
        self.gridLayout_3.addWidget(self.lblFirmwareVersion, 0, 1, 1, 3)
        self.btnEnDisPassAlwaysOnDevice = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnEnDisPassAlwaysOnDevice.setObjectName("btnEnDisPassAlwaysOnDevice")
        self.gridLayout_3.addWidget(self.btnEnDisPassAlwaysOnDevice, 4, 2, 1, 1)
        self.btnEnDisSDCardProtection = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnEnDisSDCardProtection.setObjectName("btnEnDisSDCardProtection")
        self.gridLayout_3.addWidget(self.btnEnDisSDCardProtection, 6, 2, 1, 1)
        self.btnEnDisWipeCode = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnEnDisWipeCode.setObjectName("btnEnDisWipeCode")
        self.gridLayout_3.addWidget(self.btnEnDisWipeCode, 5, 2, 1, 1)
        self.lblPinStatusLabel = QtWidgets.QLabel(self.wdgHwSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblPinStatusLabel.setFont(font)
        self.lblPinStatusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPinStatusLabel.setObjectName("lblPinStatusLabel")
        self.gridLayout_3.addWidget(self.lblPinStatusLabel, 1, 0, 1, 1)
        self.btnEnDisPass = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnEnDisPass.setAutoDefault(False)
        self.btnEnDisPass.setObjectName("btnEnDisPass")
        self.gridLayout_3.addWidget(self.btnEnDisPass, 2, 2, 1, 1)
        self.lblWipeCodeLabel = QtWidgets.QLabel(self.wdgHwSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblWipeCodeLabel.setFont(font)
        self.lblWipeCodeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblWipeCodeLabel.setObjectName("lblWipeCodeLabel")
        self.gridLayout_3.addWidget(self.lblWipeCodeLabel, 5, 0, 1, 1)
        self.lblFirmwareVersionLabel = QtWidgets.QLabel(self.wdgHwSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblFirmwareVersionLabel.setFont(font)
        self.lblFirmwareVersionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblFirmwareVersionLabel.setObjectName("lblFirmwareVersionLabel")
        self.gridLayout_3.addWidget(self.lblFirmwareVersionLabel, 0, 0, 1, 1)
        self.btnChangePin = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnChangePin.setAutoDefault(False)
        self.btnChangePin.setObjectName("btnChangePin")
        self.gridLayout_3.addWidget(self.btnChangePin, 1, 3, 1, 1)
        self.lblPassAlwaysOnDeviceLabel = QtWidgets.QLabel(self.wdgHwSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblPassAlwaysOnDeviceLabel.setFont(font)
        self.lblPassAlwaysOnDeviceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPassAlwaysOnDeviceLabel.setObjectName("lblPassAlwaysOnDeviceLabel")
        self.gridLayout_3.addWidget(self.lblPassAlwaysOnDeviceLabel, 4, 0, 1, 1)
        self.lblPassAlwaysOnDeviceStatus = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblPassAlwaysOnDeviceStatus.setObjectName("lblPassAlwaysOnDeviceStatus")
        self.gridLayout_3.addWidget(self.lblPassAlwaysOnDeviceStatus, 4, 1, 1, 1)
        self.lblPassStatus = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblPassStatus.setObjectName("lblPassStatus")
        self.gridLayout_3.addWidget(self.lblPassStatus, 2, 1, 1, 1)
        self.lblPassStatusLabel = QtWidgets.QLabel(self.wdgHwSettings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblPassStatusLabel.setFont(font)
        self.lblPassStatusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPassStatusLabel.setObjectName("lblPassStatusLabel")
        self.gridLayout_3.addWidget(self.lblPassStatusLabel, 2, 0, 1, 1)
        self.btnRefreshSDCardProtection = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnRefreshSDCardProtection.setObjectName("btnRefreshSDCardProtection")
        self.gridLayout_3.addWidget(self.btnRefreshSDCardProtection, 6, 3, 1, 1)
        self.lblLabel = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLabel.setObjectName("lblLabel")
        self.gridLayout_3.addWidget(self.lblLabel, 3, 0, 1, 1)
        self.lblLabelValue = QtWidgets.QLabel(self.wdgHwSettings)
        self.lblLabelValue.setObjectName("lblLabelValue")
        self.gridLayout_3.addWidget(self.lblLabelValue, 3, 1, 1, 1)
        self.btnChangeLabel = QtWidgets.QPushButton(self.wdgHwSettings)
        self.btnChangeLabel.setObjectName("btnChangeLabel")
        self.gridLayout_3.addWidget(self.btnChangeLabel, 3, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.wdgHwSettings)
        self.lblMessage = QtWidgets.QLabel(WdgHwSettings)
        self.lblMessage.setMinimumSize(QtCore.QSize(0, 0))
        self.lblMessage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        spacerItem1 = QtWidgets.QSpacerItem(20, 133, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(WdgHwSettings)
        QtCore.QMetaObject.connectSlotsByName(WdgHwSettings)

    def retranslateUi(self, WdgHwSettings):
        _translate = QtCore.QCoreApplication.translate
        WdgHwSettings.setWindowTitle(_translate("WdgHwSettings", "Form"))
        self.lblPinStatus.setText(_translate("WdgHwSettings", "enabled"))
        self.lblSDCardProtectionStatus.setText(_translate("WdgHwSettings", "enabled"))
        self.lblSDCardProtectionLabel.setText(_translate("WdgHwSettings", "SD card protection:"))
        self.btnEnDisPin.setText(_translate("WdgHwSettings", "Disable"))
        self.lblWipeCodeStatus.setText(_translate("WdgHwSettings", "enabled"))
        self.lblFirmwareVersion.setText(_translate("WdgHwSettings", "?"))
        self.btnEnDisPassAlwaysOnDevice.setText(_translate("WdgHwSettings", "Disable"))
        self.btnEnDisSDCardProtection.setText(_translate("WdgHwSettings", "Disable"))
        self.btnEnDisWipeCode.setText(_translate("WdgHwSettings", "Disable"))
        self.lblPinStatusLabel.setText(_translate("WdgHwSettings", "PIN:"))
        self.btnEnDisPass.setText(_translate("WdgHwSettings", "Disable"))
        self.lblWipeCodeLabel.setText(_translate("WdgHwSettings", "Wipe code:"))
        self.lblFirmwareVersionLabel.setText(_translate("WdgHwSettings", "Firmware version:"))
        self.btnChangePin.setText(_translate("WdgHwSettings", "Change"))
        self.lblPassAlwaysOnDeviceLabel.setText(_translate("WdgHwSettings", "Passphrase always on device:"))
        self.lblPassAlwaysOnDeviceStatus.setText(_translate("WdgHwSettings", "enabled"))
        self.lblPassStatus.setText(_translate("WdgHwSettings", "enabled"))
        self.lblPassStatusLabel.setText(_translate("WdgHwSettings", "Passphrase:"))
        self.btnRefreshSDCardProtection.setText(_translate("WdgHwSettings", "Refresh"))
        self.lblLabel.setText(_translate("WdgHwSettings", "Label:"))
        self.lblLabelValue.setText(_translate("WdgHwSettings", "not set"))
        self.btnChangeLabel.setText(_translate("WdgHwSettings", "Change"))
        self.lblMessage.setText(_translate("WdgHwSettings", "..."))
