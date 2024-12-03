import glfw

class CameraController:
    def __init__(self, camera, zoom_speed=0.5):
        self.camera = camera
        self.keys_pressed = set()
        self.mouse_pressed = False
        self.last_mouse_pos = None
        self.message = ""
        self.zoom_speed = zoom_speed


    def press_key(self, key):
        self.keys_pressed.add(key)

    def release_key(self, key):
        self.keys_pressed.discard(key)

    def update(self): 
        if glfw.KEY_R in self.keys_pressed:
            self.camera.position = [0.0, 1.0, 3.0]
            self.camera.angle_x = 0.0
            self.camera.angle_y = 0.0
            self.camera.distance = 5.0
    
    def mouse_button_callback(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT:
            if action == glfw.PRESS:
                self.mouse_pressed = True
                self.message = "Mouse Button Pressed: Rotation Enabled"
            elif action == glfw.RELEASE:
                self.mouse_pressed = False
                self.message = "Mouse Button Released"

    def mouse_drag_callback(self, window, xpos, ypos):
        if self.last_mouse_pos is None:
            self.last_mouse_pos = (xpos, ypos)
            return

        if not self.mouse_pressed:
            return

        dx = xpos - self.last_mouse_pos[0]
        dy = ypos - self.last_mouse_pos[1]
        self.last_mouse_pos = (xpos, ypos)

        sensitivity = 0.5
        self.camera.angle_x += dx * sensitivity
        self.camera.angle_y -= dy * sensitivity
        self.camera.angle_y = max(-89.0, min(89.0, self.camera.angle_y))

    def scroll_callback(self, window, xoffset, yoffset):
        self.camera.distance -= yoffset * self.zoom_speed
        self.camera.distance = max(1.0, self.camera.distance)
