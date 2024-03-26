from first_program import app

@app.task
def compute_power(n:int = 1):
    return n**2
