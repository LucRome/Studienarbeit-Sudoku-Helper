from csv import field_size_limit
import re
from typing import Tuple, Optional, List, Any, Dict, Callable
from sudoku.base import Sudoku, Field, NINE_RANGE, ALL_FIELD_VALUES
from .utils import UnitType, intersection_of_units, remove_candidates_from_fields, remove_candidates_from_fields_in_unit, enforce_hidden_algs, recalc_candidates_with_new_value, intersection_of_units, \
    key_to_coordinates, coordinates_to_key, find_chain_12, check_Same_Block_Rows, find_chain_16, find_chain_16_1, has_removed_candidates, get_common_units

class Algorithm:

    blocks = [[0 for _ in range(9)] for _ in range(9)]
    rows = [[0 for _ in range(9)] for _ in range(9)]
    cols = [[0 for _ in range(9)] for _ in range(9)]

    def __init__(self,sudoku:Sudoku):
        self.update_list(sudoku)
        self.sudoku = sudoku

        
    def update_list(self,sudoku:Sudoku):

        for i in range(0,81):
            row=i//9
            col=i%9
            self.rows[row][col] = sudoku.get_field(row,col).get_candidates()
            self.cols[col][row] = sudoku.get_field(row,col).get_candidates()
            self.blocks[Sudoku.get_block_nr(row,col)][self.get_block_by_row_col(row,col)] = sudoku.get_field(row,col).get_candidates()
    

    def get_row_by_block(self,blockNr:int,blockPos:int):
        return ((blockNr//3)*3 + blockPos//3)
    
    def get_col_by_block(self,blockNr:int,blockPos:int):
        return ((blockNr%3)*3 + blockPos%3)

    def get_block_by_row_col(self,row:int,col:int):
        return (((row%3)*3+(col%3)))
    
    def get_name_fn_dict(self) -> Dict[str, Callable[[], Tuple[bool, Optional[Dict[str, Any]]]]]:
        """
        returns the dict that maps the functions to the algorithm names
        """
        return {
            'open_single': self.algorithm_2,
            'hidden_single': self.algorithm_1,
            'open_pair': self.algorithm_3,
            'hidden_pair': self.algorithm_4,
            'open_three': self.algorithm_5,
            'hidden_three': self.algorithm_6,
            'open_four': self.algorithm_7,
            'hidden_four': self.algorithm_8,
            'row_block_check': self.algorithm_9,
            'block_row_check': self.algorithm_10,
            'x_wing_row': self.algorithm_11_1,
            'x_wing_col': self.algorithm_11_2,
            'steinbutt': self.algorithm_12,
            'third_eye': self.algorithm_13,
            'skyscraper': self.algorithm_14,
            'swordfish_col': self.algorithm_15_1,
            'swordfish_row': self.algorithm_15_2,
            'dragon': self.algorithm_16,
            'square_type_1': self.algorithm_17,
            'square_type_2': self.algorithm_18,
            'square_type_4': self.algorithm_20,
            'xy_wing': self.algorithm_21,
            'xyz_wing': self.algorithm_22,
            # 'x_chain': self.algorithm_23,
            'xy_chain': self.algorithm_24,  
            'swordfish_fin_col': self.algorithm_25_1,
            'swordfish_fin_row': self.algorithm_25_2,
            'w_wing': self.algorithm_26,
        }

    # hidden single
    def algorithm_1(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            blk, row, col = self.sudoku.get_block(i), self.sudoku.get_row(i), self.sudoku.get_column(i)
            for value in ALL_FIELD_VALUES:
                blk_fields, row_fields, col_fields = [], [], []

                for field in blk:
                    if (len(blk_fields) < 2) and (value in field.get_candidates()):
                        blk_fields.append(field)
                for field in row:
                    if (len(row_fields) < 2) and (value in field.get_candidates() and len(row_fields) < 2):
                        row_fields.append(field)
                for field in col:
                    if (len(col_fields) < 2) and (value in field.get_candidates()):
                        col_fields.append(field)

                reason, field = None, None        
                if len(blk_fields) == 1:
                    reason, field = UnitType.BLOCK, blk_fields[0]
                elif len(row_fields) == 1:
                    reason, field = UnitType.ROW, row_fields[0]
                elif len(col_fields) == 1:
                    reason, field = UnitType.COLUMN, col_fields[0]
                
                if reason:
                    field.set_value(value)
                    removed_candidates = recalc_candidates_with_new_value(self.sudoku, field.get_coordinates())
                    return (True, {
                        'algorithm': 'hidden_single',
                        'field': field.get_coordinates(),
                        'value': value,
                        'reason': reason.value,
                        'removed_candidates': removed_candidates
                    })              
        return (False, None)
 
    # Open single
    def algorithm_2(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for row in NINE_RANGE:
            for col in NINE_RANGE:
                field = self.sudoku.get_field(row, col)
                candidates = field.get_candidates()
                if len(candidates) == 1:
                    value = candidates[0]
                    field.set_value(value)
                    removed_candidates = recalc_candidates_with_new_value(self.sudoku, (row, col))
                    return True, {
                        'algorithm': 'open_single',
                        'field': (row, col),
                        'value': value,
                        'removed_candidates': removed_candidates,
                    }   
        return False, None

    # Open pair
    def algorithm_3(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for row in NINE_RANGE:
            for col in NINE_RANGE:
                for value1 in ALL_FIELD_VALUES:
                    for value2 in range(value1+1,10): 
                        if (len(self.rows[row][col]) == 2 and value1 in self.rows[row][col] and value2 in self.rows[row][col]):
                            reason = None
                            fields = None
                            nr: int
                            if col <= 8:
                                for a in range(col+1,9):
                                    if (value1 in self.rows[row][a] and value2 in self.rows[row][a] and len(self.rows[row][a]) == 2):
                                        reason = UnitType.ROW
                                        fields = [(row, col), (row, a)]
                                        nr = row
                                        break
                            elif row <= 8:
                                for a in range(row+1,9):
                                    if (value1 in self.cols[col][a] and value2 in self.cols[col][a] and len(self.cols[col][a]) == 2):
                                        reason = UnitType.COLUMN
                                        fields = [(row, col), (a, col)]
                                        nr = col
                                        break
                            elif self.get_block_by_row_col(row,col) <= 8:
                                for a in range(self.get_block_by_row_col(row,col)+1,9):
                                    blockNr = Sudoku.get_block_nr(row,col)
                                    if value1 in self.blocks[blockNr][a] and value2 in self.blocks[blockNr][a] and len(self.blocks[blockNr][a]) == 2:
                                        reason = UnitType.BLOCK
                                        fields = [(row, col), (self.get_row_by_block(blockNr,a), self.get_col_by_block(blockNr,a))]
                                        nr = blockNr
                                        break
                            if reason and fields:
                                removed = remove_candidates_from_fields_in_unit(self.sudoku, reason, nr, [value1, value2], fields)
                                if has_removed_candidates(removed):
                                    return (True, {
                                        'algorithm': 'open_pair',
                                        'values': [value1, value2],
                                        'fields': fields,
                                        'reason': reason.value,
                                        'removed_candidates': removed,
                                    })
        return (False,None)

    # Verstecktes Paar
    def algorithm_4(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            col = self.sudoku.get_column(i)
            block = self.sudoku.get_block(i)
            for value1 in ALL_FIELD_VALUES:
                for value2 in range(value1+1,10):
                    rowCounter = 0
                    colCounter = 0
                    blockCounter = 0
                    for j in NINE_RANGE:                        
                        
                        #block check
                        if value1 in block[j].get_candidates():
                            if value2 in block[j].get_candidates():
                                blockCounter = blockCounter + 1
                            else:
                                blockCounter = 5
                                
                        if value2 in block[j].get_candidates():
                            if value1 in block[j].get_candidates():
                                blockCounter = blockCounter + 1
                            else:
                                blockCounter = 5
                                
                        #col check
                        if value1 in col[j].get_candidates():
                            if value2 in col[j].get_candidates():
                                colCounter = colCounter + 1
                            else:
                                colCounter = 5
                                
                        if value2 in col[j].get_candidates():
                            if value1 in col[j].get_candidates():
                                colCounter = colCounter + 1
                            else:
                                colCounter = 5
                                
                        #ROW check
                        if value1 in row[j].get_candidates():
                            if value2 in row[j].get_candidates():
                                rowCounter = rowCounter + 1
                            else:
                                rowCounter = 5                                
                        if value2 in row[j].get_candidates():
                            if value1 in row[j].get_candidates():
                                rowCounter = rowCounter + 1
                            else:
                                rowCounter = 5
                    
                    reason, nr = None, None
                    if blockCounter == 4:
                        reason, nr = UnitType.BLOCK, i
                    elif colCounter == 4:
                        reason, nr = UnitType.COLUMN, i
                    elif rowCounter == 4:
                        reason, nr = UnitType.ROW, i
                    if reason:
                        values = [value1, value2]
                        removed_candidates = enforce_hidden_algs(self.sudoku, reason, nr, values)
                        if has_removed_candidates(removed_candidates):
                            return (True, {
                                'algorithm': 'hidden_pair',
                                'values': values,
                                'reason': reason.value,
                                'removed_candidates': removed_candidates,
                            })

        return (False,None)

    # Nacktes Dreier
    def algorithm_5(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            # iterate over all blocks, columns, rows
            row = self.sudoku.get_row(i)
            col = self.sudoku.get_column(i)
            block = self.sudoku.get_block(i)
            for value1 in ALL_FIELD_VALUES:
                for value2 in range(value1+1,10):
                    for value3 in range(value2+1,10):
                        # check all possible combinations
                        rowCounter = 0
                        # _fields: the fields used to build the naked three in the corresponding unit
                        # _candidates: the candidates of the respective fields
                        row_fields: List[Tuple[int, int]] = list()
                        row_candidates: List[List[int]] = list()
                        colCounter = 0
                        col_fields: List[Tuple[int, int]] = list()
                        col_candidates: List[List[int]] = list()
                        blockCounter = 0
                        block_fields: List[Tuple[int, int]] = list()
                        block_candidates: List[List[int]] = list()
                        values = (value1,value2,value3)
                        for j in NINE_RANGE:
                            #block check
                            if  value1 in block[j].get_candidates() or value2 in block[j].get_candidates() or value3 in block[j].get_candidates():
                                # one value in the candidates?
                                err = False
                                for testValue in block[j].get_candidates():
                                    if not(testValue in values):
                                        # when field has other candidates than the tested ones -> no success
                                        err = True
                                if not err:
                                    # success: increase counter by 1
                                    block_fields.append(block[j].get_coordinates())
                                    block_candidates.append(block[j].get_candidates())
                                    blockCounter = blockCounter + 1
                                
                            #col check 
                            if  value1 in col[j].get_candidates() or value2 in col[j].get_candidates() or value3 in col[j].get_candidates():
                                # same principle as block
                                err = False
                                for testValue in col[j].get_candidates():
                                    if not(testValue in values):
                                        err = True
                                if not err:
                                    col_fields.append(col[j].get_coordinates())
                                    col_candidates.append(col[j].get_candidates())
                                    colCounter = colCounter + 1
                            
                            #row check
                            if  value1 in row[j].get_candidates() or value2 in row[j].get_candidates() or value3 in row[j].get_candidates():
                                # same principle as block
                                err = False
                                for testValue in row[j].get_candidates():
                                    if not(testValue in values):
                                        err = True
                                if not err:
                                    row_fields.append(row[j].get_coordinates())
                                    row_candidates.append(row[j].get_candidates())
                                    rowCounter = rowCounter + 1

                        reason, fields, field_candidates ,nr = None, None, None, None        
                        if blockCounter == 3:
                            reason, fields, field_candidates, nr = UnitType.BLOCK, block_fields, block_candidates, i
                        elif colCounter == 3:
                            reason, fields, field_candidates, nr = UnitType.COLUMN, col_fields, col_candidates, i
                        elif rowCounter == 3:
                            reason, fields, field_candidates, nr = UnitType.ROW, row_fields, row_candidates, i
                        if reason:
                            removed = remove_candidates_from_fields_in_unit(self.sudoku, reason, nr, values, fields)
                            if has_removed_candidates(removed):
                                return (True, {
                                    'algorithm': 'open_three',
                                    'values': values,
                                    'fields': fields,
                                    'field_candidates': field_candidates,
                                    'reason': reason.value,
                                    'removed_candidates': removed,
                                })   
        return (False,None)

    # Versteckter Dreier
    def algorithm_6(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            # iterate over all blocks, columns, rows
            row = self.sudoku.get_row(i)
            col = self.sudoku.get_column(i)
            block = self.sudoku.get_block(i)
            for value1 in ALL_FIELD_VALUES:
                for value2 in range(value1+1,10):
                    for value3 in range(value2+1,10):
                        # iterate over all possible value combinations
                        rowCounter = 0
                        colCounter = 0
                        blockCounter = 0
                        blockList = [False,False,False]
                        colList = [False,False,False]
                        rowList = [False,False,False]
                        for j in NINE_RANGE:
                            #block check
                            if  value1 in block[j].get_candidates() or value2 in block[j].get_candidates() or value3 in block[j].get_candidates():
                                # any of the values in the field candidates
                                # mark which ones
                                if value1 in block[j].get_candidates():
                                    blockList[0] = True
                                if value2 in block[j].get_candidates():  
                                    blockList[1] = True 
                                if value3 in block[j].get_candidates():
                                    blockList[2] = True
                                # count how many fields contain the candidates in the unit
                                blockCounter = blockCounter + 1
                            #col check (same principle as block)
                            if  value1 in col[j].get_candidates() or value2 in col[j].get_candidates() or value3 in col[j].get_candidates():
                                if value1 in col[j].get_candidates():
                                    colList[0] = True
                                if value2 in col[j].get_candidates():  
                                    colList[1] = True 
                                if value3 in col[j].get_candidates():
                                    colList[2] = True
                                colCounter = colCounter + 1
                            #row check (same principle as block)
                            if  value1 in row[j].get_candidates() or value2 in row[j].get_candidates() or value3 in row[j].get_candidates():
                                if value1 in row[j].get_candidates():
                                    rowList[0] = True
                                if value2 in row[j].get_candidates():  
                                    rowList[1] = True 
                                if value3 in row[j].get_candidates():
                                    rowList[2] = True
                                rowCounter = rowCounter + 1
                                
                        reason, nr = None, None
                        # 3 fields with the values in the candidates and each candidate occurs at least once
                        if blockCounter == 3 and all(blockList):
                            reason, nr = UnitType.BLOCK, i  
                        if colCounter == 3 and all(colList):
                            reason, nr = UnitType.COLUMN, i
                        if rowCounter == 3 and all(rowList):
                            reason, nr = UnitType.ROW, i
                        if reason:
                            values = [value1, value2, value3]
                            removed_candidates = enforce_hidden_algs(self.sudoku, reason, nr, values)
                            if has_removed_candidates(removed_candidates):
                                return (True, {
                                    'algorithm': 'hidden_three',
                                    'values': values,
                                    'reason': reason.value,
                                    'removed_candidates': removed_candidates,
                                })
        return (False,None)

    # Nackter Vierer
    def algorithm_7(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            col = self.sudoku.get_column(i)
            block = self.sudoku.get_block(i)
            for value1 in ALL_FIELD_VALUES:
                for value2 in range(value1+1,10):
                    for value3 in range(value2+1,10):
                        for value4 in range(value3+1,10):
                            # _fields: the fields used to build the naked three in the corresponding unit
                            # _candidates: the candidates of the respective fields
                            rowCounter = 0
                            row_fields: List[Tuple[int, int]] = list()
                            row_candidates: List[List[int]] = list()
                            colCounter = 0
                            col_fields: List[Tuple[int, int]] = list()
                            col_candidates: List[List[int]] = list()
                            blockCounter = 0
                            block_fields: List[Tuple[int, int]] = list()
                            block_candidates: List[List[int]] = list()
                            values = (value1,value2,value3,value4)
                            for j in NINE_RANGE:
                                #block check
                                if  value1 in block[j].get_candidates() or value2 in block[j].get_candidates() or value3 in block[j].get_candidates() or value4 in block[j].get_candidates():
                                    # any testvalue in the candidates
                                    err = False
                                    for testValue in block[j].get_candidates():
                                        if not(testValue in values):
                                            err = True
                                            # when field has other candidates than the tested values -> no success
                                    if not err:
                                        block_fields.append(block[j].get_coordinates())
                                        block_candidates.append(block[j].get_candidates())
                                        blockCounter = blockCounter + 1
                                    
                                #col check 
                                if  value1 in col[j].get_candidates() or value2 in col[j].get_candidates() or value3 in col[j].get_candidates() or value4 in col[j].get_candidates():
                                    # same principle as block
                                    err = False
                                    for testValue in col[j].get_candidates():
                                        if not(testValue in values):
                                            err = True
                                    if not err:
                                        col_fields.append(col[j].get_coordinates())
                                        col_candidates.append(col[j].get_candidates())
                                        colCounter = colCounter + 1
                                
                                #row check
                                if  value1 in row[j].get_candidates() or value2 in row[j].get_candidates() or value3 in row[j].get_candidates() or value4 in row[j].get_candidates():
                                    # same principle as block
                                    err = False
                                    for testValue in row[j].get_candidates():
                                        if not(testValue in values):
                                            err = True
                                    if not err:
                                        row_fields.append(row[j].get_coordinates())
                                        row_candidates.append(row[j].get_candidates())
                                        rowCounter = rowCounter + 1 

                            reason, fields, field_candidates ,nr = None, None, None, None
                            if blockCounter == 4:
                                reason, fields, field_candidates, nr = UnitType.BLOCK, block_fields, block_candidates, i
                            elif colCounter == 4:
                                reason, fields, field_candidates, nr = UnitType.COLUMN, col_fields, col_candidates, i
                            elif rowCounter == 4:
                                reason, fields, field_candidates, nr = UnitType.ROW, row_fields, row_candidates, i
                            if reason:
                                removed = remove_candidates_from_fields_in_unit(self.sudoku, reason, nr, values, fields)
                                if has_removed_candidates(removed):
                                    return (True, {
                                        'algorithm': 'open_four',
                                        'values': values,
                                        'fields': fields,
                                        'field_candidates': field_candidates,
                                        'reason': reason.value,
                                        'removed_candidates': removed,
                                    })
        return (False,None)
        
    
    # Versteckter Vierer
    def algorithm_8(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            # iterate over all blocks, columns, rows
            row = self.sudoku.get_row(i)
            col = self.sudoku.get_column(i)
            block = self.sudoku.get_block(i)
            for value1 in ALL_FIELD_VALUES:
                for value2 in range(value1+1,10):
                    for value3 in range(value2+1,10):
                        for value4 in range(value3+1,10):
                            values = [value1, value2, value3, value4]
                            blockBenefit = False # TODO: what is the use of these variables???
                            colBenefit = False
                            rowBenefit = False
                            rowCounter = 0
                            colCounter = 0
                            blockCounter = 0
                            blockList = [False,False,False,False]
                            colList = [False,False,False,False]
                            rowList = [False,False,False,False]
                            for j in NINE_RANGE:
                                #block check
                                if  value1 in block[j].get_candidates() or value2 in block[j].get_candidates() or value3 in block[j].get_candidates() or value4 in block[j].get_candidates():
                                    # any of the values in the field candidates
                                    # mark which ones
                                    if value1 in block[j].get_candidates():
                                        blockList[0] = True
                                    if value2 in block[j].get_candidates():  
                                        blockList[1] = True 
                                    if value3 in block[j].get_candidates():
                                        blockList[2] = True
                                    if value4 in block[j].get_candidates():
                                        blockList[3] = True
                                    blockCounter = blockCounter + 1
                                elif block[j].get_candidates() != []:
                                    blockBenefit = True
                                #col check (same principle as block)
                                if  value1 in col[j].get_candidates() or value2 in col[j].get_candidates() or value3 in col[j].get_candidates() or value4 in col[j].get_candidates():
                                    if value1 in col[j].get_candidates():
                                        colList[0] = True
                                    if value2 in col[j].get_candidates():  
                                        colList[1] = True 
                                    if value3 in col[j].get_candidates():
                                        colList[2] = True
                                    if value4 in col[j].get_candidates():
                                        colList[3] = True
                                    colCounter = colCounter + 1
                                elif col[j].get_candidates() != []:
                                    colBenefit = True
                                #row check (same principle as block)
                                if  value1 in row[j].get_candidates() or value2 in row[j].get_candidates() or value3 in row[j].get_candidates() or value4 in row[j].get_candidates():
                                    if value1 in row[j].get_candidates():
                                        rowList[0] = True
                                    if value2 in row[j].get_candidates():  
                                        rowList[1] = True 
                                    if value3 in row[j].get_candidates():
                                        rowList[2] = True
                                    if value4 in row[j].get_candidates():
                                        rowList[3] = True
                                    rowCounter = rowCounter + 1
                                elif row[j].get_candidates() != []:
                                    rowBenefit = True

                            reason, nr = None, None
                            if blockCounter == 4 and blockBenefit and all(blockList):
                                reason, nr = UnitType.BLOCK, i
                            if colCounter == 4 and colBenefit and all(colList):
                                reason, nr = UnitType.COLUMN, i
                            if rowCounter == 4 and rowBenefit and all(rowList):
                                reason, nr = UnitType.ROW, i
                            if reason:
                                removed_candidates = enforce_hidden_algs(self.sudoku, reason, nr, values)
                                if has_removed_candidates(removed_candidates):
                                    return (True, {
                                        'algorithm': 'hidden_four',
                                        'values': values,
                                        'reason': reason.value,
                                        'removed_candidates': removed_candidates
                                    })
        return (False,None)

    # Reihe-Block-Check 
    def algorithm_9(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            # iterate over all rows
            for value in ALL_FIELD_VALUES:
                # iterate over all values
                block1 = False
                block2 = False
                block3 = False
                count = 0
                for j in NINE_RANGE:
                    # iterate over all Fields in the row
                    if value in row[j].get_candidates():
                        if j in range(0,3):
                            blockNr = Sudoku.get_block_nr(i,j)
                            count = count + 1
                            block1=True
                        if j in range(3,6):
                            blockNr = Sudoku.get_block_nr(i,j)
                            count = count + 1
                            block2=True
                        if j in range(6,9):
                            blockNr = Sudoku.get_block_nr(i,j)
                            count = count + 1
                            block3=True
                if (block1 and not block2 and not block3) or (block2 and not block1 and not block3) or (block3 and not block2 and not block1):
                    # check if there are any benefits
                    blockCount = 0
                    block = self.sudoku.get_block(blockNr)
                    for a in NINE_RANGE:
                        if(value in block[a].get_candidates()):
                            blockCount = blockCount + 1
                    if blockCount > count:
                        intersect_fields = intersection_of_units(UnitType.ROW, i, UnitType.BLOCK, blockNr)  # the fields that are in the row and in the block
                        removed_candidates = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.BLOCK, blockNr, [value], intersect_fields)
                        if has_removed_candidates(removed_candidates):
                            return (True, {
                                'algorithm': 'row_block_check',
                                'value': value,
                                'intersect_fields': intersect_fields,
                                'removed_candidates': removed_candidates
                            })
        return (False,None)
   
    # Block-Reihe_Check 
    def algorithm_10(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        for i in NINE_RANGE:
            block = self.sudoku.get_block(i)
            # iterate over all blocks
            for value in ALL_FIELD_VALUES:
                row1 = False
                row2 = False
                row3 = False
                count = 0
                for j in NINE_RANGE:
                    # iterate over all fields in the block
                    if value in block[j].get_candidates():
                        if j in range(0,3):
                            rowNr = self.get_row_by_block(i,j)
                            count = count + 1
                            row1=True
                        if j in range(3,6):
                            rowNr = self.get_row_by_block(i,j)
                            count = count + 1
                            row2=True
                        if j in range(6,9):
                            rowNr = self.get_row_by_block(i,j)
                            count = count + 1
                            row3=True
                if (row1 and not row2 and not row3) or (row2 and not row1 and not row3) or (row3 and not row2 and not row1):
                    # check if there are any benefits
                    rowCount = 0
                    row = self.sudoku.get_row(rowNr)
                    for a in NINE_RANGE:
                        if(value in row[a].get_candidates()):
                            rowCount = rowCount + 1
                    if rowCount > count:
                        intersect_fields = intersection_of_units(UnitType.ROW, rowNr, UnitType.BLOCK, i)  # the fields that are in the row and in the block
                        removed_candidates = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.ROW, rowNr, [value], intersect_fields)
                        if has_removed_candidates(removed_candidates):
                            return (True, {
                                'algorithm': 'block_row_check',
                                'value': value,
                                'intersect_fields': intersect_fields,
                                'removed_candidates': removed_candidates
                            })
        return (False,None)        

    # X-Wing Row
    def algorithm_11_1(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        Pair1 = []
        Pair2 = []        
        for value in ALL_FIELD_VALUES:
            # iterate over all values
            Counter = 0
            Pair1.clear()
            Pair2.clear()
            for i in NINE_RANGE:
                row = self.sudoku.get_row(i)
                # iterate over all rows
                for j in NINE_RANGE:
                    # iterate over all fields in rows
                    if value in row[j].get_candidates():
                        Counter = Counter + 1
                        Pair1.append((i,j))
                if(Counter==2):
                    # success for first pair -> add to pair2 and continue (pair 2: List of all pairs in all rows)
                    Pair2.append([Pair1[0],Pair1[1]]) 
                    Pair1.clear()
                    Counter = 0
                else:
                    # no success for this pair
                    Pair1.clear()
                    Counter = 0     
            if(len(Pair2)>=2):
                for a in range(0,len(Pair2)):
                    for b in range(a+1,len(Pair2)):
                        # check all pairs whether there are some that meet the requirements
                        if Pair2[a][0][1] == Pair2[b][0][1] and Pair2[a][1][1] == Pair2[b][1][1]:
                            colCount = 0
                            col1 = self.sudoku.get_column(Pair2[a][0][1])
                            col2 = self.sudoku.get_column(Pair2[a][1][1])
                            for l in NINE_RANGE:
                                # check whether the algorithm brings a benefit
                                if(value in col1[l].get_candidates()):
                                    colCount = colCount + 1
                                if(value in col2[l].get_candidates()):
                                    colCount = colCount + 1
                                if colCount > 4:
                                    intersect_fields = [Pair2[a][0], Pair2[a][1], Pair2[b][0], Pair2[b][1]]
                                    removed_candidates_1 = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.COLUMN, Pair2[a][0][1], [value], intersect_fields)
                                    removed_candidates_2 = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.COLUMN, Pair2[a][1][1], [value], intersect_fields)
                                    removed_candidates = {**removed_candidates_1, **removed_candidates_2}
                                    if has_removed_candidates(removed_candidates):
                                        return (True, {
                                            'algorithm': 'x_wing_row',
                                            'value': value,
                                            'intersect_fields': intersect_fields,
                                            'removed_candidates': removed_candidates
                                        })
        return (False,None)
    
    # X-Wing Col
    def algorithm_11_2(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        Pair1 = []
        Pair2 = []        
        for value in ALL_FIELD_VALUES:
            # iterate over all values
            Counter = 0
            Pair1.clear()
            Pair2.clear()
            for i in NINE_RANGE:
                # iterate over all columns
                col = self.sudoku.get_column(i)
                for j in NINE_RANGE:
                    # iterate over all fields in column
                    if value in col[j].get_candidates():
                        Counter = Counter + 1
                        Pair1.append((j, i))
                if(Counter==2):
                    # success for first pair -> add to pair2 and continue (pair 2: List of all pairs in all rows)
                    Pair2.append([Pair1[0],Pair1[1]]) 
                    Pair1.clear()
                    Counter = 0
                else:
                    # no success for this pair
                    Pair1.clear()
                    Counter = 0     
            if(len(Pair2)>=2):
                for a in range(0,len(Pair2)):
                    for b in range(a+1,len(Pair2)):
                        # check all pairs whether there are some that meet the requirements
                        if Pair2[a][0][0] == Pair2[b][0][0] and Pair2[a][1][0] == Pair2[b][1][0]:
                            rowCount = 0
                            row1 = self.sudoku.get_row(Pair2[a][0][0])
                            row2 = self.sudoku.get_row(Pair2[a][1][0])
                            for l in NINE_RANGE:
                                # check whether the algorithm brings a benefit
                                if(value in row1[l].get_candidates()):
                                    rowCount = rowCount + 1
                                if(value in row2[l].get_candidates()):
                                    rowCount = rowCount + 1
                                if rowCount > 4:
                                    intersect_fields = [Pair2[a][0], Pair2[a][1], Pair2[b][0], Pair2[b][1]]
                                    removed_candidates_1 = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.ROW, Pair2[a][0][0], [value], intersect_fields)
                                    removed_candidates_2 = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.ROW, Pair2[a][1][0], [value], intersect_fields)
                                    removed_candidates = {**removed_candidates_1, **removed_candidates_2}
                                    if has_removed_candidates(removed_candidates):
                                        return (True, {
                                            'algorithm': 'x_wing_col',
                                            'value': value,
                                            'intersect_fields': intersect_fields,
                                            'removed_candidates': removed_candidates
                                        })
        return (False,None)
  
    # Drittes Auge
    def algorithm_13(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        counter = 0
        rowPos = 0
        colPos= 0
        value = 0
        reason = None
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            # iterate over all rows
            for j in NINE_RANGE:
                # iterate over all fields in row
                if len(row[j].get_candidates()) == 3:
                    # field has 3 candidates
                    for a in ALL_FIELD_VALUES:
                        rowCounter = 0
                        blockCounter = 0
                        colCounter = 0
                        # check whether the candidate occurs 3 times in a unit
                        block = self.sudoku.get_block(Sudoku.get_block_nr(i,j))
                        col = self.sudoku.get_column(j)
                        for j2 in NINE_RANGE:
                            if a in block[j2].get_candidates():
                                blockCounter = blockCounter + 1
                            if a in row[j2].get_candidates():
                                rowCounter = rowCounter + 1
                            if a in col[j2].get_candidates():
                                colCounter = colCounter + 1
                        if blockCounter == 3:
                            reason = UnitType.BLOCK
                            value = a
                            rowPos = i
                            colPos = j
                        if rowCounter == 3:
                            reason = UnitType.ROW
                            value = a
                            rowPos = i
                            colPos = j
                        if colCounter == 3:
                            reason = UnitType.COLUMN
                            value = a
                            rowPos = i
                            colPos = j                               
                    counter = counter + 1
                if len(row[j].get_candidates()) > 3:
                    counter = 2
                    # no success
                    break
        
        if counter == 1:
            # success -> remove obsolete candidates
            candidates = self.sudoku.get_field(rowPos, colPos).get_candidates()
            to_remove = list(self.sudoku.get_field(rowPos, colPos).get_candidates())
            to_remove.remove(value)
            removed_candidates = {coordinates_to_key(rowPos, colPos): to_remove}
            for v in to_remove:
                candidates.remove(v)
            if has_removed_candidates(removed_candidates):
                return (True,{
                    'algorithm': 'third_eye',
                    'value': value,
                    'field': (rowPos, colPos),
                    'removed_candidates': removed_candidates,
                    'reason': reason.value
                })
            
        return (False,None)

    
    # Steinbutt
    def algorithm_12(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields: List[Field] = list()
        vStraight: List[Field] = list()
        vComplex: List[Field] = list()
        
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            for value in ALL_FIELD_VALUES:
                for j in NINE_RANGE:
                    if value in row[j].get_candidates():
                        fields.append(row[j])
                if len(fields) == 2:
                    fields_coordinates = [f.get_coordinates() for f in fields]
                    if Sudoku.get_block_nr(fields_coordinates[0][0], fields_coordinates[0][1]) != Sudoku.get_block_nr(fields_coordinates[1][0], fields_coordinates[1][1]):
                        # fields must be in different blocks!
                        for field in fields:
                            if find_chain_12(self.sudoku, field, value)[0] and find_chain_12(self.sudoku, field, value)[1] != None: 
                                vComplex = find_chain_12(self.sudoku, field, value)[1]
                            elif find_chain_12(self.sudoku, field, value)[0] == False:
                                vStraight = find_chain_12(self.sudoku, field, value)[1]

                        if vStraight != None and vComplex !=None and len(vComplex) > 2 and len(vStraight)>=2:
                            for a in range(3,len(vComplex)):
                                for b in range(0,len(vStraight)):
                                    if vComplex[a].get_coordinates()[0] == vStraight[b].get_coordinates()[0] and vComplex[a].get_coordinates()[1]==vStraight[0].get_coordinates()[1]:
                                        self.sudoku.get_field(vComplex[a].get_coordinates()[0],vComplex[a].get_coordinates()[1]).remove_candidate(value)
                                        return (True,{
                                            'algorithm': 'steinbutt',
                                            'value': value,
                                            'row': vComplex[a].get_coordinates()[0],
                                            'fields': [f.get_coordinates() for f in fields],
                                            'path_complex': [f.get_coordinates() for f in vComplex[1:3]],
                                            'removed_candidates': {coordinates_to_key(vComplex[a].get_coordinates()[0],vComplex[a].get_coordinates()[1]): [value]}
                                        })
                    fields.clear()
                    vStraight.clear()
                    vComplex.clear()      
                else:
                    fields.clear()
                    vStraight.clear()
                    vComplex.clear()   
                        
        return False,None


    # Wolkenkratzer
    def algorithm_14(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields: List[Field] = list() 
        returnFields: List[Field] = list()
        returnFields2: List[Field] = list()
        vCol: List[List[Tuple[int,int]]] = list()  
        vCol2: List[Tuple[int,int]] = list()
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            for value in range(1,10):
                for j in NINE_RANGE:
                    if value in row[j].get_candidates():
                        fields.append(row[j])
                if len(fields)>1:
                    for a in range(0,len(fields)):
                        col = self.sudoku.get_column(fields[a].get_coordinates()[1])
                        for j in NINE_RANGE:
                            if value in col[j].get_candidates():
                                vCol2.append(col[j].get_coordinates())
                        if len(vCol2) == 2:
                            if len(vCol)> 0:
                                if vCol[0][0] != vCol2[0][0]: 
                                    vCol.append(vCol2.copy())
                               
                            else:
                                vCol.append(vCol2.copy())
                        vCol2.clear()
                    for a in vCol:
                        for b in a:
                            for x in vCol:
                                for y in x:
                                    found_sth = False
                                    if b[0]==0 and (y[0]==1 or y[0]==2) and b[0]!=i and y[0]!=i:      
                                        found_sth = check_Same_Block_Rows(b,y)                                            
                                    elif b[0]==1 and (y[0]==0 or y[0]==2) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    elif b[0]==2 and (y[0]==0 or y[0]==1) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    elif b[0]==3 and (y[0]==4 or y[0]==5) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    elif b[0]==4 and (y[0]==3 or y[0]==5) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    elif b[0]==5 and (y[0]==3 or y[0]==4) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    elif b[0]==6 and (y[0]==7 or y[0]==8) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    elif b[0]==7 and (y[0]==6 or y[0]==8) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    elif b[0]==8 and (y[0]==6 or y[0]==7) and b[0]!=i and y[0]!=i:
                                        found_sth = check_Same_Block_Rows(b,y)
                                    if found_sth:
                                        y_b, x_b = b
                                        y_y, x_y = y
                                        intersect_fields1 = intersection_of_units(UnitType.BLOCK, self.sudoku.get_block_nr(y_b, x_b), UnitType.ROW, y_y)
                                        removed1 = remove_candidates_from_fields(self.sudoku, intersect_fields1, [value])
                                        intersect_fields2 = intersection_of_units(UnitType.ROW, y_b, UnitType.BLOCK, self.sudoku.get_block_nr(y_y, x_y))
                                        removed2 = remove_candidates_from_fields(self.sudoku, intersect_fields2, [value])
                                        removed_candidates = {**removed1, **removed2}
                                        if has_removed_candidates(removed_candidates):
                                            return (True, {
                                                'algorithm': 'skyscraper',
                                                'value': value,
                                                'fields_staggered': [b, y],
                                                'row_same_height': i,
                                                'removed_candidates': removed_candidates
                                            })


                vCol.clear()
                fields.clear()      
        return False,None 
       
    # Schwertfisch-Col
    def algorithm_15_1(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        Fields1 = []
        Fields2 = []
        Fields3 = []
        rows = list()      
        for value in ALL_FIELD_VALUES:
            Counter = 0
            Fields1.clear()
            Fields2.clear()
            for i in NINE_RANGE:
                col = self.sudoku.get_column(i)
                for j in NINE_RANGE:
                    if value in col[j].get_candidates():
                        Counter = Counter + 1
                        Fields1.append((j,i))
                if(Counter<=3)and Counter > 1:
                    Fields2.append(Fields1.copy()) 
                    Fields1.clear()
                    Counter = 0
                else:
                    Fields1.clear()
                    Counter = 0     
            for a in range(0,len(Fields2)):
                for b in range(a+1,len(Fields2)):
                    for c in range(b+1,len(Fields2)):
                        Fields3.append(Fields2[a])
                        Fields3.append(Fields2[b])
                        Fields3.append(Fields2[c])
                        rows.clear()
                        for d in NINE_RANGE:
                            if self.check_15_1(Fields3,d):
                                rows.append(self.sudoku.get_row(d))
                        if len(rows) == 3:
                            rowCount = 0
                            for l in NINE_RANGE:
                                if(value in rows[0][l].get_candidates()):
                                    rowCount = rowCount + 1
                                if(value in rows[1][l].get_candidates()):
                                    rowCount = rowCount + 1
                                if(value in rows[2][l].get_candidates()):
                                    rowCount = rowCount + 1
                            if rowCount > (len(Fields2[0])+len(Fields2[1])+len(Fields2[2])):
                                removed_candidates: Dict[str, Any] = {}
                                col_fields = []
                                for fl in Fields3:
                                    for f in fl:
                                        col_fields.append(f)
                                for r in [r[0].get_coordinates()[0] for r in rows]:
                                    rem = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.ROW, r, [value], col_fields)
                                    removed_candidates = {**removed_candidates, **rem}
                                if has_removed_candidates(removed_candidates):
                                    return (True, {
                                        'algorithm': 'swordfish_col',
                                        'fields': col_fields,
                                        'value': value,
                                        'removed_candidates': removed_candidates
                                    })
                        Fields3.clear()
        return (False,None)
                           
    # Schwertfisch-Row
    def algorithm_15_2(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        Fields1 = []
        Fields2 = []
        Fields3 = []
        cols = list()      
        for value in ALL_FIELD_VALUES:
            Counter = 0
            Fields1.clear()
            Fields2.clear()
            for i in NINE_RANGE:
                row = self.sudoku.get_row(i)
                for j in NINE_RANGE:
                    if value in row[j].get_candidates():
                        Counter = Counter + 1
                        Fields1.append((i,j))
                if(Counter<=3)and Counter > 1:
                    Fields2.append(Fields1.copy()) 
                    Fields1.clear()
                    Counter = 0
                else:
                    Fields1.clear()
                    Counter = 0     
            for a in range(0,len(Fields2)):
                for b in range(a+1,len(Fields2)):
                    for c in range(b+1,len(Fields2)):
                        Fields3.append(Fields2[a])
                        Fields3.append(Fields2[b])
                        Fields3.append(Fields2[c])
                        cols.clear()
                        for d in NINE_RANGE:
                            if self.check_15_2(Fields3,d):
                                cols.append(self.sudoku.get_column(d))
                        if len(cols) == 3:
                            colCount = 0
                            for l in NINE_RANGE:
                                if(value in cols[0][l].get_candidates()):
                                    colCount = colCount + 1
                                if(value in cols[1][l].get_candidates()):
                                    colCount = colCount + 1
                                if(value in cols[2][l].get_candidates()):
                                    colCount = colCount + 1
                            if colCount > (len(Fields2[0])+len(Fields2[1])+len(Fields2[2])):
                                removed_candidates: Dict[str, Any] = {}
                                row_fields = []
                                for fl in Fields3:
                                    for f in fl:
                                        row_fields.append(f)
                                for c in [c[0].get_coordinates()[1] for c in cols]:
                                    rem = remove_candidates_from_fields_in_unit(self.sudoku, UnitType.COLUMN, c, [value], row_fields)
                                    removed_candidates = {**removed_candidates, **rem}
                                if has_removed_candidates(removed_candidates):
                                    return (True, {
                                        'algorithm': 'swordfish_row',
                                        'fields': row_fields,
                                        'value': value,
                                        'removed_candidates': removed_candidates
                                    })
                        Fields3.clear()
        return (False,None)
    

    def check_15_1(self,Fields2:list,row:int)->bool:
        for a in range(0,len(Fields2[0])):
            for b in range(0,len(Fields2[1])):
                for c in range(0,len(Fields2[2])):
                    if (Fields2[0][a][0] == row or Fields2[1][b][0] == row or Fields2[2][c][0]== row):
                        return True
        return False
    
    def check_15_2(self,Fields2:list,col:int)->bool:
        for a in range(0,len(Fields2[0])):
            for b in range(0,len(Fields2[1])):
                for c in range(0,len(Fields2[2])):
                    if (Fields2[0][a][1] == col or Fields2[1][b][1] == col or Fields2[2][c][1]== col):
                        return True
        return False

    # Drachen
    def algorithm_16(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields: List[Field] = list()
        vStraight: List[Field] = list()
        vComplex: List[Field] = list()
        
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            for value in ALL_FIELD_VALUES:
                for j in NINE_RANGE:
                    if value in row[j].get_candidates():
                        fields.append(row[j])
                if len(fields) == 2 :
                    for k in range(0,2):
                        fields.reverse()
                        for field in fields:
                            if find_chain_16(self.sudoku, field, value)[0] and find_chain_16(self.sudoku, field, value)[1] != None and len(vComplex)==0: 
                                vComplex = find_chain_16(self.sudoku, field, value)[1]
                            elif find_chain_16_1(self.sudoku, field, value)[0] == True:
                                vStraight = find_chain_16_1(self.sudoku, field, value)[1]
                        if vStraight != None and vComplex != None and len(vComplex) > 2 and len(vStraight)>=2:
                            for a in range(3,len(vComplex)):
                                for b in range(0,len(vStraight)):
                                    if vComplex[a].get_coordinates()[0] == vStraight[b].get_coordinates()[0] and vComplex[a].get_coordinates()[1]==vStraight[0].get_coordinates()[1]:
                                        if value in vComplex[a].get_candidates():  # check whether its useful
                                            row = vStraight[0].get_coordinates()[0]
                                            fields_row, fields_col, row = [vStraight[0]], None, vStraight[0].get_coordinates()[0]
                                            if vComplex[0].get_coordinates()[0] == row:
                                                fields_row.append(vComplex[0])
                                                fields_col = [vComplex[1], vComplex[2]]
                                            elif vComplex[1].get_coordinates()[0] == row:
                                                fields_row.append(vComplex[1])
                                                fields_col = [vComplex[0], vComplex[2]]
                                            else:
                                                fields_row.append(vComplex[2])
                                                fields_col = [vComplex[0], vComplex[1]]
                                            vComplex[a].remove_candidate(value)
                                            y_rem, x_rem = vComplex[a].get_coordinates()
                                            return (True, {
                                                'algorithm': 'dragon',
                                                'value': value,
                                                'fields_row': [f.get_coordinates() for f in fields_row],
                                                'fields_col': [f.get_coordinates() for f in fields_col],
                                                'removed_candidates': {coordinates_to_key(y_rem, x_rem): [value]}
                                            })
                        fields.clear()
                        vStraight.clear()
                        vComplex.clear()      
                else:
                    fields.clear()
                    vStraight.clear()
                    vComplex.clear()   
                        
        return False,None
    
    def check_Viereck(self,fields:list)-> bool:
        if len(fields) == 4:
            for a in NINE_RANGE:
                rowCounter = 0
                for i in fields:
                    if i[0]==a:
                        rowCounter = rowCounter + 1
                    if rowCounter > 2:
                        return False
                if rowCounter < 2 and rowCounter > 0:
                    return False
                
            for a in NINE_RANGE:
                colCounter = 0
                for i in fields:
                    if i[1]== a:
                        colCounter = colCounter + 1
                    if colCounter > 2:
                        return False
                if colCounter < 2 and colCounter > 0:
                    return False
            return True      
        return False 
     
    #Viereck-Type1   
    def algorithm_17(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields1 = []
        fields2 = []
        returnField: List[Field] = []
        pos = 0
        for value1 in ALL_FIELD_VALUES:
            for value2 in range(value1+1,10):
                for i in NINE_RANGE:
                    for j in NINE_RANGE:
                        if value1 in self.sudoku.get_field(i,j).get_candidates() and value2 in self.sudoku.get_field(i,j).get_candidates():
                            fields1.append(self.sudoku.get_field(i,j).get_coordinates())
                fields2.clear()
                for a in range(0,len(fields1)):
                    for b in range(a+1,len(fields1)):
                        for c in range(b+1,len(fields1)):
                            for d in range(c+1,len(fields1)):
                                fields2.append(fields1[a])
                                fields2.append(fields1[b])
                                fields2.append(fields1[c])
                                fields2.append(fields1[d])
                                if self.check_Viereck(fields2):
                                    counter = 0
                                    for l in fields2:
                                        if len(self.sudoku.get_field(l[0],l[1]).get_candidates())==2:
                                            counter = counter +1
                                            returnField.append(self.sudoku.get_field(l[0],l[1]))
                                        else:
                                            pos = len(returnField)
                                            returnField.append(self.sudoku.get_field(l[0],l[1]))
                                    if counter == 3:
                                        returnField[pos].remove_candidate(value1)
                                        returnField[pos].remove_candidate(value2)
                                        y_rem, x_rem = returnField[pos].get_coordinates()
                                        return (True, {
                                            'algorithm': 'square_type_1',
                                            'values': [value1, value2],
                                            'fields': fields2,
                                            'removed_candidates': {coordinates_to_key(y_rem, x_rem): [value1, value2]}
                                        })
                                    pos = 0
                                fields2.clear()
                fields1.clear()
                                            
        return False,None
        
    #Viereck-Type2   
    def algorithm_18(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields1 = []
        fields2 = []
        returnField = []
        returnField2 = []
        returnValue = 0
        for value1 in ALL_FIELD_VALUES:
            for value2 in range(value1+1,10):
                for i in NINE_RANGE:
                    for j in NINE_RANGE:
                        if value1 in self.sudoku.get_field(i,j).get_candidates() and value2 in self.sudoku.get_field(i,j).get_candidates():
                            fields1.append(self.sudoku.get_field(i,j).get_coordinates())
                fields2.clear()
                for a in range(0,len(fields1)):
                    for b in range(a+1,len(fields1)):
                        for c in range(b+1,len(fields1)):
                            for d in range(c+1,len(fields1)):
                                fields2.append(fields1[a])
                                fields2.append(fields1[b])
                                fields2.append(fields1[c])
                                fields2.append(fields1[d])
                                if self.check_Viereck(fields2):
                                    counter = 0
                                    for l in fields2:
                                        if len(self.sudoku.get_field(l[0],l[1]).get_candidates())==2:
                                            counter = counter +1
                                            returnField.append(self.sudoku.get_field(l[0],l[1]))
                                        elif len(self.sudoku.get_field(l[0],l[1]).get_candidates())==3 and len(returnField2)==0:
                                            for k in self.sudoku.get_field(l[0],l[1]).get_candidates():
                                                if k != value1 and k != value2:
                                                    for g in fields2:
                                                        if k in self.sudoku.get_field(g[0],g[1]).get_candidates() and ((g[0]!=l[0] and g[1]==l[1])or(g[0]==l[0] and g[1]!=l[1])) and len(self.sudoku.get_field(g[0],g[1]).get_candidates()) ==3:
                                                            returnField.append(self.sudoku.get_field(l[0],l[1]))
                                                            returnField.append(self.sudoku.get_field(g[0],g[1]))
                                                            returnField2.append(self.sudoku.get_field(l[0],l[1]))
                                                            returnField2.append(self.sudoku.get_field(g[0],g[1]))
                                                            returnValue = k
                                                            
                                    if counter == 2 and len(returnField2)==2:
                                        marked_candidates_fields = [f.get_coordinates() for f in returnField2]
                                        common_units = get_common_units(marked_candidates_fields)
                                        removed_candidates: Dict[int, List[int]] = {}
                                        for type, nr in common_units:
                                            fields = self.sudoku.get_row(nr) if type == UnitType.ROW else self.sudoku.get_column(nr) if type == UnitType.COLUMN else self.sudoku.get_block(nr)
                                            rem = remove_candidates_from_fields(self.sudoku, [f.get_coordinates() for  f in fields], [returnValue], marked_candidates_fields)
                                            removed_candidates = {**removed_candidates, **rem}
                                        if has_removed_candidates(removed_candidates):
                                            return (True, {
                                                'algorithm': 'square_type_2',
                                                'value_removed': returnValue,
                                                'values_locked': [value1, value2],
                                                'fields': fields2,
                                                'fields_cricled_candidates': marked_candidates_fields,
                                                'removed_candidates': removed_candidates
                                            })
                                    returnField.clear()
                                    returnField2.clear()
                                fields2.clear()
                fields1.clear()
                                            
        return False,None
    
    #Viereck-Type4   
    def algorithm_20(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields1 = []
        fields2 = []
        fields3: List[Tuple[int, int]] = []
        for value1 in ALL_FIELD_VALUES:
            for value2 in range(value1+1,10):
                for i in NINE_RANGE:
                    for j in NINE_RANGE:
                        if value1 in self.sudoku.get_field(i,j).get_candidates() and value2 in self.sudoku.get_field(i,j).get_candidates():
                            fields1.append(self.sudoku.get_field(i,j).get_coordinates())
                fields2.clear()
                for a in range(0,len(fields1)):
                    for b in range(a+1,len(fields1)):
                        for c in range(b+1,len(fields1)):
                            for d in range(c+1,len(fields1)):
                                fields2.append(fields1[a])
                                fields2.append(fields1[b])
                                fields2.append(fields1[c])
                                fields2.append(fields1[d])
                                if self.check_Viereck(fields2):
                                    for l in fields2:
                                        if len(self.sudoku.get_field(l[0],l[1]).get_candidates()) >=3:
                                            fields3.append(l)
                                    if len(fields3)==2:
                                        value_removed, value_2nd = None, None
                                        #same block
                                        if Sudoku.get_block_nr(fields3[0][0],fields3[0][1]) == Sudoku.get_block_nr(fields3[1][0],fields3[1][1]):
                                            block = self.sudoku.get_block(Sudoku.get_block_nr(fields3[0][0],fields3[0][1]))
                                            counter = 0
                                            for b_f in block:
                                                if value1 in b_f.get_candidates():
                                                    counter = counter + 1
                                            if counter==2:
                                                value_removed, value_2nd = value2, value1
                                            counter = 0
                                            for b_f in block:
                                                if value2 in b_f.get_candidates():
                                                    counter = counter + 1
                                            if counter==2:
                                                value_removed, value_2nd = value1, value2
                                            counter = 0  
                                        #same row
                                        if fields3[0][0] == fields3[1][0]:
                                            row = self.sudoku.get_row(fields3[0][0])
                                            counter = 0
                                            for r_f in row:
                                                if value1 in r_f.get_candidates():
                                                    counter = counter + 1
                                            if counter==2:
                                                value_removed, value_2nd = value2, value1
                                            counter = 0
                                            for r_f in row:
                                                if value2 in r_f.get_candidates():
                                                    counter = counter + 1
                                            if counter==2:
                                                value_removed, value_2nd = value1, value2                              
                                        #same col
                                        if fields3[0][1] == fields3[1][1]:
                                            col = self.sudoku.get_column(fields3[0][1])
                                            counter = 0
                                            for c_f in col:
                                                if value1 in c_f.get_candidates():
                                                    counter = counter + 1
                                            if counter==2:
                                                value_removed, value_2nd = value2, value1
                                            counter = 0
                                            for c_f in col:
                                                if value2 in c_f.get_candidates():
                                                    counter = counter + 1
                                            if counter==2:
                                                value_removed, value_2nd = value1, value2
                                        if value_removed:
                                            removed_candidates = remove_candidates_from_fields(self.sudoku, fields3, [value_removed])
                                            fields_not_removed = []
                                            for f in fields2:
                                                if f not in fields3:
                                                    fields_not_removed.append(f)
                                            return (True, {
                                                'algorithm': 'square_type_4',
                                                'fields_not_removed': fields_not_removed,
                                                'value_removed': value_removed,
                                                'value_2nd': value_2nd,
                                                'removed_candidates': removed_candidates
                                            })
                                    fields3.clear()
                fields1.clear()                         
        return False,None
        
        
    #XY_wing  
    def algorithm_21(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields1: List[Field] = []
        fields2: List[Field] = []
        fields3: List[Field] = []
        err = False
        for value1 in ALL_FIELD_VALUES:
            for value2 in range(value1+1,10): 
                for value3 in range(value2+1,10):  
                    fields1.clear() 
                    for i in NINE_RANGE:
                        row = self.sudoku.get_row(i)
                        for j in NINE_RANGE:
                            if (value1 in row[j].get_candidates() or value2 in row[j].get_candidates() or value3 in row[j].get_candidates()) and len(row[j].get_candidates()) == 2:
                                for c in row[j].get_candidates():
                                    if c != value1 and c != value2 and c != value3:
                                        err = True
                                if not(err):  
                                    fields1.append(row[j])
                                err = False
                        
                    if len(fields1)>=3:
                        for f1 in range(0,len(fields1)):
                            for f2 in range(f1,len(fields1)):
                                for f3 in range(f2,len(fields1)):
                                    if fields1[f1].get_candidates() != fields1[f2].get_candidates() and fields1[f1].get_candidates() != fields1[f3].get_candidates() and fields1[f2].get_candidates() != fields1[f3].get_candidates():
                                        fields2.clear()
                                        fields2.append(fields1[f1])
                                        fields2.append(fields1[f2])
                                        fields2.append(fields1[f3])
                                        for f4 in fields2:
                                            counter = 0
                                            if (f4.get_coordinates() != fields1[f1].get_coordinates() and (Sudoku.get_block_nr(f4.get_coordinates()[0],f4.get_coordinates()[1]) == (Sudoku.get_block_nr(fields1[f1].get_coordinates()[0],fields1[f1].get_coordinates()[1])) or f4.get_coordinates()[0]== fields1[f1].get_coordinates()[0] or f4.get_coordinates()[1]== fields1[f1].get_coordinates()[1])):
                                                counter = counter + 1
                                            if (f4.get_coordinates() != fields1[f2].get_coordinates() and (Sudoku.get_block_nr(f4.get_coordinates()[0],f4.get_coordinates()[1]) == (Sudoku.get_block_nr(fields1[f2].get_coordinates()[0],fields1[f2].get_coordinates()[1])) or f4.get_coordinates()[0]== fields1[f2].get_coordinates()[0] or f4.get_coordinates()[1]== fields1[f2].get_coordinates()[1])):
                                                counter = counter + 1
                                            if (f4.get_coordinates() != fields1[f3].get_coordinates() and (Sudoku.get_block_nr(f4.get_coordinates()[0],f4.get_coordinates()[1]) == (Sudoku.get_block_nr(fields1[f3].get_coordinates()[0],fields1[f3].get_coordinates()[1])) or f4.get_coordinates()[0]== fields1[f3].get_coordinates()[0] or f4.get_coordinates()[1]== fields1[f3].get_coordinates()[1])):
                                                counter = counter + 1
                                            if counter == 2:
                                                for f5 in fields2:
                                                    for f6 in fields2:
                                                        if (Sudoku.get_block_nr(f5.get_coordinates()[0],f5.get_coordinates()[1]) != (Sudoku.get_block_nr(f6.get_coordinates()[0],f6.get_coordinates()[1])) and f5.get_coordinates()[0] != f6.get_coordinates()[0] and f5.get_coordinates()[1] != f6.get_coordinates()[1]):
                                                            if f5.get_coordinates()!=f4.get_coordinates() and f6.get_coordinates()!=f4.get_coordinates() and f5.get_coordinates() != f6.get_coordinates():
                                                                for a in f5.get_candidates():
                                                                    for b in f6.get_candidates():
                                                                        if a == b:
                                                                            fields3.clear()
                                                                            for i2 in NINE_RANGE:
                                                                                col = self.sudoku.get_column(i2)
                                                                                for j2 in NINE_RANGE:
                                                                                    if (a in col[j2].get_candidates() and (col[j2].get_coordinates()[0] == f5.get_coordinates()[0] or col[j2].get_coordinates()[1] == f5.get_coordinates()[1] or Sudoku.get_block_nr(col[j2].get_coordinates()[0],col[j2].get_coordinates()[1]) == Sudoku.get_block_nr(f5.get_coordinates()[0],f5.get_coordinates()[1]))
                                                                                        and (col[j2].get_coordinates()[0] == f6.get_coordinates()[0] or col[j2].get_coordinates()[1] == f6.get_coordinates()[1] or Sudoku.get_block_nr(col[j2].get_coordinates()[0],col[j2].get_coordinates()[1]) == Sudoku.get_block_nr(f6.get_coordinates()[0],f6.get_coordinates()[1]))): 
                                                                                            fields3.append(col[j2].get_coordinates())
                                                                            if len(fields3) != 0:
                                                                                removed_candidates = remove_candidates_from_fields(self.sudoku, fields3, [a])
                                                                                if has_removed_candidates(removed_candidates):
                                                                                    value1
                                                                                    return (True, {
                                                                                        'algorithm': 'xy_wing',
                                                                                        'fields': [f4.get_coordinates(), f5.get_coordinates(), f6.get_coordinates()],
                                                                                        'values': [value1, value2, value3],
                                                                                        'value_removed': a,
                                                                                        'removed_candidates': removed_candidates
                                                                                    })                                                            
        return False,None    
    
    #XYZ-Wing   
    def algorithm_22(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields1: List[Field] = []
        fields2: List[Field] = []
        fields21: List[Field] = []
        fields3: List[Field] = []
        err = False
        for value1 in ALL_FIELD_VALUES:
            for value2 in range(value1+1,10): 
                for value3 in range(value2+1,10):  
                    fields1.clear() 
                    for i in NINE_RANGE:
                        row = self.sudoku.get_row(i)
                        for j in NINE_RANGE:
                            if (value1 in row[j].get_candidates() or value2 in row[j].get_candidates() or value3 in row[j].get_candidates()):
                                for c in row[j].get_candidates():
                                    if c != value1 and c != value2 and c != value3:
                                        err = True
                                if not(err):  
                                    fields1.append(row[j])
                                err = False
                        
                    if len(fields1)>=3:
                        for f1 in range(0,len(fields1)):
                            for f2 in range(f1,len(fields1)):
                                for f3 in range(f2,len(fields1)):
                                    if fields1[f1].get_candidates() != fields1[f2].get_candidates() and fields1[f1].get_candidates() != fields1[f3].get_candidates() and fields1[f2].get_candidates() != fields1[f3].get_candidates():
                                        fields2.clear()
                                        fields2.append(fields1[f1])
                                        fields2.append(fields1[f2])
                                        fields2.append(fields1[f3])
                                        for f in range(0,len(fields2)):
                                            if len(fields2[f].get_candidates())==3:
                                                fields2.append(fields2[f])
                                                fields2.pop(f)
                                                
                                        if len(fields2[0].get_candidates())==2 and len(fields2[1].get_candidates())==2 and len(fields2[2].get_candidates())==3:
                                            counter = 0
                                            if ((Sudoku.get_block_nr(fields2[2].get_coordinates()[0],fields2[2].get_coordinates()[1]) == (Sudoku.get_block_nr(fields2[0].get_coordinates()[0],fields2[0].get_coordinates()[1])) or fields2[2].get_coordinates()[0]== fields2[0].get_coordinates()[0] or fields2[2].get_coordinates()[1]== fields2[0].get_coordinates()[1])):
                                                counter = counter + 1
                                            if ((Sudoku.get_block_nr(fields2[2].get_coordinates()[0],fields2[2].get_coordinates()[1]) == (Sudoku.get_block_nr(fields2[1].get_coordinates()[0],fields2[1].get_coordinates()[1])) or fields2[2].get_coordinates()[0]== fields2[1].get_coordinates()[0] or fields2[2].get_coordinates()[1]== fields2[1].get_coordinates()[1])):
                                                counter = counter + 1

                                            if counter == 2:
                                                if (Sudoku.get_block_nr(fields2[0].get_coordinates()[0],fields2[0].get_coordinates()[1]) != (Sudoku.get_block_nr(fields2[1].get_coordinates()[0],fields2[1].get_coordinates()[1])) and fields2[0].get_coordinates()[0] != fields2[1].get_coordinates()[0] and fields2[0].get_coordinates()[1] != fields2[1].get_coordinates()[1]):
                                                        for a in fields2[2].get_candidates():
                                                                if a in fields2[0].get_candidates() and a in fields2[1].get_candidates():
                                                                    fields3.clear()
                                                                    for i2 in NINE_RANGE:
                                                                        col = self.sudoku.get_column(i2)
                                                                        for j2 in NINE_RANGE:
                                                                            if (a in col[j2].get_candidates() and (col[j2].get_coordinates()[0] == fields2[0].get_coordinates()[0] or col[j2].get_coordinates()[1] == fields2[0].get_coordinates()[1] or Sudoku.get_block_nr(col[j2].get_coordinates()[0],col[j2].get_coordinates()[1]) == Sudoku.get_block_nr(fields2[0].get_coordinates()[0],fields2[0].get_coordinates()[1]))
                                                                                and (col[j2].get_coordinates()[0] == fields2[1].get_coordinates()[0] or col[j2].get_coordinates()[1] == fields2[1].get_coordinates()[1] or Sudoku.get_block_nr(col[j2].get_coordinates()[0],col[j2].get_coordinates()[1]) == Sudoku.get_block_nr(fields2[1].get_coordinates()[0],fields2[1].get_coordinates()[1]))
                                                                                and (col[j2].get_coordinates()[0] == fields2[2].get_coordinates()[0] or col[j2].get_coordinates()[1] == fields2[2].get_coordinates()[1] or Sudoku.get_block_nr(col[j2].get_coordinates()[0],col[j2].get_coordinates()[1]) == Sudoku.get_block_nr(fields2[2].get_coordinates()[0],fields2[2].get_coordinates()[1]))
                                                                                and col[j2].get_coordinates() != fields2[2].get_coordinates()): 
                                                                                    fields3.append(col[j2].get_coordinates())
                                                                    if len(fields3) != 0:
                                                                        removed_candidates = remove_candidates_from_fields(self.sudoku, fields3, [a])
                                                                        if has_removed_candidates(removed_candidates):
                                                                            return (True, {
                                                                                'algorithm': 'xyz_wing',
                                                                                'fields': [f.get_coordinates() for f in fields2],
                                                                                'values': [value1, value2, value3],
                                                                                'value_removed': a,
                                                                                'removed_candidates': removed_candidates
                                                                            })                              
        return False,None 
            
           
    #X-Chain   
    def algorithm_23(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields1 = []  # all fields with the checked candidate
        fields2 = []
        fieldstrue: List[Tuple[int,int]] = []
        fieldsfalse: List[Tuple[int,int]] = []
        ccounter = 0
        rcounter = 0
        bcounter = 0
        counter1 = 0
        counter2 = 0
        for value in ALL_FIELD_VALUES:
            fields1.clear()
            for i in NINE_RANGE:
                row = self.sudoku.get_row(i)
                for j in NINE_RANGE:
                    if value in row[j].get_candidates():
                        fields1.append(row[j].get_coordinates())
            fieldstrue.clear()
            fieldsfalse.clear()
            err = False
            for f1 in range(0,len(fields1)):
                for f2 in range(f1+1,len(fields1)):
                    ccounter = 0
                    rcounter = 0
                    bcounter = 0
                    # ckeck if both fields are in the same unit and if they are the only ones with the candidate in there
                    if (Sudoku.get_block_nr(fields1[f1][0],fields1[f1][1]) == (Sudoku.get_block_nr(fields1[f2][0],fields1[f2][1]))): 
                        block = self.sudoku.get_block(Sudoku.get_block_nr(fields1[f1][0],fields1[f1][1]))
                        bcounter = 0
                        for j in NINE_RANGE:
                            if value in block[j].get_candidates():
                                bcounter = bcounter + 1               
                    if(fields1[f1][0]== fields1[f2][0]):
                        row2 = self.sudoku.get_row(fields1[f1][0])
                        rcounter = 0
                        for j in NINE_RANGE:
                            if value in row2[j].get_candidates():
                                rcounter = rcounter + 1                   
                    if(fields1[f1][1]== fields1[f2][1]):
                        col = self.sudoku.get_column(fields1[f1][1])
                        ccounter = 0
                        for j in NINE_RANGE:
                            if value in col[j].get_candidates():
                                ccounter = ccounter + 1  
                    if rcounter > 2 or bcounter > 2 or ccounter > 2:
                        err = True
                    if rcounter == 2 or bcounter == 2 or ccounter == 2:
                        if not(fields1[f1] in fieldstrue):
                            if not(fields1[f1] in fieldsfalse):
                                if not(fields1[f2] in fieldstrue):
                                    if not(fields1[f2] in fieldsfalse):
                                       fieldstrue.append(fields1[f1])
                                       fieldsfalse.append(fields1[f2])
                                    else:
                                        fieldstrue.append(fields1[f1])
                                else:
                                    fieldsfalse.append(fields1[f1])
                            else:
                                if not(fields1[f2] in fieldstrue):
                                    if not(fields1[f2] in fieldsfalse):
                                        fieldstrue.append(fields1[f2])
                        else:
                            if not(fields1[f2] in fieldsfalse):
                                if not(fields1[f2] in fieldstrue):
                                    fieldsfalse.append(fields1[f2])
            
            r_cnt, c_cnt, b_cnt = 0, 0, 0
            err2 = False
            for ft in fieldstrue:
                for ff in fieldsfalse:
                    # same unit?
                    r_cnt, c_cnt, b_cnt = 0, 0, 0
                    if ft[0] == ff[0]:
                        row3 = self.sudoku.get_row(ft[0])
                        for f in row3:
                            if value in f.get_candidates():
                                r_cnt += 1
                    if ft[1] == ff[1]:
                        col2 = self.sudoku.get_column(ft[1])
                        for f in col2:
                            if value in f.get_candidates():
                                c_cnt += 1
                    if Sudoku.get_block_nr(ft[0], ft[1]) == Sudoku.get_block_nr(ff[0], ff[1]):
                        blk2 = self.sudoku.get_block(Sudoku.get_block_nr(ft[0], ft[1]))
                        for f in blk2:
                            if value in f.get_candidates():
                                b_cnt += 1
                if not (r_cnt > 2 or c_cnt > 2 or b_cnt > 2):
                    err2 = True
            if not(err2):
                while(not(counter1 >=2 and counter2 >=2) or len(fieldstrue)>=1 or len(fieldsfalse)>=1):
                    for f4 in fieldstrue:
                        counter1 = 0
                        for f5 in fieldsfalse:
                            if (f4[0] == f5[0] or f4[1]==f5[1] or Sudoku.get_block_nr(f4[0],f4[1]) == (Sudoku.get_block_nr(f5[0],f5[1]))):
                                counter1 = counter1 + 1
                        if counter1 <= 1:
                            fieldstrue.remove(f4)
                            break 
                        
                    for f4 in fieldsfalse:
                        counter2 = 0
                        for f5 in fieldstrue.copy():
                            if (f4[0] == f5[0] or f4[1]==f5[1] or Sudoku.get_block_nr(f4[0],f4[1]) == (Sudoku.get_block_nr(f5[0],f5[1]))):
                                counter2 = counter2 + 1
                        if counter2 <= 1:
                            fieldsfalse.remove(f4)
                            break   
                    if(counter1 >=2 and counter2 >=2) or len(fieldstrue)<=1 or len(fieldsfalse)<=1:
                        break           
                fields2.clear()
                if counter1 >=2 and counter2 >=2 :
                    for f3 in fields1:
                        if not(f3 in fieldsfalse) and not(f3 in fieldstrue):
                            for f1 in fieldstrue:
                                for f2 in fieldsfalse:
                                    if ((f3[0] == f1[0] or f3[1]==f1[1] or Sudoku.get_block_nr(f3[0],f3[1]) == (Sudoku.get_block_nr(f1[0],f1[1])))
                                        and (f3[0] == f2[0] or f3[1]==f2[1] or Sudoku.get_block_nr(f3[0],f3[1]) == (Sudoku.get_block_nr(f2[0],f2[1])))):
                                        if not(f3 in fields2):
                                            fields2.append(f3)
                    if len(fields2)>0:
                        removed_candidates = remove_candidates_from_fields(self.sudoku, fields2, [value])
                        if has_removed_candidates(removed_candidates):
                            return (True, {
                                'algorithm': 'x_chain',
                                'fields': [fieldstrue, fieldsfalse],
                                'value': value,
                                'removed_candidates': removed_candidates
                            })
        return False,None       
    
    #XY-Chain 
    def algorithm_24(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        fields1:  List[Field] = []
        returnFields:  List[Field] = []
        for i in NINE_RANGE:
            row = self.sudoku.get_row(i)
            for j in NINE_RANGE:
                if len(row[j].get_candidates())==2:
                    fields1.append(row[j])
        for f in fields1:
            if self.check_middle(fields1,f)[0]:
                fields3 = self.check_middle(fields1,f)[1]
                fields4 = self.check_middle(fields1,f)[2]
                for f1 in fields3:
                    for f2 in fields4:
                        fields21 = fields1.copy()
                        fields22 = fields1.copy()
                        for c1 in f1.get_candidates():
                            if c1 != f.get_candidates()[0]:
                               candidate1 = c1
                        for c2 in f2.get_candidates():
                            if c2 != f.get_candidates()[1]:    
                                candidate2 = c2
                        fields6 = self.get_chain_24(fields22,f2,candidate2)
                        fields5 = self.get_chain_24(fields21,f1,candidate1)
                        if fields5 == None:
                            fields5 == [candidate1,f1]
                        else:
                            fields5.append([candidate1,f1])
                        if fields6 == None:
                            fields6 == [candidate2,f2]
                        else:
                            fields6.append([candidate2,f2])
                        if fields6 != None and fields5 != None:
                            for f3 in fields5:
                                for f4 in fields6:
                                    if f3[0] == f4[0]:
                                        if f3[1].get_coordinates() != f4[1].get_coordinates():
                                            for i in NINE_RANGE:
                                                row2 = self.sudoku.get_row(i)
                                                for j in NINE_RANGE:
                                                    if (f3[0] in row2[j].get_candidates() and (Sudoku.get_block_nr(f3[1].get_coordinates()[0],f3[1].get_coordinates()[1]) == Sudoku.get_block_nr(row2[j].get_coordinates()[0],row2[j].get_coordinates()[1]) or f3[1].get_coordinates()[0] == row2[j].get_coordinates()[0] or f3[1].get_coordinates()[1] == row2[j].get_coordinates()[1])
                                                        and (Sudoku.get_block_nr(row2[j].get_coordinates()[0],row2[j].get_coordinates()[1]) == Sudoku.get_block_nr(f4[1].get_coordinates()[0],f4[1].get_coordinates()[1]) or row2[j].get_coordinates()[0] == f4[1].get_coordinates()[0] or row2[j].get_coordinates()[1] == f4[1].get_coordinates()[1])
                                                        and row2[j].get_coordinates() != f3[1].get_coordinates()  and row2[j].get_coordinates() != f4[1].get_coordinates()):
                                                        returnFields.append(row2[j])
                                            if len(returnFields) >= 1:
                                                value = f3[0]
                                                removed_candidates = remove_candidates_from_fields(self.sudoku, [f.get_coordinates() for f in returnFields], [value])
                                                # already checked if useful
                                                return (True, {
                                                    'algorithm': 'xy_chain',
                                                    'end_fields': [f3[1].get_coordinates(), f4[1].get_coordinates()],
                                                    'value': value,
                                                    'middle_field': f.get_coordinates(),
                                                    'removed_candidates': removed_candidates
                                                })
                    
        return False,None 
    
    def get_chain_24(self,fields1:  List[Field],field: Field,candidate: int) -> List[Tuple[int,Field]]:
        returnTuple = []
        fields2 = []
        if field in fields1:
            fields1.remove(field)
        for f in fields1:
            if candidate in f.get_candidates() and (Sudoku.get_block_nr(f.get_coordinates()[0],f.get_coordinates()[1]) == Sudoku.get_block_nr(field.get_coordinates()[0],field.get_coordinates()[1]) or f.get_coordinates()[0] == field.get_coordinates()[0] or f.get_coordinates()[1] == field.get_coordinates()[1]):
                for c in f.get_candidates():
                    if c != candidate:
                        fields2 = fields1.copy()
                        a = self.get_chain_24(fields2,f,c)
                        if a != None:
                            for a1 in a:
                                returnTuple.append(a1) 
                            returnTuple.append([c,f])
                        else:
                            returnTuple.append([c,f])
        if len(returnTuple)==0:         
            return None
        else:
            return returnTuple

    def check_middle(self,fields1:  List[Field],field: Field) -> Tuple[bool, Optional[List[Field]], Optional[List[Field]]]:
        fields2:  List[Field] = []
        fields3:  List[Field] = []
        for f in fields1:
            if f.get_coordinates() != field.get_coordinates() and (Sudoku.get_block_nr(f.get_coordinates()[0],f.get_coordinates()[1]) == Sudoku.get_block_nr(field.get_coordinates()[0],field.get_coordinates()[1]) or f.get_coordinates()[0] == field.get_coordinates()[0] or f.get_coordinates()[1] == field.get_coordinates()[1]):
                if field.get_candidates()[0] in f.get_candidates():
                    fields2.append(f)
                if field.get_candidates()[1] in f.get_candidates():
                    fields3.append(f)
        if len(fields2) >= 1 and len(fields3) >= 1:
            return True,fields2,fields3
        return False,None,None

    #swordfish fin col
    def algorithm_25_1(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        Fields1 = []
        Fields2 = []
        Fields3 = []
        field: Tuple[int,int] = None
        rows = list()   
        for value in ALL_FIELD_VALUES:
            Counter = 0
            Fields1.clear()
            Fields2.clear()
            for i in NINE_RANGE:
                col = self.sudoku.get_column(i)
                for j in NINE_RANGE:
                    if value in col[j].get_candidates():
                        Counter = Counter + 1
                        Fields1.append((j,i))
                if(Counter<=4)and Counter > 1:
                    Fields2.append(Fields1.copy()) 
                    Fields1.clear()
                    Counter = 0
                else:
                    Fields1.clear()
                    Counter = 0
            Fields2.sort(key=len)     
            for a in range(0,len(Fields2)):
                for b in range(a+1,len(Fields2)):
                    for c in range(b+1,len(Fields2)):
                            Fields3.append(Fields2[a])
                            Fields3.append(Fields2[b])
                            Fields3.append(Fields2[c])
                            rows.clear()
                            for d in NINE_RANGE:
                                if self.check_25_1(Fields3,d):
                                    rows.append(self.sudoku.get_row(d))
                            if len(rows) == 3:
                                for e in Fields3:
                                    for e1 in e:
                                        if(rows[0][0].get_coordinates()[0] != e1[0] and rows[1][0].get_coordinates()[0] != e1[0] and rows[2][0].get_coordinates()[0] != e1[0]):
                                            field = e1
                                rowCount = 0
                                for l in NINE_RANGE:
                                    if(field and value in rows[0][l].get_candidates()) and rows[0][l].get_coordinates()!= field and Sudoku.get_block_nr(rows[0][l].get_coordinates()[0],rows[0][l].get_coordinates()[1]) == Sudoku.get_block_nr(field[0],field[1]):
                                        check = False
                                        for e in Fields3:
                                            for e1 in e:
                                                if(rows[0][l].get_coordinates()[0] == e1[0] and rows[0][l].get_coordinates()[1] == e1[1]):
                                                    check = True
                                        if not(check):
                                            rowCount = rowCount + 1
                                    if(field and value in rows[1][l].get_candidates()) and rows[1][l].get_coordinates()!= field and Sudoku.get_block_nr(rows[1][l].get_coordinates()[0],rows[1][l].get_coordinates()[1]) == Sudoku.get_block_nr(field[0],field[1]):
                                        check = False
                                        for e in Fields3:
                                            for e1 in e:
                                                if(rows[1][l].get_coordinates()[0] == e1[0] and rows[1][l].get_coordinates()[1] == e1[1]):
                                                    check = True
                                        if not(check):
                                            rowCount = rowCount + 1
                                    if(field and value in rows[2][l].get_candidates()) and rows[2][l].get_coordinates()!= field and Sudoku.get_block_nr(rows[2][l].get_coordinates()[0],rows[2][l].get_coordinates()[1]) == Sudoku.get_block_nr(field[0],field[1]):
                                        check = False
                                        for e in Fields3:
                                            for e1 in e:
                                                if(rows[2][l].get_coordinates()[0] == e1[0] and rows[2][l].get_coordinates()[1] == e1[1]):
                                                    check = True
                                        if not(check):
                                            rowCount = rowCount + 1
                                if rowCount > 1:
                                    block_nr = Sudoku.get_block_nr(field[0], field[1])
                                    col_fields = []
                                    for fl in Fields3:
                                        for f in fl:
                                            col_fields.append(f)
                                    removed_candidates: Dict[str, Any] = {}
                                    row_nrs = [r[0].get_coordinates()[0] for r in rows] 
                                    counter = 0
                                    for f1 in col_fields:
                                        if not(f1[0] in row_nrs):
                                            counter = counter +1
                                    if counter == 1:
                                        for r in row_nrs:
                                            fields = intersection_of_units(UnitType.ROW, r, UnitType.BLOCK, block_nr)
                                            rem = remove_candidates_from_fields(self.sudoku, fields, [value], col_fields)
                                            removed_candidates = {**removed_candidates, **rem}
                                        if has_removed_candidates(removed_candidates):
                                            return (True, {
                                                'algorithm': 'swordfish_fin_col',
                                                'fields': col_fields,
                                                'value': value,
                                                'row_nrs': row_nrs,
                                                'removed_candidates': removed_candidates
                                            })
                            Fields3.clear()
        return (False,None)
    
    #swordfish fin row
    def algorithm_25_2(self) -> Tuple[bool, Optional[Dict[str, Any]]]:
        Fields1 = []
        Fields2 = []
        Fields3 = []
        field: Tuple[int,int] = None
        cols = list()      
        for value in ALL_FIELD_VALUES:
            Counter = 0
            Fields1.clear()
            Fields2.clear()
            for i in NINE_RANGE:
                row = self.sudoku.get_row(i)
                for j in NINE_RANGE:
                    if value in row[j].get_candidates():
                        Counter = Counter + 1
                        Fields1.append((i,j))
                if(Counter<=4)and Counter > 1:
                    Fields2.append(Fields1.copy()) 
                    Fields1.clear()
                    Counter = 0
                else:
                    Fields1.clear()
                    Counter = 0
            Fields2.sort(key=len)     
            for a in range(0,len(Fields2)):
                for b in range(a+1,len(Fields2)):
                    for c in range(b+1,len(Fields2)):
                            Fields3.append(Fields2[a])
                            Fields3.append(Fields2[b])
                            Fields3.append(Fields2[c])
                            cols.clear()
                            for d in NINE_RANGE:
                                if self.check_25_2(Fields3,d):
                                    cols.append(self.sudoku.get_column(d))
                            if len(cols) == 3:
                                for e in Fields3:
                                    for e1 in e:
                                        if(cols[0][0].get_coordinates()[1] != e1[1] and cols[1][0].get_coordinates()[1] != e1[1] and cols[2][0].get_coordinates()[1] != e1[1]):
                                            field = e1
                                rowCount = 0
                                for l in NINE_RANGE:
                                    if(field and value in cols[0][l].get_candidates()) and cols[0][l].get_coordinates()!= field and Sudoku.get_block_nr(cols[0][l].get_coordinates()[0],cols[0][l].get_coordinates()[1]) == Sudoku.get_block_nr(field[0],field[1]):
                                        check = False
                                        for e in Fields3:
                                            for e1 in e:
                                                if(cols[0][l].get_coordinates()[0] == e1[0] and cols[0][l].get_coordinates()[1] == e1[1]):
                                                    check = True
                                        if not(check):
                                            rowCount = rowCount + 1
                                    if(field and value in cols[1][l].get_candidates()) and cols[1][l].get_coordinates()!= field and Sudoku.get_block_nr(cols[1][l].get_coordinates()[0],cols[1][l].get_coordinates()[1]) == Sudoku.get_block_nr(field[0],field[1]):
                                        check = False
                                        for e in Fields3:
                                            for e1 in e:
                                                if(cols[1][l].get_coordinates()[0] == e1[0] and cols[1][l].get_coordinates()[1] == e1[1]):
                                                    check = True
                                        if not(check):
                                            rowCount = rowCount + 1
                                    if(field and value in cols[2][l].get_candidates()) and cols[2][l].get_coordinates()!= field and Sudoku.get_block_nr(cols[2][l].get_coordinates()[0],cols[2][l].get_coordinates()[1]) == Sudoku.get_block_nr(field[0],field[1]):
                                        check = False
                                        for e in Fields3:
                                            for e1 in e:
                                                if(cols[2][l].get_coordinates()[0] == e1[0] and cols[2][l].get_coordinates()[1] == e1[1]):
                                                    check = True
                                        if not(check):
                                            rowCount = rowCount + 1
                                if rowCount > 1:
                                    block_nr = Sudoku.get_block_nr(field[0], field[1])
                                    row_fields = []
                                    for fl in Fields3:
                                        for f in fl:
                                            row_fields.append(f)
                                    removed_candidates: Dict[str, Any] = {}
                                    col_nrs = [c[0].get_coordinates()[1] for c in cols]
                                    counter = 0
                                    for f1 in row_fields:
                                        if not(f1[1] in col_nrs):
                                            counter = counter +1
                                    if counter == 1: 
                                        for c in col_nrs:
                                            fields = intersection_of_units(UnitType.COLUMN, c, UnitType.BLOCK, block_nr)
                                            rem = remove_candidates_from_fields(self.sudoku, fields, [value], row_fields)
                                            removed_candidates = {**removed_candidates, **rem}
                                        if has_removed_candidates(removed_candidates):
                                            return (True, {
                                                'algorithm': 'swordfish_fin_row',
                                                'fields': row_fields,
                                                'value': value,
                                                'col_nrs': col_nrs,
                                                'removed_candidates': removed_candidates
                                            })
                            Fields3.clear()
        return (False,None)


    def check_25_1(self,Fields2:list,row:int)->bool:
        for a in range(0,len(Fields2[0])):
            for b in range(0,len(Fields2[1])):
                for c in range(0,len(Fields2[2])):
                    if ((Fields2[0][a][0] == row and  Fields2[1][b][0] == row) or (Fields2[0][a][0] == row and Fields2[2][c][0]== row) or (Fields2[1][b][0] == row and Fields2[2][c][0]== row)):
                        return True
        return False
    
    def check_25_2(self,Fields2:list,col:int)->bool:
        for a in range(0,len(Fields2[0])):
            for b in range(0,len(Fields2[1])):
                for c in range(0,len(Fields2[2])):
                    if ((Fields2[0][a][1] == col and  Fields2[1][b][1] == col) or (Fields2[0][a][1] == col and Fields2[2][c][1]== col) or (Fields2[1][b][1] == col and Fields2[2][c][1]== col)):
                        return True
        return False
    #W-Wing
    def algorithm_26(self) -> Tuple[bool, Optional[str]]:
        fields1: List[Field] = []
        fields2: List[Field] = []
        field: Field = None
        value: List[int]= []
        for value1 in ALL_FIELD_VALUES:
            for value2 in range(value1+1,10):
                value.append(value1)
                value.append(value2)
                for i in NINE_RANGE:
                    row = self.sudoku.get_row(i)
                    for j in NINE_RANGE:
                        if value1 in row[j].get_candidates() and value2 in row[j].get_candidates() and len(row[j].get_candidates())==2:
                            fields1.append(row[j])
                for f1 in range(0,len(fields1)):
                    for f2 in range(f1+1,len(fields1)):    
                        for i in NINE_RANGE:
                            row2 = self.sudoku.get_row(i)
                            for v1 in value:
                                for j in NINE_RANGE:
                                    if v1 in row2[j].get_candidates() and row2[j].get_coordinates()!=fields1[f1].get_coordinates() and row2[j].get_coordinates()!=fields1[f2].get_coordinates():
                                        fields2.append(row2[j])
                            
                                if len(fields2)==2:
                                    if ((fields2[0].get_coordinates()[1]== fields1[f1].get_coordinates()[1] or fields2[0].get_coordinates()[1]== fields1[f2].get_coordinates()[1]) 
                                        and (fields2[1].get_coordinates()[1]== fields1[f1].get_coordinates()[1] or fields2[1].get_coordinates()[1]== fields1[f2].get_coordinates()[1])):
                                        for v2 in value:
                                            if (v2 != v1 and (v2 in self.sudoku.get_field(fields1[f1].get_coordinates()[0], fields1[f2].get_coordinates()[1]).get_candidates())
                                                and (self.sudoku.get_field(fields1[f1].get_coordinates()[0], fields1[f2].get_coordinates()[1]).get_coordinates() != fields1[f1].get_coordinates())
                                                and (self.sudoku.get_field(fields1[f1].get_coordinates()[0], fields1[f2].get_coordinates()[1]).get_coordinates() != fields1[f2].get_coordinates())):
                                                field = self.sudoku.get_field(fields1[f1].get_coordinates()[0], fields1[f2].get_coordinates()[1])
                                            elif (v2 != v1 and (v2 in self.sudoku.get_field(fields1[f2].get_coordinates()[0], fields1[f1].get_coordinates()[1]).get_candidates())
                                                and (self.sudoku.get_field(fields1[f2].get_coordinates()[0], fields1[f1].get_coordinates()[1]).get_coordinates() != fields1[f1].get_coordinates())
                                                and (self.sudoku.get_field(fields1[f2].get_coordinates()[0], fields1[f1].get_coordinates()[1]).get_coordinates() != fields1[f2].get_coordinates())):
                                                field = self.sudoku.get_field(fields1[f2].get_coordinates()[0], fields1[f1].get_coordinates()[1])
                                            if field != None:
                                                # already checked if improvement is made
                                                field.remove_candidate(v2)
                                                y_rem, x_rem = field.get_coordinates()
                                                removed_candidates = {coordinates_to_key(y_rem, x_rem): [v2]}
                                                return (True, {
                                                    'algorithm': 'w_wing',
                                                    'fields_1': [fields1[f1].get_coordinates(), fields1[f2].get_coordinates()],
                                                    'fields_2': [fields2[0].get_coordinates(), fields2[1].get_coordinates()],
                                                    'values_locked': value,
                                                    'removed_candidates': removed_candidates
                                                })
                            fields2.clear()
                value.clear()
                fields1.clear()
        return False,None 