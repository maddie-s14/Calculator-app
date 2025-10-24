import dearpygui.dearpygui as dpg

dpg.create_context()

initial_point = (0, 0)
points = []
current_color = (0, 0, 0, 255)  # Alpha value fixed to 255 (max)

def clear_handler(sender, app_data):
    dpg.delete_item("drawing_list", children_only=True)

def click_handler(sender, app_data):
    global initial_point
    initial_point = dpg.get_drawing_mouse_pos()

def change_mouse_drag_handler(sender, app_data):
    # app_data is (delta_x, delta_y), but we want current mouse position
    current_pos = dpg.get_drawing_mouse_pos()
    points.append(current_pos)
    
    if len(points) >= 2:
        dpg.draw_line(points[-2], points[-1],
                      color=current_color,
                      thickness=3,
                      parent="drawing_list")

def release_handler(sender, app_data):
    global points
    points = []

with dpg.handler_registry():
    dpg.add_mouse_drag_handler(callback=change_mouse_drag_handler)
    dpg.add_mouse_click_handler(callback=click_handler)
    dpg.add_mouse_release_handler(callback=release_handler)
    dpg.add_key_press_handler(key=dpg.mvKey_C, callback=clear_handler)

with dpg.window(label="Drawing App", tag="main_window"):

    with dpg.drawlist(width=400, height=400, parent="main_window", tag="drawing_list"):
        pass

dpg.create_viewport(title="DearPyGUI Drawing", width=400, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

