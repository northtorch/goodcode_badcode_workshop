from __future__ import annotations
import os
from text_summarizer import TextSummarizer


IMPORTANT_NOUNS = [ '猫', '人間', ]
IMPORTANT_VERBS = [ '鳴く', '泣く', ]
IMPORTANT_ADJECTIVES = [ '黒い', 'じめじめした', ]
IMPORTANCE_THRESHOLD = 0.025

TARGET_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "cat.txt")

def main():
    # ファイルから対象の文章を読み込む
    with open(TARGET_FILE, "r") as f:
        target_text = f.read()
    # TextSummarizerを使って要約を作成する
    ts = TextSummarizer(importantNouns=IMPORTANT_NOUNS, importantVerbs=IMPORTANT_VERBS, importantAdjectives=IMPORTANT_ADJECTIVES, importanceThreshold=IMPORTANCE_THRESHOLD)
    # 結果を表示する
    print("========== TEXT ==========")
    print(target_text)
    print("---------- SUMMARY ----------")
    print(ts.summarizeText(target_text))


if __name__ == '__main__':
    """ファイル名指定で実行されたとき、main関数を実行する"""
    main()
