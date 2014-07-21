"""
Tests the code completion mode
"""
import functools
from pyqode.core.qt import QtCore, QtWidgets
from pyqode.core.qt.QtTest import QTest
from pyqode.core.api import TextHelper
from pyqode.core import modes

from ..helpers import cwd_at, server_path, wait_for_connected
from ..helpers import preserve_editor_config


def get_mode(editor):
    return editor.modes.get(modes.CodeCompletionMode)


def ensure_visible(func):
    """
    Ensures the frontend is connect is connected to the server. If that is not
    the case, the code completion server is started automatically
    """
    @functools.wraps(func)
    @cwd_at('test')
    def wrapper(editor, *args, **kwds):
        QtWidgets.QApplication.setActiveWindow(editor)
        editor.setFocus(True)
        editor.setReadOnly(False)
        return func(editor, *args, **kwds)
    return wrapper


code = '''"""
Empty module
"""
'''


def ensure_empty(func):
    @functools.wraps(func)
    @cwd_at('test')
    def wrapper(editor, *args, **kwds):
        editor.file._path = None
        editor.setPlainText(code, 'text/x-python', 'utf-8')
        return func(editor, *args, **kwds)
    return wrapper


def ensure_connected(func):
    """
    Ensures the frontend is connect is connected to the server. If that is not
    the case, the code completion server is started automatically
    """
    @functools.wraps(func)
    @cwd_at('test')
    def wrapper(editor, *args, **kwds):
        if not editor.backend.connected:
            editor.backend.start(server_path())
            wait_for_connected(editor)
        return func(editor, *args, **kwds)
    return wrapper


@ensure_empty
@ensure_visible
@ensure_connected
def test_enabled(editor):
    mode = get_mode(editor)
    assert mode.enabled
    mode.enabled = False
    mode.enabled = True


@ensure_empty
@ensure_visible
@ensure_connected
def test_properties(editor):
    mode = get_mode(editor)
    mode.trigger_key = 'A'
    assert mode.trigger_key == 'A'
    mode.trigger_length = 3
    assert mode.trigger_length == 3
    mode.trigger_symbols = ['.', '->']
    assert len(mode.trigger_symbols) == 2
    assert '.' in mode.trigger_symbols
    assert '->' in mode.trigger_symbols
    mode.show_tooltips = False
    assert mode.show_tooltips is False
    mode.case_sensitive = True
    assert mode.case_sensitive is True
    mode.trigger_key = 1


@ensure_empty
@ensure_visible
@ensure_connected
@preserve_editor_config
def test_request_completion(editor):
    mode = get_mode(editor)
    QTest.qWait(1000)
    if editor.backend.connected:
        editor.backend.stop()
    # request a completion at start of the document, this request will be
    # skipped because we are in a comment/docstring zone.
    assert mode.request_completion() is False
    TextHelper(editor).goto_line(4)
    QTest.qWait(100)
    assert mode.request_completion() is True
    # starts the server after the request to test the retry on NotConnected
    # mechanism
    editor.backend.start(server_path())
    QTest.qWait(2000)
    # only the first request should be accepted
    ret1 = mode.request_completion()
    ret2 = mode.request_completion()
    assert ret1 is True and ret2 is False


@ensure_visible
@ensure_empty
@ensure_connected
@preserve_editor_config
def test_events(editor):
    assert editor.backend.connected
    QTest.qWait(1000)
    TextHelper(editor).goto_line(4)
    QTest.keyPress(editor, QtCore.Qt.Key_Space, QtCore.Qt.ControlModifier)
    QTest.qWait(2000)
    QTest.keyPress(editor, QtCore.Qt.Key_Escape)
    QTest.qWait(500)
    QTest.keyPress(editor, 'm')
    QTest.keyPress(editor, 'o')
    QTest.qWait(1000)
    QTest.keyPress(editor, QtCore.Qt.Key_Escape)
    QTest.keyPress(editor, ' ')
    QTest.keyPress(editor, 'm')
    QTest.keyPress(editor, 'o')
    QTest.keyPress(editor, 'd')
    QTest.qWait(10)
    QTest.keyPress(editor, ' ')
    QTest.qWait(500)
    QTest.keyPress(editor, 'e')
    QTest.keyPress(editor, 'n')
    QTest.keyPress(editor, 'a')
    QTest.keyPress(editor, 'b')
    QTest.keyPress(editor, 'l')
    QTest.keyPress(editor, 'e')
    QTest.keyPress(editor, 'd')
    QTest.qWait(500)

    QTest.keyPress(editor, ' ')
    QTest.keyPress(editor, 'Q')
    QTest.keyPress(editor, 't')
    QTest.keyPress(editor, '.')
    QTest.qWait(500)

    QTest.keyPress(editor, 'Q')
    QTest.keyPress(editor, 't')
    QTest.qWait(500)
    QTest.keyPress(editor, QtCore.Qt.Key_Space, QtCore.Qt.ControlModifier)


@ensure_empty
@ensure_visible
@ensure_connected
def test_insert_completions(editor):
    assert editor.backend.connected
    TextHelper(editor).goto_line(4)
    # check insert completions
    QTest.keyPress(editor, 'm')
    QTest.keyPress(editor, 'o')
    QTest.qWait(500)
    QTest.keyPress(editor, QtCore.Qt.Key_Return)

    # feature request #126: Key_Tab should select a completion
    QTest.keyPress(editor, QtCore.Qt.Key_Return)
    QTest.keyPress(editor, 'Q')
    QTest.keyPress(editor, 'T')
    QTest.keyPress(editor, 'e')
    QTest.keyPress(editor, 's')
    QTest.qWait(500)
    QTest.keyPress(editor, 't')

    QTest.qWait(100)


@ensure_empty
@ensure_connected
def test_show_completion_with_tooltip(editor):
    mode = get_mode(editor)
    mode.show_tooltips = True
    mode._show_completions([{'name': 'test', 'tooltip': 'test desc'}])
    mode._display_completion_tooltip('test')
    mode._display_completion_tooltip('spam')
    mode.show_tooltips = False
    mode._display_completion_tooltip('test')


@ensure_empty
@ensure_connected
def test_show_completion_with_icon(editor):
    mode = get_mode(editor)
    mode._show_completions([{'name': 'test',
                             'icon': ':/pyqode-icons/rc/edit-undo.png'}])
