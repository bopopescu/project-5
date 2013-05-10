package scenegraph;

import java.util.ArrayList;

import javax.media.opengl.GL;
import javax.media.opengl.GLAutoDrawable;

import modelloader.OBJLoader;

import com.sun.opengl.cg.CGcontext;
import com.sun.opengl.cg.CGprogram;
import com.sun.opengl.cg.CgGL;

public abstract class SceneGraphNode {
	
	// path to file
	private String modelPath = "";
	
	// list with all the children of this node object
	protected ArrayList<SceneGraphNode> children;
	
	// objectList returned by the OBJLoader 
	private int objectList;
	
	protected String fpShaderPath = "";

	protected String vpShaderPath = "";
	
	private CGcontext cgContext;

	protected CGprogram cgVertexProg = null;

	protected CGprogram cgFragmentProg = null;

	private int cgVertexProfile, cgFragProfile;

	protected float[] translation = new float[3],
						rotation = new float[3], 
						scale = new float[3],
						pivot = new float[3];
	
	// constructor
	public SceneGraphNode(GLAutoDrawable drawable, String modelPath, float scale, String vpShaderPath, String fpShaderPath){
		this.children = new ArrayList<SceneGraphNode>();
		this.modelPath = modelPath;
		this.fpShaderPath = fpShaderPath;
		this.vpShaderPath = vpShaderPath;
		objectList = new OBJLoader(modelPath,scale,drawable.getGL()).getDisplayList();
		init(drawable);
		initCg();
	}
	
	public SceneGraphNode(GLAutoDrawable drawable, String modelPath, float scale){
		this.children = new ArrayList<SceneGraphNode>();
		this.modelPath = modelPath;
		objectList = new OBJLoader(modelPath,scale,drawable.getGL()).getDisplayList();
		init(drawable);
	}
	
	// constructor
	public SceneGraphNode(GLAutoDrawable drawable){
		this.children = new ArrayList<SceneGraphNode>();
	}
	
	public abstract void init(GLAutoDrawable drawable);
	public abstract void bindParameters();
	public abstract void animate(GLAutoDrawable drawable);
	
	
	/**
	 * Add a child to this node.
	 * 
	 * @param child
	 */
	public void addChild(SceneGraphNode child){
		this.children.add(child);
	}
	
	/**
	 * remove child from this parent with referred path.
	 * @param path
	 */
	public void removeChild(String path){
		for(SceneGraphNode n : this.children){
			if(path.equals(n.getPath()))
				this.children.remove(n);
		}
	}
	
	/**
	 * get child from this parent with referred path.
	 * @param path
	 */
	public SceneGraphNode getChild(String path){
		for(SceneGraphNode n : this.children){
			if(path.equals(n.getPath()))
				return n;
		}
		return null;
	}	
	
	/**
	 * Method for rendering an model and its children. 
	 * 
	 * @param gl
	 */
	public void render(GLAutoDrawable drawable){
		GL gl = drawable.getGL();
		gl.glPushMatrix(); // save matrix
		animate(drawable); // call virtual animate method to animate current node
		gl.glTranslatef(translation[0], translation[1], translation[2]);
		gl.glRotatef(rotation[0], 1, 0, 0);
		gl.glRotatef(rotation[1], 0, 1, 0);
		gl.glRotatef(rotation[2], 0, 0, 1);
		this.draw(drawable);// draw the current object
		for(SceneGraphNode child : children){ // render every child
			child.render(drawable);
		}

		gl.glPopMatrix(); // restore matrix
	}
	
	public abstract void draw(GLAutoDrawable drawable);
	
	public void initCg()
	{
		cgVertexProg = loadShader(getCgVertexProfile(), vpShaderPath);
		cgFragmentProg = loadShader(getCgFragProfile(), fpShaderPath);
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

	protected CGprogram loadShader(int profile, String filename)
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
	
	public void setMaterial(GL gl, float[] material) {
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_AMBIENT, material, 0);
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_DIFFUSE, material, 4);
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_SPECULAR, material, 8);
		gl.glMaterialfv(GL.GL_FRONT, GL.GL_SHININESS, material, 12);
	}

	
				//////////////////////	
				// getter and setter//
				//////////////////////
	
	public int getObjectList(){
		return this.objectList;
	}
	
	public String getPath() {
		return modelPath;
	}
	
	public void setTranslation(float[] trans){
		this.translation = trans;
	}
	
	public void setTranslation(float x, float y, float z){
		this.translation[0] = x;
		this.translation[1] = y;
		this.translation[2] = z;
	}
	
	public float[] getTranslation() {
		return this.translation;
	}
	
	public void setRotation(float[] rot){
		this.rotation = rot;
	}
	public void setRotation(float x, float y, float z){
		this.rotation[0] = x;
		this.rotation[1] = y;
		this.rotation[2] = z;
	}
	
	public float[] getRotation() {
		return this.rotation;
	}
	
	public void setScale(float[] scale){
		this.scale = scale;
	}
	
	public void setScale(float x, float y, float z){
		this.scale[0] = x;
		this.scale[1] = y;
		this.scale[2] = z;
	}
	
	public void setPivot(float[] trans){
		this.pivot = trans;
	}
	
	public void setPivot(float x, float y, float z){
		this.pivot[0] = x;
		this.pivot[1] = y;
		this.pivot[2] = z;
	}
	
	public float[] getPivot(){
		return this.pivot;
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
}