import PyQt5.QtWidgets as pq5
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIntValidator, QPixmap

from main import Datenbank

class GUI(pq5.QMainWindow):
    def __init__(self, Chemie, Mathe, Physik, fach, table):
        super(GUI, self).__init__()
        uic.loadUi("untitled.ui", self)

        self.Chemie = Chemie
        self.Mathe = Mathe
        self.Physik = Physik
        self.fach = fach
        self.table = table

        self.label_Logo.setPixmap(QPixmap("logo.png"))
        self.label_Logo.setScaledContents(True)

        self.lineEdit_id.setValidator(QIntValidator())

        self.btn_safe.clicked.connect(lambda: self.addStuff(self.textEdit.toPlainText(), self.textEdit_A.toPlainText(), self.textEdit_B.toPlainText(), self.textEdit_C.toPlainText(), self.textEdit_D.toPlainText()))
        self.btn_show.clicked.connect(lambda: self.showStuff(self.lineEdit_id.text()))
        self.btn_change.clicked.connect(lambda: self.changeStuff(self.textEdit.toPlainText(), self.textEdit_A.toPlainText(), self.textEdit_B.toPlainText(), self.textEdit_C.toPlainText(), self.textEdit_D.toPlainText(), self.lineEdit_id.text()))
        self.btn_del.clicked.connect(lambda: self.delStuff(self.lineEdit_id.text()))
        self.action_Mathe.triggered.connect(lambda: self.changeDb('Mathe'))
        self.action_Physik.triggered.connect(lambda: self.changeDb('Physik'))
        self.action_Chemie.triggered.connect(lambda: self.changeDb('Chemie'))

        self.showAll()
    
    def changeDb(self, str):
        if str == 'Mathe':
            self.fach = self.Mathe
            self.table = fach.showMain()
            self.label_Fach.setText('Mathe')
        elif str == 'Physik':
            self.fach = self.Physik
            self.table = fach.showMain()
            self.label_Fach.setText('Physik')
        elif str == 'Chemie':
            self.fach = self.Chemie
            self.table = fach.showMain()
            self.label_Fach.setText('Chemie')
        self.showAll()

    def showAll(self):
        self.table = self.fach.showMain()
        self.tableWidget.clear()
        columns = ['id','Frage','Antwort A','Antwort B','Antwort C','Antwort D']
        self.tableWidget.setHorizontalHeaderLabels(columns)
        for row in enumerate(self.table):
            self.tableWidget.insertRow(row[0])
            for col in enumerate(row[1]):
                self.tableWidget.setItem(row[0], col[0], QtWidgets.QTableWidgetItem(str(self.table[row[0]][col[0]])))

    def addStuff(self, frage, antwort_a, antwort_b, antwort_c, antwort_d):
        self.fach.inMain(frage, antwort_a, antwort_b, antwort_c, antwort_d)
        self.showAll()
    
    def showStuff(self, id):
        try:
            for row in self.table:
                if row[0]==int(id):
                    index=self.table.index(row)
                    self.textEdit.setText(self.table[index][1])
                    self.textEdit_A.setText(self.table[index][2])
                    self.textEdit_B.setText(self.table[index][3])
                    self.textEdit_C.setText(self.table[index][4])
                    self.textEdit_D.setText(self.table[index][5])
        except:
            print('bitte ID eingeben')
    
    def changeStuff(self, frage, antwort_a, antwort_b, antwort_c, antwort_d, id):
        try:
            self.fach.upMain(frage, antwort_a, antwort_b, antwort_c, antwort_d, int(id))
            self.showAll()
        except:
            print('bitte ID eingeben')

    def delStuff(self, id):
        try:
            self.fach.delMain(f'{int(id)}')
            self.clearAll()
            self.showAll()
        except:
            print('bitte ID eingeben')
    
    def clearAll(self):
        self.textEdit.setText('')
        self.textEdit_A.setText('')
        self.textEdit_B.setText('')
        self.textEdit_C.setText('')
        self.textEdit_D.setText('')
        self.lineEdit_id.setText('')

Chemie = Datenbank("Chemie.db")
Mathe = Datenbank("Mathe.db")
Physik = Datenbank("Physik.db")
Chemie.ctMain()
Mathe.ctMain()
Physik.ctMain()

fach = Chemie
table = fach.showMain()

def main():
    app = pq5.QApplication([])
    window = GUI(Chemie, Mathe, Physik, fach, table)
    window.show()       
    app.exec_()         

if __name__ == '__main__':
    main()