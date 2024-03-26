from tasks import power

def dispatch_tasks():
    result_objs = [power.delay(number, 2) for number in range(1, 10001)]
    results = [result.get(timeout = 10) for result in result_objs]
    return results

if __name__ == "__main__":
    results = dispatch_tasks()
    print(results[:10])