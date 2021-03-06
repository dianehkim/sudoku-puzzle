#Diane Kim
#CmpSc132, Spring 2021
#Final Lab: Create a Sudoku Puzzle Class

class SudokuPuzzle:

    def __init__(self):

        self.chart = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def setChart(self, ch):
        self.chart = ch

    def getChart(self):
        return self.chart

    def validateRow(self, RowNum):
        checklist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        answer = 1

        for j in range(9):
            cellValue = self.chart[RowNum][j]

            if cellValue >= 1 and cellValue <= 9:
                checklist[cellValue - 1] = checklist[cellValue - 1] + 1

            elif cellValue != 0:
                answer = 0

        if answer == 1:
            for x in checklist:
                if x > 1:
                    answer = 0
                if x < 1 and answer != 0:
                    if x == 0:
                        answer = -1


        print(self.printValidity(answer) + ' Row '+ str(RowNum + 1))
        return answer

    def validateColumn(self, ColNum):
        checklist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        answer = 1

        for i in range(9):
            cellValue = self.chart[i][ColNum]

            if cellValue >= 1 and cellValue <= 9:
                checklist[cellValue - 1] = checklist[cellValue - 1] + 1

            elif cellValue != 0:
                answer = 0

        if answer == 1:
            for x in checklist:
                if x > 1:
                    answer = 0
                if x < 1 and answer != 0:
                    if x == 0:
                        answer = -1


        print(self.printValidity(answer) + ' Column '+ str(ColNum + 1))
        return answer

    def validateSection(self, SectNum):
        #Sections are counted left to right from the top
        a = SectNum - SectNum % 3
        b = SectNum % 3 * 3
        checklist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        answer = 1

        for i in range(3):
            for j in range(3):
                cellValue = self.chart[a + i][b + j]

                if cellValue >= 1 and cellValue <= 9:
                    checklist[cellValue - 1]  = checklist[cellValue - 1] + 1

                elif cellValue != 0:
                    answer = 0

        if answer == 1:
            for x in checklist:
                if x > 1:
                    answer = 0
                if x < 1 and answer != 0:
                    if x == 0:
                        answer = -1


        print(self.printValidity(answer) + ' Section '+ str(SectNum + 1))
        return answer

    def printValidity(self, num):
        if num == 1:
            return str('Valid')

        elif num == 0:
            return str('Invalid')

        elif num == -1:
            return str('Incomplete')

    def validatePuzzle(self):
        answer = 1

        for q in range(9):
            rowAnswer = self.validateRow(q)
            columnAnswer = self.validateColumn(q)
            sectionAnswer = self.validateSection(q)

            if rowAnswer == 0 or columnAnswer == 0 or sectionAnswer == 0:
                answer = 0
            if answer != 0:
                if rowAnswer == -1 or columnAnswer == -1 or sectionAnswer == -1:
                    answer = -1

        print('Whole Puzzle: ' + self.printValidity(answer))
        return answer
