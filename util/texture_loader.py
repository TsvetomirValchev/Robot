import OpenGL.GL as GL
from PIL import Image

def load_texture(filename):
    image = Image.open(filename)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image_data = image.convert("RGBA").tobytes()

    texture_id = GL.glGenTextures(1)
    GL.glBindTexture(GL.GL_TEXTURE_2D, texture_id)

    GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA,
                    image.width, image.height, 0,
                    GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, image_data)

    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
    GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)

    return texture_id

def draw_textured_cube(scale_x=1.0, scale_y=1.0, scale_z=1.0, texture_id=None):
    if texture_id:
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, texture_id)

    GL.glPushMatrix()
    GL.glScalef(scale_x, scale_y, scale_z)
    GL.glBegin(GL.GL_QUADS)

    # Front face
    GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f(-0.5, -0.5,  0.5)
    GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f( 0.5, -0.5,  0.5)
    GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f( 0.5,  0.5,  0.5)
    GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f(-0.5,  0.5,  0.5)

    # Back face
    GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f(-0.5, -0.5, -0.5)
    GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f( 0.5, -0.5, -0.5)
    GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f( 0.5,  0.5, -0.5)
    GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f(-0.5,  0.5, -0.5)

    # Left face
    GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f(-0.5, -0.5, -0.5)
    GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f(-0.5, -0.5,  0.5)
    GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f(-0.5,  0.5,  0.5)
    GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f(-0.5,  0.5, -0.5)

    # Right face
    GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f( 0.5, -0.5, -0.5)
    GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f( 0.5, -0.5,  0.5)
    GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f( 0.5,  0.5,  0.5)
    GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f( 0.5,  0.5, -0.5)

    # Top face
    GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f(-0.5,  0.5,  0.5)
    GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f( 0.5,  0.5,  0.5)
    GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f( 0.5,  0.5, -0.5)
    GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f(-0.5,  0.5, -0.5)

    # Bottom face
    GL.glTexCoord2f(0.0, 0.0); GL.glVertex3f(-0.5, -0.5,  0.5)
    GL.glTexCoord2f(1.0, 0.0); GL.glVertex3f( 0.5, -0.5,  0.5)
    GL.glTexCoord2f(1.0, 1.0); GL.glVertex3f( 0.5, -0.5, -0.5)
    GL.glTexCoord2f(0.0, 1.0); GL.glVertex3f(-0.5, -0.5, -0.5)

    GL.glEnd()
    GL.glPopMatrix()

    if texture_id:
        GL.glDisable(GL.GL_TEXTURE_2D)
