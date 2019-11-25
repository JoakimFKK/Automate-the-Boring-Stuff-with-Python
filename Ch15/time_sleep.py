import datetime, time

new_years = datetime.datetime(2020, 1, 1, 0, 0, 0)
while datetime.datetime.now() < new_years:
    print("Not 2020 yet.")
    time.sleep(5)