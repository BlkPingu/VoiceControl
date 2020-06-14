 # takes process()
    def to_array(self, data, cols):

        df = pd.DataFrame.from_records(data, columns = cols)

        return df