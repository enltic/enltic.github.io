import os
import json

def extract_info_from_filename(filename):
    # 假设文件名格式为 "{Artist} - {Title}.flac"
    artist, title = filename.rsplit('-', 1)
    title = title.rsplit('.mp3', 1)[0]
    return artist, title

def build_json_entry(artist, song_name):
    # 构建JSON条目
    json_path = f"https://storage.enltc.pages.dev/music/{artist}-{song_name}.mp3"
    cover_path = f"/music/{artist} - {song_name}.png"
    lrc_path = f"https://storage.enltc.pages.dev/lrc/{artist}-{song_name}.lrc"
    return {
        "name": song_name,
        "artist": artist,
        "url": json_path,
        "cover": cover_path,
        "lrc": lrc_path
    }

def scan_music_folder(folder_path):
    music_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3'):
            artist, song_name = extract_info_from_filename(filename)
            music_list.append(build_json_entry(artist, song_name))
    return music_list

def save_as_json(music_list, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(music_list, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    folder_path = 'music'  # 将这里替换为你的音乐文件夹路径
    json_file_path = 'musiclist.json'  # 将这里替换为你希望保存的JSON文件路径
    music_list = scan_music_folder(folder_path)
    save_as_json(music_list, json_file_path)
