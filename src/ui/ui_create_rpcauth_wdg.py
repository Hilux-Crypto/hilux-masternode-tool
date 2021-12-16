# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_create_rpcauth_wdg.ui
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WdgCreateRpcauth(object):
    def setupUi(self, WdgCreateRpcauth):
        WdgCreateRpcauth.setObjectName("WdgCreateRpcauth")
        WdgCreateRpcauth.resize(595, 399)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(WdgCreateRpcauth)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pages = QtWidgets.QStackedWidget(WdgCreateRpcauth)
        self.pages.setObjectName("pages")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblDescription = QtWidgets.QLabel(self.page1)
        self.lblDescription.setWordWrap(True)
        self.lblDescription.setObjectName("lblDescription")
        self.verticalLayout_3.addWidget(self.lblDescription)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pages.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.page2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edtPassword = QtWidgets.QLineEdit(self.page2)
        self.edtPassword.setObjectName("edtPassword")
        self.gridLayout.addWidget(self.edtPassword, 1, 1, 1, 1)
        self.edtUser = QtWidgets.QLineEdit(self.page2)
        self.edtUser.setObjectName("edtUser")
        self.gridLayout.addWidget(self.edtUser, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.lblPage2Message = QtWidgets.QLabel(self.page2)
        self.lblPage2Message.setObjectName("lblPage2Message")
        self.verticalLayout.addWidget(self.lblPage2Message)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pages.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblSummaryMessage = QtWidgets.QLabel(self.page3)
        self.lblSummaryMessage.setText("")
        self.lblSummaryMessage.setWordWrap(False)
        self.lblSummaryMessage.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblSummaryMessage.setObjectName("lblSummaryMessage")
        self.verticalLayout_2.addWidget(self.lblSummaryMessage)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pages.addWidget(self.page3)
        self.verticalLayout_4.addWidget(self.pages)

        self.retranslateUi(WdgCreateRpcauth)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WdgCreateRpcauth)

    def retranslateUi(self, WdgCreateRpcauth):
        _translate = QtCore.QCoreApplication.translate
        WdgCreateRpcauth.setWindowTitle(_translate("WdgCreateRpcauth", "Form"))
        self.lblDescription.setText(_translate("WdgCreateRpcauth", "<h3>Description</h3>\n"
"This function allows you to generate a <code>rpcauth</code> string with the provided username and password. The <code>rpcauth</code> parameter is used when you want to start RPC interface on your hilux node, but you don\'t want to leave an unencrypted password in the node\'s configuration file.<br><br>\n"
"General steps:\n"
"<ol>\n"
"<li>Enter the username and password that you will use to connect to your Hilux node.</li>\n"
"<li>Generate the <code>rpcauth</code> string.</li>\n"
"<li>Enter the resulting string into your node\'s <code>hilux.conf</code> file. It is also recommended to remove the <code>rpcuser</code> and <code>rpcpassword</code> parameters.</li>\n"
"<li>Restart the <code>hiluxd</code> process.</li>\n"
"</ol>\n"
"<h4>Click &lt;Continue&gt; to go to step 1</h4> "))
        self.label.setText(_translate("WdgCreateRpcauth", "User"))
        self.label_2.setText(_translate("WdgCreateRpcauth", "Password"))
        self.lblPage2Message.setText(_translate("WdgCreateRpcauth", "<h4>Click &lt;Continue&gt; to generate the <code>rpcauth</code> parameter."))
