"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_keyword_select.component import keyword_select


class State(rx.State):
    """The app state."""

    test_value: str = ''

    test_options: list[list[str]] = [
        ['-1', 'All'],
        ['0', 'Apple'],
        ['1', 'Banana'],
        ['2', 'Mango'],
        ['3', 'Melon'],
    ]


def index() -> rx.Component:
    return rx.container(
        keyword_select(
            _title='Fruits',
            _options=State.test_options,
            _name='keyword_select',
            _value=State.test_value,
            _on_change=State.set_test_value,
        )
    )


app = rx.App()
app.add_page(index)
