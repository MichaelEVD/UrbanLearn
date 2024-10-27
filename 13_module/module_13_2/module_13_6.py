import asyncio
from aiogram import Bot,Dispatcher,types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

klava = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
klava.row(button1,button2)

inlklava = InlineKeyboardMarkup()
ibutton1 = InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories')
ibutton2 = InlineKeyboardButton(text='Формулы расчёта',callback_data='formulas')
inlklava.row(ibutton1,ibutton2)

@dp.message_handler(commands=['start'])
async def start(massage):
    await massage.answer("Привет! Я бот помогающий твоему здоровью.",reply_markup=klava)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()

@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer(text='Выберите опцию',reply_markup=inlklava)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст,полных лет:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def  set_growth(message, state):
    await state.update_data(let=message.text)
    await message.answer('Введите свой рост, в см:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def  set_weight(message, state):
    await state.update_data(rost=message.text)
    await message.answer('Введите свой вес, в кг:')
    await UserState.weigth.set()

@dp.message_handler(state=UserState.weigth)
async def  send_calories(message, state):
    await state.update_data(ves=message.text)
    data = await state.get_data()
    norm_calor_men = 10 * int(data['ves'])  + 6.25 * int(data['rost']) - 5 * int(data['let']) + 5
    await message.answer(f'Норма калорий для мужчины, при указанных возрасте,весе и росте - {norm_calor_men}')
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)