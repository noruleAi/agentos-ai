import subprocess

async def run_python(code: str):

    with open("temp.py", "w") as file:
        file.write(code)

    result = subprocess.run(
        ["python", "temp.py"],
        capture_output=True,
        text=True
    )

    return result.stdout