from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью. Для расчета калорий набери Calories")


@dp.message_handler(text="Calories")
async def calories(message):
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def growth_handler(message, state):
    await state.update_data(first=message.text)
    data = await state.get_data()
    await message.answer("Введите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def weight_handler(message, state):
    await state.update_data(second=message.text)
    data = await state.get_data()
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
