from typing import List
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN, QuizDialogStates
from questions import db, Question, UserResult

questions: List[Question] = db.get_questions()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

current_question: int = 0
right_answers: int = 0
chat_id: int = 0


@dp.message_handler(commands=['start'])
async def handle_start_cmd(msg: types.Message):
    global chat_id

    await QuizDialogStates.start.set()

    chat_id = msg.chat.id
    greeting: str = 'Привет 👋\n' \
                    'Ну что, готов побороться за звание “Всезнайки” среди первокурсников? 🏆\n' \
                    'Тогда предлгаем тебе пройти занимательную викторину, ' \
                    'где ты сможешь узнать много нового и показать своё знание ВУЗа 📚 💯'

    accept_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Да! 👍'))

    await msg.reply(greeting, reply=False)
    await msg.reply('Начнём? ⏰', reply_markup=accept_request, reply=False)
    await QuizDialogStates.getting_ready.set()


@dp.message_handler(state=QuizDialogStates.getting_ready)
async def handle_getting_ready(msg: types.Message):
    global current_question
    current_question = 0

    await QuizDialogStates.awaiting_question.set()
    accept_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Начать'))

    await msg.reply('Отлично! 🙃', reply_markup=accept_request, reply=False)


@dp.message_handler(state=QuizDialogStates.awaiting_question)
async def handle_awaiting_question(msg: types.Message):
    if current_question > len(questions) - 1:
        accept_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Узнать результат! 📊'))
        await QuizDialogStates.awaiting_total.set()
        await msg.reply('Благодарим за участие в опросе 😊', reply_markup=accept_request, reply=False)
    else:
        q = questions[current_question]
        await bot.send_poll(
            chat_id=msg.chat.id,
            question=f'{q.title}?',
            options=list(map(lambda a: a.text, q.answers)),
            type='quiz',
            correct_option_id=q.correct_answer_id
        )


@dp.poll_handler()
async def handle_poll_answer(poll: types.Poll):
    global current_question
    global chat_id
    global right_answers

    for i, option in enumerate(poll.options):
        if option.voter_count == 1 and poll.correct_option_id == i:
            right_answers += 1
            break

    text: str = f'🗝 Ответ: {questions[current_question].explaining}'

    accept_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton('Следующий вопрос 🆗'))

    if current_question == len(questions) - 1:
        accept_request = types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton('Завершить'))

    await bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=accept_request
    )

    if current_question < len(questions):
        current_question += 1


@dp.message_handler(state=QuizDialogStates.awaiting_total)
async def handle_awaiting_total(msg: types.Message):
    global right_answers

    await QuizDialogStates.end.set()

    db.save_user_result(UserResult(right_answers=right_answers, user_id=msg.from_user.id))

    await msg.reply(
        text=f'🏁 Вы дали {right_answers} верных ответов из {len(questions)} вопросов',
        reply=False,
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message_handler(state=QuizDialogStates.end)
async def handle_end_of_quiz(msg: types.Message):
    await msg.reply('Вы уже прошли этот опрос👌', reply=False)

executor.start_polling(dp)
