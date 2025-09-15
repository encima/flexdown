import reflex as rx
from reflex_monaco import monaco
from app.states.editor_state import EditorState


def editor() -> rx.Component:
    """The editor component."""
    return rx.el.div(
        monaco(
            key=EditorState.current_path,
            default_value=EditorState.current_note_content,
            language="markdown",
            theme="vs-dark",
            on_change=EditorState.set_current_note_content.debounce(150),
            options={
                "wordWrap": "on",
                "minimap": {"enabled": False},
                "lineNumbers": "off",
                "glyphMargin": False,
                "folding": False,
                "lineDecorationsWidth": 0,
                "lineNumbersMinChars": 0,
            },
        ),
        class_name="w-full h-full border-r border-gray-200 bg-[#1e1e1e]",
    )