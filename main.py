# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'odev.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDialog, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from IPython.display import display
from info import Ui_DataSetInfo
from islem import Ui_IslemPanel
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy import stats
import collections
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont

class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 80, 661, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.onaylaButton = QtWidgets.QPushButton(self.centralwidget)
        self.onaylaButton.setGeometry(QtCore.QRect(230, 380, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(10)
        self.onaylaButton.setFont(font)
        self.onaylaButton.setObjectName("onaylaButton")
        self.datasetInfo = QtWidgets.QPushButton(self.centralwidget)
        self.datasetInfo.setGeometry(QtCore.QRect(550, 400, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(10)
        self.datasetInfo.setFont(font)
        self.datasetInfo.setObjectName("datasetInfo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 350, 195, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 50, 230, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.browseButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(10)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(340, 320, 195, 117))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_2.addWidget(self.comboBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.onaylaButton.setText(_translate("MainWindow", "Onayla"))
        self.datasetInfo.setText(_translate("MainWindow", "Onayla"))
        self.label.setText(_translate("MainWindow", "İşlem Seçiniz"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ortalama"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Medyan"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Mod"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Frekans"))
        self.comboBox.setItemText(4, _translate("MainWindow", "IQR"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Aykırı Değerler"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Beş Sayı Özeti (Min,Q1,M,Q3,Max)"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Kutu Grafiği"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Varyans ve Standart Sapma"))
        self.browseButton.setText(_translate("MainWindow", "DataSet Seçiniz"))
        self.label_2.setText(_translate("MainWindow", "Eksik Veri Tamamlama"))
        self.label_3.setText(_translate("MainWindow", "Metod"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Ortalama"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Medyan"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Mod"))
        self.label_4.setText(_translate("MainWindow", "Column"))
        self.fileName_=""
        self.dataSet=""
        self.dataSetNotNanValues=""
        self.missingValuesArray=["n.a.","NA","n/a", "na","NaN", 0]
        self.browseButton.clicked.connect(self.openFileNameDialog)
        self.datasetInfo.clicked.connect(self.openInfo)
        self.onaylaButton.clicked.connect(self.onaylaButtonFunc)

    def openInfo(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_DataSetInfo()
        self.ui.setupUi(self.window)
        #islemler burada
        self.ui.dataSet_info.clear()
        self.dataSetNotNanValues=pd.read_csv(self.fileName_)
        index = self.comboBox_2.currentIndex()
        print(index)
        if index==0:
            self.dataSetNotNanValues[self.comboBox_3.currentText()].fillna(self.dataSetNotNanValues[self.comboBox_3.currentText()].mean(), inplace=True)
        elif index==1:
            self.dataSetNotNanValues[self.comboBox_3.currentText()].fillna(self.dataSetNotNanValues[self.comboBox_3.currentText()].median(), inplace=True)
        else:
            self.dataSetNotNanValues[self.comboBox_3.currentText()].fillna(self.dataSetNotNanValues[self.comboBox_3.currentText()].mode(), inplace=True)
        
        self.ui.dataSet_info.setText(self.dataSetNotNanValues.to_string(col_space =20,justify="justify"))
        self.window.show()

    def onaylaButtonFunc(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_IslemPanel()
        self.ui.setupUi(self.window)
        self.ui.islem_Label.setText(self.comboBox.currentText())
        font = QFont()
        font.setFamily(u"Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(20)
        font.setPointSize(13)
        
        self.ui.islem_textBrowser.setFont(font)
        #islemler
        index=self.comboBox.currentIndex()
        if index==0:
            #ortalama
            self.ortalamaHesapla()
        elif index==1:
            #medyan
            self.medyanHesapla()
        elif index==2:
            #mod
            self.modHesapla()
        elif index==3:
            #frekans
            self.frekansHesapla()
        elif index==4:
            #iqr
            self.IQRHesapla()
            #q75, q25 = np.percentile(self.dataSet[self.comboBox_3.currentText()], [75 ,25])
            #iqr = q75 - q25
        elif index==5:
            #aykiri degerler
            self.aykiriDegerler()
        elif index==6:
            #bes sayi ozeti
            self.besSayiOzeti()
        elif index==7:
            #kutu grafigi
            self.kutuGrafigi()
        else:
            self.varyansStSapma()


        self.window.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","(*) Csv Files (*.csv)", options=options)
        self.fileName_=fileName
        self.dataSet=pd.read_csv(fileName)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.textBrowser.setStyleSheet('color: blue')
        self.textBrowser.setText(self.dataSet.to_string(col_space =14,justify="justify"))
        self.comboBox_3.clear()
        for col in self.dataSet.columns:
            self.comboBox_3.addItem(str(col))
        print(self.dataSet.info())


        
    def ortalamaHesapla(self):
        bosDegersizVeriSeti=self.dataSet.dropna(subset=[self.comboBox_3.currentText()])
        col_one_arr = bosDegersizVeriSeti.to_numpy()
        j=0;
        count=0;
        for i in col_one_arr:
            j+=1
            count+=i[self.comboBox_3.currentIndex()]
        ortalama_sonuc=count/j
        print(count)
        print(j)
        print(ortalama_sonuc)

        self.ui.islem_textBrowser.setText(self.comboBox_3.currentText()+".Sutununun Ortalamasi:\n "+str(ortalama_sonuc))
    def medyanHesapla(self):
        k=0
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        vektor = sorted(col_one_arr)
        veriAdedi = len(col_one_arr)
        medyan=0
        if veriAdedi % 2 == 1:
            medyan=vektor[veriAdedi // 2]
            self.ui.islem_textBrowser.setText(self.comboBox_3.currentText()+".Sutununun Medyani:\n "+str(medyan))
        else:
            i = veriAdedi // 2
            medyan= (vektor[i - 1] + vektor[i]) / 2
            self.ui.islem_textBrowser.setText(self.comboBox_3.currentText()+".Sutununun Medyani:\n "+str(medyan))        
    def modHesapla(self):
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        mode = stats.mode(col_one_arr)
        self.ui.islem_textBrowser.setText(self.comboBox_3.currentText()+".Sutununun Modu:\n "+str(mode[0]))
    def frekansHesapla(self):
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].tolist()
        frequency = collections.Counter(col_one_arr)
        self.ui.islem_textBrowser.setText(str(dict(frequency)))
        plt.hist(self.dataSetNotNanValues[self.comboBox_3.currentText()], bins=np.arange(self.dataSetNotNanValues[self.comboBox_3.currentText()].min(), self.dataSetNotNanValues[self.comboBox_3.currentText()].max()+1)-0.5)
        plt.show()
    def IQRHesapla(self):
        k=0
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        for i in self.dataSetNotNanValues[self.comboBox_3.currentText()]:
            k+=1
        vektor = sorted(col_one_arr)
        z=int(k/4)
        y=int((k*3)/4)
        print(k)
        print(z)
        print(y)
        q3=vektor[y]
        q1=vektor[z]
        iqr=q3-q1
        self.ui.islem_textBrowser.setText(self.comboBox_3.currentText()+".Sutununun IQR Degeri:\n "+str(iqr))
    def aykiriDegerler(self):
        k=0
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        for i in self.dataSetNotNanValues[self.comboBox_3.currentText()]:
            k+=1
        vektor = sorted(col_one_arr)
        z=int(k/4)
        y=int((k*3)/4)
        q3=vektor[y]
        q1=vektor[z]
        iqr=q3-q1
        aykiridegerUst=q3+iqr*1.5
        aykiridegerAlt=q1-iqr*1.5
        array=[]
        for i in self.dataSetNotNanValues[self.comboBox_3.currentText()]:
            if i>aykiridegerUst or i<aykiridegerAlt:
                array.append(str(i))

        self.ui.islem_textBrowser.setText("Aykiri Deger Sinirlari: "+str(aykiridegerAlt)+" "+str(aykiridegerUst)+"\n"+str(array))
    def besSayiOzeti(self):
        k=0
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        for i in self.dataSetNotNanValues[self.comboBox_3.currentText()]:
            k+=1
        siralanmisVeriSeti = sorted(col_one_arr)
        z=int(k/4)
        y=int((k*3)/4)
        q3=siralanmisVeriSeti[y]
        q1=siralanmisVeriSeti[z]
        min=self.dataSetNotNanValues[self.comboBox_3.currentText()].min()    
        max=self.dataSetNotNanValues[self.comboBox_3.currentText()].max()

        self.ui.islem_textBrowser.setText(self.comboBox_3.currentText()+" Sutununun \nMinimum Degeri: "+str(min)+"\nQ1 Degeri: "+str(q1)+"\nQ3 Degeri: "+str(q3)+"\nMaksimum Degeri: "+str(max)) 
    def kutuGrafigi(self):
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        siralanmisVeriSeti = sorted(col_one_arr)
        fig = plt.figure(figsize =(10, 7))
 
        # Creating plot
        plt.boxplot(siralanmisVeriSeti)
 
        # show plot
        plt.show()
    def varyansStSapma(self):
        sd = 0.0 # standart sapma
        varyans=0.0 #varyans
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        vektor = sorted(col_one_arr)
        veriAdedi = len(vektor)
        if veriAdedi <= 1:
            sd=0.0
        else:
            for _ in vektor:
                sd += (float(_) - self.ortalamaBul()) ** 2
            sd = (sd / float(veriAdedi)) ** 0.5

        varyans=sd**2
        self.ui.islem_textBrowser.setText(self.comboBox_3.currentText()+" Sutununun \nVaryansı :"+str(varyans)+"\nStandart Sapması: "+str(sd))
    def ortalamaBul(self):
        col_one_arr = self.dataSetNotNanValues[self.comboBox_3.currentText()].to_numpy()
        vektor = sorted(col_one_arr)
        veriAdedi = len(vektor)
        if veriAdedi <= 1:
            return vektor
        else:
            return sum(vektor) / veriAdedi
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
