import pandas as pd
from ..models import Job


def save_dataframe_to_db(data: pd.DataFrame):
    for index, row in data.iterrows():
        job = Job(
            title=row['title'],
            company=row['company'],
            location=row['location'],
            description=row['description'],
            requirements=row['requirements'],
            related_keywords=row['related_keywords'],
            url=row['url']
        )
        job.save()