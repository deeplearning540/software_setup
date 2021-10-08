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
system's package manager  (say `apt` on Debian or Ubuntu GNU/Linux) or using
the `pip` Python package manager

```sh
$ pip install -r requirements.txt
```

Note that we by default install `tensorflow-cpu`. If you have a GPU, use
`tensorflow` instead.

You may want to create a [virtual environment][venv_basics] in case you need to
separate those packages from the rest of your system.

You can now run

```sh
./check_install.py
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

## Conda (local) or Google Colab (cloud)

You can also install Python packages using the [Conda package manager][conda].
As a fallback, you can also use a could-backed [Jupyter notebook running on
Google Colab][gco]. Both methods are explained [here][carpentries_setup].


## Interactive environment

Some of the course code material is presented in form of Jupyter notebooks and
many people like to use the [Jupyter] interactive environment to run them.

You can also execute all code from the lesson notebooks

* in your normal Python interactive shell
* using the [ipython] interactive shell
* put the code in normal Python scripts and run it

[carpentries_setup]: https://carpentries-incubator.github.io/deep-learning-intro/setup
[venv_basics]: https://realpython.com/python-virtual-environments-a-primer/
[gco]: https://colab.research.google.com
[conda]: https://docs.conda.io/en/latest
[Jupyter]: https://jupyter.org
[ipython]: https://ipython.org/
