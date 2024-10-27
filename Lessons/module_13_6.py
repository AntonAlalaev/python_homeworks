from aiogram import Bot, Dispatcher, executor  # , types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# import asyncio


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = "xx"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()

button_info = KeyboardButton(text="Информация")
button_start = KeyboardButton(text="Рассчитать")

kb.add(button_info)
kb.add(button_start)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
            InlineKeyboardButton(text="Формулы расчета", callback_data="formulas")
        ]
    ], resize_keyboard=True
)
button_cal = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button_formula = InlineKeyboardButton(text="Формулы расчета", callback_data="formulas")


@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью. Что вы хотите сделать?", reply_markup=inline_kb)


@dp.callback_query_handler(text="calories")
async def calories(call):
    await call.message.answer("Введите свой рост")
    await call.answer()
    await UserState.growth.set()


@dp.callback_query_handler(text="formulas")
async def formulas(call):
    await call.message.answer("М: 10*вес (кг) + 6,25*рост (см) - 5*возраст (г) + 5")
    await call.message.answer("Ж: 10*вес (кг) + 6,25*рост (см) - 5*возраст (г) - 161")
    await call.answer()


@dp.message_handler(text="Рассчитать")
async def calories(message):
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def growth_handler(message, state):
    await state.update_data(first=message.text)
    # data = await state.get_data()
    await message.answer("Введите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def weight_handler(message, state):
    await state.update_data(second=message.text)
    # data = await state.get_data()
    await message.answer("Введите свой возраст")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def weight_handler(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    try:
        await message.answer(f"Вы ввели = рост {data['first']} вес {data['second']} возраст {data['third']}")
        man_norma = 10 * int(data['second']) + 6.25 * int(data['first']) - 5 * int(data['third']) + 5
        await message.answer(f"Если вы мужчина то ваша норма калорий: {man_norma}")
        women_norma = man_norma - 166
        await message.answer(f"Если вы женщина то ваша норма калорий: {women_norma}")
    except ValueError:
        await message.answer("Произошла ошибка в расчетах, вероятно вы ввели неправильные данные, должны быть числа")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print(f"Мы получили сообщение! {message.text}")
    await message.answer("Введите команду /start чтобы начать общение")
    print("Введите команду /start чтобы начать общение")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
