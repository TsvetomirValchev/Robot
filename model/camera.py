import math
import OpenGL.GLU as GLU

class Camera:
    def __init__(self):
        self.position = [0.0, 1.0, 3.0]
        self.angle_x = 0.0
        self.angle_y = 0.0
        self.distance = 5.0
        self.up = [0.0, 1.0, 0.0]
    
    def update_position(self, dx, dy, dz):
        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz
    
    def rotate(self, d_angle_x, d_angle_y):
        self.angle_x += d_angle_x
        self.angle_y += d_angle_y
        self.angle_y = max(-89.0, min(89.0, self.angle_y))  # Prevent camera flipping

    def apply(self):
        cam_x = self.distance * math.sin(math.radians(self.angle_x)) * math.cos(math.radians(self.angle_y))
        cam_y = self.distance * math.sin(math.radians(self.angle_y))
        cam_z = self.distance * math.cos(math.radians(self.angle_x)) * math.cos(math.radians(self.angle_y))

        GLU.gluLookAt(cam_x, cam_y, cam_z, 0.0, 0.75, 0.0, 0.0, 1.0, 0.0)