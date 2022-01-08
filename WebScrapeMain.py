# packages (only import necessary)
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QWidget
import sys
import random

# random greeting list > can add only later but will need to change rage of rand_greeting
greeting_list = ["Welcome to Web Scrape GUI", "Gratam Web Scrape GUI", "Benvenuto nella GUI di Web Scrape",
                 "Byenveni nan Web Scrape GUI", "Bienvenido a Web Scrape GUI"]


def popUP(title, text, QMessageBox_icon_):
    popup = QMessageBox()
    popup.setWindowTitle(title)
    popup.setText(text)
    popup.setIcon(QMessageBox_icon_)
    show = popup.exec_()


class WebScrapeGUI(QMainWindow):
    def __init__(self):
        super(WebScrapeGUI, self).__init__()
        loadUi("web_scrape_main_page.ui", self)
        rand_greeting = str(greeting_list[random.randint(0, 4)])
        self.welcomeLabel.setText(rand_greeting)

        self.submit.clicked.connect(self.search)
        self.sub = helpPopUp()
        self.howToUse.clicked.connect(self.sub.show)


        self.tableWidget.setColumnWidth(0, 550)
        self.tableWidget.setColumnWidth(1, 99)

    # import functions sheet here to that it doesn't open on start
    def search(self):
        import WebScrapeFunctions as w
        store = self.comboBox.currentText()
        item = self.item.text()

        if store == "Best Buy":
            results = w.bestbuy(item)
            self.loadData(results)
        elif store == "Amazon":
            results = w.amazon(item)
            self.loadData(results)

    def loadData(self, items):
        row = 0
        self.tableWidget.setRowCount(len(items))
        for i in items:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            row += 1
        popUP("Results Loaded",
              "The results have successfully loaded",
              QMessageBox.Information)


class helpPopUp(QWidget):
    def __init__(self):
        super(helpPopUp, self).__init__()
        loadUi("help_page.ui", self)
        self.setWindowTitle("Help Page")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    page = WebScrapeGUI()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(page)
    widget.setFixedHeight(900)
    widget.setFixedWidth(1381)
    widget.setWindowTitle("Web Scrapper")
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Application Closing")
