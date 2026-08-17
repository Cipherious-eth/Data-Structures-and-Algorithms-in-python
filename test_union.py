from Algorithms import get_union
tests= [{"function" : get_union,"input": [[0,3,6,9,0,12,15],[2,4,6,8,10,12,14,16]],"output":[0,3,6,9,12,15,2,4,8,10,14,16]
}
]

num_successes = 0 
num_failures  = 0
for test in  tests:
    function = test['function']
    test_input = test["input"]
    desired_output = test["output"]
    actual_output = function(*test_input)
    if actual_output == desired_output:
        num_successes += 1
    else:
        num_failures +=1
        function_name = function.__name__
        print(f"")
        print(f"{function_name} failed on the input{test_input}")
        print(f"/ desired output {desired_output}")
        print(f"/ actual output  {actual_output}")

print(f"Testing Complete:{num_successes} successes and {num_failures} failures")
