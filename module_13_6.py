from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import  asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton(text="Рассчитать")
button_info = KeyboardButton(text="Информация")
kb.add(button_calculate)
kb.add(button_info)

ikb = InlineKeyboardMarkup()
ibutton_calculate = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data = 'calories')
ibutton_formula = InlineKeyboardButton(text='Формулы расчёта', callback_data = 'formulas')
ibutton_man = InlineKeyboardButton(text='для мужчин', callback_data='man_formula')
ibutton_woman = InlineKeyboardButton(text='для женщин', callback_data='woman_formula')
ikb.add(ibutton_calculate)
ikb.add(ibutton_formula)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = ikb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup = kb)

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('информация о боте')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await UserState.age.set()
    data = await  state.get_data()
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth = message.text)
    await UserState.growth.set()
    data = await  state.get_data()
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def set_(message, state):
    await state.update_data(weight = message.text)
    await UserState.weight.set()
    data = await  state.get_data()
    calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    await message.answer(f"Ваша норма калорий: {calories}")

@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
