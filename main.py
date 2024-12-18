from Parser_class import Parser

def processing():
     parser = Parser()
     while True:
            path = input("Введите путь до файла, либо 'q' для выхода: ").strip()
            if path.lower() == 'q':
                break
            try:
                if path.endswith('.csv'):
                    parser.parse_csv(path)
                elif path.endswith('.xml'):
                    parser.parse_xml(path)
                else:
                    print("Некорректный ввод")
            except Exception as e:
                print(f"ERROR {e}")


if __name__ == "__main__" :
     processing()
    