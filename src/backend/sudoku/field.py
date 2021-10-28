from typing import List, Optional
from exceptions import *

class Field:
    """
    represents a single field 
    with a value and the candidates
    """
    __value: Optional[int]
    __candidates: List[int] = list()

    def set_value(self, val: int) -> None:
        if val < 0 or val > 9:
            raise WrongFieldValueExcetion(val)
        else:
            self.__value = val
    
    def add_candidate(self, val: int) -> None:
        if val < 0 or val > 9:
            raise WrongFieldCandidateException(val)
        else:
            if val not in self.__candidates:
                self.__candidates.append(val)
    
    def remove_candidate(self, val: int) -> None:
        try:
            self.__candidates.remove(val)
        except ValueError:
            pass

    def get_value(self) -> Optional[int]:
        return self.__value
    
    def get_candidates(self) -> List[int]:
        return self.__candidates
    


