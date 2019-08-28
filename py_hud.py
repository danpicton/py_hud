import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyle, qApp, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

# from PyQt5.QtWidgets import

html = '''
<html>
<head>
<title>A Sample Page</title>
</head>
<h1>Hello, World!</h1>
<hr />
I have nothing to say.
</body>
</html>
'''


class myWebView(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        # self.load(image)
        self.setHtml(html)
        self.setWindowOpacity(0.7)
        radius = 10.0
        path = QtGui.QPainterPath()
        self.resize(640, 480)
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.move(QtGui.QCursor.pos())
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint
            # | QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
            QtCore.QSize(640, 480),
            qApp.desktop().availableGeometry())
        )
        self.setStyleSheet('QWebView{background-color: darkgray; border: 5px solid darkgray}')
        self.grabMouse()
        self.grabKeyboard()
        print(self.keyboardGrabber())

    def mousePressEvent(self, event):
        # qApp.quit()
        self.close()
        # print("click")

    def keyPressEvent(self, e):
        # print("hello")
        if e.key() == Qt.Key_Escape:
            self.close()


app = QApplication(sys.argv)
browser = myWebView()

browser.show()
# app.exec_()
sys.exit(app.exec_())
