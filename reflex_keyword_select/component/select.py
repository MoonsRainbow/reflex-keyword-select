import reflex as rx


def select_item_component(_option: list[str]):
    return rx.select.item(
        _option[1],
        value=_option[0],
    )


def select_component(
        _options: list[list[str]],
        _name: str,
        _value,
        _open,
        _on_open_change,
        _on_change,
        _on_focus,
) -> rx.Component:
    return rx.flex(
        rx.select.root(
            rx.select.trigger(
                radius='full'
            ),
            rx.select.content(
                rx.select.group(
                    rx.foreach(
                        _options,
                        select_item_component
                    ),
                ),
                modal=False,
                position='popper',
                side='bottom',
                align='center',
            ),
            name=_name,
            open=_open,
            on_open_change=_on_open_change,
            value=_value,
            on_change=_on_change,
            on_focus=_on_focus,
            size='3',
        ),
        top='-44px',
        position='relative',
        z_index=-999,
        direction='column',
        width='100$',
        spacing='0',
    )
