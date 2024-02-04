from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget, QFileDialog)
import os
from PyQt5.QtGui import QPixmap
from PIL import Image
app = QApplication([])
window = QWidget()
window.setWindowTitle('ImageEditor')
workdir = ''
def chooseWorkdir():
  global workdir #обращаемся к глобальной переменнуой
  workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
  result = []
  for filename in files:
    for ext in extensions:
      if filename.endswith(ext):
        result.append(filename)
  return result

def showFilenamesList():
  extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
  chooseWorkdir()
  filenames = filter(os.listdir(workdir), extensions)
  Files_lst.clear()
  for filename in filenames:
    Files_lst.addItem(filename)
Pic_lbl = QLabel('')
Left_btn = QPushButton('Лево')
Right_btn = QPushButton('Право')
Sharp_btn = QPushButton('Резкость')
Mirror_btn = QPushButton('Зеркало')
B_W_btn = QPushButton('Ч/Б')

Folder_btn = QPushButton('Папка')

Files_lst = QListWidget()

Layout_1 = QVBoxLayout()
Layout_2 = QHBoxLayout()
Layout_3 = QVBoxLayout()
Layout_4 = QHBoxLayout()

Layout_1.addWidget(Folder_btn)
Layout_1.addWidget(Files_lst)
Layout_2.addWidget(Left_btn)
Layout_2.addWidget(Right_btn)
Layout_2.addWidget(Sharp_btn)
Layout_2.addWidget(Mirror_btn)
Layout_2.addWidget(B_W_btn)
Layout_3.addWidget(Pic_lbl)
Layout_3.addLayout(Layout_2)
Layout_4.addLayout(Layout_1)
Layout_4.addLayout(Layout_3)

window.setLayout(Layout_4)
class ImageProcessor:
  def __init__(self, img =None, fname = None, subdir = 'Modified'):
    self.img = img
    self.fname = fname
    self.subdir = subdir
  def loadImage(self, filename):
    self.fname = filename
    image_path = os.path.join(workdir, filename)
    self.img = Image.open(image_path)
  def showImage(self, path):
    Pic_lbl.hide()
    pixmapimage = QPixmap(path)
    w, h = Pic_lbl.width(), Pic_lbl.height()
    pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
    Pic_lbl.setPixmap(pixmapimage)
    Pic_lbl.show()

def showChosenImage():
  if Files_lst.currentRow() >= 0:
    filename = Files_lst.currentItem().text()
    workimage.loadImage(filename)
    image_path = os.path.join(workdir, workimage.fname)
    workimage.showImage(image_path)
workimage = ImageProcessor() #текущая рабочая картинка для работы
Files_lst.currentRowChanged.connect(showChosenImage)
Folder_btn.clicked.connect(showFilenamesList)

window.show()
app.exec()