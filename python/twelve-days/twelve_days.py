class Verse:
    def __init__(self, ordinal_text: str, gift: str):
        self.ordinal_text = ordinal_text
        self.gift = gift


def recite(start_verse, end_verse):
    verses = {
        1:  Verse('first', 'a Partridge in a Pear Tree'),
        2:  Verse('second', 'two Turtle Doves'),
        3:  Verse('third', 'three French Hens'),
        4:  Verse('fourth', 'four Calling Birds'),
        5:  Verse('fifth', 'five Gold Rings'),
        6:  Verse('sixth', 'six Geese-a-Laying'),
        7:  Verse('seventh', 'seven Swans-a-Swimming'),
        8:  Verse('eighth', 'eight Maids-a-Milking'),
        9:  Verse('ninth', 'nine Ladies Dancing'),
        10: Verse('tenth', 'ten Lords-a-Leaping'),
        11: Verse('eleventh', 'eleven Pipers Piping'),
        12: Verse('twelfth', 'twelve Drummers Drumming'),
    }
    lyrics = []
    for day in range(start_verse, end_verse + 1):
        lyric = f'On the {verses[day].ordinal_text} day of Christmas my true love gave to me: '
        for idx in range(day, 0, -1):
            sep = ', '
            if idx == day:
                sep = ''
            elif idx == 1:
                sep = ', and '
            verse = verses[idx]
            lyric += (sep + verse.gift)
        lyric += '.'
        lyrics.append(lyric)
    return lyrics
