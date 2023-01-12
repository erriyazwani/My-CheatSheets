#movie was showing error  Need ffmpeg exe. You can download it by calling:
#fix
pip install imageio
import imageio
imageio.plugins.ffmpeg.download()
