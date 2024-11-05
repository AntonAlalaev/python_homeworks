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


api = "xxx"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()

button_info = KeyboardButton(text="Информация")
button_start = KeyboardButton(text="Рассчитать")
button_buy = KeyboardButton(text="Купить")

kb.add(button_info)
kb.add(button_start)
kb.add(button_buy)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Product1", callback_data="product_buying"),
            InlineKeyboardButton(text="Product2", callback_data="product_buying"),
            InlineKeyboardButton(text="Product3", callback_data="product_buying"),
            InlineKeyboardButton(text="Product4", callback_data="product_buying")
        ]
    ], resize_keyboard=True
)


@dp.callback_query_handler(text="product_buying")
async def get_buying_list(call):
    await call.message.answer("Куплено!")


product_dict = {"Private Jet": "image1.jpeg", "Yacht": "image2.jpg", "Private Island": "image3.jpg",
                "Private Castle": "image4.jpg"}


@dp.message_handler(text="Купить")
async def buy(message):
    for key in product_dict:
        await message.answer(f"Продукт: {key}")
        await message.answer_photo(photo=open(f"pictures/{product_dict[key]}", 'rb'))
    await message.answer("Выберите продукт для покупки", reply_markup=inline_kb)


@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью. Что вы хотите сделать?", reply_markup=kb)


@dp.message_handler(text="Информация")
async def formulas(message):
    await message.answer("М: 10*вес (кг) + 6,25*рост (см) - 5*возраст (г) + 5")
    await message.answer("Ж: 10*вес (кг) + 6,25*рост (см) - 5*возраст (г) - 161")


@dp.message_handler(text="Рассчитать")
async def calories(message):
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def growth_handler(message, state):
    await state.update_data(first=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def weight_handler(message, state):
    await state.update_data(second=message.text)
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
