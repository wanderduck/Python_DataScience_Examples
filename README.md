# <center> :duck: **<u>Python Data Science Examples</u>** :duck: </center>
<br><br>
![Wanderduck at Desk](wanderduck_office_coloured_withLogos.png#center)

---
# <center>:building_construction:**THIS IS CURRENTLY A WORK IN PROGRESS AND WILL BECOME MORE COMPLETE OVER TIME**:construction_worker_man:</center>

---
### &nbsp;&nbsp;<center> :nerd_face: **<u>General</u>**: Within this repository is a directory of jupyter notebooks, each of which contain examples of many different concepts that one might use when working with Python in the field of Data Science or Analytics, as well as many fundamentals of Python programming. *</center>

---
-  :notebook: Notebooks for each section of the `Table of Contents` below are stored in the `notebooks/` directory [see here](https://github.com/wanderduck/Python_DataScience_Examples/tree/master/notebooks) and are named to reflect the general information contained within (i.e. the notebook at `notebooks/sampling.ipynb` contains information and examples pertaining to statistical sampling in Python).
<br><br>
- Any data sets necessary for particular notebooks are stored in the `data/` directory within a folder whose name is the same as the notebook to which it belongs (i.e. the data for the notebook at `notebooks/sampling.ipynb` can be found at `data/sampling/`).
  - **NOTE**: Not all data has been uploaded to the repository to conserve space. For notebooks where the necessary dataset(s) has not been uploaded, the corresponding folder within the `data/` directory contains a Markdown (`.md`) file where a link to the dataset(s) can be found for downloading; simply download the dataset(s) to the directory where the Markdown file is located, and everything will work for you.
<br><br>
- The notebooks in this repository use many GPU accelerated libraries and tools, such as RAPIDS (specifically `cudf` instead of using `pandas`) and `jax.numpy` (imported as `jnp`)
- I have included, for the most part, examples of both non-GPU accelerated code and GPU accelerated code
- If you are going to use GPU acceleration you will need to run this to get jax to work:
	- ```pip install --upgrade "jax[cuda13-local]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html```
		- **<u>NOTE</u>**: the install script above is for Cuda version 13, if you have another version of Cuda, just change the number in `cuda13-local` to your specific version 
---
## &nbsp;&nbsp;<center>**:computer: <u>PURPOSE</u>**: This repository is mostly for my own reference and memorization, but it is also available for anyone else to either learn Python and the Data Science tools of Python or just as a reference/cookbook to look back to when something isn't coming to mind immediately--or whatever else you want to use it for: I don't care :trollface: 

---

---
##  <center>:book: **<u>Table of Contents</u>** :book: </center>

- **1. <u>PYTHON & PANDAS FUNDAMENTALS</u>**
	- 1.a The Basics
     - 1.b List/Dictionary Comprehensions and Generators
	- 1.c
	- 1.d
	- 1.e
	- 1.f
	- 1.g
-   **2. <u></u>**
	- 2.a
	- 2.b
	- 2.c
	- 2.d
	- 2.e   
- **3. <u></u>**
