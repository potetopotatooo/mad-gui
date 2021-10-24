from pathlib import Path

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QFileDialog

from typing import Optional

def ask_for_file_name(base_dir: Path, parent=None, file_type="*.*") -> Optional[str]:
    data_file = QFileDialog(parent=parent).getOpenFileName(
        parent=None, caption="Select file to open", dir=str(base_dir), filter=file_type
    )[0]
    if data_file == "":
        # User clicked cancel
        return None
    return data_file


def ask_for_dir_name(base_dir: Path, parent=None) -> Optional[str]:
    dialog = QFileDialog(parent=parent)
    dialog.setFileMode(QFileDialog.Directory)
    data_dir = QFileDialog.getExistingDirectory(parent=None, caption="Select control/stress folder of subject to open",
                                                dir=str(base_dir))
    if data_dir == "":
        # User clicked cancel
        return None
    return data_dir


def set_cursor(window, cursor_type):
    window.setCursor(cursor_type)
    QCoreApplication.processEvents()  # On windows, we have to force GUI to update the cursor
