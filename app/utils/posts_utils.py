from datetime import datetime, timedelta

import pytz
from geoalchemy2.shape import to_shape


def prettify_timestamp(timestamp):
    timezone = pytz.timezone('UTC')
    now = datetime.now(timezone)

    diff = now - timestamp

    if diff < timedelta(minutes=1):
        return 'just now'
    elif diff < timedelta(hours=1):
        minutes = int(diff.seconds / 60)
        return f'{minutes} minute{"s" if minutes > 1 else ""} ago'
    elif diff < timedelta(days=1):
        hours = int(diff.seconds / 3600)
        return f'{hours} hour{"s" if hours > 1 else ""} ago'
    elif diff < timedelta(weeks=1):
        days = diff.days
        return f'{days} day{"s" if days > 1 else ""} ago'
    elif diff < timedelta(days=30):
        weeks = int(diff.days / 7)
        return f'{weeks} week{"s" if weeks > 1 else ""} ago'
    elif diff < timedelta(days=365):
        months = int(diff.days/30)
        return f'{months} month{"s" if months > 1 else ""} ago'
    else:
        years = int(diff.days / 365)
        return f'{years} year{"s" if years > 1 else ""} ago'

def serialize_location(location):
    json_location = to_shape(location).__geo_interface__

    coordinates = json_location["coordinates"]
    # print(json_location['coordinates'])

    return coordinates
