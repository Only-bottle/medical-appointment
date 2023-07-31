from datetime import datetime, timedelta, time

# 의사의 영업 시간 정보
opening_time = time(9, 0, 0)
closing_time = time(19, 0, 0)
lunch_start_time = time(11, 0, 0)
lunch_end_time = time(12, 0, 0)
off_days = ["Saturday", "Sunday"]

# 진료 요청 시간
appointment_time = datetime(2023, 8, 5, 1, 0, 0)  # 예시로 2022년 1월 15일 새벽 1시를 가정


import ipdb; ipdb.set_trace()
# 의사의 다음 영업 시작 시간 계산
while True:
    next_day = appointment_time.date() + timedelta(days=1)
    next_day = next_day.strftime('%A').lower()
    operating_day = doctor.operatinghours.filter(day_of_week=next_day).first()
    if operating_day:
        break

print(f"예상하는 날짜는 다음주 월요일: {operating_day}")

print(f"next_day: {next_day}")
next_opening_time = datetime.combine(next_day, opening_time)
print(f"next_opening_time: {next_opening_time}")

# 진료 요청 후 20분이 지난 시간 계산
expire_time = appointment_time + timedelta(minutes=20)
print(f"expire_time: {expire_time}")

# 진료 요청이 의사의 영업 시간에 해당하는지 확인하여 만료 시간 설정
if appointment_time.time() < opening_time:
    expiration_time = next_opening_time
elif expire_time.time() < lunch_start_time:
    expiration_time = expire_time
elif lunch_end_time < expire_time.time() < closing_time:
    expiration_time = next_opening_time + timedelta(minutes=15)
else:
    # 진료 요청이 영업 시간에 해당하지 않는 경우
    print("진료 요청 시간이 영업 시간에 해당하지 않습니다.")
    expiration_time = None

# 만료 시간 출력
if expiration_time:
    print("진료 요청이 만료되는 시간:", expiration_time)
