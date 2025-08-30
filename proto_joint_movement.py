import bpy 



pointer_knuckle = bpy.data.objects["pointer_finger_knu"].data.vertices
pointer_tip = bpy.data.objects["pointer_finger_tip"].data.vertices



def move_pointer_knuckle_x(cm):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.x -= cm 
        pointer_tip[i].co.x -= cm

def move_pointer_knuckle_y(cm):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.y -= cm
        pointer_tip[i].co.y -= cm

def move_pointer_knuckle_z(cm):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.z -= cm
        pointer_tip[i].co.z -= cm

def rotate_pointer_knuckle_x(rad):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.rotate_axis('X', rad)
        pointer_tip[i].co.rotate_axis('X', rad)

def rotate_pointer_knuckle_y(rad):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.rotate_axis('Y', rad)
        pointer_tip[i].co.rotate_axis('Y', rad)

def rotate_pointer_knuckle_z(rad):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.rotate_axis('Z', rad)
        pointer_tip[i].co.rotate_axis('Z', rad)

def reset_pointer_knuckle():
    bpy.data.objects["pointer_finger_knu"].data.location = (0,0,0)
    #bpy.data.objects["pointer_finger_knu"].data.rotation_euler = (0,0,0)
    bpy.data.objects["pointer_finger_tip"].data.location = (10,0,0)


def get_pointer_knuckle_position():
    return (pointer_knuckle[0].co.x, pointer_knuckle[0].co.y, pointer_knuckle[0].co.z)
def get_pointer_tip_position():
    return (pointer_tip[0].co.x, pointer_tip[0].co.y, pointer_tip[0].co.z)

def xyz_move_pointer_knuckle(x, y, z):
    move_pointer_knuckle_x(x)
    move_pointer_knuckle_y(y)
    move_pointer_knuckle_z(z)

def xyz_rotate_pointer_knuckle(x, y, z):
    rotate_pointer_knuckle_x(x)
    rotate_pointer_knuckle_y(y)
    rotate_pointer_knuckle_z(z)

reset_pointer_knuckle()

xyz_move_pointer_knuckle(10,10,10)