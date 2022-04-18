#!python3
# coding=utf8
"""
Project:七巧板
Author:42024130-宋加运
Date:2022.4.18
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QBrush, QPolygonF
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPolygonItem, QGraphicsItem, QApplication, \
    QGraphicsRectItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("E:\大二上学期课程资料\python程序设计\作业5\q7.ui", self)
        self.scene = QGraphicsScene(0, 0, 400, 400)
        self.graphicsView.setScene(self.scene)
        self.init_shapes()
        self.pushButton_6.clicked.connect(self.onRotateLeft)
        self.pushButton_7.clicked.connect(self.onRotateRight)
        self.pushButton_8.clicked.connect(self.onMoveUp)
        self.pushButton_4.clicked.connect(self.onMoveDown)
        self.pushButton_3.clicked.connect(self.onMoveLeft)
        self.pushButton_5.clicked.connect(self.onMoveRight)

    def init_shapes(self):
        i1 = QGraphicsPolygonItem(QPolygonF([QPointF(0, 0), QPointF(0, 400), QPointF(200, 200)]))
        i1.setBrush(QBrush(Qt.yellow))
        i1.setTransformOriginPoint(100, 200)
        i1.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        i2 = QGraphicsPolygonItem(QPolygonF([QPointF(200, 200), QPointF(0, 400), QPointF(400, 400)]))
        i2.setBrush(QBrush(Qt.blue))
        i2.setTransformOriginPoint(200, 300)
        i2.setPos(0, 0)
        i2.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        i3 = QGraphicsPolygonItem(QPolygonF([QPointF(0, 0), QPointF(200, 0), QPointF(300, 100), QPointF(100, 100)]))
        i3.setBrush(QBrush(Qt.darkBlue))
        i3.setTransformOriginPoint(150, 50)
        i3.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        i4 = QGraphicsPolygonItem(QPolygonF([QPointF(100, 100), QPointF(300, 100), QPointF(200, 200)]))
        i4.setBrush(QBrush(Qt.green))
        i4.setTransformOriginPoint(200, 150)
        i4.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        i5 = QGraphicsPolygonItem(
            QPolygonF([QPointF(200, 200), QPointF(300, 100), QPointF(400, 200), QPointF(300, 300)]))
        i5.setBrush(QBrush(Qt.cyan))
        i5.setTransformOriginPoint(300, 200)
        i5.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        i6 = QGraphicsPolygonItem(QPolygonF([QPointF(300, 300), QPointF(400, 200), QPointF(400, 400)]))
        i6.setBrush(QBrush(Qt.darkCyan))
        i6.setTransformOriginPoint(350, 300)
        i6.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        i7 = QGraphicsPolygonItem(QPolygonF([QPointF(200, 0), QPointF(400, 0), QPointF(400, 200)]))
        i7.setBrush(QBrush(Qt.red))
        i7.setTransformOriginPoint(300, 100)
        i7.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

        self.scene.addItem(i1)
        self.scene.addItem(i2)
        self.scene.addItem(i3)
        self.scene.addItem(i4)
        self.scene.addItem(i5)
        self.scene.addItem(i6)
        self.scene.addItem(i7)
        self.scene.addItem(i1)
        self.scene.addItem(i2)
        self.scene.addItem(i3)
        self.scene.addItem(i4)
        self.scene.addItem(i5)
        self.scene.addItem(i6)
        self.scene.addItem(i7)

    def onRotateLeft(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.setRotation(90 + item.rotation())

    def onRotateRight(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.setRotation(-90 + item.rotation())

    def onMoveUp(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.moveBy(0, -10)

    def onMoveDown(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.moveBy(0, 10)

    def onMoveLeft(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.moveBy(-10, 0)

    def onMoveRight(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.moveBy(10, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
