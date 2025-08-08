import sys, re, traceback
from unittest import TestCase

class Evaluate(TestCase):

    def test_exercise(self):
        import exercise

        def check_variable():
            """Check if 'button_label' variable is correctly defined"""
            
            # Check if 'button_label' is declared
            if not hasattr(exercise, "button_label"):
                sys.exit("You must define a 'button_label' variable.")
            
            # Check if 'button_label' is assigned the correct value
            if exercise.button_label != "submit":
                sys.exit("The 'button_label' variable should be assigned the string 'submit'.")

        def check_capitalize_usage():
            """Check if the capitalize() method is used correctly"""
            with open("exercise.py") as file:
                content = file.read()

            # Check for capitalize() usage on button_label
            capitalize_check = re.search(r"button_label\.capitalize\(\)", content)
            if not capitalize_check:
                sys.exit("It looks like your code doesn't have a 'button_label.capitalize()' line.")

            # Ensure the user did not manually capitalize the string
            manual_capitalization_check = re.search(r"print\(\s*[\"']Submit[\"']\s*\)", content)
            if manual_capitalization_check:
                sys.exit("It looks like you're manually capitalizing 'Submit' instead of using the 'capitalize()' method.")

        def check_print_missing():
            """Check if print() is included"""
            with open("exercise.py") as file:
                content = file.read()

            if "print(" not in content:
                sys.exit("It looks like there is no print() function in your code. Did you forget to print out the output?")
        
        def check_print_output():
            """Compare expected output with user's printed output"""
            try:
                user_output = sys.stdout.getvalue().strip("\n")
            except Exception:
                extracted_exception = traceback.format_exc().splitlines()[3:]
                traceback_string = ''
                for line in extracted_exception:
                    if r'/eval/' in line:
                        line = line.replace(r'/eval/', '')
                    traceback_string = traceback_string + line + "\n"
                sys.exit(traceback_string)

            correct_output = "Submit"

            message_output = f"Your code generates this output:\n→{user_output}←\nBut, the expected output is:\n→{correct_output}←"

            if correct_output == user_output:
                pass
            else:
                sys.exit(
                    message_output + "\n\nPlease compare the two outputs carefully. \nSometimes you might be missing a space in your text, \nor using a lowercase letter instead of uppercase or vice-versa.")

        check_variable()
        check_capitalize_usage()
        check_print_missing()
        check_print_output()