""" UI Module
"""
from PyQt4 import QtCore, QtGui
from Password import Password

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(text):
        """ Wrapper function
            :param text: The text
        """
        return text

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, extra):
        """ Translate
            :param context: The App context
            :param text: The text
            :param extra: Extra parameter
        """
        return QtGui.QApplication.translate(context, text, extra, _encoding)
except AttributeError:
    def _translate(context, text, extra):
        """ Translate
            :param context: The App context
            :param text: The text
            :param extra: Extra parameter
        """
        return QtGui.QApplication.translate(context, text, extra)


class UiMain(object):
    """ UI Class
    """
    APP = "PyPass"

    SIZE_X = 640
    SIZE_Y = 480

    # Font types
    FONT_TITLE = 0
    FONT_SMALL = 1

    # Where the elements should start
    POSITION_LEFT_X = 30
    POSITION_RIGHT_X = 455
    POSITION_TOP_X = 390
    POSITION_SECTION_TOP_Y = 110

    LABEL_LENGTH = 120
    LABEL_HEIGHT = 20

    TEXT_HEIGHT = 30

    TEXT_AREA_HEIGHT = 110

    BUTTON_LENGTH = 100
    BUTTON_HEIGHT = 40

    def __init__(self, main):
        """ __init__
            :param main: The main widget
        """
        self.main = main

        self.lbl_title = QtGui.QLabel(self.main)
        self.lbl_version = QtGui.QLabel(self.main)
        self.lbl_master_password = QtGui.QLabel(self.main)
        self.lbl_algorithm = QtGui.QLabel(self.main)
        self.lbl_raw_text = QtGui.QLabel(self.main)
        self.lbl_encrypted_text = QtGui.QLabel(self.main)

        self.btn_encrypt = QtGui.QPushButton(self.main)
        self.btn_decrypt = QtGui.QPushButton(self.main)

        self.txt_master_password = QtGui.QLineEdit(self.main)
        self.txt_encrypted_text = QtGui.QPlainTextEdit(self.main)
        self.txt_raw_text = QtGui.QPlainTextEdit(self.main)

        self.cmb_algorithm = QtGui.QComboBox(self.main)
        self.line = QtGui.QFrame(self.main)

    def setup_ui(self):
        """ create the ui interface
        """

        # Main Window
        self.main.setObjectName(_fromUtf8(UiMain.APP))
        self.main.resize(self.SIZE_X, self.SIZE_Y)
        self.main.setMinimumSize(QtCore.QSize(self.SIZE_X, self.SIZE_Y))
        self.main.setMaximumSize(QtCore.QSize(self.SIZE_X, self.SIZE_Y))
        self.main.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.main.setWindowIcon(self._get_icon())

        self._set_labels()
        self._set_buttons()
        self._set_text()
        self._set_combo()
        self._set_decorator()
        self._translate_ui()
        self._set_tab_order()
        self._connect_slots()

    def _set_labels(self):
        """ Set all the labels for the UI
        """
        # title
        label_object = QtCore.QRect(
            self.POSITION_LEFT_X, 10, 180, 70)
        self.lbl_title.setGeometry(label_object)
        self.lbl_title.setFont(self._get_font_properties(self.FONT_TITLE))
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))

        # version
        label_object = QtCore.QRect(
            550, 455, self.LABEL_LENGTH, self.LABEL_HEIGHT)
        self.lbl_version.setGeometry(label_object)
        self.lbl_version.setFont(self._get_font_properties(self.FONT_SMALL))
        self.lbl_version.setObjectName(_fromUtf8("lbl_version"))

        # master password
        label_object = QtCore.QRect(
            self.POSITION_TOP_X, 20,
            self.LABEL_LENGTH, self.LABEL_HEIGHT)
        self.lbl_master_password.setGeometry(label_object)
        self.lbl_master_password.setObjectName(_fromUtf8("lbl_master_password"))

        # algorithm
        label_object = QtCore.QRect(
            self.POSITION_RIGHT_X, self.POSITION_SECTION_TOP_Y,
            self.LABEL_LENGTH, self.LABEL_HEIGHT)
        self.lbl_algorithm.setGeometry(label_object)
        self.lbl_algorithm.setObjectName(_fromUtf8("lbl_algorithm"))

        # raw text
        label_object = QtCore.QRect(
            self.POSITION_LEFT_X, self.POSITION_SECTION_TOP_Y,
            self.LABEL_LENGTH, self.LABEL_HEIGHT)
        self.lbl_raw_text.setGeometry(label_object)
        self.lbl_raw_text.setObjectName(_fromUtf8("lbl_raw_text"))

        # encrypted text
        label_object = QtCore.QRect(
            self.POSITION_LEFT_X, 303,
            self.LABEL_LENGTH, self.LABEL_HEIGHT)
        self.lbl_encrypted_text.setGeometry(label_object)
        self.lbl_encrypted_text.setObjectName(_fromUtf8("lbl_encrypted_text"))

    def _set_buttons(self):
        """ Set all the buttons for the UI
        """
        button_object = QtCore.QRect(
            self.POSITION_LEFT_X, 245, self.BUTTON_LENGTH, self.BUTTON_HEIGHT)
        self.btn_encrypt.setGeometry(button_object)
        self.btn_encrypt.setObjectName(_fromUtf8("btn_encrypt"))

        button_object = QtCore.QRect(
            510, 280, self.BUTTON_LENGTH, self.BUTTON_HEIGHT)
        self.btn_decrypt.setGeometry(button_object)
        self.btn_decrypt.setObjectName(_fromUtf8("btn_decrypt"))

    def _set_text(self):
        """ Set all the line edit for the UI
        """
        # master password
        txt_object = QtCore.QRect(
            self.POSITION_TOP_X, 40, 220, self.TEXT_HEIGHT)
        self.txt_master_password.setGeometry(txt_object)
        self.txt_master_password.setText("")
        self.txt_master_password.setMaxLength(32)
        self.txt_master_password.setEchoMode(QtGui.QLineEdit.Password)
        self.txt_master_password.setObjectName(_fromUtf8("txt_master_password"))

        # raw text
        txt_object = QtCore.QRect(
            self.POSITION_LEFT_X, 130, 400, self.TEXT_AREA_HEIGHT)
        self.txt_raw_text.setGeometry(txt_object)
        self.txt_raw_text.setObjectName(_fromUtf8("txt_raw_text"))

        # encrypted text
        txt_object = QtCore.QRect(
            self.POSITION_LEFT_X, 325, 580, self.TEXT_AREA_HEIGHT)
        self.txt_encrypted_text.setGeometry(txt_object)
        self.txt_encrypted_text.setObjectName(_fromUtf8("txt_encrypted_text"))

    def _set_combo(self):
        """ Set all the combo for the UI
        """
        combo_object = QtCore.QRect(
            self.POSITION_RIGHT_X, 130, 160, self.TEXT_HEIGHT)
        self.cmb_algorithm.setGeometry(combo_object)
        self.cmb_algorithm.setEditable(False)
        self.cmb_algorithm.setObjectName(_fromUtf8("algorithm"))

        # populate with data
        cipher_list = Password.get_cipher_list()

        for cipher in cipher_list:
            self.cmb_algorithm.addItem(_fromUtf8(cipher))

        # select first one
        self.cmb_algorithm.setCurrentIndex(0)

    def _set_decorator(self):
        """ Set all the decorators for the UI
        """

        # line
        self.line.setGeometry(QtCore.QRect(0, 80, 640, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

    def _set_tab_order(self):
        """ Set the TAB orders
        """

        self.main.setTabOrder(self.txt_master_password, self.txt_raw_text)
        self.main.setTabOrder(self.txt_raw_text, self.txt_encrypted_text)
        self.main.setTabOrder(self.txt_encrypted_text, self.cmb_algorithm)
        self.main.setTabOrder(self.cmb_algorithm, self.btn_encrypt)
        self.main.setTabOrder(self.btn_encrypt, self.btn_decrypt)

    def _connect_slots(self):
        """ Set the events
        """

        QtCore.QObject.connect(self.btn_encrypt,
                               QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self._encrypt_data
                               )

        QtCore.QObject.connect(self.btn_decrypt,
                               QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self._decrypt_data
                               )
        QtCore.QMetaObject.connectSlotsByName(self.main)

    def _get_icon(self):
        """ Get the app icon
            :return QIcon
        """
        icon = QtGui.QIcon(self.main)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("UI/app.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def _translate_ui(self):
        """ Translate UI
        """

        self.main.setWindowTitle(
            _translate(UiMain.APP, "PyPass", None))
        self.btn_encrypt.setText(
            _translate(UiMain.APP, "encrypt", None))
        self.lbl_title.setText(
            _translate(UiMain.APP, "PyPass", None))
        self.lbl_master_password.setText(
            _translate(UiMain.APP, "Master Password", None))
        self.lbl_algorithm.setText(
            _translate(UiMain.APP, "Algorithm", None))
        self.lbl_raw_text.setText(
            _translate(UiMain.APP, "Raw Text", None))
        self.lbl_encrypted_text.setText(
            _translate(UiMain.APP, "Encrypted Text", None))
        self.btn_decrypt.setText(
            _translate(UiMain.APP, "decrypt", None))
        self.lbl_version.setText(
            _translate(UiMain.APP, "PyPass version 1.0", None))

    def _encrypt_data(self):
        """ Encrypt the raw data
        """

        if not self._check_master_password():
            self._show_message("Error: The master password is not set")
            return

        raw_text = self.txt_raw_text.toPlainText()
        cipher = self.cmb_algorithm.currentText()

        my_pass = Password(self.txt_master_password.text(), cipher)
        encrypted_text = my_pass.encrypt_text(raw_text)

        self.txt_encrypted_text.setPlainText(QtCore.QString(encrypted_text))

    def _decrypt_data(self):
        """ Decrypt the encrypted data
        """
        encrypted_text = self.txt_encrypted_text.toPlainText()
        cipher = self.cmb_algorithm.currentText()

        my_pass = Password(self.txt_master_password.text(), cipher)
        raw_text = my_pass.decrypt_text(encrypted_text)

        self.txt_raw_text.setPlainText(QtCore.QString(raw_text))

    def _check_master_password(self):
        """ Check if the master password is set
        """
        master = self.txt_master_password.text()
        return len(master) > 0

    def _show_message(self, message):
        """ Show error message
            :param message: The error message
        """
        self.txt_encrypted_text.setPlainText(QtCore.QString(message))

    def _get_font_properties(self, font_type):
        """ Get the font properties
            :param font_type: The font type
            :return: QFont()
        """
        font = QtGui.QFont()
        if font_type == self.FONT_TITLE:
            font.setPointSize(32)
            font.setBold(True)
            font.setWeight(75)
        else:
            font.setPointSize(7)
        return font
