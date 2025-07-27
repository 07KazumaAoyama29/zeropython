from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding = "utf-8")
    except:
        print(f"ごめんなさい、 {path} は見当たりません。")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"ファイル {path} には約 {num_words} の単語が含まれています。")

if __name__ == "__main__":
    filenames = ["alice.txt", "guests.txt", "hun.txt"]
    for filename in filenames:
        path = Path(filename)
        count_words(path)