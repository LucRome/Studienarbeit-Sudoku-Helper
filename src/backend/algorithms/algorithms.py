from traceback import print_list
from typing import Any, Dict, Tuple, Optional, Callable, List, Dict
from sudoku.base import Sudoku, Field, NINE_RANGE, ALL_FIELD_VALUES

class Algorithm:


    blocks = [[0 for _ in range(9)] for _ in range(9)]
    rows = [[0 for _ in range(9)] for _ in range(9)]
    cols = [[0 for _ in range(9)] for _ in range(9)]

    def __init__(self,sudoku:Sudoku):
        self.update_list(sudoku)

        
    def update_list(self,sudoku:Sudoku):

        for i in range(0,81):
            row=i//9
            col=i%9
            self.rows[row][col] = sudoku.get_field(row,col).get_candidates()
            self.cols[col][row] = sudoku.get_field(row,col).get_candidates()
            self.blocks[Sudoku.get_block_nr(row,col)][self.get_block_by_row_col(row,col)] = sudoku.get_field(row,col).get_candidates()

        #self.print_list()
    
    def print_list(self):
        print('Blocks:',self.blocks)
        print('Rows:',self.rows)
        print('Cols:',self.cols)

    def get_row_by_block(self,blockNr:int,blockPos:int):
        return ((blockNr//3)*3 + blockPos//3)
    
    def get_col_by_block(self,blockNr:int,blockPos:int):
        return ((blockNr%3)*3 + blockPos%3)

    def get_block_by_row_col(self,row:int,col:int):
        return (((row%3)*3+(col%3)))

    # all algorithms
    def get_all_algorithms(self) -> List[Callable[[], Tuple[bool, Dict[str, Any]]]]:
        return [
            self.algorithm_1,
            self.algorithm_2,
            self.algorithm_3,
            self.algorithm_4,
            self.algorithm_5,
            self.algorithm_6,
            self.algorithm_7,
            self.algorithm_8,
            self.algorithm_9,
            self.algorithm_10,
        ]

    # hidden single
    def algorithm_1(self) -> Tuple[bool, Optional[str]]:
        blockCounter = 0
        rowCounter = 0
        colCounter = 0
        for i in NINE_RANGE:
            for value in ALL_FIELD_VALUES:
                for j in NINE_RANGE:
                    if (value in self.blocks[i][j]):
                        blockCounter = blockCounter + 1
                    if (rowCounter <= 1) and (value in self.rows[i][j]):
                        rowCounter = rowCounter + 1
                    if (colCounter <= 1) and (value in self.cols[i][j]):
                        colCounter = colCounter + 1     
                                     
                if blockCounter == 1:
                    return (True, f'hidden Single in Row:{self.get_row_by_block(i,j)}, Colum:{self.get_col_by_block(i,j)}, because its the only Field in the Block:{i} with a {value} in the Candidates.')
                elif rowCounter == 1:
                    return (True, f'hidden Single in Row:{i}, Colum:{j}, because its the only Field in the Row:{i} with a {value} in the Candidates.')
                elif colCounter == 1:
                    return (True, f'hidden Single in Row:{j}, Colum:{i}, because its the only Field in the Colum:{i} with a {value} in the Candidates.')    
                else:    
                    blockCounter = 0    
                    rowCounter = 0    
                    colCounter = 0               
        return (False, None)
 
    # Open single
    def algorithm_2(self) -> Tuple[bool, Optional[str]]:
        for i in range(0,81):
            row=i//9
            col=i%9
            if len(self.rows[row][col]) == 1:
                return (True,'In the Field Row:{row}, Colum:{col} there is only one Candidate remaining!')        
        return (False,None)

    # Open pair
    def algorithm_3(self) -> Tuple[bool, Optional[str]]:
        for i in range(0,81):
            row=i//9
            col=i%9
            for value1 in ALL_FIELD_VALUES:
                for value2 in range(value1+1,10): 
                    if (len(self.rows[row][col]) == 2 and value1 in self.rows[row][col] and value2 in self.rows[row][col]):
                        print('!!!!!!!!!')
                        if col <= 8:
                            for a in range(col+1,9):
                                if (value1 in self.rows[row][a] and value2 in self.rows[row][a] and len(self.rows[row][a]) == 2):
                                    return (True, f'Row: Open pair ({value1},{value2}) in (Row:{row}, Colum:{col}) and (Row:{row}, Colum:{a}), you can erase {value1} and {value2} from all Fields in the same Unit')
                        if row <= 8:
                            for a in range(row+1,9):
                                if (value1 in self.cols[col][a] and value2 in self.cols[col][a] and len(self.cols[col][a]) == 2):
                                    return (True, f'Col: Open pair ({value1},{value2}) in (Row:{row}, Colum:{col}) and (Row:{a}, Colum:{col}), you can erase {value1} and {value2} from all Fields in the same Unit')
                        if self.get_block_by_row_col(row,col) <= 8:
                            for a in range(self.get_block_by_row_col(row,col)+1,9):
                                blockNr = Sudoku.get_block_nr(row,col)
                                if value1 in self.blocks[blockNr][a] and value2 in self.blocks[blockNr][a] and len(self.blocks[blockNr][a]) == 2:
                                    return (True, f'Block: Open pair ({value1},{value2}) in (Row:{row}, Colum:{col}) and (Row:{self.get_row_by_block(blockNr,a)}, Colum:{self.get_col_by_block(blockNr,a)}), you can erase {value1} and {value2} from all Fields in the same Unit')

        return (False,None)

    # Verstecktes Paar
    def algorithm_4(self) -> Tuple[bool, Optional[str]]:

        return True,'a'

    # Nacktes Dreier
    def algorithm_5(self) -> Tuple[bool, Optional[str]]:

        return True,'a'

    # Versteckter Dreier
    def algorithm_6(self) -> Tuple[bool, Optional[str]]:

        return True,'a'

    # Nackter/Versteckter Vierer
    def algorithm_7(self) -> Tuple[bool, Optional[str]]:

        return True,'a'

    # Reihe-Block-Check 
    def algorithm_8(self) -> Tuple[bool, Optional[str]]:

        return True,'a'
   
    # Block-Reihe_Check 
    def algorithm_9(self) -> Tuple[bool, Optional[str]]:

        return True,'a'

    # Erweiterter BRC
    def algorithm_10(self) -> Tuple[bool, Optional[str]]:

        return True,'a'


