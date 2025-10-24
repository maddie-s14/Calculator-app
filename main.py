import dearpygui.dearpygui as dpg
import traceback

print("✅ Starting calculator app...")

try:
    # Create the context and viewport
    dpg.create_context()
    dpg.create_viewport(title="Styled Calculator", width=700, height=600)
    dpg.setup_dearpygui()

    # Register all needed values
    with dpg.value_registry():
        dpg.add_string_value(default_value="", tag="left_operand")
        dpg.add_string_value(default_value="", tag="right_operand")
        dpg.add_string_value(default_value="", tag="operator")
        dpg.add_string_value(default_value="", tag="result")

    # Try loading delete image
    delete_texture_loaded = False
    with dpg.texture_registry():
        try:
            data = dpg.load_image("delete_button.png")
            dpg.add_static_texture(width=100, height=100, default_value=data, tag="delete_button_texture")
            delete_texture_loaded = True
            print("✅ delete_button.png loaded successfully.")
        except Exception as e:
            print("⚠️ Failed to load delete_button.png:", e)

    # Button logic
    def update_number(sender, app_data, user_data):
        if dpg.get_value("operator") == "":
            dpg.set_value("left_operand", dpg.get_value("left_operand") + user_data)
        else:
            dpg.set_value("right_operand", dpg.get_value("right_operand") + user_data)

    def delete_number(sender, app_data, user_data):
        if dpg.get_value("right_operand") != "":
            dpg.set_value("right_operand", dpg.get_value("right_operand")[:-1])
        elif dpg.get_value("operator") != "":
            dpg.set_value("operator", "")
        elif dpg.get_value("left_operand") != "":
            dpg.set_value("left_operand", dpg.get_value("left_operand")[:-1])

    def update_operator(sender, app_data, user_data):
        dpg.set_value("operator", user_data)

    def perform_operation(sender, app_data):
        try:
            left = int(dpg.get_value("left_operand"))
            right = int(dpg.get_value("right_operand"))
            operator = dpg.get_value("operator")
            result = ""

            if operator == "+":
                result = str(left + right)
            elif operator == "-":
                result = str(left - right)
            elif operator == "/":
                result = str(left / right)
            elif operator == "x":
                result = str(left * right)
            elif operator == "%":
                result = str(left % right)

            dpg.set_value("result", result)
        except Exception as e:
            dpg.set_value("result", "Error")
            print("❌ Error performing calculation:", e)

    # Create the main window
    with dpg.window(label="Styled Calculator") as main_window:
        with dpg.group(horizontal=True):
            dpg.add_text(source="left_operand")
            dpg.add_text(source="operator")
            dpg.add_text(source="right_operand")
            dpg.add_text(label=" = ")
            dpg.add_text(source="result")

        # Number and operator buttons
        with dpg.group(horizontal=True):
            dpg.add_button(label="7", callback=update_number, user_data="7", width=100, height=100)
            dpg.add_button(label="8", callback=update_number, user_data="8", width=100, height=100)
            dpg.add_button(label="9", callback=update_number, user_data="9", width=100, height=100)
            if delete_texture_loaded:
                dpg.add_image_button(texture_tag="delete_button_texture", callback=delete_number, width=100, height=100)
            else:
                dpg.add_button(label="DEL", callback=delete_number, width=100, height=100)
            dpg.add_button(label="/", callback=update_operator, user_data="/", width=100, height=100)

        with dpg.group(horizontal=True):
            dpg.add_button(label="4", callback=update_number, user_data="4", width=100, height=100)
            dpg.add_button(label="5", callback=update_number, user_data="5", width=100, height=100)
            dpg.add_button(label="6", callback=update_number, user_data="6", width=100, height=100)
            dpg.add_button(label="x", callback=update_operator, user_data="x", width=100, height=100)

        with dpg.group(horizontal=True):
            dpg.add_button(label="1", callback=update_number, user_data="1", width=100, height=100)
            dpg.add_button(label="2", callback=update_number, user_data="2", width=100, height=100)
            dpg.add_button(label="3", callback=update_number, user_data="3", width=100, height=100)
            dpg.add_button(label="%", callback=update_operator, user_data="%", width=100, height=100)
            dpg.add_button(label="-", callback=update_operator, user_data="-", width=100, height=100)

        with dpg.group(horizontal=True):
            dpg.add_button(label="0", callback=update_number, user_data="0", width=100, height=100)
            dpg.add_button(label="=", callback=perform_operation, width=100, height=100)
            dpg.add_button(label="+", callback=update_operator, user_data="+", width=100, height=200)

    # Global theme (styled buttons)
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 50, category=dpg.mvThemeCat_Core)

    dpg.bind_item_theme(main_window, global_theme)

    # Launch app
    dpg.show_viewport()
    print("✅ GUI launched.")
    dpg.start_dearpygui()
    print("✅ App exited cleanly.")
    dpg.destroy_context()

except Exception as e:
    print("❌ Uncaught error:")
    traceback.print_exc()

input("\nPress Enter to exit...")
