from aiogram.dispatcher.filters.state import StatesGroup, State


class QuizDialogStates(StatesGroup):
    start: State = State()
    getting_ready: State = State()
    awaiting_question: State = State()
    replying_question: State = State()
    awaiting_total: State = State()
    end: State = State()


TOKEN: str = '1187104621:AAFCFPu5f-wb5svkPCm4_byZKm3N10oEnxQ'


