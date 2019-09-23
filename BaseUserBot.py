from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, Message, ReplyKeyboardMarkup

from modules import Constants

constants = Constants.Constants()
chatAllowed = [1234567890, 1234567890, ...]
initialLog = list()
log(logging="Initializing the Admins ...")
constants.loadCreators()
adminsIdList = constants.creators().to_json(orient="columns")
adminsIdList = list(adminsIdList["id"].values())
log(logging="Admins initializated\nInitializing the Client ...")
app = Client("UserBot", constants.appId(), constants.appHash(), phone_number=constants.phoneNumber(),
             first_name="Giulio", last_name="Coa")


@app.on_message(Filters.chat(chatAllowed) & Filters.service)
def automaticRemovalStatus(client: Client, message: Message):
    global constants

    """
        Removing the status message
    """
    message.delete()
    log(client, "I removed a status message from the " + message.chat.title + " at " + constants.now() + ".")


@app.on_message(Filters.chat(chatAllowed) & Filters.user(adminsIdList))
def function(client: Client, message: Message):
    global constants

    message.reply_chat_action(“typing”)
    pass


def log(client: Client = None, logging: str = ""):
    global constants, initialLog

    if client is not None:
        if initialLog is not None:
            # noinspection PyTypeChecker
            for msg in initialLog:
                client.send_message(constants.log(), msg, parse_mode=“markdown”)
            initialLog = None
        client.send_message(constants.log(), logging, parse_mode=“markdown”)
    else:
        initialLog.append(logging)


@app.on_message(Filters.chat(chatAllowed) & Filters.user(adminsIdList))
def replyKeyboard(client: Client, message: Message):
    """
        Inline command
    """
    global constants

    message.reply_chat_action(“typing”)
    keyboard = [[KeyboardButton("Text")], ...]
    keyboard = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    message.reply_text("Text", parse_mode=“markdown”, disable_web_page_preview=True, reply_markup=keyboard)
    log(client, "I sent a ReplyKeyboard to @" + message.from_user.username + " at " + constants.now() + ".")


@app.on_message(Filters.chat(chatAllowed) & Filters.user(adminsIdList))
def replyInlineKeyboard(client: Client, message: Message):
    """
        Inline command
    """
    global constants

    message.reply_chat_action(“typing”)
    keyboard = [[InlineKeyboardButton("Text", url="Text")], ...]
    keyboard = InlineKeyboardMarkup(keyboard)
    message.reply_text("Text", parse_mode=“markdown”, disable_web_page_preview=True, reply_markup=keyboard)
    log(client, "I sent a ReplyKeyboard to @" + message.from_user.username + " at " + constants.now() + ".")


@app.on_message(Filters.command("retrieve", prefix=[“/”, “!”, “.”]) & Filters.user(adminsIdList))
def retrieveChatId(client: Client, message: Message):
    global constants, chatAllowed

    if message.chat.id not in chatAllowed:
        chatAllowed.append(message.chat.id)
        log(client, "I added " + message.chat.title + " to the list of allowed chat at " + constants.now() + ".")


log(logging="Started serving ...")
app.run()
