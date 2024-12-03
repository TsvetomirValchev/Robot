import OpenGL.GL as GL
import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
from util.texture_loader import load_texture, draw_textured_cube

class Robot:
    def __init__(self, texture_filename):
        self.texture_filename = texture_filename
        self.texture_id = load_texture(texture_filename)
        self.position = [0.0, 0.0, 0.0]
        self.swing_angle = 0
        self.swing_direction = 1

    def draw(self):
        GL.glPushMatrix()
        GL.glTranslatef(self.position[0], self.position[1], self.position[2])

        self.draw_head()
        self.draw_neck()
        self.draw_body()
        self.draw_arms()
        self.draw_legs()

        GL.glPopMatrix()

    def draw_body(self):
        GL.glPushMatrix()
        GL.glTranslatef(0.0, 0.75, 0.0)
        draw_textured_cube(scale_x=1.0, scale_y=1.5, scale_z=0.5, texture_id=self.texture_id)
        GL.glPopMatrix()

    def draw_neck(self):
        texture_id = self.texture_id

        GL.glPushMatrix()
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glColor3f(1.0, 1.0, 1.0)
        GL.glTranslatef(0.0, 1.5, 0.0)
        draw_textured_cube(scale_x=0.2, scale_y=0.5, scale_z=0.2, texture_id=texture_id)
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glPopMatrix()


    def draw_head(self):
        GL.glPushMatrix()
        GL.glTranslatef(0.0, 1.9, 0.0)
        
        draw_textured_cube(scale_x=0.5, scale_y=0.5, scale_z=0.5, texture_id=self.texture_id)
        
        GL.glPushMatrix()
        GL.glTranslatef(0.0, 0.0, 0.26)
        self.draw_face()
        GL.glPopMatrix()
        
        GL.glPopMatrix()

    def draw_face(self):
        GL.glBegin(GL.GL_QUADS)
        
        GL.glColor3f(0.0, 0.0, 0.0)
        GL.glVertex3f(-0.1, 0.05, 0.0)
        GL.glVertex3f(-0.05, 0.05, 0.0)
        GL.glVertex3f(-0.05, 0.1, 0.0)
        GL.glVertex3f(-0.1, 0.1, 0.0)

        GL.glVertex3f(0.05, 0.05, 0.0)
        GL.glVertex3f(0.1, 0.05, 0.0)
        GL.glVertex3f(0.1, 0.1, 0.0)
        GL.glVertex3f(0.05, 0.1, 0.0)

        GL.glColor3f(1.0, 0.0, 0.0)
        GL.glVertex3f(-0.1, -0.05, 0.0)
        GL.glVertex3f(0.1, -0.05, 0.0)
        GL.glVertex3f(0.1, -0.02, 0.0)
        GL.glVertex3f(-0.1, -0.02, 0.0)

        GL.glEnd()

        GL.glColor3f(1.0, 1.0, 1.0)

    def draw_arms(self):
        texture_id = self.texture_id

        GL.glPushMatrix()
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glColor3f(0.0, 0.0, 1.0)
        GL.glTranslatef(-0.6, 1.35, 0.0)
        GLU.gluQuadricTexture(GLU.gluNewQuadric(), GL.GL_TRUE)
        GLUT.glutSolidSphere(0.15, 20, 20)
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glPopMatrix()

        GL.glPushMatrix()
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glColor3f(1.0, 1.0, 1.0)
        GL.glTranslatef(-0.6, 0.85, 0.0)
        GL.glRotatef(self.swing_angle, 1.0, 0.0, 0.0)
        draw_textured_cube(scale_x=0.25, scale_y=1.0, scale_z=0.25, texture_id=texture_id)
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glPopMatrix()

        GL.glPushMatrix()
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glColor3f(0.0, 0.0, 1.0)
        GL.glTranslatef(0.6, 1.35, 0.0)
        GLU.gluQuadricTexture(GLU.gluNewQuadric(), GL.GL_TRUE)
        GLUT.glutSolidSphere(0.15, 20, 20)
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glPopMatrix()

        GL.glPushMatrix()
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glColor3f(1.0, 1.0, 1.0)
        GL.glTranslatef(0.6, 0.85, 0.0)
        GL.glRotatef(-self.swing_angle, 1.0, 0.0, 0.0)
        draw_textured_cube(scale_x=0.25, scale_y=1.0, scale_z=0.25, texture_id=texture_id)
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glPopMatrix()



    def draw_legs(self):
        GL.glPushMatrix()
        GL.glTranslatef(-0.3, -0.25, 0.0)
        draw_textured_cube(scale_x=0.3, scale_y=1.0, scale_z=0.3, texture_id=self.texture_id)
        GL.glPopMatrix()

        GL.glPushMatrix()
        GL.glTranslatef(0.3, -0.25, 0.0)
        draw_textured_cube(scale_x=0.3, scale_y=1.0, scale_z=0.3, texture_id=self.texture_id)
        GL.glPopMatrix()
        
    def update_animation(self, swing_speed):
        self.swing_angle += self.swing_direction * swing_speed
        if self.swing_angle > 15:
            self.swing_direction = -1
        elif self.swing_angle < -15:
            self.swing_direction = 1
