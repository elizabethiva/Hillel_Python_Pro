from pympler import asizeof


def find_in_file(file_name='rockyou.txt', pattern=input('Enter the search word: ')):
    total_lines = 0
    with open (file_name, 'r') as file:
        with open('results.txt', 'w') as results:
            while True:
                line = file.readline()
                if not line:
                    break
                if pattern in line:
                    results.write(line)
                    total_lines += 1
    return f"Total lines: {total_lines}. Total size:{asizeof.asized(results)}"

                        
def main():
    res = find_in_file()
    print(res)


if __name__ == '__main__':
    main()