from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def create_lyric_video(video_path, lyrics_path, output_path):
    with open(lyrics_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    video = VideoFileClip(video_path)
    clips = []
    duration_per_line = video.duration / len(lines)

    for i, line in enumerate(lines):
        txt = TextClip(line, fontsize=48, color='white', bg_color='black', font='Arial')
        txt = txt.set_position(('center', 'bottom')).set_duration(duration_per_line).set_start(i * duration_per_line)
        clips.append(txt)

    final = CompositeVideoClip([video] + clips)
    final.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    create_lyric_video("digital salvation erye.mov", "lyrics.txt", "output_video.mp4")
