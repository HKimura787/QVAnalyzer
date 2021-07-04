# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

#"*.py"ファイルの読み込み
from ui_main1 import Ui_MainWindow
from videoControl import videoController

#メイン関数
def main():
    
    #GUI起動
    app = QtWidgets.QApplication(sys.argv)
    window = mainGui()
    window.show()
    
    #GUI終了
    sys.exit(app.exec_())
    
#GUI部分
#QT参考http://dorafop.my.coocan.jp/Qt/Qt006.html
class mainGui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(mainGui, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #追加モジュールの読み込み
        self.ply: videoController
    
    #slotにリンクする関数
    #ファイルを開いてビデオ再生
    def slot1_OpenFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/', 'Video files (*.avi *.mp4 *.wmv *.mov)')
        #ビデオのコントロール
        if len(fname[0])!=0:
            self.ply=videoController(fname[0], playFps = 60)
            self.ui.VideoPosition.setRange(0, self.ply.getVideoLength())
            self.ply.videoPlayer()
            
            
    def slot1_PlayVideo(self):
        self.ply.playVideo()
    def slot1_pauseVideo(self):
        self.ply.paseVideo()
    def slot1_PlayBack(self):
        self.ply.playVideoBack()
    def slot1_gobackFrame(self):
        self.ply.VideoBeforeFrame()
    def slot1_goNextFrame(self):
        self.ply.VideoNextFrame()
        
            

if __name__ == "__main__":
    main()