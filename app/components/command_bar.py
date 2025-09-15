import reflex as rx
from app.states.editor_state import EditorState


def command_bar() -> rx.Component:
    """The command bar component."""
    return rx.el.div(
        rx.el.div(
            rx.el.span(EditorState.context, class_name="text-gray-900"),
            rx.icon("chevron-right", class_name="h-4 w-4 text-gray-400"),
            rx.el.span(EditorState.stream, class_name="text-gray-900"),
            rx.icon("chevron-right", class_name="h-4 w-4 text-gray-400"),
            rx.el.span(EditorState.note_name, class_name="font-semibold text-gray-900"),
            class_name="flex items-center gap-2 text-sm font-medium",
        ),
        class_name="flex items-center h-12 px-4 border-b border-gray-200 bg-gray-50",
    )