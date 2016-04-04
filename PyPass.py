#!/usr/bin/env python
#  -*- coding: utf-8 -*-
""" Main program
"""
import sys
from PyQt4 import QtGui
from UI import UiMain


def main():
    """ Main program
    """
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    main_ui = UiMain(widget)
    main_ui.setup_ui()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
