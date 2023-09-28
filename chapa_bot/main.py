import os, logging, string, random
from dotenv import load_dotenv
from typing import Final, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pyperclip3 import copy
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    ChatAction,
    ParseMode,
)
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

logging.basicConfig(level=logging.DEBUG)
load_dotenv()
TOKEN: Final[str] = os.getenv("TOKEN")
app: FastAPI = FastAPI()
USDT_ADDRESS: Final[str] = "6661370496:AAENCRyfkghI1spqh0SASjmWMg9oRTjkRho"

# class TelegramWebhook(BaseModel):
#     updated_id: [int]
#     message: Optional[dict]
#     edited_message: Optional[dict]
#     callback_query: Optional[dict]


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
    pass


def one_to_one(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Credit Card", callback_data="cc_1to1")],
        [InlineKeyboardButton("USDT", callback_data="usdt_1to1")],
    ]
    query.delete_message()
    query.answer()
    query.bot.send_message(
        chat_id=query.from_user.id,
        text="Some description here",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def cc_1to1(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Pay", url="https://buy.stripe.com/7sI9B264Mdwl4ww146")],
    ]
    query.delete_message()
    query.answer()
    query.bot.send_message(
        chat_id=query.from_user.id,
        text="Some description here",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def copy_usdt_address_1to1(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton("Send Screenshot", url="https://t.me/hun_era")]]
    query.bot.send_message(
        chat_id=query.from_user.id,
        text=f"Copy the Address below:`{USDT_ADDRESS}`\nFinish the payment and send screen shot to @sdfkjd",
        parse_mode=ParseMode.MARKDOWN,
        # reply_markup=InlineKeyboardMarkup(keyboard),
    )


def usdt_1to1(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Copy Address", callback_data="copy_usdt_address_1to1")],
    ]
    query.delete_message()
    query.answer()
    query.bot.send_message(
        chat_id=query.from_user.id,
        text="Some description here",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def vip(update: Update, context: CallbackContext):
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Exness", callback_data="exness")],
        [InlineKeyboardButton("USDT(TRC20)", callback_data="vip_usdt")],
    ]
    query.delete_message()
    query.answer()
    video = open("description.MP4", "rb")
    query.bot.send_chat_action(
        chat_id=query.from_user.id, action=ChatAction.UPLOAD_VIDEO
    )
    query.bot.send_video(chat_id=query.from_user.id, video=video)
    query.bot.send_message(
        chat_id=query.from_user.id,
        text="Some description here",
        reply_markup=InlineKeyboardMarkup(keyboard),
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


def main():
    """
    This is main method to control the bot events and add the handlers
    """
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(vip, pattern="vip_plan"))
    dispatcher.add_handler(CallbackQueryHandler(vip_exness, pattern="exness"))
    dispatcher.add_handler(CallbackQueryHandler(one_to_one, pattern="one_to_one"))
    dispatcher.add_handler(CallbackQueryHandler(cc_1to1, pattern="cc_1to1"))
    dispatcher.add_handler(CallbackQueryHandler(usdt_1to1, pattern="usdt_1to1"))
    dispatcher.add_handler(
        CallbackQueryHandler(copy_usdt_address_1to1, pattern="copy_usdt_address_1to1")
    )
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
