'''
    Simple layer to add a reverse lstm and lstm, as well as to call the respective save layers.
'''
class BLSTM(object):

    def __init__(self, LSTM, revLSTM):
        '''

        :param LSTM: A LSTM Layer with back = False
        :param revLSTM: A LSTM Layer with back = True
        '''
        self.LSTM = LSTM
        self.revLSTM = revLSTM
        self.params = self.LSTM.params + self.revLSTM.params #Concat the vectors also

    def __call__(self, input):
        input = self.LSTM(input) + self.revLSTM(input)
        return input

    def inv(self, output):

        return output

    def load(self, filename):
        if filename is None: pass
        if not filename.endswith('.npz'): filename += '.npz'
        self.revLSTM.load(filename+'revlstm')
        self.LSTM.load(filename+'lstm')
        self.params = self.LSTM.params + self.revLSTM.params

    def save(self, filename):
        if filename is None: pass
        self.LSTM.save()
        self.revLSTM.save()

