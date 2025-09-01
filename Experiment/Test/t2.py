import sys, re, traceback
from unittest import TestCase

sentence = "the sky is blue today."
name = "sarah smith"

print(sentence.capitalize())
print(name.title())

class Evaluate(TestCase):

    def test_exercise(self):
        import exercise

        def check_variables():
            """Check if 'sentence' and 'name' variables are correctly defined"""
            
            # Check if 'sentence' is declared
            if not hasattr(exercise, "sentence"):
                sys.exit("You must define a 'sentence' variable.")
            
            # Check if 'sentence' is assigned the correct value
            if exercise.sentence != "the sky is blue today.":
                sys.exit("The 'sentence' variable should be assigned the string 'the sky is blue today.'")

            # Check if 'name' is declared
            if not hasattr(exercise, "name"):
                sys.exit("You must define a 'name' variable.")

            # Check if 'name' is assigned the correct value
            if exercise.name != "sarah smith":
                sys.exit("The 'name' variable should be assigned the string 'sarah smith'.")

        def check_methods_usage():
            """Check if capitalize() and title() methods are used"""
            with open("exercise.py") as file:
                content = file.read()

            # Check for capitalize() usage on sentence
            capitalize_check = re.search(r"sentence\.capitalize\(\)", content)
            if not capitalize_check:
                sys.exit("It looks like you forgot to use 'sentence.capitalize()'.")

            # Check for title() usage on name
            title_check = re.search(r"name\.title\(\)", content)
            if not title_check:
                sys.exit("It looks like you forgot to use 'name.title()'.")

            # Ensure manual modification is not used for sentence
            manual_sentence_cap_check = re.search(r"print\(\s*[\"']The sky is blue today\.[\"']\s*\)", content)
            if manual_sentence_cap_check:
                sys.exit("It looks like you're manually capitalizing the sentence instead of using the 'capitalize()' method.")

            # Ensure manual modification is not used for name
            manual_name_title_check = re.search(r"print\(\s*[\"']Sarah Smith[\"']\s*\)", content)
            if manual_name_title_check:
                sys.exit("It looks like you're manually titling the name instead of using the 'title()' method.")

        def check_print_missing():
            """Check if print() is included"""
            with open("exercise.py") as file:
                content = file.read()

            if "print(" not in content:
                sys.exit("It looks like there is no print() function in your code. Did you forget to print out the output?")
        
        def check_print_output():
            """Compare expected output with user's printed output"""
            try:
                user_output = sys.stdout.getvalue().strip("\n").split("\n")
            except Exception:
                extracted_exception = traceback.format_exc().splitlines()[3:]
                traceback_string = ''
                for line in extracted_exception:
                    if r'/eval/' in line:
                        line = line.replace(r'/eval/', '')
                    traceback_string = traceback_string + line + "\n"
                sys.exit(traceback_string)

            correct_output = ["The sky is blue today.", "Sarah Smith"]

            message_output = f"Your code generates this output:\n→{user_output}←\nBut, the expected output is:\n→{correct_output}←"

            if correct_output == user_output:
                pass
            else:
                sys.exit(
                    message_output + "\n\nPlease compare the two outputs carefully. \nSometimes you might be missing a space in your text, \nor using a lowercase letter instead of uppercase or vice-versa.")

        check_variables()
        check_methods_usage()
        check_print_missing()
        check_print_output()