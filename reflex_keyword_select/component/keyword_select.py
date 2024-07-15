import reflex as rx
from copy import deepcopy
from .text import title_component
from .input import input_component
from .select import select_component


class KeywordSelect(rx.ComponentState):
    is_select_open: bool = False
    is_search_hidden: bool = True

    options: list[list[str]]
    options_searching: list[list[str]]

    selected_index: int
    selected_value: str
    selected_text: list[str]

    input_text: list[str]

    spacing = 3
    param_width = 165

    param_style = {
        'height': '66px',
        'spacing': '1',
    }

    param_short_style = {
        'width': f'{param_width}px',
        **param_style,
    }

    param_long_style = {
        'width': f'{(param_width * 2) + (spacing * 4)}px',
        **param_style,
    }

    def initial(self, _option, _value):
        self.set_options(_option)
        self.set_options_searching(deepcopy(_option))
        self.set_selected_value(_value)

    def reset_values(self):
        self.set_selected_value('-1')
        self.set_selected_index(0)
        self.selected_text = ['All']
        self.input_text = ['All']

    def toggle_select(self):
        self.set_options_searching(deepcopy(self.options))
        self.is_select_open = not self.is_select_open

    def change_input(self, _):
        self.is_select_open = not self.is_select_open

    def validate_input(self, _text):
        self.is_search_hidden = True
        _text = _text.strip().lower()
        for _index, _option in enumerate(self.options):
            if _option[1].lower() == _text:
                self.set_selected_value(_option[0])
                self.set_selected_index(_index)
                self.set_selected_text([_option[1]])
                self.input_text = self.selected_text
                break
        else:
            self.input_text = self.selected_text

    def selected(self, _selected_value):
        self.selected_value = _selected_value
        self.selected_index = [_ for _, __ in enumerate(self.options) if __[0] == _selected_value][0]
        self.selected_text = [_ for _ in self.options if _[0] == _selected_value][0][1:]
        self.input_text = self.selected_text
        self.is_search_hidden = True

    def start_typing(self, _):
        self.input_text = ['']

    def typing(self, _text):
        self.input_text = [_text]
        self.is_search_hidden = False

    def searching(self, _text):
        self.set_options_searching(deepcopy(self.options))
        _temp_options, _text = [], _text.lower()
        for _option in self.options:
            if _text in _option[1].lower():
                _temp_options.append(deepcopy(_option))
        self.set_options_searching(deepcopy(_temp_options))

    @classmethod
    def get_component(cls, **props):
        _title = props.pop('_title')
        _options = props.pop('_options')
        _name = props.pop('_name')
        _input_id = f'{_name}_input'
        _value = props.pop('_value')
        _on_change = props.pop('_on_change')
        _placeholder = props.pop('_placeholder') if '_placeholder' in props else ''
        _is_long = props.pop('_is_long') if '_is_long' in props else False
        _param_style = cls.param_long_style if _is_long else cls.param_short_style

        return rx.vstack(
            title_component(
                _text=_title
            ),
            input_component(
                _id=_input_id,
                _placeholder=_placeholder,
                _on_click=cls.toggle_select,
                _value=cls.input_text,
                _on_focus=[
                    cls.start_typing
                ],
                _on_change=[
                    cls.typing,
                    cls.change_input,
                    cls.searching,
                ],
                _on_blur=[
                    cls.validate_input
                ],
            ),
            select_component(
                _options=cls.options_searching,
                _name=_name,
                _value=cls.selected_value,
                _on_change=cls.selected,
                _open=cls.is_select_open,
                _on_open_change=cls.set_is_select_open,
                _on_focus=rx.set_focus(_input_id),
            ),
            on_mount=[
                cls.initial(_options, _value),  # type: ignore
                cls.reset_values
            ],
            # **_param_style,
            # **props,
        )


keyword_select = KeywordSelect.create
