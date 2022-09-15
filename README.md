# Course software requirements

## Python

Make sure you run Python 3. Check by starting the interpreter, for instance

```sh
$ python3
Python 3.9.7 (default, Sep 24 2021, 09:43:00)
[GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

On some systems, the default `python` is `python3`.


## Minimal local setup

The minimal set of Python packages you need to install are listed in
`requirements.txt`. Install them on your local machine, e.g. using your
system's package manager  (say `apt` on Debian or Ubuntu GNU/Linux).

If you use the [`pip` Python package manager](https://pip.pypa.io/en/stable),
then you may want to create a [virtual environment][venv_basics] in case you
need to separate packages from the rest of your system.

```sh
$ python3 -m venv course_env && . ./course_env/bin/activate
```

Install packages:

```sh
(course_env) $ pip install -r requirements.txt
```

Note that we install `tensorflow-cpu` by default. If you have a GPU, then you
may use `tensorflow` instead, which will utilize that. But all examples we use
are very light weight, so the CPU version will suffice.

You can now run

```sh
(course_env) $ ./check_install.py
```

which should print

```
numpy                ... ok
matplotlib           ... ok
sklearn              ... ok
pandas               ... ok
seaborn              ... ok
tensorflow.keras     ... ok
```

## Anaconda distribution + Conda package manager (local)

Instead of using your system tools or `pip`, you can install Python itself and
packages using the [Anaconda distribution][anaconda]. Once installed, you can
install more packages using the [Conda package manager][conda] which comes with
Anaconda. This might be the easiest option on Windows systems. More details can
be found [here][carpentries_setup].

## Google Colab (cloud)

You can use a free cloud-backed [Jupyter notebook running on Google
Colab][gco]. Using that, most of the packages we require are already installed.
You can install missing ones by [following the Google Colab
documentation](https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb).

## Interactive environment

Some of the course code material is presented in form of Jupyter notebooks and
many people like to use the [JupyterLab or Jupyter Notebook][Jupyter]
interactive environments to run them (e.g. Google Colab Jupyter notebook).

But this is not required. If you don't have/want a Jupyter environment, you
can also execute all code from the lesson notebooks

* in your normal Python interactive shell (terminal based, start `python` or
  `python3`)
* using the more powerful [ipython] interactive shell (start `ipython` or
  `ipython3`)


[carpentries_setup]: https://carpentries-incubator.github.io/deep-learning-intro/setup
[venv_basics]: https://realpython.com/python-virtual-environments-a-primer/
[gco]: https://colab.research.google.com
[conda]: https://docs.conda.io/en/latest
[Jupyter]: https://jupyter.org
[ipython]: https://ipython.org/
[anaconda]: https://www.anaconda.com/products/distribution
