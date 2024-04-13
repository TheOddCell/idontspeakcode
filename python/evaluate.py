from pyscript import document
import io
import sys

def evaluate(event):
    input_text = document.querySelector("#code")
    code = input_text.value
    output_div = document.querySelector("#output")
    # Redirect standard output
    stdout = io.StringIO()
    sys.stdout = stdout

    # Evaluate the expression
    result = eval(code)

    # Reset standard output
    sys.stdout = sys.__stdout__

    # Get the printed output
    printed_output = stdout.getvalue()
    output_div.innerText = str(result) + "\n\n" + printed_output