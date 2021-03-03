import sys
import os
from interfaces.mainInterface import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class ResizeImage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_choose_file.clicked.connect(self.open_image)
        self.btn_resize_file.clicked.connect(self.resize_proportion)
        self.btn_save_file.clicked.connect(self.save_image)
        
        self.__default_path = os.path.expandvars("%userprofile%")

    
    def open_image(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            image, _ = QFileDialog.getOpenFileName(
                self,
                'Abrir imagem',
                self.__default_path,
                'Image Files(*.png *.jpg *.bmp)',
                options=options
            )
            if image:
                self.input_open_file.setText(image)
                self.original_image = QPixmap(image)
                self.label_img.setPixmap(self.original_image)
                self.set_scale_image(
                    self.original_image.width(),
                    self.original_image.height()
                )
                
        except Exception as err:
            print(err)
    
    def resize_proportion(self):
        new_width = int(self.input_width.text())
        self.new_image = self.original_image.scaledToWidth(new_width)
        self.label_img.setPixmap(self.new_image)
        self.set_scale_image(
            self.new_image.width(),
            self.new_image.height()
        )
 
    def set_scale_image(self, width, height):
        self.input_width.setText(str(width))
        self.input_height.setText(str(height))
    
    def save_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        image, _ = QFileDialog.getSaveFileName(
            self,
            'Salvar imagem',
            self.__default_path,
            'Image Files(*.png *.jpg *.bmp)',
            options=options
        )
        if image:
            self.new_image.save(image, 'PNG')
        else:
            print("Você não pode salvar a mesma imagem")


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    resizeImage = ResizeImage()
    resizeImage.show()
    qt.exec_()