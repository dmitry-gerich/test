import subprocess

def test_app():
    """
    Verifies that app.py echoes the input string correctly.
    """
    input_text = "Hello, this is a test!\nJunie is here.\n"
    process = subprocess.Popen(
        ['python3', 'app.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout_data, stderr_data = process.communicate(input=input_text)
    
    if stdout_data == input_text:
        print("SUCCESS: Input and output match.")
    else:
        print(f"FAILURE: Expected '{repr(input_text)}', got '{repr(stdout_data)}'")
        exit(1)

if __name__ == "__main__":
    test_app()
