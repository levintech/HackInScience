from dataclasses import dataclass, replace


@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def frame_text(text: str, frame: Frame) -> str:
    
    length = max([len(line) for line in text.split("\n")])
    framed_text = frame.top_left + ''.join([frame.top for index in range(length)]) + frame.top_right + '\n'
    
    for line in text.split("\n"):
        framed_text = framed_text + frame.left + line + ''.join([' ' for item in range(length - len(line))]) + frame.right + '\n'
    
    framed_text = framed_text + frame.bottom_left + ''.join([frame.bottom for index in range(length)]) + frame.bottom_right
        
    return framed_text