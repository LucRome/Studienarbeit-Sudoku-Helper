from typing import Tuple, Optional
from sudoku.base import Sudoku, Field

class Algorithm:

    blocks = []
    rows = []
    cols =[]

    def __init__(self,sudoku:Sudoku):
        self.update_list(sudoku)

        
    def update_list(self,sudoku:Sudoku):
        self.blocks.clear()
        self.rows.clear()
        self.cols.clear()
        for i in range(0,81):
            row=i//9
            col=i%9
            self.rows[row].append(sudoku.get_field(row,col).get_candidates())
            self.cols[col].append(sudoku.get_field(row,col).get_candidates())
            self.blocks[sudoku.get_block_nr(row,col)].append(sudoku.get_field(row,col).get_candidates())
    
    def print_list(self):
        print('Blocks:',self.blocks)
        print('Rows:',self.rows)
        print('Cols:',self.cols)

    # Versteckter single
    def algorithm_1(self) -> Tuple[bool, Optional[str]]:

        return True,'a'
 
    # Nackter single
    def algorithm_2(self) -> Tuple[bool, Optional[str]]:

        return True,'a'

    # Nacktes Paar
    def algorithm_3(self) -> Tuple[bool, Optional[str]]:

        return True,'a'

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


