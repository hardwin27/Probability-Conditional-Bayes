import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from Probably import Ui_MainWindow as MainUi

class App(QtWidgets.QMainWindow, MainUi):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        self.probability_combo_asked_param.currentIndexChanged.connect(self.prob_combo_asked_param_changed)
        self.conditional_combo_asked_param.currentIndexChanged.connect(self.cond_combo_asked_param_changed)
        self.bayes_combo_asked_param.currentIndexChanged.connect(self.bay_combo_asked_param_changed)

        self.btn_calc_probability.clicked.connect(self.calculate_prob)
        self.btn_calc_conditional.clicked.connect(self.calculate_cond)
        self.btn_calc_bayes.clicked.connect(self.calculate_bay)

    def prob_combo_asked_param_changed(self, index):
        if index == 1:
            self.lbl_param_1_probability.setText("Number of A")
            self.lbl_param_2_probability.setText("Total Outcomes")
        elif index == 2:
            self.lbl_param_1_probability.setText("P(A)")
            self.lbl_param_2_probability.setText("Total Outcomes")
        elif index == 3:
            self.lbl_param_1_probability.setText("Number of A")
            self.lbl_param_2_probability.setText("P(A)")

    def cond_combo_asked_param_changed(self, index):
        if index == 1:
            self.lbl_param_1_conditional.setText("P(A ∩ B)")
            self.lbl_param_2_conditional.setText("P(B)")
        elif index == 2:
            self.lbl_param_1_conditional.setText("P(A|B)")
            self.lbl_param_2_conditional.setText("P(B)")
        elif index == 3:
            self.lbl_param_1_conditional.setText("P(A ∩ B)")
            self.lbl_param_2_conditional.setText("P(A|B)")

    def bay_combo_asked_param_changed(self, index):
        if index == 0:
            self.lbl_param_1_bayes.setText("-")
            self.lbl_param_2_bayes.setText("-")
            self.lbl_param_3_bayes.setText("-")
        elif index == 1:
            self.lbl_param_1_bayes.setText("P(B)")
            self.lbl_param_2_bayes.setText("P(A|B)")
            self.lbl_param_3_bayes.setText("P(B|A)")
        elif index == 2:
            self.lbl_param_1_bayes.setText("P(A)")
            self.lbl_param_2_bayes.setText("P(A|B)")
            self.lbl_param_3_bayes.setText("P(B|A)")
        elif index == 3:
            self.lbl_param_1_bayes.setText("P(A)")
            self.lbl_param_2_bayes.setText("P(B)")
            self.lbl_param_3_bayes.setText("P(B|A)")
        elif index == 4:
            self.lbl_param_1_bayes.setText("P(A)")
            self.lbl_param_2_bayes.setText("P(B)")
            self.lbl_param_3_bayes.setText("P(A|B)")

    def calculate_prob(self):
        asked_param = self.probability_combo_asked_param.currentIndex()
        result = 0.0
        try:
            param1 = float(self.line_param_probability_1.text())
            param2 = float(self.line_param_probability_2.text())
            if asked_param == 0:
                self.lbl_result.setText("Error: Asked parameter not slected yet")
            else:
                if asked_param == 1:
                    #result = Number of A / Total Outcomes
                    result = param1 / param2
                elif asked_param == 2:
                    #result = P(A) * Total Outcomes
                    result = param1 * param2
                elif asked_param == 1:
                    #result = Number of A / P(A)
                    result = param1 / param2

                self.lbl_result_probability.setText(str(result))
        except ValueError:
            self.lbl_result_probability.setText("Error: Some input not valid")
    
    def calculate_cond(self):
        asked_param = self.conditional_combo_asked_param.currentIndex()
        result = 0.0
        try:
            param1 = float(self.line_param_conditional_1.text())
            param2 = float(self.line_param_conditional_2.text())
            if asked_param == 0:
                self.lbl_result.setText("Error: Asked parameter not slected yet")
            else:
                if asked_param == 1:
                    #result = P(A n B) / P(B)
                    result = param1 / param2
                elif asked_param == 2:
                    #result = P(A|B) * P(B)
                    result = param1 * param2
                elif asked_param == 1:
                    #result = P(A n B) / P(A|B)
                    result = param1 / param2

                self.lbl_result_conditional.setText(str(result))
        except ValueError:
            self.lbl_result_probability.setText("Error: Some input not valid")

    def calculate_bay(self):
        asked_param = self.bayes_combo_asked_param.currentIndex()
        result = 0.0
        try:
            param1 = float(self.line_param_bayes_1.text())
            param2 = float(self.line_param_bayes_2.text())
            param3 = float(self.line_param_bayes_3.text())
            if asked_param == 0:
                self.lbl_result_bayes.setText("Error: Asked parameter not slected yet")
            else:
                if asked_param == 1:
                    #result = P(A|B) * P(B) / P(B|A)
                    result = param2 * param1 / param3
                elif asked_param == 2:
                    #result = P(B|A) * P(A) / P(A|B)
                    result = param3 * param1 / param2
                elif asked_param == 3:
                    #result = P(B|A) * P(A) / P(B)
                    result = param3 * param1 / param2
                elif asked_param == 4:
                    #result = P(A|B) * P(B) / P(A)
                    result = param3 * param2 / param1

                self.lbl_result_bayes.setText(str(result))
        except ValueError:
            self.lbl_result_bayes.setText("Error: Some input not valid")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    program = App()
    program.show()
    sys.exit(app.exec_())