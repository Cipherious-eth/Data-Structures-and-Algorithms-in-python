from Algorithms import floor
tests =[{"function":floor,"inputs":0.54,"outputs":0},{"function": floor,"inputs": -5.67438,"outputs": -6},{"function":floor,"inputs": 575489745.378,"outputs": 575489745  }]
num_successes = 0
num_failures = 0
for test in tests:
    print("Testing in progress.........")
    function = test["function"]
    test_input = test["inputs"]
    desired_output = test["outputs"]
    actual_output  = function(test_input)
    if actual_output == desired_output:
        num_successes += 1
    else:
        num_failures += 1
        function_name = function.__name__
        print("")
        print(f'{function_name} failed on input {test_input}')
        print(f'/ tDesired Output : {desired_output}')
        print(f'/ tActual Output  : {actual_output}')
print(f"Testing complete: {num_successes} successes {num_failures} failures")




