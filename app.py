import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebView - Google")

        # Configurando o layout
        self.browser = QWebEngineView()
        self.browser.setUrl("https://www.google.com")

        # Adicionando o WebView à janela principal
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebView()
    window.show()
    sys.exit(app.exec_())
