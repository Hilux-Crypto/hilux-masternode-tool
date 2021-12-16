# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ui_main_dlg.ui
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layMessage = QtWidgets.QHBoxLayout()
        self.layMessage.setContentsMargins(0, -1, -1, 0)
        self.layMessage.setSpacing(0)
        self.layMessage.setObjectName("layMessage")
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMessage.sizePolicy().hasHeightForWidth())
        self.lblMessage.setSizePolicy(sizePolicy)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setOpenExternalLinks(False)
        self.lblMessage.setObjectName("lblMessage")
        self.layMessage.addWidget(self.lblMessage)
        self.verticalLayout.addLayout(self.layMessage)
        self.gbMain = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gbMain.sizePolicy().hasHeightForWidth())
        self.gbMain.setSizePolicy(sizePolicy)
        self.gbMain.setTitle("")
        self.gbMain.setObjectName("gbMain")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbMain)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.gbMain)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1027, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuClear = QtWidgets.QMenu(self.menuTools)
        self.menuClear.setObjectName("menuClear")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.action_open_recent_files = QtWidgets.QMenu(self.menuFile)
        self.action_open_recent_files.setObjectName("action_open_recent_files")
        self.menuMasternode = QtWidgets.QMenu(self.menuBar)
        self.menuMasternode.setObjectName("menuMasternode")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_hw_wallet = QtWidgets.QAction(MainWindow)
        self.action_hw_wallet.setObjectName("action_hw_wallet")
        self.action_sign_message_with_collateral_addr = QtWidgets.QAction(MainWindow)
        self.action_sign_message_with_collateral_addr.setObjectName("action_sign_message_with_collateral_addr")
        self.action_load_config_file = QtWidgets.QAction(MainWindow)
        self.action_load_config_file.setObjectName("action_load_config_file")
        self.action_save_config_file_as = QtWidgets.QAction(MainWindow)
        self.action_save_config_file_as.setObjectName("action_save_config_file_as")
        self.action_save_config_file = QtWidgets.QAction(MainWindow)
        self.action_save_config_file.setObjectName("action_save_config_file")
        self.action_check_network_connection = QtWidgets.QAction(MainWindow)
        self.action_check_network_connection.setObjectName("action_check_network_connection")
        self.action_open_settings_window = QtWidgets.QAction(MainWindow)
        self.action_open_settings_window.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.action_open_settings_window.setObjectName("action_open_settings_window")
        self.action_open_proposals_window = QtWidgets.QAction(MainWindow)
        self.action_open_proposals_window.setObjectName("action_open_proposals_window")
        self.action_connect_hw = QtWidgets.QAction(MainWindow)
        self.action_connect_hw.setObjectName("action_connect_hw")
        self.action_disconnect_hw = QtWidgets.QAction(MainWindow)
        self.action_disconnect_hw.setObjectName("action_disconnect_hw")
        self.action_hw_tools = QtWidgets.QAction(MainWindow)
        self.action_hw_tools.setObjectName("action_hw_tools")
        self.action_check_for_updates = QtWidgets.QAction(MainWindow)
        self.action_check_for_updates.setObjectName("action_check_for_updates")
        self.action_open_log_file = QtWidgets.QAction(MainWindow)
        self.action_open_log_file.setObjectName("action_open_log_file")
        self.action_about_app = QtWidgets.QAction(MainWindow)
        self.action_about_app.setMenuRole(QtWidgets.QAction.AboutRole)
        self.action_about_app.setObjectName("action_about_app")
        self.action_import_masternode_conf = QtWidgets.QAction(MainWindow)
        self.action_import_masternode_conf.setObjectName("action_import_masternode_conf")
        self.action_about_qt = QtWidgets.QAction(MainWindow)
        self.action_about_qt.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_gen_mn_priv_key_compressed = QtWidgets.QAction(MainWindow)
        self.action_gen_mn_priv_key_compressed.setObjectName("action_gen_mn_priv_key_compressed")
        self.action_gen_mn_priv_key_uncompressed = QtWidgets.QAction(MainWindow)
        self.action_gen_mn_priv_key_uncompressed.setObjectName("action_gen_mn_priv_key_uncompressed")
        self.action_command_console = QtWidgets.QAction(MainWindow)
        self.action_command_console.setObjectName("action_command_console")
        self.action_run_trezor_emulator = QtWidgets.QAction(MainWindow)
        self.action_run_trezor_emulator.setObjectName("action_run_trezor_emulator")
        self.action_open_data_folder = QtWidgets.QAction(MainWindow)
        self.action_open_data_folder.setObjectName("action_open_data_folder")
        self.action_clear_wallet_cache = QtWidgets.QAction(MainWindow)
        self.action_clear_wallet_cache.setObjectName("action_clear_wallet_cache")
        self.action_clear_proposals_cache = QtWidgets.QAction(MainWindow)
        self.action_clear_proposals_cache.setObjectName("action_clear_proposals_cache")
        self.action_restore_config_from_backup = QtWidgets.QAction(MainWindow)
        self.action_restore_config_from_backup.setObjectName("action_restore_config_from_backup")
        self.action_sign_message_with_owner_key = QtWidgets.QAction(MainWindow)
        self.action_sign_message_with_owner_key.setObjectName("action_sign_message_with_owner_key")
        self.action_sign_message_with_voting_key = QtWidgets.QAction(MainWindow)
        self.action_sign_message_with_voting_key.setObjectName("action_sign_message_with_voting_key")
        self.action_export_configuration = QtWidgets.QAction(MainWindow)
        self.action_export_configuration.setObjectName("action_export_configuration")
        self.action_import_configuration = QtWidgets.QAction(MainWindow)
        self.action_import_configuration.setObjectName("action_import_configuration")
        self.action_wallet_tools = QtWidgets.QAction(MainWindow)
        self.action_wallet_tools.setObjectName("action_wallet_tools")
        self.action_register_masternode = QtWidgets.QAction(MainWindow)
        self.action_register_masternode.setObjectName("action_register_masternode")
        self.action_update_masternode_payout_address = QtWidgets.QAction(MainWindow)
        self.action_update_masternode_payout_address.setObjectName("action_update_masternode_payout_address")
        self.action_update_masternode_operator_key = QtWidgets.QAction(MainWindow)
        self.action_update_masternode_operator_key.setObjectName("action_update_masternode_operator_key")
        self.action_update_masternode_voting_key = QtWidgets.QAction(MainWindow)
        self.action_update_masternode_voting_key.setObjectName("action_update_masternode_voting_key")
        self.action_revoke_masternode = QtWidgets.QAction(MainWindow)
        self.action_revoke_masternode.setObjectName("action_revoke_masternode")
        self.action_new_masternode_entry = QtWidgets.QAction(MainWindow)
        self.action_new_masternode_entry.setShortcutVisibleInContextMenu(True)
        self.action_new_masternode_entry.setObjectName("action_new_masternode_entry")
        self.action_update_masternode_service = QtWidgets.QAction(MainWindow)
        self.action_update_masternode_service.setObjectName("action_update_masternode_service")
        self.action_show_masternode_details = QtWidgets.QAction(MainWindow)
        self.action_show_masternode_details.setObjectName("action_show_masternode_details")
        self.action_delete_masternode_entry = QtWidgets.QAction(MainWindow)
        self.action_delete_masternode_entry.setShortcutVisibleInContextMenu(True)
        self.action_delete_masternode_entry.setObjectName("action_delete_masternode_entry")
        self.action_clone_masternode_entry = QtWidgets.QAction(MainWindow)
        self.action_clone_masternode_entry.setObjectName("action_clone_masternode_entry")
        self.action_new_configuration = QtWidgets.QAction(MainWindow)
        self.action_new_configuration.setObjectName("action_new_configuration")
        self.menuClear.addAction(self.action_clear_wallet_cache)
        self.menuClear.addAction(self.action_clear_proposals_cache)
        self.menuTools.addAction(self.action_hw_wallet)
        self.menuTools.addAction(self.action_wallet_tools)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_check_for_updates)
        self.menuTools.addAction(self.action_command_console)
        self.menuTools.addAction(self.action_open_log_file)
        self.menuTools.addAction(self.action_open_data_folder)
        self.menuTools.addAction(self.menuClear.menuAction())
        self.menuFile.addAction(self.action_new_configuration)
        self.menuFile.addAction(self.action_load_config_file)
        self.menuFile.addAction(self.action_open_recent_files.menuAction())
        self.menuFile.addAction(self.action_restore_config_from_backup)
        self.menuFile.addAction(self.action_save_config_file)
        self.menuFile.addAction(self.action_save_config_file_as)
        self.menuFile.addAction(self.action_export_configuration)
        self.menuFile.addAction(self.action_import_configuration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_open_settings_window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_about_app)
        self.menuFile.addAction(self.action_about_qt)
        self.menuMasternode.addAction(self.action_show_masternode_details)
        self.menuMasternode.addSeparator()
        self.menuMasternode.addAction(self.action_new_masternode_entry)
        self.menuMasternode.addAction(self.action_clone_masternode_entry)
        self.menuMasternode.addAction(self.action_delete_masternode_entry)
        self.menuMasternode.addSeparator()
        self.menuMasternode.addAction(self.action_register_masternode)
        self.menuMasternode.addAction(self.action_update_masternode_payout_address)
        self.menuMasternode.addAction(self.action_update_masternode_operator_key)
        self.menuMasternode.addAction(self.action_update_masternode_voting_key)
        self.menuMasternode.addAction(self.action_update_masternode_service)
        self.menuMasternode.addAction(self.action_revoke_masternode)
        self.menuMasternode.addSeparator()
        self.menuMasternode.addAction(self.action_sign_message_with_collateral_addr)
        self.menuMasternode.addAction(self.action_sign_message_with_owner_key)
        self.menuMasternode.addAction(self.action_sign_message_with_voting_key)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuMasternode.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.toolBar.addAction(self.action_open_settings_window)
        self.toolBar.addAction(self.action_save_config_file)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_check_network_connection)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_connect_hw)
        self.toolBar.addAction(self.action_disconnect_hw)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_open_proposals_window)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_hw_wallet)
        self.toolBar.addAction(self.action_wallet_tools)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_open_recent_files.setTitle(_translate("MainWindow", "Recent Configuration Files"))
        self.menuMasternode.setTitle(_translate("MainWindow", "Masternode"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_hw_wallet.setText(_translate("MainWindow", "Wallet"))
        self.action_sign_message_with_collateral_addr.setText(_translate("MainWindow", "Sign Message with Collateral Address..."))
        self.action_sign_message_with_collateral_addr.setToolTip(_translate("MainWindow", "Sign message with the collateral address of the current masternode"))
        self.action_load_config_file.setText(_translate("MainWindow", "Open Configuration File..."))
        self.action_load_config_file.setToolTip(_translate("MainWindow", "Open Configuration File"))
        self.action_load_config_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save_config_file_as.setText(_translate("MainWindow", "Save Configuration As..."))
        self.action_save_config_file_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action_save_config_file.setText(_translate("MainWindow", "Save Configuration"))
        self.action_save_config_file.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_check_network_connection.setText(_translate("MainWindow", "Check Network Connection"))
        self.action_check_network_connection.setToolTip(_translate("MainWindow", "Check Hilux Network Connection"))
        self.action_open_settings_window.setText(_translate("MainWindow", "Settings"))
        self.action_open_settings_window.setToolTip(_translate("MainWindow", "Settings"))
        self.action_open_proposals_window.setText(_translate("MainWindow", "Proposals"))
        self.action_open_proposals_window.setToolTip(_translate("MainWindow", "Proposals"))
        self.action_connect_hw.setText(_translate("MainWindow", "Connect Hardware Wallet"))
        self.action_disconnect_hw.setText(_translate("MainWindow", "Disconnect Hardware Wallet"))
        self.action_hw_tools.setText(_translate("MainWindow", "Hardware Wallet Tools..."))
        self.action_check_for_updates.setText(_translate("MainWindow", "Check For Updates"))
        self.action_open_log_file.setText(_translate("MainWindow", "Open Log File"))
        self.action_open_log_file.setShortcut(_translate("MainWindow", "Meta+Alt+L"))
        self.action_about_app.setText(_translate("MainWindow", "About HiluxMasternodeTool..."))
        self.action_import_masternode_conf.setText(_translate("MainWindow", "Import masternodes from the masternode.conf file..."))
        self.action_about_qt.setText(_translate("MainWindow", "About Qt..."))
        self.action_about_qt.setToolTip(_translate("MainWindow", "About Qt"))
        self.action_gen_mn_priv_key_compressed.setText(_translate("MainWindow", "Generate masternode private key (compressed)"))
        self.action_gen_mn_priv_key_compressed.setShortcut(_translate("MainWindow", "Ctrl+Alt+C"))
        self.action_gen_mn_priv_key_uncompressed.setText(_translate("MainWindow", "Generate masternode private key (uncompressed)"))
        self.action_gen_mn_priv_key_uncompressed.setToolTip(_translate("MainWindow", "Generate masternode private key (uncompressed)"))
        self.action_gen_mn_priv_key_uncompressed.setShortcut(_translate("MainWindow", "Ctrl+Alt+U"))
        self.action_command_console.setText(_translate("MainWindow", "Command Console"))
        self.action_command_console.setShortcut(_translate("MainWindow", "Meta+Alt+C"))
        self.action_run_trezor_emulator.setText(_translate("MainWindow", "Run Trezor T emulator"))
        self.action_run_trezor_emulator.setToolTip(_translate("MainWindow", "Run Trezor T emulator"))
        self.action_open_data_folder.setText(_translate("MainWindow", "Open Application Data Folder"))
        self.action_clear_wallet_cache.setText(_translate("MainWindow", "Wallet Cache"))
        self.action_clear_proposals_cache.setText(_translate("MainWindow", "Proposals Cache"))
        self.action_restore_config_from_backup.setText(_translate("MainWindow", "Restore Configuration from Backup..."))
        self.action_restore_config_from_backup.setToolTip(_translate("MainWindow", "Restore Configuration from Backup..."))
        self.action_restore_config_from_backup.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.action_sign_message_with_owner_key.setText(_translate("MainWindow", "Sign Message with Owner Key..."))
        self.action_sign_message_with_owner_key.setToolTip(_translate("MainWindow", "Sign message with the masternode owner key"))
        self.action_sign_message_with_voting_key.setText(_translate("MainWindow", "Sign Message with Voting Key..."))
        self.action_sign_message_with_voting_key.setToolTip(_translate("MainWindow", "Sign message with the masternode voting key"))
        self.action_export_configuration.setText(_translate("MainWindow", "Export Configuration..."))
        self.action_export_configuration.setToolTip(_translate("MainWindow", "Export Configuration"))
        self.action_import_configuration.setText(_translate("MainWindow", "Import Configuration..."))
        self.action_import_configuration.setToolTip(_translate("MainWindow", "Import Configuration"))
        self.action_wallet_tools.setText(_translate("MainWindow", "Toolbox"))
        self.action_register_masternode.setText(_translate("MainWindow", "Register Masternode..."))
        self.action_update_masternode_payout_address.setText(_translate("MainWindow", "Update Payout Address..."))
        self.action_update_masternode_payout_address.setToolTip(_translate("MainWindow", "Send a transaction setting up a new payout address"))
        self.action_update_masternode_operator_key.setText(_translate("MainWindow", "Update Operator Key..."))
        self.action_update_masternode_operator_key.setToolTip(_translate("MainWindow", "Send a transaction setting up a new operator key"))
        self.action_update_masternode_voting_key.setText(_translate("MainWindow", "Update Voting Key..."))
        self.action_update_masternode_voting_key.setToolTip(_translate("MainWindow", "Send a transaction setting up a new voting key"))
        self.action_revoke_masternode.setText(_translate("MainWindow", "Revoke Masternode..."))
        self.action_revoke_masternode.setToolTip(_translate("MainWindow", "Send a transaction revoking masternode"))
        self.action_new_masternode_entry.setText(_translate("MainWindow", "Add New Masternode Entry..."))
        self.action_new_masternode_entry.setToolTip(_translate("MainWindow", "Add a new masternode entry to configuration"))
        self.action_new_masternode_entry.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_update_masternode_service.setText(_translate("MainWindow", "Update Service (IP/port/operator payout address)..."))
        self.action_update_masternode_service.setToolTip(_translate("MainWindow", "Update masternode IP address, TCP port or operator payout address"))
        self.action_show_masternode_details.setText(_translate("MainWindow", "Go to Masternode Details"))
        self.action_show_masternode_details.setToolTip(_translate("MainWindow", "Show masternode configuration details"))
        self.action_delete_masternode_entry.setText(_translate("MainWindow", "Delete Masternode Entry"))
        self.action_delete_masternode_entry.setToolTip(_translate("MainWindow", "Delete seleted masternode entry"))
        self.action_delete_masternode_entry.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_clone_masternode_entry.setText(_translate("MainWindow", "Clone Masternode Entry"))
        self.action_clone_masternode_entry.setToolTip(_translate("MainWindow", "Clone masternode configuration entry"))
        self.action_new_configuration.setText(_translate("MainWindow", "New Configuration"))
        self.action_new_configuration.setToolTip(_translate("MainWindow", "Creates a new configuration file"))
