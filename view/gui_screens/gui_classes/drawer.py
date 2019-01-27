import math

ROBOT_RADIUS = 15
ROBOT_FACE_LENGTH = 20

VERTEX_RADIUS = 7
VERTEX_COLOR = 'blue'
VERTEX_STARVATION_TEMPLATE = 'ST: {}/{}'
VERTEX_PROBABILITY_TEMPLATE = 'P: {}'

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
        # text = VERTEX_STARVATION_TEMPLATE.format(0,v.st,v.ts,0),
    )

    vertex_probability_text = canvas.create_text(
        v['position'].x,
        v['position'].y - 20,
        # text = VERTEX_PROBABILITY_TEMPLATE.format(v.p),
    )

    return {
        'body': vertex_body,
        'text': {
            'starvation': vertex_starvation_text,
            'probability': vertex_probability_text,
        },
    }

def update_vertex(canvas,vertex,vertex_data,frame_index,show_text):
    v = vertex_data
    canvas.itemconfigure(
        vertex['text']['starvation'],
        # text = VERTEX_STARVATION_TEMPLATE.format(frame_index - v.lv, v.st),
        fill = 'red' if frame_index > v.lv + v.st else 'black',
        state = 'normal' if show_text['starvation'] else 'hidden',
    )
    canvas.itemconfigure(
        vertex['text']['probability'],
        # text = VERTEX_PROBABILITY_TEMPLATE.format('%.3f' % v.p),
        state = 'normal' if show_text['probability'] else 'hidden',

    )