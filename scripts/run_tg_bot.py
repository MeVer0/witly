from src.bot.witly import bot

if __name__ == '__main__':
    print('starting bot...')
    bot.polling(none_stop=True)