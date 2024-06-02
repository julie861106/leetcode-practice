# Leetcode Practice
Use this repo to practice leetcode &amp; git command

**Table of Contents**

- [Leetcode Practice](#leetcode-practice)
  - [Installation](#installation)
  - [Test Case Mapping](#test-case-mapping)
  - [Run the Test Case](#run-the-test-case)

---

## Installation


1. Clone the repository:

   ```shell
   git clone git@github.com:julie861106/leetcode-practice.git
   ```

2. Navigate to the project directory:
   ```shell
   cd dlm_g2
   ```

3. Create a Python virtual environment:

   ```shell
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the required packages

    ```shell
    pip3 install -r requirements.txt
    ```
---

## Test Case Mapping
| Problem | Test Case |
| :---- | :---- |
| [344. Reverse String](https://leetcode.com/problems/reverse-string/description/) | `test_string` |


## Run the Test Case

```
pytest testcase/xxx
```

When executing a test, `pytest` will automatically go to the test folder (`tests` by default) to look for files starting with `test_` and execute functions starting with `test_`
```
pytest -vv
```
