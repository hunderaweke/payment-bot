import os, logging
from typing import Final, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from telegram import (
    Bot,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    ChatAction,
    ParseMode,
)
from telegram.ext import (
    Dispatcher,
    Updater,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler,
)

logging.basicConfig(level=logging.DEBUG)
TOKEN = os.environ.get("TOKEN")
app = FastAPI()
USDT_ADDRESS: Final[str] = "6661370496:AAENCRyfkghI1spqh0SASjmWMg9oRTjkRho"


class TelegramWebhook(BaseModel):
    """
    Telegram Webhook Model using Pydantic for request body validation
    """

    update_id: int
    message: Optional[dict]
    edited_message: Optional[dict]
    channel_post: Optional[dict]
    edited_channel_post: Optional[dict]
    inline_query: Optional[dict]
    chosen_inline_result: Optional[dict]
    callback_query: Optional[dict]
    shipping_query: Optional[dict]
    pre_checkout_query: Optional[dict]
    poll: Optional[dict]
    poll_answer: Optional[dict]


def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("VIP plan", callback_data="vip_plan"),
        ],
        [
            InlineKeyboardButton("Master Class", callback_data="master_plan"),
        ],
        [
            InlineKeyboardButton("One to One Mentorship", callback_data="one_to_one"),
        ],
    ]
    update.message.reply_text(
        """Welcome to our XE SNIPER Subscription Bot""",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def master_class(update: Update, context: CallbackContext):
    text = """XE Sniper Master Class Program

Basic to advanced forex trading knowledge

Advanced Trading Psychology

Risk and money management

Access our Discord community.

Access a free-quality gold signal for two month

24/7 student guidance

A big giveaway at the end of the class\nFinish Your Payment Using One of the methods and send the screenshot to @xesniper9"""
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton(
                "Credit Card", url="https://buy.stripe.com/dR66oQ1Ow2RH3ssaEF"
            )
        ],
        [InlineKeyboardButton("USDT(TRC20)", callback_data="copy_usdt_address")],
    ]
    query.delete_message()
    query.answer()
    query.bot.send_message(
        chat_id=query.from_user.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def one_to_one(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton(
                "Credit Card", url="https://buy.stripe.com/7sI9B264Mdwl4ww146"
            )
        ],
        [InlineKeyboardButton("USDT(TRC20)", callback_data="copy_usdt_address")],
    ]
    query.delete_message()
    query.answer()
    query.bot.send_message(
        chat_id=query.from_user.id,
        text="Some description here",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def copy_usdt_address(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("Send Screenshot", url="https://t.me/xesniper9")]]
    query.bot.send_message(
        chat_id=query.from_user.id,
        text=f"Copy the Address below:`{USDT_ADDRESS}`\nFinish the payment and send screen shot to @xesniper9",
        parse_mode=ParseMode.MARKDOWN,
    )


def vip(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("YES 👌", callback_data="have_exness")],
        [InlineKeyboardButton("NO  😥", callback_data="no_exness")],
    ]
    query.delete_message()
    query.answer()

    query.bot.send_message(
        chat_id=query.from_user.id,
        text="""XE VIP signa

👉🏾 LIVE TRADE 
👉🏾 daily signals  
👉🏾 XE E-BOOK 
👉🏾 more than 90% win rate  

To join xe sniper vip signal 
we require you to have an Exness account. do you have Exness account?""",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def no_exness(update: Update, context: CallbackContext):
    query = update.callback_query
    text = "Create Exness Account Using this 👇 Link\n If there is any problem contact us\n**Change your Ib\!** \nAfter you finish your verification processes \nSend your screenshot and your Exness Email to this user\mn  👉🏼 Using the Button bellow"
    keyboard = [
        [
            InlineKeyboardButton(
                "Create Exness Account", url="https://one.exness-track.com/a/f5l76iz61m"
            )
        ],
        [
            InlineKeyboardButton("Send Screenshot", url="https://t.me/xesniper9"),
        ],
        [
            InlineKeyboardButton("Contact Us", url="https://t.me/xesniper9"),
        ],
        [
            InlineKeyboardButton("Finish Payment", callback_data="pay_vip"),
        ],
    ]
    query.bot.send_message(
        chat_id=query.from_user.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN_V2,
    )


def yes_exness(update: Update, context: CallbackContext):
    query = update.callback_query
    text = "**Change your Ib\!** \nAfter you finish your verification processes \nSend your screenshot and your Exness Email to us  👉🏼 Using the Button bellow and Finish Your Payment"
    keyboard = [
        [
            InlineKeyboardButton("Send Screenshot", url="https://t.me/xesniper9"),
        ],
        [
            InlineKeyboardButton("Finish Payment", callback_data="pay_vip"),
        ],
    ]
    video = open("/description.MP4", "rb")
    query.bot.send_chat_action(
        chat_id=query.from_user.id, action=ChatAction.UPLOAD_VIDEO
    )
    query.bot.send_video(chat_id=query.from_user.id, video=video)
    query.bot.send_message(
        chat_id=query.from_user.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN_V2,
    )


def pay_vip(update: Update, context: CallbackContext):
    query = update.callback_query
    text = "👉🏼 Using the Button bellow and Finish Your Payment and Send the screenshot to Us"
    keyboard = [
        [
            InlineKeyboardButton(
                "Credit Card", url="https://buy.stripe.com/cN24gI2SA9g5bYY8ww"
            ),
        ],
        [
            InlineKeyboardButton("USDT(TRC20)", callback_data="copy_usdt_address"),
        ],
    ]
    query.bot.send_message(
        chat_id=query.from_user.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN_V2,
    )


def vip_exness(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton(
                text="Pay", url="https://buy.stripe.com/7sI9B264Mdwl4ww146"
            )
        ]
    ]
    query.bot.send_message(
        chat_id=query.from_user.id,
        text="Some description here",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def register_handlers(dispatcher):
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(CallbackQueryHandler(vip, pattern="vip_plan"))
    dispatcher.add_handler(CallbackQueryHandler(master_class, pattern="master_plan"))
    dispatcher.add_handler(CallbackQueryHandler(no_exness, pattern="no_exness"))
    dispatcher.add_handler(CallbackQueryHandler(yes_exness, pattern="have_exness"))
    dispatcher.add_handler(CallbackQueryHandler(one_to_one, pattern="one_to_one"))
    dispatcher.add_handler(CallbackQueryHandler(pay_vip, pattern="pay_vip"))
    dispatcher.add_handler(
        CallbackQueryHandler(copy_usdt_address, pattern="copy_usdt_address")
    )


@app.post("/webhook")
def webhook(webhook_data: TelegramWebhook):
    """
    Telegram Webhook
    """
    bot = Bot(token=TOKEN)
    update = Update.de_json(webhook_data.__dict__, bot)
    dispatcher = Dispatcher(bot, None, workers=4)
    register_handlers(dispatcher)
    dispatcher.process_update(update)
    return {"message": "ok"}


@app.get("/")
def index():
    return {"message": "Working"}
