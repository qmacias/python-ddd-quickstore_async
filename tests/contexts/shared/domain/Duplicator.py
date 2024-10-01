from typing import Any
from copy import deepcopy


class Duplicator:
    @staticmethod
    def with_(
            obj: Any,
            new_params: dict,
    ) -> Any:
        duplicated = deepcopy(obj)

        for k, v in new_params.items():
            setattr(duplicated, k, v)

        return duplicated
