from tasks import power

def test_single_task():
    result = power.delay(2, 3)
    print(result.get(timeout=10))  # Adjust timeout as needed

if __name__ == "__main__":
    test_single_task()