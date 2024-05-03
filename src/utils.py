import os
import pandas as pd
import numpy as np
import sys
from src.logger import logging
from src.exception import CustomException


def strip_text(df):
    for i in df.columns:
        if df[i].dtype=='object':
            df[i]=df[i].map(str.strip)
        else:
            pass

    return df