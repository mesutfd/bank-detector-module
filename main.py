def len_checker(number: str) -> bool:
    return len(number) == 16

def card_checker(number: str) -> bool:
    must_sum = []
    card_list = [int(i) for i in number]

    counter = 0
    for i in card_list:
        counter += 1
        if counter % 2 == 0:
            zarb = i * 1
            if zarb >= 10:
                must_sum.append(zarb - 9)
            else:
                must_sum.append(zarb)
        else:
            zarb = int(i) * 2
            if zarb >= 10:
                must_sum.append(zarb - 9)
            else:
                must_sum.append(zarb)
    sum_numbers = sum(must_sum)
    if sum_numbers % 10 == 0:
        return True
    else:
        return False

banks = {
    627412: "بانک اقتصاد نوین",
    207177: "بانک توسعه صادرات ایران",
    627381: "بانک انصار",
    502229: "بانک پاسارگاد ",
    505785: "بانک ایران زمین",
    502806: "بانک شهر",
    622106: " بانک پارسیان",
    502908: " بانک توسعه تعاون",
    639194: " بانک پارسیان",
    502910: "بانک کارآفرین",
    627884: "بانک پارسیان",
    502938: " بانک دی",
    639347: "بانک پاسارگار",
    505416: "بانک گردشگری",
    636214: "  بانک تات",
    505801: " موسسه اعتباری کوثر",
    627353: "  بانک تجارت",
    589210: "بانک سپه",
    589463: "بانک رفاه کارگران",
    627648: " بانک توسعه صادرات ایران",
    603769: "بانک صادرات ایران",
    603770: "بانک کشاورزی",
    636949: "بانک حکمت ایرانیان",
    603799: "بانک ملی ایران",
    606373: " بانک قرض الحسنه مهر ایران",
    610433: " بانک ملت",
    621986: "بانک سامان",
    639346: "بانک سینا",
    627488: " بانک کارآفرین",
    627961: "بانک صنعت و معدن",
    639217: "بانک کشاورزی",
    636795: " بانک مرکزی",
    628023: " بانک مسکن",
    639370: " بانک مهر اقتصاد",
    627760: " پست بانک ایران",
    639599: "بانک قوامین",
    628157: " وسسه اعتباری توسعه",
    639607: "بانک سرمایه",
    991975: "بانک ملت"
}

def where(number: str):
    if len_checker(number) and card_checker(number):
        number = number[:6]
        for j, k in banks.items():
            if int(number) == j:
                return k
    else:
        raise ValueError('SomeThing is Wrong !(len or card number)')

# print(where('6037997350202355'))