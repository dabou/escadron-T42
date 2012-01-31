#!/usr/bin/env python
from kivy.gesture import GestureDatabase

gdb = GestureDatabase()

vertical = \
gdb.str_to_gesture('eNq1l8ty2jAUhvd6kbApI52rzgvQbWd4gA5JPIRJCh4gbfP2lY4dbGbasmDkBYafo0+Xz8JmsXvd/fxYbrvT+f3Yha/juY9h8dynsH7Yb350D6GH8racMJzWD6fz8fDancpHCou3nsPir5C1l4VeKkpL+/6w259rs1yb2T+afatVoU/DCOoQPkqTBGEVlyKJ1NhSRlEkq6P5Xb/FsPoSlzEJ5yQIwhglxajh9Lj5fzfk3XDYDj2wqESIFAdOAWwvcCCbjtL9bbhPPWkbeHa4NYGDrz6kTzhFQl9yMcyqTDN6jMCcPrtOyHgbD47HVniXCtwK71pBW+FdLFgjPLpavKgFBIvTrim9D/hKxzxuJQDihPk23MUitoG7VuQ2cJeK2gbuStGawMmF0kVoFBOCzJqGV7gL7kIJ28BdKHEbuAslbQN3oWRN4OxCeRRatznRnA5R7sK7UsZWeJfK3ArvWllb4V0s2wVfGvF0V2W8a6uKm5XUiO5iBRvR3atMXiHq/EesPEPdQ3etoo3oblUmq8CS6710vHfqXdeMulVNjehuVSerkI1ptjR3wV2qTlIxURwBlE3tBrz+G3g6dt3+8mxfJlse7lXDYoXKyxhWpFhO515z2Eyh8NLmB9UKGyrEKzh6sxyH0DxMY5g8zPXTCiUPIcxDGEOch3FsTrMQVIeQ56GMlTIPaWTqVThW5nmINIR2FcL1nLVUWLyqSN7M5tMDsPqgNx1YK+CqYhiXlbkOUl663fblXHSUdS0jrEte0l+75/NLDTmsxuh8eOuOm/1T/Y9nUkWnGo9Xy/f+eHh+f3KQFtDSMpGhScxUbnhl054el38AMsG4pA==')

ligne = \
gdb.str_to_gesture('eNq1l81y2jAURvd6kbApo/svvQDddoYH6NDEQ5ik4AHSNm9f6QIBd0rsjby4Tr5cHck+xDKzzcvm1/t83R2Ob/sufD2f+xhmTz2E5cN29bN7CD2WH8uJwmH5cDjudy/dofzKYfbaS5j9F7L0ttBrRVkZ3+8222MdluqwfGfYt9oVejitoC7hvQwBDIsvcR4jW0KO0VQgMZPWBf2pDeQNnMgoXwpDOPxYfT4P+zwS1p9Msb7QBRDypWBJR/F+9WDT8JA053OxWJY2ik+Ozzf4aGCkEYDNTAnhyqfhIaN4dAkF0QiPjqdpeASgdFMm8N0tSjO+y0Vrxne7mFvxyfXSRL0AlpJeywS++yVqxne/JM347pcm+i3/2VHlWhKOT+CCKTebgN0wQ7sJXDFTuwncMZ8dVwQRm6YoJIrJ0C4P0PK3bKIfRbKO090wWyO66+Xchi7uVmAKHTJE0Y9C4zuLuFihRnS3KtKI7lZlklVMLHItZacepbtVyW3o6lYVGtHdqk6yevsiVcr4bVeXqtIG7k7V2sBdqU5SypQj3pRRuLlRgzZwF2qThA7fjcuuMwp3oTZJqMQEFC8FHV6/Kzzuu2778eZfBpRXf7MwWyDpPIYFgczz7cHh2FsKq5GO7B3MdztS9A7B+x1w6sj3O9A7jE4dVk4lpBpSHIbsIeogFA+FB6F6aOdZ0ym0GnKEf9dw7fBbwiiDYX4XmO02zH7hrDQI/VrZeBD65XGKg5BOIQ7Ccnknoc/dZv18LCqzhAXW7f56lCdu6fi9eTo+1wYtDVxvSAmPu9duv9o+1u+S2fyxXuPz5+57v989vT06NlWsEQOqckbkrL4Zzv8CCbHPtw==')

lance = \
gdb.str_to_gesture('eNq1WMtyHDcMvM+PWJeoSDyJH1CuqfIHpBR7S1Y5kbYkOYn/PiDAnaG864wu2stKmGYT0w2AlK7uv97//f367vD88u3psPw6vo9lufp8rMvHDw+3fx0+LEfwH/0Ll+ePH55fnh6/Hp79V1qu/jzycnWR5GPAlqN0KvX1x8f7h5e+rPVl9pNlv3XUcqyZQU/huy+psNyUa+YiTaExAKKo9mz+7U9xufnFHxcytCbABMbMy/Mft/+/CcUmvNwlP5lVKs2QtKgVWZ7vBjUx4imM2mCfOl676kqNULFwo2pAaLZRI1LzlxFTNuKC+9QtqO0dqCFUh3qixrbxuq7KGzeQwlCjdFdonxyCHFdy3JiZEDfuSganpKtWk33ucBL4XbjDSlitBOvVhSAkhZrX0MpdpMpUP9j2ucNLWL0E9pza5Ocgd25ga2oKXBpbMd13E8NNXN0ErMVMWJAVW5OVuwK6KLVKw0a+yX7eGF4ivgd1WImrlVC7yiu76cZtUqwWYXekGPcne9xhJa5WVp2drBs1MGgnFahmWGG/SjCcxNXJStu4KMVtW7mxkpCqCAIWeEORUPhIq4+e6FTBjTa1UcXbnFBoaL7PHUbSaqQX1tzVGzUBNOParMQGb1CEwkhajSz6akyVrbap+a9M1qBVbfs2UthIq42FZhdLgSntAnCSmnyPfe7wkVYfS03aUYBKNBlpLVkj8zeQczjJw8k+MaBupeC5blUCqBhyiFHlVvePHA4rGd+HPMxk3sjltLoos8nUln5SjirpZcj7lcLhJ+tGPo06b3A/8dYxSCKnjvfmfEOFcxjK9i7kEobKZmgFYi1EoshoNJ+YBecO8HbeJQ9DZTO08tokXXqYyU01LkU5GfY1lzBUNkOrpZdSqlc5F5jOTJ9XGze/IfMwVDZDAVa9Xd766iJRax03tt7Db7hISDgqm6OgVCZl6kTeGo0x2Q9V2Z8tGo7q5ijYMDOH3ySL9z9Ot9H9JtIwVDdD/ZYy1ZtNVwlUP9qmG8w+d/ipm59oOg8+nS6zPhGhuGh52w3B+73+09Ph8LDe0n32+zXdL9lXN9Dkuiw3hOXa5g8tL0dty21HtECA+pcHLYKWy6BGsJUedNEiWPScq9VAYCzzN89lEEHmCDbLIEZQIYNjA4pgQOLZ+QbcEf7SgZDBJRGE5BLfZ/5IR2ggEAPBdgERKhCVHx+NxB1hicjXYIiglQy2C8sGIiTxnvvxZW6QMn2DRGgQUxpgmEG7sEwSEWKR5DtRJml8Cp4vw3M5LZU7l+wn8JRR0l7C3DKV05rBdNJSLE2xsJ1z+SmfEDtBSkRTrlZeR+EVnY5oaiTpO8KlTVIkyoxBLkFSMswdoQzuVKbWc2VqHZBQw8/KWFh4RFsWdlZoOdGFHlGbi7cVZbRmQ0WleAfqeVn6aA1IaO2QsXXNlkKKqMqIZk9By+gJm02V3QFySYLK2diSEBgLJaO5kNul7FKCognh19wakNSj5JszXIKkOCXfkewCBFKpUhMilyA1R1bmMvqhAmQ0t+8yzh8MCCZkbD/eHuhVtFza0WXLyfvlcH/35SX+zeEV4sfMj2jH/HP/+eVLQNQhUQIefXn88/B0+/DpEE9aXL96fJwRvx+fHj9/+5TU5lP3uvVrg/iRKNr/evLRf/0fgMqGqw==')
