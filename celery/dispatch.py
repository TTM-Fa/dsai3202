from tasks import is_prime

def dispatch_tasks():
    result_objs = [is_prime.apply_async((number,)) 
                   for number in range(1, 10001)]
    
    results = [result.get()
               for result in result_objs
               if result.get() is not None]
    # results = []
    # for result in result_objs:
    #     prime = result[1].get()
    #     if prime:
    #         results.append(result[0])
    return results

if __name__ == "__main__":
    results = dispatch_tasks()
    print(results)
