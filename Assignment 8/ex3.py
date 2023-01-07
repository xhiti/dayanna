class Aggregator:
    sum = 0
    aggregation = ""

    def __init__(self, agg_type: type, ignore_errors: bool = True):
        self.agg_type = agg_type
        self.ignore_errors = ignore_errors

    def __call__(self, *args):
        for arg in args:
            if self.ignore_errors is True:
                if type(arg) is not self.agg_type:
                    pass
                else:
                    if self.agg_type == int:
                        Aggregator.sum += arg
                    elif self.agg_type == str:
                        Aggregator.aggregation += arg
            elif self.ignore_errors is False:
                if type(arg) is not str and self.agg_type == str:
                    raise TypeError("TypeError: aggregation only works on type 'str', not 'int' !")
                elif type(arg) is not int and self.agg_type == int:
                    raise TypeError("TypeError: sum only works on type 'int', not 'str' !")
                else:
                    if self.agg_type == int:
                        Aggregator.sum += arg
                    elif self.agg_type == str:
                        Aggregator.aggregation += arg

        if self.agg_type == int:
            return Aggregator.sum
        elif self.agg_type == str:
            return Aggregator.aggregation


int_agg = Aggregator(agg_type=int)
int_agg(1, 2, 3)
int_agg(4, "hi", 5.1)
print("INT Aggregator: ", int_agg())
str_agg = Aggregator(agg_type=str, ignore_errors=False)
print("STRING Aggregator: ", str_agg("this", " ", "is a test"))
try:
    str_agg(1)
except TypeError as e:
    print(f"{type(e).__name__}: {e}")