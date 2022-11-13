# Supplimental Instructor Notes

## Chapter 1 - Introduction to Python

### 1.1 Introducing Python
- _Where is Python on my Machine?_ need to provide company specific instructions as an add-on
#### Exercises
- _1.4: Where is My Bus?_ - needs an alternative
  - Specified url results in 404 error; web site mentions that an API key is needed to get Bus Tracker info
  - Regardless, better to not spam a web site with a bunch of student requests
### 1.2 A First Program
#### Exercises
- _1.6: Debugging_ - consider running once with python3.9 and once with python3.10+; this will show off the enhanced error messages of later versions of python
### 1.3 Numbers
Also show this form
```python
if a <= b <= c:
    print('b is between a and c')
```
### 1.6 File Management
for maxbytes example, the `[`, `]` are not valid syntax. better to show
```python
# Read only up to 'maxbytes' bytes
data = f.read(maxbytes)
```
