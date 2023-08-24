from datetime import tzinfo

import numpy as np
from pandas.core.arrays.datetimelike import (
    DatelikeOps,
    DatetimeLikeArrayMixin,
    TimelikeOps,
)

from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype

def tz_to_dtype(tz): ...

class DatetimeArray(DatetimeLikeArrayMixin, TimelikeOps, DatelikeOps):
    __array_priority__: int = ...
    def __init__(self, values, dtype=..., freq=..., copy: bool = ...) -> None: ...
    # ignore in dtype() is from the pandas source
    @property
    def dtype(self) -> np.dtype | DatetimeTZDtype: ...  # type: ignore[override]
    @property
    def tz(self): ...
    @tz.setter
    def tz(self, value) -> None: ...
    @property
    def tzinfo(self) -> tzinfo | None: ...
    @property
    def is_normalized(self): ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __iter__(self): ...
    def astype(self, dtype, copy: bool = ...): ...
    def tz_convert(self, tz): ...
    def tz_localize(self, tz, ambiguous: str = ..., nonexistent: str = ...): ...
    def to_pydatetime(self): ...
    def normalize(self): ...
    def to_period(self, freq=...): ...
    def to_perioddelta(self, freq): ...
    def month_name(self, locale=...): ...
    def day_name(self, locale=...): ...
    @property
    def time(self): ...
    @property
    def timetz(self): ...
    @property
    def date(self): ...
    year = ...
    month = ...
    day = ...
    hour = ...
    minute = ...
    second = ...
    microsecond = ...
    nanosecond = ...
    weekofyear = ...
    week = ...
    dayofweek = ...
    weekday = ...
    dayofyear = ...
    quarter = ...
    days_in_month = ...
    daysinmonth = ...
    is_month_start = ...
    is_month_end = ...
    is_quarter_start = ...
    is_quarter_end = ...
    is_year_start = ...
    is_year_end = ...
    is_leap_year = ...
    def to_julian_date(self): ...

def objects_to_datetime64ns(
    data,
    dayfirst,
    yearfirst,
    utc: bool = ...,
    errors: str = ...,
    require_iso8601: bool = ...,
    allow_object: bool = ...,
): ...
def maybe_convert_dtype(data, copy): ...
def validate_tz_from_dtype(dtype, tz): ...
