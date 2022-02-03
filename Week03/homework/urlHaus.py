# Func: Import the Python package for interpreting CSV files.
# Fix: Needed to import missing packages: re
import csv
import re


# Func: Define a new function, named "ur1HausOpen", that takes in two variables, "filename" and "searchTerm".
# Fix: The function name had a 1 in place of an 'l'.
# Also, the '' needed to be removed from the 'filename' variable, as it is not calling a specific file.
def urlHausOpen(filename, searchTerm):
    # Func: Use the with function to open and parse the inputted csv file.
    # Fix: This line of code needed to be indented to be considered as part of the function.
    # The while function also had to be changed to the with function. The 'r' attribute needed adding to the open function.
    with open(filename, 'r') as f:
        # Func: Store the parsed values from the CSV file into a variable.
        # Fix: Code line required the proper indentation to work with the opened file.
        # Review is not a valid csv function, switched to reader.
        # One equal sign needed to be removed. Variable passed into csv.reader needed to be changed to 'f'.
        contents = csv.reader(f)
        # Func: Begin a for loop to skip the first 9 entries of data
        # in the parsed csv file. Uses the underscore as a throwaway variable for streamline purposes.
        # Fix: Needed to be indented properly.
        for _ in range(9):
            # Func: Uses the next function to cycle through the
            # different elements in the parsed content.
            # Fix: Required proper indentation.
            next(contents)

        # Func: Starts a new loop with the content processes earlier in the code. Uses the inputted searchTerm variable.
        # Fix: Required proper indentation. Needed to remove an 's' from
        # searchTerm to match earlier use of the variable.
        for keyword in searchTerm:
            print(keyword)
            # Func: Reads through each line in the contents variable.
            # Fix: Required proper indentation.
            for eachLine in contents:
                # Func: If the line contains the keyword then it will store formatted data in the variable 'x'.
                # Fix: Needed indentation. Required the inclusion of proper re-formatting,
                # specifically the inclusion of '' after the 'r' and before the comma.
                x = re.findall(r'' + keyword + '', eachLine[2])
                # Func: Begin a new loop to go through the newly processes and formatted data.
                # Again, using the underscore as a throwaway variable.
                # Fix: Required indentation.
                for _ in x:
                    # Func: Separating and replacing the value "HTTP" to "HXXP" to avoid clicking on real links.
                    # Fix: Required Indentation.
                    the_url = eachLine[2].replace("http", "hxxp")
                    # Func: Separate out the source element from the data and store it in a function.
                    # Fix: Required Indentation.
                    the_src = eachLine[5]
                    # Func: Separate out the time element from the data and store it in a function.
                    # Fix: I added this for program depth.
                    the_time = eachLine[1]
                    # Func: Print out a formatted string using the date processes above.
                    # Fix: This was a lot. I needed to remove the 'f' from before the initial quotations, add {}s after the URL and Info sections,
                    # And I changed the '+' to a '*' to achieve the desired line effect. I also needed to indent the section properly.
                    print("""
                        Time: {}
                        URL: {}
                        Info: {}
                        {}
                        """.format(the_time, the_url, the_src, "*" * 60))
