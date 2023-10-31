# TobeIT 67, KMITL Computer programming submission

This repository is mainly for storing and sharing the solutions and testcase scripts.

## Testcase script
In this repo, there is 2 version of testcase:
- `testcase.py` is the old testcase script for `.tc` file.
- `testcase2.py` is the new testcase script for `.tc.md` file
Using `testcase2.py` is recommended. It is more readable and easier to use.

### Usage
```bash
nodemon ./testcase2.py <problem_id> <arguments>
```

#### Prerequisite
- `nodemon`, Install it with `npm install -g nodemon`
- `python3`, Install with `sudo apt install python3`
- That's it, you're good to go.

#### Create a new testcase
Assume that the problem ID is `book_cover`:

1. Run the following command after you're in the root directory of this repo.
```bash
nodemon ./testcase2.py book_cover --create
```
   `--create` is to tell the script to automatically create a new testcase file for you.

2. The script will create a new file named `book_cover.tc.md` and `book_cover.py` in the `problems` directory.

3. Edit the `book_cover.tc.md` file to add your testcase. Please read the [Testcase file format](#testcase-file-format) section for more information.

4. Since the script is run using nodemon, you don't need to re-running everything. Just open the newly created file and enjoy.

### Testcase file format
The testcase file is a markdown file with some special syntax. The syntax is used to tell the script what is the input and what is the expected output.

Here is the minimal example of the testcase file:
```markdown
##### 1
AEIOU
8
----
12

##### 2
ASdf
1
----
5
```
Explanation:
- `##### 1` is the testcase name. It is used to tell the script that the following lines are the testcase for the testcase name `1`.
- Input:
  - `AEIOU` is the first line of the input.
  - `8` is the second line of the input.
- `----` is the separator between the input and the expected output.
- Expected output:
  - `12` is the first line of the expected output.
> **NOTE**
> The testcase name must be unique. And do not add a blank line between the testcase name and the input!

And for readability and to provide more useful information, you can write anything before the first testcase name and the script will ignore everything before that. And script will also ignore anyline that starts with three backtick <code>\`\`\`</code>.

Here is the example of the testcase file with more information:
```markdown
# Book Cover
This is the problem description.
you can write anything here.

## Input specification
Line 1: The first line of the input.
Line 2: The second line of the input.

## Output specification
Line 1: The first line of the expected output.

## Testcases
\`\`\`
##### 1
AEIOU
8
----
12

##### 2
ASdf
1
----
5
\`\`\`
```

#### Script options
Sometime the default behavior of the input and output is not what you want (sometime the display window is too small to draw box or you just want to overide and see the input/output of the testcase). You can use the following syntax to change the behavior of the input and output by put it in the first line of the testing script file.

For example, to suppress box drawing around the input/output and always show input/output even when the testcase is pass when testing `book_cover.py` script, you can add the following line to the top of the file:
```python
#debug: no_box show_input_output
... rest of the code ...
```

Options available:

| Option | Description |
| --- | --- |
| `no_box` | Suppress box drawing around the input/output |
| `show_input_output` | Always show input/output even when the testcase is pass |
| `show_got_only` | Only show the output of the script and hide input and expected result |

## Questions?
Feel free to read the source code of `testcase2.py`!