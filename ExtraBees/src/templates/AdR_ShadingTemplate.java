package templates;


/**
 * @author Andreas Elsner / Stephan Arens / Gitta Domik
 * 
 * AdR Shading Template
 * Department of Computer Science at the University of Paderborn, Germany
 * Research Group of Prof. Gitta Domik - Computer Graphics, Visualization and Digital Image Processing
 */


import java.awt.event.KeyEvent;
import java.io.File;
import java.io.IOException;

import javax.media.opengl.GL;
import javax.media.opengl.GLAutoDrawable;
import javax.media.opengl.GLException;

import modelloader.MeshLoader;

import com.sun.opengl.cg.CGcontext;
import com.sun.opengl.cg.CGparameter;
import com.sun.opengl.cg.CGprogram;
import com.sun.opengl.cg.CgGL;
import com.sun.opengl.util.texture.Texture;
import com.sun.opengl.util.texture.TextureIO;

public class AdR_ShadingTemplate extends JoglTemplate
{
	private static final long serialVersionUID = 1L;

	// TODO: Assignment 3_3: create your own toon shader and load it here
	protected static final String FRAGMENT_SHADER = "shader/fp_phongPerPixel.cg";

	protected static final String VERTEX_SHADER = "shader/vp_phongPerPixel.cg";

	static final float[] BRASS_MATERIAL = { 0.33f, 0.22f, 0.03f, 1.0f, 0.78f,
			0.57f, 0.11f, 1.0f, 0.99f, 0.91f, 0.81f, 1.0f, 5.0f };

	static final float[] REDPLASTIC_MATERIAL = { 0.3f, 0.0f, 0.0f, 1.0f, 0.6f,
			0.0f, 0.0f, 1.0f, 0.8f, 0.4f, 0.4f, 1.0f, 10.0f };

	static final float[] WHITESHINEY_MATERIAL = { 1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
			1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 100.0f };

	static final float[][] MATERIALS = { BRASS_MATERIAL, REDPLASTIC_MATERIAL,
			WHITESHINEY_MATERIAL };

	static final float[] MOVING_LIGHT_ADS = { 0.2f, 0.2f, 0.2f, 1f, 0.95f, 0.95f,
			0.95f, 1f, 0.95f, 0.95f, 0.95f, 1f };

	private CGcontext cgContext;

	private CGprogram cgVertexProg = null, cgFragmentProg = null;

	private CGparameter cgBlackHolePosition, cgTime, cgStretchFactor;

	private int cgVertexProfile, cgFragProfile;

	protected int dList;

	private int frameCounter = 0;

	private int currentMaterial = 0;

	private boolean stretch = false, animation = true;

	private Texture crate = null;
	public static void main(String[] args)
	{
		AdR_ShadingTemplate assignment = new AdR_ShadingTemplate();
		assignment.setVisible(true);
	}

	public void init(GLAutoDrawable drawable)
	{
		super.init(drawable);
		GL gl = drawable.getGL();
		// init Cg
		initCg();
		// load and compile shader
		cgVertexProg = loadShader(getCgVertexProfile(), VERTEX_SHADER);
		cgFragmentProg = loadShader(getCgFragProfile(), FRAGMENT_SHADER);
		// bind CGParameters to vertex and fragment program
		bindParameters();
		// z-buffer test
		gl.glEnable(GL.GL_DEPTH_TEST);
		// backface culling
		gl.glEnable(GL.GL_CULL_FACE);
		// load mesh
		dList = MeshLoader.loadObj(gl, "models/bunny.obj", 0.5f);
		try {
			crate = TextureIO.newTexture(new File("textures/crate.png"), false);
		} catch (GLException e1) {e1.printStackTrace();
		} catch (IOException e1) {e1.printStackTrace();}
		
	}

	public void initCg()
	{
		cgContext = CgGL.cgCreateContext();
		cgVertexProfile = CgGL.cgGLGetLatestProfile(CgGL.CG_GL_VERTEX);
		if (cgVertexProfile == CgGL.CG_PROFILE_UNKNOWN)
		{
			System.err.println("Invalid vertex profile");
			System.exit(1);
		}
		CgGL.cgGLSetOptimalOptions(cgVertexProfile);

		cgFragProfile = CgGL.cgGLGetLatestProfile(CgGL.CG_GL_FRAGMENT);
		if (cgFragProfile == CgGL.CG_PROFILE_UNKNOWN)
		{
			System.err.println("Invalid fragment profile");
			System.exit(1);
		}
		CgGL.cgGLSetOptimalOptions(cgFragProfile);
	}

	public CGprogram loadShader(int profile, String filename)
	{
		CGprogram shaderprog = CgGL.cgCreateProgramFromFile(getCgContext(),
				CgGL.CG_SOURCE, filename, profile, null, null);
		if (shaderprog == null)
		{
			int err = CgGL.cgGetError();
			System.err.println("Compile shader [" + filename + "] "
					+ CgGL.cgGetErrorString(err));
			if (CgGL.cgGetLastListing(getCgContext()) != null)
			{
				System.err.println(CgGL.cgGetLastListing(getCgContext()) + "\n");
			}
			System.exit(1);
		}

		CgGL.cgGLLoadProgram(shaderprog);

		int err = CgGL.cgGetError();
		if (err != CgGL.CG_NO_ERROR)
		{
			System.out.println("Load shader [" + filename + "]: "
					+ CgGL.cgGetErrorString(err));
			System.exit(1);
		}

		return shaderprog;
	}

	protected void bindParameters()
	{
		cgBlackHolePosition = CgGL.cgGetNamedParameter(cgFragmentProg, "blackHolePosition");
		cgTime = CgGL.cgGetNamedParameter(cgFragmentProg, "time");
		// TODO: Assignment 3_1: bind stretch factor
		cgTime = CgGL.cgGetNamedParameter(cgVertexProg, "time");
		cgStretchFactor = CgGL.cgGetNamedParameter(cgVertexProg, "stretchFactor");
	}

	public void display(GLAutoDrawable drawable)
	{
		// if animation is on, increase frame counter
		if (animation)
			incFrameCounter();
		// get the gl object
		GL gl = drawable.getGL();
		// set the erasing color (black)
		gl.glClearColor(0.5f, 0.5f, 0.5f, 1.0f);
		// clear screen with the defined erasing color and depth buffer
		gl.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
		gl.glPushMatrix();
		applyMouseTranslation(gl);
		applyMouseRotation(gl);

		// set material for cg
		float[] material = MATERIALS[currentMaterial];
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, material, 0);
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, material, 4);
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, material, 8);
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, material, 12);

		// blackHole for cg
		float[] blackHolePosition = new float[] { -5f, 5f, 0f, 1f };
		CgGL.cgGLSetParameter3fv(cgBlackHolePosition, blackHolePosition, 0);
		CgGL.cgGLSetParameter1f(cgTime, getFrameCounter());

		// set light properties
		gl.glLightfv(GL.GL_LIGHT0, GL.GL_AMBIENT, MOVING_LIGHT_ADS, 0);
		gl.glLightfv(GL.GL_LIGHT0, GL.GL_DIFFUSE, MOVING_LIGHT_ADS, 4);
		gl.glLightfv(GL.GL_LIGHT0, GL.GL_SPECULAR, MOVING_LIGHT_ADS, 8);
		
		// set light properties
		gl.glLightfv(GL.GL_LIGHT1, GL.GL_AMBIENT, MOVING_LIGHT_ADS, 0);
		gl.glLightfv(GL.GL_LIGHT1, GL.GL_DIFFUSE, MOVING_LIGHT_ADS, 4);
		gl.glLightfv(GL.GL_LIGHT1, GL.GL_SPECULAR, MOVING_LIGHT_ADS, 8);

		// calculate light position
		float dLightHeight = 5.0f;
		double dLightRadius = 5.0d;
		float[] lightPos = new float[] {
				(float) (dLightRadius * Math.cos(getFrameCounter() * 3.14 / 200.0)),
				(float) (dLightRadius * Math.sin(getFrameCounter() * 3.14 / 200.0)),
				dLightHeight, 1.0f };
		float[] lightPos_Cam = new float[] {0f,5f,-5f,1f	};
		gl.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, lightPos, 0);
		gl.glLightfv(GL.GL_LIGHT1, GL.GL_POSITION, lightPos_Cam, 0);

		// draw light as sphere (without shader)
		gl.glPushMatrix();
		gl.glTranslatef(lightPos[0], lightPos[1], lightPos[2]);
		gl.glColor3f(1f, 1f, 1f);
		getGlu().gluSphere(getGlu().gluNewQuadric(), 0.3, 10, 10);
		gl.glPopMatrix();
		
		// draw light as sphere (without shader)
		gl.glPushMatrix();
		gl.glTranslatef(lightPos_Cam[0], lightPos_Cam[1], lightPos_Cam[2]);
		gl.glColor3f(1f, 1f, 1f);
		getGlu().gluSphere(getGlu().gluNewQuadric(), 0.3, 10, 10);
		gl.glPopMatrix();

		// move vertices along normals (see vertex program)
		float stretchFactor = 0;
		if (stretch)
		{
			// TODO: Assignment 3_1: use Math.sin and getFrameCounter here to
			// calculate stretchFactor
			stretchFactor = (float) ((getFrameCounter()));
			System.out.println(stretchFactor);
		}
		// TODO: Assignment 3_1: set cgStretch parameter

		CgGL.cgGLSetParameter2f(cgStretchFactor, stretchFactor, 0f);
		// enable profiles, bind shaders
		crate.bind();
		CgGL.cgGLEnableProfile(getCgVertexProfile());
		CgGL.cgGLBindProgram(cgVertexProg);
		CgGL.cgGLEnableProfile(getCgFragProfile());
		CgGL.cgGLBindProgram(cgFragmentProg);
		// draw mesh
		gl.glCallList(dList);
		// disable profiles, unload shaders
		CgGL.cgGLDisableProfile(getCgVertexProfile());
		CgGL.cgGLDisableProfile(getCgFragProfile());

		// TODO: Assignment 3_3: draw comic outlines here

		gl.glPopMatrix();
	}

	/**
	 * This method increases the frame counter
	 * 
	 * @see getFrameCounter()
	 */
	private void incFrameCounter()
	{
		if (frameCounter < Integer.MAX_VALUE)
		{
			frameCounter++;
		}
		else
			frameCounter = 0;
	}

	@Override
	public void keyPressed(KeyEvent e)
	{
		super.keyPressed(e);
		if (e.getKeyCode() == KeyEvent.VK_M)
		{
			currentMaterial = currentMaterial < MATERIALS.length - 1 ? currentMaterial + 1
					: 0;
			System.out.println("Material: " + currentMaterial);
		}
		else if (e.getKeyCode() == KeyEvent.VK_S)
		{
			stretch = !stretch;
			System.out.println("Stretch: " + stretch);
		}
		else if (e.getKeyCode() == KeyEvent.VK_SPACE)
		{
			animation = !animation;
			System.out.println("Animation: " + animation);
		}
	}

	public int getCgVertexProfile()
	{
		return cgVertexProfile;
	}

	public int getCgFragProfile()
	{
		return cgFragProfile;
	}

	public CGprogram getCgVertexProg()
	{
		return cgVertexProg;
	}

	public void setCgVertexProg(CGprogram cgVertexProg)
	{
		this.cgVertexProg = cgVertexProg;
	}

	public CGprogram getCgFragmentProg()
	{
		return cgFragmentProg;
	}

	public void setCgFragmentProg(CGprogram cgFragmentProg)
	{
		this.cgFragmentProg = cgFragmentProg;
	}

	public CGcontext getCgContext()
	{
		return cgContext;
	}

	public int getFrameCounter()
	{
		return frameCounter;
	}
}