"""

시간 계산법
1. 시간에 * 60 하고 분을 그대로 + 해준다
2. 출차 시간 - 입차 시간 해준다.
07:59 -> 19:09 : 670분 == 1149 - 479
**** 만약 출차 내역이 없다면 23:59에 출차한 것으로 한다.

==========
까다로운 부분
글자를 잘라서 조건에 맞게 자료구조를 만드는 것 (파싱)
요금을 계산하는 기준을 잘 파악해서 올림하는 것
"""
import math

def solution(fees, records):
    result_fee_dict = dict() #dict[차량번호] = 주차요금
    record_dict = dict() #dict[차량번호] = 입차 시각

    for record in records:
        record_token = record.split() # [0]: 시각 , [1]: 차 번호
        car_num = record_token[1]
        record_time = record_token[0]

        if car_num not in record_dict.keys(): # 입차했던 차가 아니면 기록만 추가 하고 넘어간다.
            record_dict[car_num] = record_time
            continue

        #  입차했던 차면 없애고 시간 업데이트
        in_time = record_dict.pop(car_num)
        parking_time = cal_parking_time(parse_string_time(in_time), parse_string_time(record_time))
        result_fee_dict[car_num] = result_fee_dict.get(car_num, 0) + parking_time

    # 남아 있는 애들은 출차시간 지정해서 마저 계산해준다.
    for car_num, in_time in record_dict.items():
        parking_time = cal_parking_time(parse_string_time(in_time), parse_string_time("23:59"))
        result_fee_dict[car_num] = result_fee_dict.get(car_num, 0) + parking_time

    # result_fee_dict를 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
    sorted_result = []
    for car_num in sorted(result_fee_dict.keys()):
        total_parking_time = result_fee_dict[car_num]
        total_fee = cal_fee(fees, total_parking_time)
        sorted_result.append(total_fee)

    return sorted_result

def cal_fee(fees, total_parking_time):
    basic_time, basic_fee, unit_time, unit_fee = fees
    if total_parking_time <= basic_time:
        return basic_fee
    extra_time = total_parking_time - basic_time
    extra_fee = math.ceil(extra_time / unit_time) * unit_fee
    return basic_fee + extra_fee

def cal_parking_time(in_time_list, out_time_list):
    return (int(out_time_list[0]) * 60 + int(out_time_list[1])) - (int(in_time_list[0]) * 60 + int(in_time_list[1]))

def parse_string_time(string_time):
    return string_time.split(':')


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))