import reflex as rx


def title_component(_text):
    return rx.text(
        _text,
        align='left',
        justify='center',
        font_size='14px',
        color=rx.color_mode_cond(
            light='#666',
            dark='#AAA',
        ),
    )
