
from digitalhub_runtime_python import handler
import pandas as pd
import requests

@handler(outputs=["dataset"])
def downloader(project, url):
    # read and rewrite to normalize and export as data
    df = url.as_df(file_format='csv',sep=";")
    return df
