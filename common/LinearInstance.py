from hypergraph.Instance import Instance

class LinearInstance(Instance):
    def __init__(self, instance_id, weight, input, output):
        super().__init__(instance_id, weight, input, output)
        self.word_seq = None

    def size(self):
        # print('input:', self.input)
        return len(self.input)

    def duplicate(self):
        dup = LinearInstance(self.instance_id, self.weight, self.input, self.output)
        dup.word_seq = self.word_seq
        # print('dup input:', dup.get_input())
        return dup

    def removeOutput(self):
        self.output = None

    def removePrediction(self):
        self.prediction = None

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def get_prediction(self):
        return self.prediction

    def set_prediction(self, prediction):
        self.prediction = prediction

    def has_output(self):
        return self.output != None

    def has_prediction(self):
        return self.prediction != None

    def __str__(self):
        return 'input:' + str(self.input) + '\toutput:' + str(self.output) + ' is_labeled:' + str(self.is_labeled)

