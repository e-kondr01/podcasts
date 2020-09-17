import pydub

from pathlib import Path


def slice_audio(filename, start_seconds, finish_seconds):
    '''starts_seconds:finish_seconds is the part to delete '''
    base_dir = Path(__file__).resolve().parent

    audio = pydub.AudioSegment.from_mp3(base_dir/filename)
    start = start_seconds * 1000
    finish = finish_seconds * 1000

    audio1 = audio[0: start]
    audio2 = audio[finish:]
    res = audio1 + audio2

    res.export(f"{filename}_sliced.mp3", format="mp3")

    return res


def add_fade(filename, fade_in_seconds=2, fade_out_seconds=3):
    base_dir = Path(__file__).resolve().parent

    audio = pydub.AudioSegment.from_mp3(base_dir/filename)

    fade_in = fade_in_seconds * 1000
    fade_out = fade_out_seconds * 1000

    faded_audio = audio.fade_in(fade_in).fade_out(fade_out)
    faded_audio.export(f"{filename}_faded.mp3", format="mp3")
    return faded_audio


def combine_audio(original_filename, filename_to_add):
    base_dir = Path(__file__).resolve().parent
    sound1 = pydub.AudioSegment.from_file(base_dir/original_filename)
    sound2 = pydub.AudioSegment.from_file(base_dir/filename_to_add) - 20

    combined = sound1.overlay(sound2)

    combined.export(f"{original_filename}_combined.mp3", format='mp3')

    return combined


#slice_audio("mozart.mp3", 3, 6)
#add_fade('mozart.mp3', 10, 10)
#combine_audio('mozart.mp3', 'dub.mp3')
