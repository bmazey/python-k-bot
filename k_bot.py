from pynput.keyboard import Controller, Key


def press_k() -> None:
    keyboard = Controller()

    # Press and release the 'K' key
    keyboard.press('k')
    keyboard.release('k')


if __name__ == '__main__':
    press_k()
