from typing import Dict, List, Optional


class Answer(Dict):
    def __init__(self, text: str, is_right: bool = False):
        self.text: str = text
        self.is_right: bool = is_right


class Question:
    def __init__(self, title: str, answers: List[Answer], explaining: Optional[str] = None):
        self.title: str = title
        self.answers: List[Answer] = answers

        if explaining:
            self.explaining: Optional[str] = explaining

        for i, answer in enumerate(answers):
            if answer.is_right:
                self.correct_answer_id: int = i
                break


questions: List[Question] = [
    Question(answers=[
        Answer(text='В 1994 году'),
        Answer(text='В 2016 году', is_right=True),
        Answer(text='В 2005 году'),
        Answer(text='В 2014 году'),
    ],
        title="Когда появился наш институт (ИЭИТУС)",
        explaining="В апреле 2016 года решением Ученого Совета образован институт энергетики, "
                   "информационных технологий и управляющих систем (ЭИТУС) на основе объединения "
                   "энергетического института (ЭИ) и института информационных технологий "
                   "и управляющих систем (ИИТУС)"
    ),
    Question(answers=[
            Answer(text='7'),
            Answer(text='8'),
            Answer(text='9', is_right=True),
            Answer(text='6'),
        ],
            title="Сколько институтов включает в себя БГТУ им. В.Г. Шухова",
            explaining="9. (АИ, ИСИ, ИЭИТУС, ИТОМ, ИЭМ, ТТИ, ХТИ, ИМ, ИЗО)"
        ),
    Question(answers=[
            Answer(text='ИТОМ'),
            Answer(text='ИЭМ', is_right=True),
            Answer(text='ИСИ'),
            Answer(text='ИЭИТУС'),
        ],
            title="Какой самый многочисленный институт в БГТУ им. В. Г. Шухова",
            explaining="ИСИ"
        ),
    Question(answers=[
        Answer(text='ИЭМ'),
        Answer(text='АИ'),
        Answer(text='ИСИ'),
        Answer(text='ИЭИТУС', is_right=True),
    ],
        title="В студенческом объединении какого института больше всего людей",
        explaining="Несмотря на то, что в ИСИ больше людей. Самым многочисленным и одним из самых активным является студсовет ИЭИТУСа."
    ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
    # Question(answers=[
    #     Answer(text=''),
    #     Answer(text='', is_right=True),
    #     Answer(text=''),
    #     Answer(text=''),
    # ],
    #     title="",
    #     explaining=""
    # ),
]