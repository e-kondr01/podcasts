import pydub

from pathlib import Path


def slice_audio(filename, start_seconds, finish_seconds):
    base_dir = Path(__file__).resolve().parent

    audio = pydub.AudioSegment.from_mp3(base_dir/filename)
    start = start_seconds * 1000
    finish = finish_seconds * 1000

    sliced_audio = audio[start: finish]

    sliced_audio.export(f"{filename}_edited.mp3", format="mp3")

    return sliced_audio


slice_audio("mozart.mp3", 0, 5)
