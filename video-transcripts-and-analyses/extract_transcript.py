import os
from youtube_transcript_api import YouTubeTranscriptApi

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transcript_raw.txt")

api = YouTubeTranscriptApi()
res = api.fetch('GilHlBAQxyY')

with open(output_path, "w", encoding="utf-8") as f:
    for item in res:
        m, s = divmod(int(item.start), 60)
        f.write(f"[{m:02d}:{s:02d}] {item.text}\n")

print(f"Successfully wrote {len(res)} items to {output_path}")
