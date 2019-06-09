"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["abcd"],
            "answer": ["ab", "cd"]
        },
        {
            "input": ["abc"],
            "answer": ["ab", "c_"]
        },
        {
            "input": ["abcdf"],
            "answer": ["ab", "cd", "f_"]
        },
        {
            "input": ["a"],
            "answer": ["a_"]
        },
        {
            "input": [""],
            "answer": ["__"]
        },
    ],
    "Extra": [
        {
            "input": ["hh"],
            "answer": ["hh"]
        },
        {
            "input": ["hhh"],
            "answer": ["hh", "h_"]
        },
        {
            "input": ["hhh1"],
            "answer": ["hh", "h1"]
        }
    ]
}
