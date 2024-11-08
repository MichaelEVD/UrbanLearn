import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from crud_functions_2 import get_all_products, is_included,add_user

info_prod = get_all_products()

api = '7859581492:AAGylJp5-UGmElg52UNGPBxJV7GZhLcNiOc'
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

klava = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
klava.row(button1,button2)
klava.row(button3)
klava.row(button4)

inlklava = InlineKeyboardMarkup()
ibutton1 = InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories')
ibutton2 = InlineKeyboardButton(text='Формулы расчёта',callback_data='formulas')
inlklava.row(ibutton1,ibutton2)

inlklava_2 = InlineKeyboardMarkup()
bbutton1 = InlineKeyboardButton(text='Product1',callback_data="product_buying")
bbutton2 = InlineKeyboardButton(text='Product2',callback_data="product_buying")
bbutton3 = InlineKeyboardButton(text='Product3',callback_data="product_buying")
bbutton4 = InlineKeyboardButton(text='Product4',callback_data="product_buying")
inlklava_2.row(bbutton1, bbutton2, bbutton3, bbutton4)


@dp.message_handler(commands=['start'])
async def start(massage):
    await massage.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=klava)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weigth = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer(text='Выберите опцию',reply_markup=inlklava)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    await message.answer(f"Название: {info_prod[0][0]} | Описание: {info_prod[0][1]} | Цена: {info_prod[0][2]}")
    with open("C:/Users/Admin/PycharmProjects/UrbanLearn/module 14/foto/foto_1.jpg", 'rb') as img:
        await message.answer_photo(img)
    await message.answer(f"Название: {info_prod[1][0]} | Описание: {info_prod[1][1]} | Цена: {info_prod[1][2]}")
    with open("C:/Users/Admin/PycharmProjects/UrbanLearn/module 14/foto/foto_2.jpg", 'rb') as img:
        await message.answer_photo(img)
    await message.answer(f"Название: {info_prod[2][0]} | Описание: {info_prod[2][1]} | Цена: {info_prod[2][2]}")
    with open("C:/Users/Admin/PycharmProjects/UrbanLearn/module 14/foto/foto_3.jpg", 'rb') as img:
        await message.answer_photo(img)
    await message.answer(f"Название: {info_prod[3][0]} | Описание: {info_prod[3][1]} | Цена: {info_prod[3][2]}")
    with open("C:/Users/Admin/PycharmProjects/UrbanLearn/module 14/foto/foto_4.jpg", 'rb') as img:
        await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=inlklava_2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

@dp.callback_query_handler(text="product_buying")
async def end_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def  set_username(message, state):
    if is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def  set_email(message, state):
    await state.update_data(mail=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def  set_age(message, state):
    await state.update_data(let=message.text)
    data = await state.get_data()
    add_user(data['username'], data['mail'], data['let'])
    await state.finish()
    await message.answer('Регистрация прошла успешно')

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

@dp.callback_query_handler(text=['Регистрация'])
async def set_age(call):
    await call.message.answer('Введите свой возраст,полных лет:')
    await UserState.age.set()

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)