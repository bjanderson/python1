import getopt
import sys


# get command-line args
def get_args():
    """Get the operation, input file, keyword file, and output file locations"""

    operation = "encrypt"
    input_file = "plaintext.txt"
    keyword_file = "keyword.txt"
    output_file = "ciphertext.txt"
    usage = (
        "substitution-cipher.py -i <inputfile> -o <outputfile> -k <keywordfile> [-e -d]"
    )

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(
            argv, "hi:o:k:e:d", ["ifile=", "ofile=", "kfile=", "encrypt=", "decrypt="]
        )
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print(usage)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-k", "--kfile"):
            keyword_file = arg
        elif opt in ("-e", "--encrypt"):
            operation = "encrypt"
        elif opt in ("-d", "--decrypt"):
            operation = "decrypt"

    return {
        "operation": operation,
        "input_file": input_file,
        "keyword_file": keyword_file,
        "output_file": output_file,
    }


# read text from file
def get_text(filename):
    text = list("")
    try:
        with open(filename, "r") as file:
            text = file.readlines()
    except Exception as ex:
        print(f"ex: {ex}")

    return "".join(text)


# write text to file
def write_text(text, filename):
    try:
        with open(filename, "w") as file:
            text = file.write(text)
    except Exception as ex:
        print(f"ex: {ex}")


def get_plain_text_alphabet():
    alphabet = ["\n"]  # ascii: 10
    # the visible keyboard characters are represented by the numbers in the range from 32 to 127
    for num in range(32, 127):
        alphabet.append(chr(num))
    return alphabet


def get_cipher_text_alphabet(keyword):
    kw = deduplicate_keyword_characters(keyword)
    plain_alphabet = get_plain_text_alphabet()
    cipher_alphabet = list(filter(lambda a: a not in kw, plain_alphabet))
    cipher_alphabet = kw + cipher_alphabet
    return cipher_alphabet


def deduplicate_keyword_characters(keyword):
    keyword_chars = list(keyword)
    kw = []
    for char in keyword_chars:
        if char not in kw:
            kw.append(char)
    return kw


def convert(input_text, input_alphabet, output_alphabet):
    input_chars = list(input_text)
    output_chars = []
    for char in input_chars:
        try:
            i = input_alphabet.index(char)
            output_chars.append(output_alphabet[i])
        except Exception as ex:
            print(f"ex: {ex}")

    return "".join(output_chars)


# run the program
def run():
    args = get_args()
    input_text = get_text(args["input_file"])
    keyword = get_text(args["keyword_file"])
    input_alphabet = []
    output_alphabet = []
    if args["operation"] == "encrypt":
        input_alphabet = get_plain_text_alphabet()
        output_alphabet = get_cipher_text_alphabet(keyword)
    else:
        input_alphabet = get_cipher_text_alphabet(keyword)
        output_alphabet = get_plain_text_alphabet()
    output_text = convert(input_text, input_alphabet, output_alphabet)
    write_text(output_text, args["output_file"])


if __name__ == "__main__":
    run()
