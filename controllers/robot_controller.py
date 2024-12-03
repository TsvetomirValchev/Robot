import glfw

class RobotController:
    def __init__(self, robot):
        self.robot = robot
        self.keys_pressed = set()
        self.is_walking = False

    def press_key(self, key):
        self.keys_pressed.add(key)
        if key in (glfw.KEY_W, glfw.KEY_S):
            self.is_walking = True

    def release_key(self, key):
        self.keys_pressed.discard(key)
        if key in (glfw.KEY_W, glfw.KEY_S) and not (glfw.KEY_W in self.keys_pressed or glfw.KEY_S in self.keys_pressed):
            self.is_walking = False

    def update_robot_position(self, step=0.1):
        if glfw.KEY_W in self.keys_pressed:
            self.robot.position[2] += step
        if glfw.KEY_S in self.keys_pressed:
            self.robot.position[2] -= step
        if glfw.KEY_A in self.keys_pressed:
            self.robot.position[0] -= step
        if glfw.KEY_D in self.keys_pressed:
            self.robot.position[0] += step

    def update(self, step=0.1, swing_speed=1):
        self.update_robot_position(step)
        if self.is_walking:
            self.robot.update_animation(swing_speed)
