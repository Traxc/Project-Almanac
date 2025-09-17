import bpy 



### For initializing spheres that represent the knuckle and tip joint of the pointer finger 
#bpy.ops.mesh.primitive_uv_sphere_add(
#    segments=32,
#    ring_count=16,
#    radius=1.0,
#    location=(0, 0, 0),
#    rotation=(0, 0, 0),
#    scale=(1, 1, 1)
#)

#bpy.context.selected_objects[0].name = "pointer_finger_knu" 
#bpy.ops.mesh.primitive_uv_sphere_add(
#    segments=32,
#    ring_count=16,
#    radius=1.0,
#    location=(0, 10, 0),
#    rotation=(0, 0, 0),
#    scale=(1, 1, 1)
#)
#bpy.context.selected_objects[0].name = "pointer_finger_tip" 



### Global Variables 
pointer_knuckle_true = bpy.data.objects["pointer_finger_knu"]
pointer_knuckle_loc = pointer_knuckle_true.location 

pointer_tip_true = bpy.data.objects["pointer_finger_tip"]
pointer_tip_loc = pointer_tip_true.location 


pointer_knuckle = bpy.data.objects["pointer_finger_knu"].data.vertices
pointer_tip = bpy.data.objects["pointer_finger_tip"].data.vertices
print( bpy.data.objects["pointer_finger_tip"].data)



##NOTE: ALL MEASURMENTS IN METRIC SYSTEM ( mostly use cm/mm) 

### As we move the kunckle joint the tip must follow, must code for independent movement change in the tip joint 

### MOVE the pointer knuckle joint in the x direction 
def move_pointer_knuckle_x(cm):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.x -= cm 
        pointer_tip[i].co.x -= cm

### MOVE the pointer knuckle joint in the y direction 
def move_pointer_knuckle_y(cm):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.y -= cm
        pointer_tip[i].co.y -= cm
        
### MOVE the pointer knuckle joint in the z direction 
def move_pointer_knuckle_z(cm):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.z -= cm
        pointer_tip[i].co.z -= cm

### Rotate the pointer knuckle along x axis, 

def rotate_pointer_knuckle_x(rad):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.rotate_axis('X', rad)
        pointer_tip[i].co.rotate_axis('X', rad)

### Rotate the pointer knuckle along x axis, 
def rotate_pointer_knuckle_y(rad):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.rotate_axis('Y', rad)
        pointer_tip[i].co.rotate_axis('Y', rad)

### Rotate the pointer knuckle along x axis, 
def rotate_pointer_knuckle_z(rad):
    for i, j  in enumerate(list(pointer_knuckle)): 
        pointer_knuckle[i].co.rotate_axis('Z', rad)
        pointer_tip[i].co.rotate_axis('Z', rad)

def reset_pointer_knuckle():
    pointer_knuckle_true.location = (0.0,0.0,0.0)
    #bpy.data.objects["pointer_finger_knu"].data.rotation_euler = (0,0,0)
    pointer_tip_true.location = (10.0,0.0,0.0)


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

#xyz_move_pointer_knuckle(10,10,10)