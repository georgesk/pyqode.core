import logging
from pyqode.core.api.mode import Mode
from pyqode.core.qt import QtWidgets, QtGui


def _logger():
    """ Returns module's logger """
    return logging.getLogger(__name__)


class Panel(QtWidgets.QWidget, Mode):
    """
    Base class for editor panels.

    A panel is a mode and a QWidget.

    .. note:: Use enabled to disable panel actions and setVisible to change the
        visiblity of the panel.
    """
    class Position:  # pylint: disable=no-init, too-few-public-methods
        """
        Enumerates the possible panel positions
        """
        #: Top margin
        TOP = 0
        #: Left margin
        LEFT = 1
        #: Right margin
        RIGHT = 2
        #: Bottom margin
        BOTTOM = 3

        @classmethod
        def iterable(cls):
            """ Returns possible positions as an iterable (list) """
            return [cls.TOP, cls.LEFT, cls.RIGHT, cls.BOTTOM]

    @property
    def scrollable(self):
        """
        A scrollable panel will follow the editor's scroll-bars. Left and right
        panels follow the vertical scrollbar. Top and bottom panels follow the
        horizontal scrollbar.

        :type: bool
        """
        return self._scrollable

    @scrollable.setter
    def scrollable(self, value):
        # pylint: disable=missing-docstring
        self._scrollable = value

    def __init__(self):
        Mode.__init__(self)
        QtWidgets.QWidget.__init__(self)
        #: Panel order into the zone it is installed to. This value is
        #: automatically set when installing the panel but it can be changed
        #: later (negative values can also be used).
        self.order_in_zone = -1
        self._scrollable = False
        self._background_brush = None
        self._foreground_pen = None
        #: Position in the editor (top, left, right, bottom)
        self.position = -1

    def on_install(self, editor):
        """
        Extends :meth:`pyqode.core.api.Mode.on_install` method to set the
        editor instance as the parent widget.

        .. warning:: Don't forget to call **super** if you override this
            method!

        :param editor: editor instance
        :type editor: pyqode.core.api.CodeEdit
        """
        Mode.on_install(self, editor)
        self.setParent(editor)
        self.setPalette(QtWidgets.QApplication.instance().palette())
        self.setFont(QtWidgets.QApplication.instance().font())
        self.editor.panels.refresh()
        self._background_brush = QtGui.QBrush(QtGui.QColor(
            self.palette().window().color()))
        self._foreground_pen = QtGui.QPen(QtGui.QColor(
            self.palette().windowText().color()))

    def paintEvent(self, event):
        """ Fills the panel background. """
        # pylint: disable=invalid-name
        if self.isVisible():
            # fill background
            self._background_brush = QtGui.QBrush(QtGui.QColor(
                self.palette().window().color()))
            self._foreground_pen = QtGui.QPen(QtGui.QColor(
                self.palette().windowText().color()))
            painter = QtGui.QPainter(self)
            painter.fillRect(event.rect(), self._background_brush)

    def setVisible(self, visible):
        """
        Shows/Hides the panel

        Automatically call CodeEdit.refresh_panels.
        """
        # pylint: disable=invalid-name
        _logger().debug('%s visibility changed', self.name)
        super().setVisible(visible)
        if self.editor:
            self.editor.panels.refresh()
