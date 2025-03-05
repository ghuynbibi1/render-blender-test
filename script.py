import bpy

# Set samples to 8 for both viewport and final render
bpy.context.scene.cycles.samples = 8  # Final render
bpy.context.scene.cycles.preview_samples = 8  # Viewport render (optional)

# Enable AI Denoising (OptiX for NVIDIA GPUs)
bpy.context.scene.cycles.use_denoising = True
bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'  # Options: 'OPTIX', 'OPENIMAGEDENOISE', 'N

# Print current render engine
print("Render Engine:", bpy.context.scene.render.engine)

# Print GPU settings
prefs = bpy.context.preferences.addons['cycles'].preferences
print("Compute Device Type:", prefs.compute_device_type)

# Print available devices
print("Available Devices:")
for device in prefs.devices:
    print(f"- {device.name} ({device.type}) - Enabled: {device.use}")
