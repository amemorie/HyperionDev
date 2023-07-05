"""
HyperionDev Skills Bootcamp in Software Engineering (Fundamentals)
T17 - Capstone Project - Lists, Functions, and String Handling

Unit test for Compulsory Task 1:
"""
# =============
# Import block.
# =============
import task_manager

# from code snippet at: 
# https://code-maven.com/mocking-input-and-output-for-python-testing
def test_task_manager():
    test_parameters = [
        ["admin","password","r", "bob","bob1", "bob1", "e", "True"],
        ["admin","password","r", "cary","cary2", "cary2", "e", "True"],
        ["bob","bob1", "r", "daisy","daisy3", "daisy3", "e", "True"],
        ["daisy","daisy3","r","daisy", "evan","evan4", "evan4", "e", "True"],
        ["cary","cary2","a","bib","a","bob","new task1","this is a new task","2023-06-30","e","True"],
        ["daisy","daisy3","a","cary","new task2","this is another new task","20222222","2023-07-21","e","True"],
        ["daisy","daisy3","a","daisy","new task3","this is a new task again","2023-08-09","e","True"],
        ["daisy","daisy3","a","daisy","new task4","daisy has a lot of tasks","2023-05-01","e","True"],
        ["daisy","daisy3","va","e","True"],
        ["daisy","daisy3","vm","-1", "e","True"],
        ["cary","cary2","vm","3","m", "-1", "e","True"],
        ["admin","password","gr", "e","True"],
        ["evan","evan4", "gr","e","True"],
        ["admin","password","ds","e","True"]
    ]            
        
    nn = 0
    for x in range(len(test_parameters)):
        str_n = str(nn+1)
        input_values = test_parameters[nn][:-1]
        output_value = test_parameters[nn][-1]
        test_string = "Test "+str_n+" : Inputs:("+", ".join(input_values)+") Output: "+output_value
     
        def mock_input(s):
            output.append(s)
            return input_values.pop(0)
        
        ss = " "    
        task_manager.input = mock_input
        task_manager.print = lambda ss: ss
        output = []
        output = str(task_manager.task_manager())

        assert output == output_value, print(output, output_value)
        print(test_string+" : completed correctly")
        nn +=1
            
if __name__ == '__main__':
    test_task_manager()