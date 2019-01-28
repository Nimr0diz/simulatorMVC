import math

ROBOT_RADIUS = 15
ROBOT_FACE_LENGTH = 20

VERTEX_RADIUS = 7
VERTEX_COLOR = 'blue'
VERTEX_TARGET_COLOR = 'magenta'
VERTEX_STARVATION_TEMPLATE = 'ST: {}/{}'
VERTEX_PROBABILITY_TEMPLATE = 'P: {}'
VERTEX_TS_TEMPLATE = 'TS: {}'

DEFAULT_FONT = ('Helvetica',-10)

def create_robot(canvas,position):
    robot_body = canvas.create_oval(
        position.x -  ROBOT_RADIUS,
        position.y -  ROBOT_RADIUS,
        position.x +  ROBOT_RADIUS,
        position.y +  ROBOT_RADIUS,
        outline = 'black',
    )
    
    robot_face = canvas.create_line(
        position.x,
        position.y,
        position.x + ROBOT_FACE_LENGTH,
        position.y,
    )

    return {
        'body': robot_body,
        'face': robot_face,
    }

def update_robot(canvas,robot,position,angle):
    canvas.coords(
        robot['body'],
        position.x -  ROBOT_RADIUS,
        position.y -  ROBOT_RADIUS,
        position.x +  ROBOT_RADIUS,
        position.y +  ROBOT_RADIUS,
    )
    canvas.coords(
        robot['face'],
        position.x,
        position.y,
        position.x + math.cos(angle) * ROBOT_FACE_LENGTH,
        position.y + math.sin(angle) * ROBOT_FACE_LENGTH,
    )

def create_vertex(canvas,vertex):
    v = vertex
    vertex_body = canvas.create_oval(
        v['position'].x - VERTEX_RADIUS,
        v['position'].y - VERTEX_RADIUS,
        v['position'].x + VERTEX_RADIUS,
        v['position'].y + VERTEX_RADIUS,
        fill = VERTEX_COLOR,
    )

    vertex_starvation_text = canvas.create_text(
        v['position'].x,
        v['position'].y - 40,
        text = VERTEX_STARVATION_TEMPLATE.format(0,v['starvation'],0,0),
        font = DEFAULT_FONT
    )

    vertex_probability_text = canvas.create_text(
        v['position'].x,
        v['position'].y - 30,
        text = VERTEX_PROBABILITY_TEMPLATE.format(v['probability']),
        font = DEFAULT_FONT
    )

    vertex_total_starvation_text = canvas.create_text(
        v['position'].x,
        v['position'].y - 20,
        text = VERTEX_TS_TEMPLATE.format(0),
        font = DEFAULT_FONT
    )

    return {
        'body': vertex_body,
        'text': {
            'starvation': vertex_starvation_text,
            'probability': vertex_probability_text,
            'total_starvation': vertex_total_starvation_text,
        },
    }

def update_vertex(canvas,vertex,vertex_static,vertex_live,frame_index,show_text):
    canvas.itemconfigure(
        vertex['body'],
        fill = VERTEX_TARGET_COLOR if vertex_live['is_target'] else VERTEX_COLOR
    )
    canvas.itemconfigure(
        vertex['text']['starvation'],
        text = VERTEX_STARVATION_TEMPLATE.format(frame_index - vertex_live['last_visit'], vertex_static['starvation']),
        fill = 'red' if frame_index > vertex_live['last_visit'] + vertex_static['starvation'] else 'black',
        state = 'normal' if show_text else 'hidden',
    )
    canvas.itemconfigure(
        vertex['text']['probability'],
        # text = VERTEX_PROBABILITY_TEMPLATE.format('%.3f' % vertex_static['probability']),
        state = 'normal' if show_text else 'hidden',
    )
    canvas.itemconfigure(
        vertex['text']['total_starvation'],
        text = VERTEX_TS_TEMPLATE.format(vertex_live['total_starvation']),
        state = 'normal' if show_text else 'hidden',
    )