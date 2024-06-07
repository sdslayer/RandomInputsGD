import random
import keyboard
import pyautogui
import time

def holdRelease(key, holdtime):
    with pyautogui.hold(key):
        pyautogui.sleep(holdtime)

def pressKey(key):
    pyautogui.press(key)

def holdRelease2Keys(key1, key2, holdtime):
    pyautogui.keyDown(key1)
    pyautogui.keyDown(key2)
    time.sleep(holdtime)
    pyautogui.keyUp(key2)
    pyautogui.keyUp(key1)

def holdReleaseRandomTime(key):
    holdtime = random.uniform(0.1,1)
    with pyautogui.hold(key):
        pyautogui.sleep(holdtime)

while True:

    if keyboard.is_pressed('P'):
        exit()
    
    randomInt = random.randint(0,22)

    if randomInt == 0: # Short Left
        print(f"Random Choice: {randomInt} (Short Left)")
        holdRelease('A', 0.1)
    if randomInt == 1: # Medium Left
        print(f"Random Choice: {randomInt} (Medium Left)")
        holdRelease('A', 0.5)
    if randomInt == 2: # Long Left
        print(f"Random Choice: {randomInt} (Long Left)")
        holdRelease('A', 1)
    if randomInt == 3: # Short Right
        print(f"Random Choice: {randomInt} (Short Right)")
        holdRelease('D', 0.1)
    if randomInt == 4: # Medium Right
        print(f"Random Choice: {randomInt} (Medium Right)")
        holdRelease('D', 0.5)
    if randomInt == 5: # Long Right
        print(f"Random Choice: {randomInt} (Long Right)")
        holdRelease('D', 1)
    if randomInt == 6: # Jump
        print(f"Random Choice: {randomInt} (Jump)")
        pressKey('W')
    if randomInt == 7: # Jump & Hold (Dash Orb)
        print(f"Random Choice: {randomInt} (Jump & Hold (Dash Orb))")
        holdRelease('W', 0.3)
        holdRelease('W', 2)
    if randomInt == 8: # Left Jump
        print(f"Random Choice: {randomInt} (Left Jump)")
        holdRelease2Keys('A','W',0.5)
    if randomInt == 9: # Left Jump
        print(f"Random Choice: {randomInt} (Left Jump)")
        holdRelease2Keys('A','W',0.5)
    if randomInt == 10: # Long Left Jump
        print(f"Random Choice: {randomInt} (Long Left Jump)")
        holdRelease2Keys('A','W',2)
    if randomInt == 11: # Right Jump
        print(f"Random Choice: {randomInt} (Right Jump)")
        holdRelease2Keys('D','W',0.5)
    if randomInt == 12: # Right Jump
        print(f"Random Choice: {randomInt} (Right Jump)")
        holdRelease2Keys('D','W',0.5)
    if randomInt == 13: # Long Right Jump
        print(f"Random Choice: {randomInt} (Long Right Jump)")
        holdRelease2Keys('D','W',2)
    if randomInt == 14: # Rest (incase you have to not move)
        print(f"Random Choice: {randomInt} (Rest for 1 second)")
        time.sleep(1)
    if randomInt == 15: # Random (0.1,1) Left
        print(f"Random Choice: {randomInt} (Random (0.1,1) Left)")
        holdRelease('A', 1)
    if randomInt == 16: # Random (0.1,1) Right
        print(f"Random Choice: {randomInt} (Random (0.1,1) Right)")
        holdRelease('D', 1)
    if randomInt == 17: # Place Checkpoint
        print(f"Random Choice: {randomInt} (Place Checkpoint)")
        pressKey('Z')
    if randomInt == 18: # Place Checkpoint
        print(f"Random Choice: {randomInt} (Place Checkpoint)")
        pressKey('Z')
    if randomInt == 19: # Delete Checkpoint
        print(f"Random Choice: {randomInt} (Delete Checkpoint)")
        pressKey('X')
    if randomInt == 20: # Medium Right
        print(f"Random Choice: {randomInt} (Medium Right)")
        holdRelease('D', 0.5)
    if randomInt == 21: # Right Jump
        print(f"Random Choice: {randomInt} (Right Jump)")
        holdRelease2Keys('D','W',0.5)
    if randomInt == 22: # Place Checkpoint
        print(f"Random Choice: {randomInt} (Place Checkpoint)")
        pressKey('Z')