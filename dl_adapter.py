class DLAdapter:

    def __init__(self):
        self.vocab = {}
        self.index = 0

    def encode(self, tokens):
        sequence = []
        for token in tokens:
            if token.type not in self.vocab:
                self.vocab[token.type] = self.index
                self.index += 1
            sequence.append(self.vocab[token.type])
        return sequence
