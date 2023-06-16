def sum_numbers(a, b):
    res = a + b
    print(res)
class ConsoleWriter:

    def write_to_console(self, entity_to_print):
        print(entity_to_print)


class TxtWriter:

    def write_to_txt(self, entity_to_print):
        # code to write to txt
        pass


if __name__ == '__main__':
    cw = ConsoleWriter()
    tw = TxtWriter()

    cw.write_to_console(sum_numbers(1,2))
    tw.write_to_txt(sum_numbers(1,2))