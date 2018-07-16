# Python TDD CI Tutorial

A nano tutorial on Test Driven Development (TDD) and Continuous Integration (CI). Let's check if a number is prime or not.

[![Build Status](https://travis-ci.org/zekedran/python_tdd_ci_tutorial.svg?branch=master)](https://travis-ci.org/zekedran/python_tdd_ci_tutorial)

## Why Test Driven Development?

TDD allows us to write software based on goals or tests. Pass all the tests and the software is done. 

Bare minimum things we need to start is 
- some hardcoded output*
- test cases we want the software (which you will write) to handle

*that looks like output. i.e., same data structure, same data-type, etc., 

It is okay to begin with a hardcoded value or random variable being outputted. And now when we run the tests, some will pass and some will fail. This should give an estimate of how much we have progressed. We then write code to make every test pass. Some test cases can be added along the way as well just like we did in this repo, if you do not know all the test cases before building the software.

## Am I wasting time writing the tests?

Maybe. Maybe not. Depends on
- effort you would put in to write the tests 
- time to test all those cases manually
- development iterations
- number of developers involved

If it's a single developer and a one iteration build (which even small projects usually won't be) that can be easily tested manually and if it would take ages to write them as code, yes you may not want to do this. You can write the software once and for all, see if it works at the end, make quick changes or add dirty hacks just to get it working, hand it over and done, right?

But unfortunately, even a very simple task like `is_prime(number)` would require multiple iterations. Every single time you make changes, you can check if the change you made has broken your app or not. 

It would become so messy when more than one developer is involved. How do I know if I broke the code, or my colleague broke it? Run the tests before and after your colleague's commit, and voila! You know who the criminal is ;)  

And remember, passing the tests do not mean your code is bug-free, it just means that it passes the test cases that we aimed for. 

## Why Continuous Integration?

With CI, we can be sure if this piece of software will work just the way we would expect on any machine with a given configuration in the world. In this case, we ensure this software runs on any machine that can run

  - Python 2.6
  - Python 2.7
  - Python 3.4
  - Python 3.5
  - Python 3.6
  - Python 3.7-dev
  
## How do I start?

Check the commit history of this repo and that should help you get started.

## MIT License

Copyright (c) 2018 Saravanabalagi Ramachandran

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

