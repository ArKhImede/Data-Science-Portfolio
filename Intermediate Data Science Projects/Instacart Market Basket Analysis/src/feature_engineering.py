def convert_time_to_part_of_day(time: int) -> str:
    if 6 <= time <= 11:
        return "morning"
    elif 12 <= time <= 17:
        return "afternoon"
    elif 18 <= time <= 21:
        return "evening"
    else:
        return "night"

def get_product_name_len(value: str) -> int:
    if not isinstance(value, str):
        return 0
    return len(value)