def alarm():
    import winsound
    import msvcrt
    import time
    import pyautogui

    pyautogui.click(463, 746)

    while True:
        duration = 1000  # milliseconds
        freq = 300  # Hz
        winsound.Beep(freq, duration)
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 27:
                z = input("Enter c to continue.  Any other key ends the program. ")
                time.sleep(5)
                break

    return z
