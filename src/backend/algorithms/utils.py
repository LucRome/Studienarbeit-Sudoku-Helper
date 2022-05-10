from sudoku.base import Sudoku, Field

# TODO: implement Function that removes the given candidates from the fields in the given unit, except the given fields

def remove_candidates_from_fields_in_unit(self, sudoku: Sudoku,type: Literal['row', 'block', 'column'], nr: int,
    candidates_to_remove: List[int], excluded_fields: List[Tuple[int, int]]) -> Dict[Tuple[int, int], List[int]]:
    """
    Removes the given candidates from the fields of the given unit (except the excluded fields)
    :param type: The unit Type (row/block/column)
    :param nr: The nr of the unit (row nr/block nr/column nr)
    :param candidates_to_remove: The list of the candidates to remove
    :param excluded fields: The coordinates of the fields to exclude
    :returns: Dictionary of all the removed candidates
    """

    if type == 'row':
        unit = self.get_row(nr)
    elif type == 'block':
        unit = self.get_block(nr)
    else:
        unit == self.get_column(nr)

    for field in unit:
        if field