import pyautogui
from time import sleep
from keyboard import add_hotkey
from lib.utils import color_print

class Willump:
  def kill(self):
    if self.__state == True:
      self.__state = False

    color_print(
      'Willump - Desactivation! Current state: {}'.format(self.__state), 
      'green' if self.__state else 'red'
    )

    color_print(
      'Nunu - Willump! Don\'t leave me!',
      'blue'
    )

  def launch(self):
    if self.__state == False:
      self.__state = True

    color_print(
      'Willump - Activation! Current state: {}'.format(self.__state), 
      'green' if self.__state else 'red'
    )

    color_print(
      'Nunu - This way to... Adventure!',
      'blue'
    )

  def snowball(self):
    def locateAndClick(asset, message):
      locate = pyautogui.locateOnScreen(asset, confidence=0.9)
      if locate != None:
        color_print(
          message,
          'green'
        )
        location = pyautogui.center(locate)
        pyautogui.moveTo(x=location.x, y=location.y)
        sleep(1)
        pyautogui.mouseDown()
        sleep(0.5)
        pyautogui.mouseUp()
        sleep(1)
        pyautogui.moveTo(100,200)

    while True:
      if self.__state == True:
        locateAndClick('./assets/location/find.png', 'Willump - Match Initialization')
        locateAndClick('./assets/location/accept.png', 'Willump - Match Confirmed')
        locateAndClick('./assets/location/exit.png', 'Willump - Match closed')
        locateAndClick('./assets/location/ok.png', 'Willump - Match closed')
        locateAndClick('./assets/location/buy1.png', 'Willump - Champion buyed')
        locateAndClick('./assets/location/buy2.png', 'Willump - Champion buyed')
        locateAndClick('./assets/location/buy3.png', 'Willump - Champion buyed')

  def __init__(self):
    self.__state = False
    print('='*50)

    color_print(
      'Nunu&Willump Bot',
      'magenta'
    )

    color_print(
      'An automated Bot that plays Teamfight Tactics for you while you sleep!',
      'cyan'
    )

    color_print(
      ' - Press $ARROW_UP on your keyboard to start the bot',
      'white'
    )

    color_print(
      ' - Press $ESC on your keyboard to pause the bot',
      'white'
    )

    print('='*50)

    add_hotkey('up arrow', lambda: self.launch())
    add_hotkey('esc', lambda: self.kill())

Nunu = Willump()
Nunu.snowball()