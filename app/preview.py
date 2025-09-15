import reflex as rx
from app.states.editor_state import EditorState


def preview() -> rx.Component:
    """The preview component."""
    return rx.el.div(
        rx.markdown(
            EditorState.current_note_content,
            component_map={
                "h1": lambda text: rx.el.h1(
                    text, class_name="text-3xl font-bold my-4 text-gray-800"
                ),
                "h2": lambda text: rx.el.h2(
                    text, class_name="text-2xl font-bold my-3 text-gray-700"
                ),
                "h3": lambda text: rx.el.h3(
                    text, class_name="text-xl font-bold my-2 text-gray-600"
                ),
                "p": lambda text: rx.el.p(
                    text, class_name="text-base my-2 text-gray-600 leading-relaxed"
                ),
                "ul": lambda text: rx.el.ul(
                    text, class_name="list-disc list-inside my-4 pl-4 text-gray-600"
                ),
                "ol": lambda text: rx.el.ol(
                    text, class_name="list-decimal list-inside my-4 pl-4 text-gray-600"
                ),
                "li": lambda text: rx.el.li(text, class_name="my-1"),
                "code": lambda text: rx.el.code(
                    text,
                    class_name="bg-gray-100 text-red-500 font-mono px-1 py-0.5 rounded text-sm",
                ),
                "a": lambda text, **props: rx.el.a(
                    text, **props, class_name="text-blue-500 hover:underline"
                ),
            },
        ),
        class_name="w-full h-full p-8 overflow-y-auto bg-white",
    )