import argparse
import base_generator
import interactive_spellchecker

parser = argparse.ArgumentParser()
parser.add_argument("-s", "-setup",
                    action="store_true",
                    dest="setup_activated")
parser.add_argument("word")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.setup_activated:
        base_generator.generate_base()
    fitting_words = interactive_spellchecker.spell_check(args.word)
    print("Возможно, вы имели в виду:")
    for word in fitting_words:
        print(word)

