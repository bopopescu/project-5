package particlesystem;

import com.sun.opengl.util.texture.Texture;

public class ParticleSystemSettings {
	
	
	public int capacity;
	public float emitRate; //particles emission per millisecond.
	
	//defines the general external force e.g. gravity
	//the array should contain at least three entries (x,y,z)
	public float[] general_external_force;
	
	public float lifetime; //in nano seconds
	
	public ParticleEmitterSettings emitter_settings = null;
	public ParticleEmitter emitter = null;
		
	

}
