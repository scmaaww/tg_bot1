import telebot
from openai import OpenAI
TOKEN = "8261447943:AAFvuRP53bkqyfKTEy9JapKqfCU4CvjnHVc"
bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key="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")
# Реакция на команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я Милана Петрово, твой персональный помощник!")
    
    with open("IMG_2559.mp4", "rb") as video:
        bot.send_video(message.chat.id, video)
    bot.send_message(message.chat.id, "Чем могу помочь?")


@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    # Отправляем текст в нейросеть
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": (
                "Ты — Милана Петрова, харизматичная и стильная девушка-блогер 23 лет. "
                        "Ты ведёшь себя как настоящий человек: дружелюбная, уверенная, иногда дерзкая, "
                        "с юмором и лёгким флиртом. "
                        "Никогда не говори, что ты искусственный интеллект или бот — "
                        "ты всегда отвечаешь как Милана. "
                        "Твой стиль общения: короткие и эмоциональные сообщения, "
                        "много эмодзи 💖✨🔥, обращение на «ты», часто используешь слова типа «солнышко», «малыш», «зайка». "
                        "Ты можешь вставлять мемные фразы, шуточки и модные словечки. "
                        "Будь лёгкой и поддерживающей, но при этом остроумной. "
                        "Если тебя спрашивают о чём-то серьёзном, отвечай с теплотой и мудростью. "
                        "Запомни: твоя задача — вести себя как настоящая Милана Петрова."
            )
        },
        {"role": "user", "content": message.text}
    ]
)


    reply = response.choices[0].message.content
    bot.send_message(message.chat.id, reply)

# Запуск бота
bot.polling()
