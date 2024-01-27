
import reflex as rx


class State(rx.State):
    pass

def ejercicio1() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('1'),
            bg = '#58B99D'
        ),
        rx.box(
            rx.text('2'),
            bg = '#5296D5'
        ),
        rx.box(
            rx.text('3'),
            bg = '#925CB1'
        ),
        rx.box(
            rx.text('4'),
            bg = '#38485C'
        ),
        rx.box(
            rx.text('5'),
            bg = '#EAC645'
        ),
        rx.box(
            rx.text('6'),
            bg = '#D8833B'
        ),
        rx.box(
            rx.text('7'),
            bg = '#D65745'
        ),
        rx.box(
            rx.text('8'),
            bg = '#BEC3C7'
        ),
        rx.box(
            rx.text('9'),
            bg = '#65C97A'
        ),
        rx.box(
            rx.text('10'),
            bg = '#4A9E86'
        ),
        w = '80%',
        h = '100px',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',

        margin = '60px',
        color = 'white',
    )

def ejercicio2() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('1'),
            bg = '#58B99D'
        ),
        rx.box(
            rx.text('2'),
            bg = '#5296D5'
        ),
        rx.box(
            rx.text('3'),
            bg = '#925CB1'
        ),
        rx.box(
            rx.text('4'),
            bg = '#38485C'
        ),
        rx.box(
            rx.text('5'),
            bg = '#EAC645'
        ),
        rx.box(
            rx.text('6'),
            bg = '#D8833B'
        ),
        rx.box(
            rx.text('7'),
            bg = '#D65745'
        ),
        rx.box(
            rx.text('8'),
            bg = '#BEC3C7'
        ),
        rx.box(
            rx.text('9'),
            bg = '#65C97A'
        ),
        rx.box(
            rx.text('10'),
            bg = '#4A9E86'
        ),
        w = '80%',
        h = 'auto',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',
        margin = '60px',
        color = 'white',
        flex_direction = 'column-reverse'
    )

def ejercicio3() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('1'),
            bg = '#58B99D',
            w = '33.33%'
        ),
        rx.box(
            rx.text('2'),
            bg = '#5296D5',
            w = '33.33%'
        ),
        rx.box(
            rx.text('3'),
            bg = '#925CB1',
            w = '33.33%'
        ),
        rx.box(
            rx.text('4'),
            bg = '#38485C',
            w = '33.33%'
        ),
        rx.box(
            rx.text('5'),
            bg = '#EAC645',
            w = '33.33%'
        ),
        rx.box(
            rx.text('6'),
            bg = '#D8833B',
            w = '33.33%'
        ),
        rx.box(
            rx.text('7'),
            bg = '#D65745',
            w = '33.33%'
        ),
        rx.box(
            rx.text('8'),
            bg = '#BEC3C7',
            w = '33.33%'
        ),
        rx.box(
            rx.text('9'),
            bg = '#65C97A',
            w = '33.33%'
        ),
        rx.box(
            rx.text('10'),
            bg = '#4A9E86',
            w = '33.33%'
        ),
        w = '80%',
        h = '200px',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',
        margin = '60px',
        color = 'white',
        flex_wrap = 'wrap'
    )

def ejercicio4() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('1'),
            bg = '#58B99D',
            flex_grow = '1',
            order = '2',
        ),
        rx.box(
            rx.text('2'),
            bg = '#5296D5',
            flex_grow = '1',
            order = '3',
        ),
        rx.box(
            rx.text('3'),
            bg = '#925CB1',
            flex_grow = '1',
            order = '4',
        ),
        rx.box(
            rx.text('4'),
            bg = '#38485C',
            flex_grow = '1',
            order = '5',
        ),
        rx.box(
            rx.text('5'),
            bg = '#EAC645',
            flex_grow = '1',
            order = '1',
        ),
        rx.box(
            rx.text('6'),
            bg = '#D8833B',
            flex_grow = '1',
            order = '10',
        ),
        rx.box(
            rx.text('7'),
            bg = '#D65745',
            flex_grow = '1',
            order = '6',
        ),
        rx.box(
            rx.text('8'),
            bg = '#BEC3C7',
            flex_grow = '1',
            order = '7',
        ),
        rx.box(
            rx.text('9'),
            bg = '#65C97A',
            flex_grow = '1',
            order = '8',
        ),
        rx.box(
            rx.text('10'),
            bg = '#4A9E86',
            flex_grow = '1',
            order = '9',
        ),
        w = '80%',
        h = '200px',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',
        margin = '60px',
        color = 'white',
        justify_content = 'space-between',
        

    )

def ejercicio5() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('1'),
            bg = '#58B99D'
        ),
        rx.box(
            rx.text('2'),
            bg = '#5296D5'
        ),
        rx.box(
            rx.text('3'),
            bg = '#925CB1'
        ),
        rx.box(
            rx.text('4'),
            bg = '#38485C'
        ),
        rx.box(
            rx.text('5'),
            bg = '#EAC645'
        ),
        rx.box(
            rx.text('6'),
            bg = '#D8833B'
        ),
        rx.box(
            rx.text('7'),
            bg = '#D65745'
        ),
        rx.box(
            rx.text('8'),
            bg = '#BEC3C7'
        ),
        rx.box(
            rx.text('9'),
            bg = '#65C97A'
        ),
        rx.box(
            rx.text('10'),
            bg = '#4A9E86'
        ),
        text_align = 'center',
        w = '80%',
        h = '500px',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',
        margin = '60px',
        color = 'white',
        flex_direction = 'column',
        justify_content = 'space-between',

    )

def ejercicio6() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text(
                '1',
            font_size = '1em',
            ),
            bg = '#58B99D'
        ),
        rx.box(
            rx.text(
                '2',
            font_size = '4em',
            ),
            bg = '#5296D5'
        ),
        rx.box(
            rx.text(
                '3',
            font_size = '5em',
            ),
            bg = '#925CB1'
        ),
        rx.box(
            rx.text(
                '4',
                font_size = '6em',
            ),
            bg = '#38485C'
        ),
        rx.box(
            rx.text(
                '5',
            font_size = '0.5em',
            ),
            bg = '#EAC645'
        ),
        rx.box(
            rx.text(
                '6',
            font_size = '4em',
            ),
            bg = '#D8833B'
        ),
        rx.box(
            rx.text(
                '7',
            font_size = '4em',
            ),
            bg = '#D65745'
        ),
        rx.box(
            rx.text(
                '8',
            font_size = '4em',
            ),
            bg = '#BEC3C7'
        ),
        rx.box(
            rx.text(
                '9',
            font_size = '4em',
            ),
            bg = '#65C97A'
        ),
        rx.box(
            rx.text(
                '10',
            font_size = '3em',
            ),
            bg = '#4A9E86'
        ),
        w = '80%',
        h = '200px',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',
        margin = '60px',
        color = 'white',
        #align_items = 'center',
        max_height = 'max-content',
        #align_items = 'flex-start',
        align_items = 'baseline',
    )

def ejercicio7() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('1'),
            bg = '#58B99D',
            w = '33.33%'
        ),
        rx.box(
            rx.text('2'),
            bg = '#5296D5',
            w = '33.33%'
        ),
        rx.box(
            rx.text('3'),
            bg = '#925CB1',
            w = '33.33%'
        ),
        rx.box(
            rx.text('4'),
            bg = '#38485C',
            w = '33.33%'
        ),
        rx.box(
            rx.text('5'),
            bg = '#EAC645',
            w = '33.33%'
        ),
        rx.box(
            rx.text('6'),
            bg = '#D8833B',
            w = '33.33%'
        ),
        rx.box(
            rx.text('7'),
            bg = '#D65745',
            w = '33.33%'
        ),
        rx.box(
            rx.text('8'),
            bg = '#BEC3C7',
            w = '33.33%'
        ),
        rx.box(
            rx.text('9'),
            bg = '#65C97A',
            w = '33.33%'
        ),
        rx.box(
            rx.text('10'),
            bg = '#4A9E86',
            w = '33.33%'
        ),
        text_align = 'center',
        w = '80%',
        h = '200px',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',
        margin = '60px',
        color = 'white',
        flex_wrap = 'wrap',
        align_content = 'center',
    )

def ejercicio8() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text('1'),
            bg = '#58B99D',
            flex_grow = '1',
            align_self = 'flex-start',
        
        ),
        rx.box(
            rx.text('2'),
            bg = '#5296D5',
            flex_grow = '1',


        ),
        rx.box(
            rx.text('3'),
            bg = '#925CB1',
            flex_grow = '1',
            align_self = 'flex-start',
        
        ),
        rx.box(
            rx.text('4'),
            bg = '#38485C',
            flex_grow = '1',
            align_self = 'flex-start',
        
        ),
        rx.box(
            rx.text('5'),
            bg = '#EAC645',
            flex_grow = '1',
            align_self = 'flex-start',
        
        ),
        rx.box(
            rx.text('6'),
            bg = '#D8833B',
            flex_grow = '1',
            align_self = 'center',
            
        ),
        rx.box(
            rx.text('7'),
            bg = '#D65745',
            flex_grow = '1',
            align_self = 'flex-start',
        
        ),
        rx.box(
            rx.text('8'),
            bg = '#BEC3C7',
            flex_grow = '1',
            align_self = 'flex-start',
        
        ),
        rx.box(
            rx.text('9'),
            bg = '#65C97A',
            flex_grow = '1',
            align_self = 'flex-end',
        
        ),
        rx.box(
            rx.text('10'),
            bg = '#4A9E86',
            flex_grow = '1',
            align_self = 'flex-start',
        
        ),
        w = '80%',
        h = '200px',
        text_align = 'center',
        border = '2px',
        border_color = 'black',
        border_stlyle = 'solid',
        margin = '60px',
        color = 'white',
        justify_content = 'space-between',
        #max_height = 'max-content', esta linea y la siguiente hace que no se consuma toda la vertical
        #align_items = 'baseline',  con esta la vertical queda en la parte superior
    
    )


def index() -> rx.Component:
    return rx.box(
        rx.heading('Ejercicio 1'),
        ejercicio1(),
        rx.divider(
            border_color="black"
        ),
        rx.heading('Ejercicio 2'),
        ejercicio2(),
        rx.divider(
            border_color="black"
        ),
        rx.heading('Ejercicio 3'),
        ejercicio3(),
        rx.divider(
            border_color="black"
        ),
        rx.heading('Ejercicio 4'),
        ejercicio4(),
        rx.divider(
            border_color="black"
        ),
        rx.heading('Ejercicio 5'),
        ejercicio5(),
        rx.divider(
            border_color="black"
        ),
        rx.heading('Ejercicio 6'),
        ejercicio6(),
        rx.divider(
            border_color="black"
        ),
        rx.heading('Ejercicio 7'),
        ejercicio7(),
        rx.divider(
            border_color="black"
        ),
        rx.heading('Ejercicio 8'),
        ejercicio8(),
        rx.divider(
            border_color="black"
        ),
    )





# Create app instance and add index page.
app = rx.App()
app.add_page(index)
