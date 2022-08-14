x = ["video_clip", "intro_audio", "outro_audio", "content_audio_clips", "master_audio", "headlines", "headlines_csv", "todays_date"]

for item in x:
    print(f"\ndef get_{item}(self):\n\treturn self.{item}\n\ndef set_{item}(self, set):\n\tself.{item} = set")
