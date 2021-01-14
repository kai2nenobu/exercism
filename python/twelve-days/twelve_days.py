from dataclasses import dataclass


@dataclass
class Verse:
    ordinal_text: str
    gift: str


def day_lyric(day: int) -> str:
    verses = {
        1: Verse('first', 'a Partridge in a Pear Tree'),
        2: Verse('second', 'two Turtle Doves'),
        3: Verse('third', 'three French Hens'),
        4: Verse('fourth', 'four Calling Birds'),
        5: Verse('fifth', 'five Gold Rings'),
        6: Verse('sixth', 'six Geese-a-Laying'),
        7: Verse('seventh', 'seven Swans-a-Swimming'),
        8: Verse('eighth', 'eight Maids-a-Milking'),
        9: Verse('ninth', 'nine Ladies Dancing'),
        10: Verse('tenth', 'ten Lords-a-Leaping'),
        11: Verse('eleventh', 'eleven Pipers Piping'),
        12: Verse('twelfth', 'twelve Drummers Drumming'),
    }
    lyric = f'On the {verses[day].ordinal_text} day of Christmas my true love gave to me: '
    for idx in range(day, 0, -1):
        if idx == day:  # first
            sep = ''
        elif idx == 1:  # last
            sep = ', and '
        else:  # middle
            sep = ', '
        lyric += (sep + verses[idx].gift)
    return lyric + '.'


def recite(start_verse, end_verse):
    return [day_lyric(day) for day in range(start_verse, end_verse + 1)]
