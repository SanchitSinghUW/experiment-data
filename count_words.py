import os

# reads all files in the provided directory and outputs the total word count
def count_words():
    root = os.environ.get('TASK1_PATH')
    total = 0
    for path, _, files in os.walk(root):
        for name in files:
            fullPath = os.path.join(path, name)
            file = open(fullPath, encoding = "ISO-8859-1")
            data = file.read()
            words = data.split()
            total += len(words)
            file.close()
    result = open("output_data", "w")
    result.write("word_count: " + str(total))
    result.close()

count_words()
#count_words('/Users/sanchits/Desktop/beaker_example/dataset')
