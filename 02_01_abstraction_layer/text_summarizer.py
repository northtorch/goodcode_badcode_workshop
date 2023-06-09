from __future__ import annotations

import MeCab

class TextSummarizer:
    def __init__(self, importantNouns: list[str], importantVerbs: list[str], importantAdjectives: list[str], importanceThreshold: float = 0.5):
        self.importantNouns = importantNouns
        self.importantVerbs = importantVerbs
        self.importantAdjectives = importantAdjectives
        self.importanceThreshold = importanceThreshold

    def summarizeText(self, text: str) -> str:
        # テキストを段落に分割する
        paragraphs = self._splitIntoParagraphs(text)
        # 段落ごとに重要度を計算する
        paragraphImportances = [self._calcurateImportance(paragraph) for paragraph in paragraphs]
        # 重要度が閾値を超える段落のみを抽出する
        importantParagraphs = [paragraph for paragraph, importance in zip(paragraphs, paragraphImportances) if importance > self.importanceThreshold]
        # 抽出した段落を結合して返す
        return "\n\n".join(importantParagraphs)


    def _calcurateImportance(self, paragraph: str) -> float:
        # 名詞・動詞・形容詞の重要度を計算する
        importanceNouns = self._calcImportanceNouns(paragraph)
        importanceVerbs = self._calcImportanceVerbs(paragraph)
        importanceAdjectives = self._calcImportanceAdjectives(paragraph)
        # 重要度の平均を計算する
        return (importanceNouns + importanceVerbs + importanceAdjectives) / 3


    def _calcImportanceNouns(self, paragraph: str) -> float:
        mecabTagger = MeCab.Tagger()
        noun_count = {}
        # 形態素解析した結果から名詞を抽出する
        node = mecabTagger.parseToNode(paragraph)
        while node:
            word = node.surface
            features = node.feature.split(",")
            if features[0] == "名詞":
                # 名詞の場合
                if word not in noun_count:
                    noun_count[word] = 0
                noun_count[word] += 1
            node = node.next
        # 重要な名詞とそれ以外の名詞の出現回数を計算する
        important_noun_count = sum([count for word, count in noun_count.items() if word in self.importantNouns])
        other_noun_count = sum([count for word, count in noun_count.items() if word not in self.importantNouns])
        # 名詞が存在しなかったら0を返す
        if important_noun_count + other_noun_count < 1:
            return 0
        # 重要な名詞の出現回数を、全名詞の出現回数で割って重要度を計算する
        return important_noun_count / (important_noun_count + other_noun_count)


    def _calcImportanceVerbs(self, paragraph: str) -> float:
        mecabTagger = MeCab.Tagger()
        verb_count = {}
        # 形態素解析した結果から動詞を抽出する
        node = mecabTagger.parseToNode(paragraph)
        while node:
            word = node.surface
            features = node.feature.split(",")
            if features[0] == "動詞":
                # 動詞の場合
                if word not in verb_count:
                    verb_count[word] = 0
                verb_count[word] += 1
            node = node.next
        # 重要な動詞とそれ以外の動詞の出現回数を計算する
        important_verb_count = sum([count for word, count in verb_count.items() if word in self.importantVerbs])
        other_verb_count = sum([count for word, count in verb_count.items() if word not in self.importantVerbs])
        # 動詞が存在しなかったら0を返す
        if important_verb_count + other_verb_count < 1:
            return 0
        # 重要な動詞の出現回数を、全動詞の出現回数で割って重要度を計算する
        return important_verb_count / (important_verb_count + other_verb_count)


    def _calcImportanceAdjectives(self, paragraph: str) -> float:
        mecabTagger = MeCab.Tagger()
        adjective_count = {}
        # 形態素解析した結果から形容詞を抽出する
        node = mecabTagger.parseToNode(paragraph)
        while node:
            word = node.surface
            features = node.feature.split(",")
            if features[0] == "形容詞":
                # 形容詞の場合
                if word not in adjective_count:
                    adjective_count[word] = 0
                adjective_count[word] += 1
            node = node.next
        # 重要な形容詞とそれ以外の形容詞の出現回数を計算する
        important_adjective_count = sum([count for word, count in adjective_count.items() if word in self.importantAdjectives])
        other_adjective_count = sum([count for word, count in adjective_count.items() if word not in self.importantAdjectives])
        # 形容詞が存在しなかったら0を返す
        if important_adjective_count + other_adjective_count < 1:
            return 0
        # 重要な形容詞の出現回数を、全形容詞の出現回数で割って重要度を計算する
        return important_adjective_count / (important_adjective_count + other_adjective_count)


    def _splitIntoParagraphs(self, text: str) -> list[str]:
        paragraphs = []
        start = self._detectParagraphStartOffset(text, 0)
        while start is not None:
            end = self._detectParagraphEndOffset(text, start)
            if end is None:
                # 最後の段落
                paragraphs.append(text[start:])
                break
            else:
                # 途中の段落
                paragraphs.append(text[start:end])
                start = self._detectParagraphStartOffset(text, end)
        return paragraphs


    def _detectParagraphStartOffset(self, text: str, fromOffset: int) -> int | None:
        # fromOffset以降のテキストの中で、全角スペースを探す
        # 全角スペースが見つかったら、その位置を返す
        # 全角スペースが見つからなかったら、Noneを返す
        offset = text.find("\u3000", fromOffset)
        if offset < 0:
            return None
        else:
            return offset


    def _detectParagraphEndOffset(self, text: str, fromOffset: int) -> int | None:
        # fromOffset以降のテキストの中で、改行を探す
        # 改行が見つからなかったら、Noneを返す
        endOffset = text.find("\n", fromOffset)
        if endOffset < 0:
            # 改行が見つからなかった
            return None
        else:
            # 改行が見つかった
            return endOffset
