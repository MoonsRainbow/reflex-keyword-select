import reflex as rx


def input_component(
        _id: str,
        _placeholder: str,
        _value,
        _on_click,
        _on_focus,
        _on_change,
        _on_blur,
) -> rx.Component:
    return rx.input(
        rx.input.slot(
            padding='8px'
        ),
        rx.input.slot(
            rx.icon(
                'chevron-down',
                size=19,
                color=rx.color_mode_cond(
                    light='color(display-p3 0.129 0.126 0.111)',
                    dark='color(display-p3 0.933 0.933 0.926)'
                ),
                stroke_width=1.5,
            ),
            order=999,
            cursor='pointer',
            on_click=_on_click,
        ),
        id=_id,
        padding='8px 0px 8px 0px',
        spacing='0',
        placeholder=_placeholder,
        background=rx.color_mode_cond(
            light='#FEFEFE',
            dark='#292929'
        ),
        value=_value[0],
        on_change=_on_change,
        on_focus=_on_focus,
        on_blur=_on_blur,
        width='100%',
        radius='full',
        size='3',
        debounce_timeout=500,
    )
