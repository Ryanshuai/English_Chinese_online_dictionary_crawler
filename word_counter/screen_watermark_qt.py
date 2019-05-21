import sys
from PyQt5 import QtWidgets,QtCore

class SigSlot(QtWidgets.QWidget):#继承自父类QtWidgets.QMainWindow
    def __init__(self,parent=None):#parent = None代表此QWidget属于最上层的窗口,也就是MainWindows.
        super(SigSlot, self).__init__()#因为继承关系，要对父类初始化
#通过super初始化父类，__init__()函数无self，若直接QtWidgets.QMainWindow).__init__(self)，括号里是有self的

        self.setWindowTitle(u'')  # 仅仅设置窗体标题，不设置位置。
        self.lcd=QtWidgets.QLCDNumber(self)#创建LCD数字显示栏
        self.lcd.setStyleSheet("border: 0px solid black; color: black; background: transparent;")

        vbox = QtWidgets.QVBoxLayout()  # 垂直布局
        vbox.addWidget(self.lcd)#将lcd数字显示控件放入vbox垂直布局中
        self.setLayout(vbox)  # 对整个窗口实现垂直布局
        self.resize(300,200)

    def refresh(self, num):
        self.lcd.display(num)



app=QtWidgets.QApplication(sys.argv)
window=SigSlot()
window.show()
window.refresh(55)
sys.exit(app.exec_())
window.refresh(33)