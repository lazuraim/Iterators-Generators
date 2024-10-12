import random
import time


def emit_gel(max_step: int):
    last = random.randint(0, 100)
    while True:
        sign = (yield last)
        last += sign * random.randint(0, max_step)
        if last > 100:
            last = last - (last - 100)


def valve(generator):
    sign: int = 1
    pressure = next(generator)
    while True:
        pressure = generator.send(sign)
        if pressure < 10 or pressure > 90:
            print(f"Emergency break: pressure is {pressure}")
            generator.close()
            exit(0)
        elif pressure < 20 or pressure > 80:
            sign = -sign
        print(pressure)
        time.sleep(0.1)


if __name__ == "__main__":
    step: int = 10
    gen = emit_gel(step)
    valve(gen)
