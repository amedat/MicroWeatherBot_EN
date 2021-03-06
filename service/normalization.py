import datetime


def text_to_date(text_date):
    today = datetime.datetime.now()
    one_more_day = datetime.timedelta(days=1)

    if text_date == "today":
        return today.date()
    if text_date == "tomorrow":
        return (today + one_more_day).date()
    if text_date == "the day after tomorrow":
        return (today + one_more_day * 2).date()

    # Not supported by weather API provider freely
    if text_date == "the next day after tomorrow":
        # return 3
        return (today + one_more_day * 3).date()

    if text_date.startswith("星期"):
        # TODO: using calender to compute relative date
        # not support yet
        return None

    if text_date.startswith("下星期"):
        # TODO: using calender to compute relative date
        # not support yet
        return None

    # follow APIs are not supported by weather API provider freely
    if text_date == "昨天":
        return None
    if text_date == "前天":
        return None
    if text_date == "大前天":
        return None
