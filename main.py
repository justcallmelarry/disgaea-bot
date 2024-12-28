import time
from dataclasses import dataclass
from pathlib import Path
from typing_extensions import Annotated

import pydirectinput
import typer
from pynput.keyboard import Listener


class StartIteration(Exception):
    pass


@dataclass
class Instruction:
    action: str
    button: str
    wait: float = 0

    def validate(self) -> None:
        if self.action not in ("#", ">", "<"):
            raise ValueError("Invalid instruction")

        if self.wait < 0:
            raise ValueError("Wait time cannot be negative")


def on_press(key):
    if str(key) == "Key.f8":
        raise InterruptedError

    if str(key) != "Key.f12":
        return

    raise StartIteration


def parse_instructions(file_contents: str) -> list[Instruction]:
    instructions = []
    for line in file_contents.splitlines():
        if line.startswith("//"):
            continue

        instruction = Instruction(
            action=line[:1],
            button=line[1:2],
        )
        if len(line) > 2:
            instruction.wait = float(line[2:])

        instruction.validate()
        instructions.append(instruction)

    return instructions


def run_instructions(instructions: list[Instruction]) -> None:
    for i in instructions:
        match i.action:
            case "#":
                pydirectinput.press(i.button, _pause=False)
            case ">":
                pydirectinput.keyDown(i.button)
            case "<":
                pydirectinput.keyUp(i.button)

        if i.wait:
            time.sleep(i.wait)


def main(
    filename: Path,
    iterations: Annotated[int, typer.Option("--iterations", "-i")] = 50,
) -> None:
    with open(filename) as f:
        file_contents = f.read()

    instructions = parse_instructions(file_contents)

    try:
        with Listener(on_press=on_press, on_release=None) as listener:
            listener.join()
    except StartIteration:
        keep_going = True
    except InterruptedError:
        pass

    i = 0
    current_time = time.time()
    while keep_going:
        run_instructions(instructions)
        i += 1
        now = time.time()
        print(f"Run {i} done in {round(now - current_time, 1)}s!")
        current_time = now
        if i >= iterations:
            break


if __name__ == "__main__":
    typer.run(main)
