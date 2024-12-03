import glfw
import OpenGL.GL as GL
import OpenGL.GLU as GLU
from model.camera import Camera
from controllers.camera_controller import CameraController
from model.robot import Robot
from controllers.robot_controller import RobotController
from util.utils import draw_text


robot_controller = None

def init_glfw():
    if not glfw.init():
        raise Exception("GLFW initialization failed")
    window = glfw.create_window(800, 600, "Robot with Texture", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window creation failed")
    glfw.make_context_current(window)
    return window

def setup_projection():
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GLU.gluPerspective(45.0, 800 / 600, 0.1, 100.0)
    GL.glMatrixMode(GL.GL_MODELVIEW)

def initialize_opengl():
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glClearColor(0.1, 0.1, 0.1, 1.0)

def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        robot_controller.press_key(key)
        camera_controller.press_key(key)
    elif action == glfw.RELEASE:
        robot_controller.release_key(key)
        camera_controller.release_key(key)

def main():
    global robot_controller
    global camera_controller
    window = init_glfw()
    initialize_opengl()
    
    camera = Camera()
    camera_controller = CameraController(camera)
    robot = Robot("robot_texture.jpg")
    robot_controller = RobotController(robot)
    
    glfw.set_scroll_callback(window, camera_controller.scroll_callback)
    glfw.set_key_callback(window, key_callback)
    glfw.set_mouse_button_callback(window, camera_controller.mouse_button_callback)
    glfw.set_cursor_pos_callback(window, camera_controller.mouse_drag_callback)
    setup_projection()
    
    while not glfw.window_should_close(window):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()

        camera.apply()
        robot_controller.update(step=0.01, swing_speed=1.5)
        camera_controller.update()
        robot.draw()
        draw_text(camera_controller.message, -0.9, -0.9)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
