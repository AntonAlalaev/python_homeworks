from aiogram import Bot, Dispatcher, executor  # , types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from crud_functions import get_all_products
from crud_functions import is_included
from crud_functions import add_user

# загрузка данных из БД
product_data = get_all_products()

# присвоение имен файлам рисунков
product_pic = []
for index in product_data:
    product_pic.append(f"image{index[0]}.jpg")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

api = "x"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()

button_info = KeyboardButton(text="Информация")
button_start = KeyboardButton(text="Рассчитать")
button_buy = KeyboardButton(text="Купить")
button_registration = KeyboardButton(text="Регистрация")

kb.add(button_info)
kb.add(button_start)
kb.add(button_buy)
kb.add(button_registration)

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
async def send_confirm_message(call):
    await call.message.answer("Куплено!")


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for item in product_data:
        await message.answer_photo(photo=open(f"pictures/{product_pic[item[0] - 1]}", 'rb'))
        await message.answer(
            f"Продукт: {item[1]} | Описание: {item[2]} | Цена: {item[3]}$")
    await message.answer("Выберите продукт для покупки", reply_markup=inline_kb)


@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью. Что вы хотите сделать?", reply_markup=kb)


@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит)")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if message.text.isascii():
        if is_included(message.text):
            await message.answer("Пользователь уже существует. Введите другое имя.")
        else:
            await state.update_data(username=message.text)
            await message.answer("Введите ваш email")
            await RegistrationState.email.set()
    else:
        await message.answer("Имя пользователя может содержать только ASCII символы. Пожалуйста, попробуйте еще раз.")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer(f"Пользователь {data['username']} успешно добавлен")
    await state.finish()


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
