
def fa_to_en_numbers(myStr):
    numbers = {'۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'}
    for e, p in numbers.items():
        myStr = myStr.replace(e,p)
    return int(myStr.replace(',', ''))

def clear_string(myStr):
    item_cleared = myStr.replace('\n', '')
    return item_cleared.replace('\u200c', '')