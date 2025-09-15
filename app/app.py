import reflex as rx
from app.states.editor_state import EditorState
from app.editor import editor
from app.preview import preview
from app.components.command_bar import command_bar


def index() -> rx.Component:
    """The main page of the app."""
    return rx.el.div(
        command_bar(),
        rx.el.main(
            rx.el.div(
                editor(), preview(), class_name="grid grid-cols-1 md:grid-cols-2 flex-1"
            ),
            class_name="flex flex-col h-[calc(100vh-3rem)]",
        ),
        class_name="font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    route="/[[...splat]]",
    title="Reflex Markdown Editor",
    on_load=EditorState.on_load,
)