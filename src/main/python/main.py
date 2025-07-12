# SPDX-License-Identifier: GPL-2.0-or-later
import ssl
import certifi
import os

if ssl.get_default_verify_paths().cafile is None:
    os.environ['SSL_CERT_FILE'] = certifi.where()

import traceback

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import pyqtSignal

import functools

import sys

from main_window import MainWindow


# http://timlehr.com/python-exception-hooks-with-qt-message-box/
from util import init_logger


def show_exception_box(log_msg):
    if QtWidgets.QApplication.instance() is not None:
        errorbox = QtWidgets.QMessageBox()
        errorbox.setText(log_msg)
        errorbox.exec()


class UncaughtHook(QtCore.QObject):
    _exception_caught = pyqtSignal(object)

    def __init__(self, *args, **kwargs):
        super(UncaughtHook, self).__init__(*args, **kwargs)

        # this registers the exception_hook() function as hook with the Python interpreter
        sys._excepthook = sys.excepthook
        sys.excepthook = self.exception_hook

        # connect signal to execute the message box function always on main thread
        self._exception_caught.connect(show_exception_box)

    def exception_hook(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            # ignore keyboard interrupt to support console applications
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            log_msg = '\n'.join([''.join(traceback.format_tb(exc_traceback)),
                                 '{0}: {1}'.format(exc_type.__name__, exc_value)])

            # trigger message box show
            self._exception_caught.emit(log_msg)
        sys._excepthook(exc_type, exc_value, exc_traceback)

class VialApplicationContext:
    def __init__(self):
        self.build_settings = {
            "app_name": "Vial",
            "version": "0.7.3"
        }
        self._app = None
    
    @property
    def app(self):
        if self._app is None:
            # Override the app definition in order to set WM_CLASS.
            self._app = QtWidgets.QApplication(sys.argv)
            self._app.setApplicationName(self.build_settings["app_name"])
            self._app.setOrganizationDomain("vial.today")
            self._app.setApplicationVersion(self.build_settings["version"])
        return self._app
    
    def get_resource(self, resource_path):
        """Get resource file path - replacement for fbs functionality"""
        import os
        script_dir = os.path.dirname(os.path.abspath(__file__))
        resource_dir = os.path.join(script_dir, "..", "resources", "base")
        return os.path.join(resource_dir, resource_path)

def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--linux-recorder":
        from linux_keystroke_recorder import linux_keystroke_recorder

        linux_keystroke_recorder()
    else:
        appctxt = VialApplicationContext()       # 1. Instantiate ApplicationContext
        
        # Force QApplication creation by accessing the app property
        _ = appctxt.app
        
        # Initialize themes after QApplication is created
        from themes import initialize_palettes
        initialize_palettes()
        
        init_logger()
        qt_exception_hook = UncaughtHook()
        window = MainWindow(appctxt)
        window.show()
        exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
        sys.exit(exit_code)

if __name__ == '__main__':
    main()
