import json
from typing import Iterable, Sequence, Union, Any, List

FeatureInput = Union[None, int, str, Sequence[Any]]


def _coerce_int(value: Any) -> int:
    """Best-effort conversion of assorted scalar values into ints."""
    if value is None:
        raise ValueError('Cannot convert None to int')
    if isinstance(value, bool):
        raise ValueError('Boolean values are not valid feature IDs')
    if isinstance(value, int):
        return int(value)
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        raise ValueError('Feature IDs must be whole numbers')
    text = str(value).strip()
    if not text:
        raise ValueError('Empty strings are not valid feature IDs')
    return int(text)


def serialize_feature_ids(value: FeatureInput) -> Union[str, None]:
    """Convert user input into a deterministic JSON string suitable for storage."""
    if value is None:
        return None

    if isinstance(value, str):
        normalized = value.strip()
        if not normalized:
            return None
        if normalized.startswith('['):
            try:
                parsed = json.loads(normalized)
                if isinstance(parsed, list):
                    return json.dumps([_coerce_int(item) for item in parsed])
            except json.JSONDecodeError:
                pass
        tokens = [token.strip() for token in normalized.split(',')]
        cleaned: List[int] = []
        for token in tokens:
            if not token:
                continue
            try:
                cleaned.append(_coerce_int(token))
            except (TypeError, ValueError):
                continue
        return json.dumps(cleaned)

    if not isinstance(value, (list, tuple, set)):
        iterable: Iterable[Any] = [value]
    else:
        iterable = value

    cleaned_list = []
    for item in iterable:
        try:
            cleaned_list.append(_coerce_int(item))
        except (TypeError, ValueError):
            continue
    return json.dumps(cleaned_list)


def deserialize_feature_ids(value: FeatureInput) -> List[int]:
    """Convert the stored value back into a list of ints for API responses."""
    if value in (None, '', []):
        return []

    if isinstance(value, (list, tuple, set)):
        result: List[int] = []
        for item in value:
            try:
                result.append(_coerce_int(item))
            except (TypeError, ValueError):
                continue
        return result

    if isinstance(value, str):
        normalized = value.strip()
        if not normalized:
            return []
        parsed: Any = None
        if normalized.startswith('['):
            try:
                parsed = json.loads(normalized)
            except json.JSONDecodeError:
                parsed = None
        source = parsed if isinstance(parsed, list) else [token.strip() for token in normalized.split(',')]
        result: List[int] = []
        for item in source:
            if item == '':
                continue
            try:
                result.append(_coerce_int(item))
            except (TypeError, ValueError):
                continue
        return result

    try:
        return [_coerce_int(value)]
    except (TypeError, ValueError):
        return []
