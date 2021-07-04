# This Python file uses the following encoding: utf-8
import cv2
import time
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

#"*.py"ファイルの読み込み
from ui_main1 import Ui_MainWindow


def main():
    # #変数の定義
    # videoPath: str = ""
    # playFps: int =  60#mm
    
    # ply=videoController(videoPath, playFps)
    # ply.videoPlayer()
    
    #GUI起動
    app = QtWidgets.QApplication(sys.argv)
    window = mainGui()
    window.show()
    
    #GUI終了
    sys.exit(app.exec_())
    
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
            self.ui.VideoPosition.setRange(1, self.ply.getVideoLength())
            self.ui.VideoLen.setText("/ " + str(self.ply.getVideoLength()))
            self.videoPlay()
            #self.ply.videoPlayer()
            
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
    def slot1_showFrame(self):
        print("This; "+str(self.ui.VideoPosition.value()))
        self.ply.ShowPosition(self.ui.VideoPosition.value())
        
    def videoPlay(self):
        #self.ply.__setVideoPosition()
        self.ply._videoController__setVideoPosition()
        #print("FPS:" + str(self.__initialFps))
    
        #映像の表示
        if self.ply._videoController__srcVideo.isOpened():
            #1フレーム目の読み込み
            retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.read()
            #すべて読み込むまでループ
            while True:
                if retval:
                    cv2.imshow(self.ply._videoController__videoWindow, self.ply._videoController__srcFrame)
                    #現在のフレームを取得
                    self.ply._videoController__curFrame = int(self.ply._videoController__srcVideo.get(cv2.CAP_PROP_POS_FRAMES))
                    self.videoStatus = "Frame: " + str(self.ply._videoController__curFrame) + " / " + str(self.ply._videoController__videoLength) + ", FPS:" + str(self.ply._videoController__initialFps)
                    #現在のフレームの位置を表示
                    self.ui.VideoPosition.setValue(self.ply._videoController__curFrame)
                    self.ply._videoController__pressedKey = self.ply._videoController__waitInput()
                else:
                    #最終フレームでの動作
                    self.ply._videoController__curFrame = self.ply._videoController__videoLength
                    self.ply._videoController__setVideoPosition()
                    self.ply._videoController__srcVideo.grab()
                    retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.retrieve()
                    cv2.imshow(self.ply._videoController__videoWindow, self.ply._videoController__srcFrame)
                    self.ply._videoController__pressedKey = self.ply._videoController__waitInput()
                if self.ply._videoController__pressedKey & 0xFF == ord('q'):
                    #Qキーを押すと終了
                    break
                if self.ply._videoController__pressedKey == 8:
                    #バックスペースを押されたとき再生方向を逆転する
                    self.ply._videoController__playBackword = self.switchParaBool(self.ply._videoController__playBackword)
                    continue
                if self.ply._videoController__pressedKey == 32:
                    #スペースキーを押されたとき
                    self.ply._videoController__poseFrame = self.switchParaBool(self.ply._videoController__poseFrame)
                    self.ply._videoController__waitImp = self.switchParaBool(self.ply._videoController__waitImp)
                    continue
                
                if self.ply._videoController__poseFrame:#__frameByFrame:
                    if not self.ply._videoController__playBackword: #バックスペースを押されてないとき
                        #次のフレーム読み込み
                        if self.ply._videoController__pressedKey == 2555904: #右十字キー
                            self.ply._videoController__srcVideo.grab()
                            retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.retrieve()
                        elif self.ply._videoController__pressedKey == 2424832: #左十字キー
                            #一旦リリースしてから動画を再読み込み
                            self.ply._videoController__srcVideo.release()
                            self.ply._videoController__srcVideo = cv2.VideoCapture(self.ply._videoController__videoPath)
                            #前のフレームの読み込み
                            self.ply._videoController__curFrame -= 1
                            self.ply._videoController__setVideoPosition()
                            self.ply._videoController__srcVideo.grab()
                            retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.retrieve()
                        else:
                            continue
                            
                    else:
                        #次のフレーム読み込み
                        if self.ply._videoController__pressedKey == 2555904: #右十字キー
                            self.ply._videoController__srcVideo.grab()
                            retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.retrieve()
                        elif self.ply._videoController__pressedKey == 2424832: #左十字キー
                            #一旦リリースしてから動画を再読み込み
                            self.ply._videoController__srcVideo.release()
                            self.ply._videoController__srcVideo = cv2.VideoCapture(self.ply._videoController__videoPath)
                            #前のフレームの読み込み
                            self.ply._videoController__curFrame -= 1
                            self.ply._videoController__setVideoPosition()
                            self.ply._videoController__srcVideo.grab()
                            retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.retrieve()
                        else:
                            continue
                else:
                    #通常再生モード
                    if not self.ply._videoController__playBackword: #バックスペースを押されてないとき
                        #次のフレーム読み込み
                        self.ply._videoController__srcVideo.grab()
                        retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.retrieve()
                    else:
                        #バックスペースを押されたとき
                        #一旦リリースしてから動画を再読み込み
                        self.ply._videoController__srcVideo.release()
                        self.ply._videoController__srcVideo = cv2.VideoCapture(self.ply._videoController__videoPath)
                        #前のフレームの読み込み
                        self.ply._videoController__curFrame -= 1
                        self.ply._videoController__setVideoPosition()
                        self.ply._videoController__srcVideo.grab()
                        retval, self.ply._videoController__srcFrame = self.ply._videoController__srcVideo.retrieve()
                                            
            cv2.destroyAllWindows()
        #映像型の開放
        self.ply._videoController__srcVideo.release()
        

    
class videoController:
    def __init__(self, videoPath: str, playFps: int, startPos: int = 1):
        #videoPath: 読み込むビデオのパス, playFps: 再生する速度（FPS）, startPos: 読み込み開始位置
        #変数の設定1
        self.__videoPath: str = videoPath          #動画のパス
        self.__curFrame: int = startPos            #動画読み込み開始位置
        self.__delay: int = int(1000/playFps)      #読み込みの間隔（ms）
        self.__retval: bool                        #フレームが読み込まれているか
        self.__srcFrame: cv2.Mat                   #オリジナルのフレーム
        self.__pressedKey: int                     #キーコード
        self.__playBackword: bool = False          #逆方向に再生するか
        self.__poseFrame: bool = True              #再生を一時停止するか#コマ送り再生するか
        self.__videoWindow: str = "video" + str(1) #ウィンドウ名の指定
        self.__waitImp: bool = True                #入力待ち
        self.__waitTime: float = 1000/playFps      #入力待ち時間
        self.videoStatus: str = "Frame: 0 / 0, FPS: 0" #GUIに表示する文字
        #ビデオ読み込み
        self.__srcVideo: cv2.VideoCapture = cv2.VideoCapture(self.__videoPath)
        #ビデオの初期値を取得
        self.__initialFps: int = int(self.__srcVideo.get(cv2.CAP_PROP_FPS)) #FPS
        self.__videoLength: int  = int(self.__srcVideo.get(cv2.CAP_PROP_FRAME_COUNT)) #フレームの長さ
        
        #ウィンドウの生成
        cv2.namedWindow(self.__videoWindow,cv2.WINDOW_KEEPRATIO)
        
        
    def getVideoLength(self):
        return self.__videoLength
    
    
    def __setVideoPosition(self):
        #ビデオの再生開始位置を指定
        self.__srcVideo.set(cv2.CAP_PROP_POS_FRAMES, self.__curFrame-1)
    
    def switchParaBool(self, parameter: bool):
        if parameter:
            return False
        else:
            return True
        
    #waitKeyの代わりの関数    
    def __waitInput(self):
        if(self.__waitImp):
            self.__poseFrame = True
            while(True):
                inp: int = cv2.waitKeyEx(self.__delay)
                if inp != (-1) or not(self.__poseFrame):
                    break
        else:
            inp: int = cv2.waitKeyEx(self.__delay)
        return inp
    
    #動画の順再生を開始    
    def playVideo(self):
        self.__poseFrame = False
        self.__waitImp = False
        self.__playBackword = False
    #動画の逆再生を開始    
    def playVideoBack(self):
        self.__poseFrame = False
        self.__waitImp = False
        self.__playBackword = True
    #動画を一時停止    
    def paseVideo(self):
        self.__poseFrame = True
        self.__waitImp = True

    #動画の順方向コマ送り再生を開始    
    def VideoNextFrame(self):
        self.__poseFrame = False
        self.__waitImp = True
        self.__playBackword = False
        self.__pressedKey = 2555904

    #動画の逆方向コマ送り再生を開始    
    def VideoBeforeFrame(self):
        self.__poseFrame = False
        self.__waitImp = True
        self.__playBackword = True
        self.__pressedKey = 2424832
        
    def ShowPosition(self, Position: int):
        #一旦リリースしてから動画を再読み込み
        self.__srcVideo.release()
        self.__srcVideo = cv2.VideoCapture(self.__videoPath)
        #指定のフレームの読み込み
        self.__curFrame = Position
        self.__setVideoPosition()
        self.__srcVideo.grab()
        retval, self.__srcFrame = self.__srcVideo.retrieve()
        
    #Playerの起動    
    def videoPlayer(self):
        self.__setVideoPosition()
        #print("FPS:" + str(self.__initialFps))
    
        #映像の表示
        if self.__srcVideo.isOpened():
            #1フレーム目の読み込み
            retval, self.__srcFrame = self.__srcVideo.read()
            #すべて読み込むまでループ
            while True:
                if retval:
                    cv2.imshow(self.__videoWindow, self.__srcFrame)
                    #現在のフレームを取得
                    self.__curFrame = int(self.__srcVideo.get(cv2.CAP_PROP_POS_FRAMES))
                    print("Frame: " + str(self.__curFrame) + " / " + str(self.__videoLength) + ", FPS:" + str(self.__initialFps))
                    self.__pressedKey = self.__waitInput()#cv2.waitKeyEx(self.__delay)
                    
                    #スペースキーもしくはコマ送りモードで一時停止
                    # if self.__poseFrame:# or self.__frameByFrame:
                    #     self.__pressedKey = self.__waitInput()#cv2.waitKeyEx(0)
                else:
                    #最終フレームでの動作
                    self.__curFrame = self.__videoLength
                    self.__setVideoPosition()
                    self.__srcVideo.grab()
                    retval, self.__srcFrame = self.__srcVideo.retrieve()
                    cv2.imshow(self.__videoWindow, self.__srcFrame)
                    self.__pressedKey = self.__waitInput()#cv2.waitKeyEx(0) 
                if self.__pressedKey & 0xFF == ord('q'):
                    #Qキーを押すと終了
                    break
                if self.__pressedKey == 8:
                    #バックスペースを押されたとき再生方向を逆転する
                    self.__playBackword = self.switchParaBool(self.__playBackword)
                    continue
                if self.__pressedKey == 32:
                    #スペースキーを押されたとき
                    self.__poseFrame = self.switchParaBool(self.__poseFrame)
                    self.__waitImp = self.switchParaBool(self.__waitImp)
                    continue
                
                if self.__poseFrame:#__frameByFrame:
                    if not self.__playBackword: #バックスペースを押されてないとき
                        #次のフレーム読み込み
                        if self.__pressedKey == 2555904: #右十字キー
                            self.__srcVideo.grab()
                            retval, self.__srcFrame = self.__srcVideo.retrieve()
                        elif self.__pressedKey == 2424832: #左十字キー
                            #一旦リリースしてから動画を再読み込み
                            self.__srcVideo.release()
                            self.__srcVideo = cv2.VideoCapture(self.__videoPath)
                            #前のフレームの読み込み
                            self.__curFrame -= 1
                            self.__setVideoPosition()
                            self.__srcVideo.grab()
                            retval, self.__srcFrame = self.__srcVideo.retrieve()
                        else:
                            continue
                            
                    else:
                        #次のフレーム読み込み
                        if self.__pressedKey == 2555904: #右十字キー
                            self.__srcVideo.grab()
                            retval, self.__srcFrame = self.__srcVideo.retrieve()
                        elif self.__pressedKey == 2424832: #左十字キー
                            #一旦リリースしてから動画を再読み込み
                            self.__srcVideo.release()
                            self.__srcVideo = cv2.VideoCapture(self.__videoPath)
                            #前のフレームの読み込み
                            self.__curFrame -= 1
                            self.__setVideoPosition()
                            self.__srcVideo.grab()
                            retval, self.__srcFrame = self.__srcVideo.retrieve()
                        else:
                            continue
                else:
                    #通常再生モード
                    if not self.__playBackword: #バックスペースを押されてないとき
                        #次のフレーム読み込み
                        self.__srcVideo.grab()
                        retval, self.__srcFrame = self.__srcVideo.retrieve()
                    else:
                        #バックスペースを押されたとき
                        #一旦リリースしてから動画を再読み込み
                        self.__srcVideo.release()
                        self.__srcVideo = cv2.VideoCapture(self.__videoPath)
                        #前のフレームの読み込み
                        self.__curFrame -= 1
                        self.__setVideoPosition()
                        self.__srcVideo.grab()
                        retval, self.__srcFrame = self.__srcVideo.retrieve()
                                            
            cv2.destroyAllWindows()
        #映像型の開放
        self.__srcVideo.release()
    
#矢印キーASCIIコード
#Upkey : 2490368
#DownKey : 2621440
#LeftKey : 2424832
#RightKey: 2555904
#Space : 32
#Delete : 3014656

if __name__ == "__main__":
    main()
